#!/usr/bin/env bash
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -eo pipefail -o errtrace
shopt -s inherit_errexit

declare -r usage="Usage: ${0##*/} [-h | --help | help] [bazel options ...]
Run the programs in tests/, and on Linux, also build the programs in apps/.

If the first option on the command line is -h, --help, or help, this help text
will be printed and the program will exit. Any other options on the command
line are passed directly to Bazel.

Note: the MacOS VMs in GitHub runners may run on different-capability CPUS, so
all AVX versions of programs in tests/ are excluded."

# Exit early if the user requested help.
if [[ "$1" == "-h" || "$1" == "--help" || "$1" == "help" ]]; then
    echo "$usage"
    exit 0
fi

# Run all basic tests. This should work on all platforms.
bazel test "$@" \
    tests:bitstring_test \
    tests:channels_cirq_test \
    tests:circuit_qsim_parser_test \
    tests:expect_test \
    tests:fuser_basic_test \
    tests:gates_qsim_test \
    tests:hybrid_avx_test \
    tests:matrix_test \
    tests:qtrajectory_avx_test \
    tests:run_qsim_test \
    tests:run_qsimh_test \
    tests:simulator_basic_test \
    tests:simulator_sse_test \
    tests:statespace_basic_test \
    tests:statespace_sse_test \
    tests:unitary_calculator_basic_test \
    tests:unitary_calculator_sse_test \
    tests:unitaryspace_basic_test \
    tests:unitaryspace_sse_test \
    tests:vectorspace_test

# Apps are sample programs and are only meant to run on Linux.
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    bazel build --config=sse "$@" apps:all
    bazel build "$@" apps:all
fi
