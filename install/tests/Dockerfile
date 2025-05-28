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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Docker image used to verify that installing from the `qsimcirq` PyPI package
# will work correctly. See the docker-compose.yaml file in this directory.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Base OS
FROM ubuntu:24.04

# Update package list & install some basic tools we'll need.
RUN apt-get update
RUN apt-get install -y python3-dev python3-pip python3-venv wget

# The default version of CMake is 3.28. Get a newer version from Kitware.
RUN apt remove --purge --auto-remove cmake
RUN wget https://github.com/Kitware/CMake/releases/download/v3.31.7/cmake-3.31.7-linux-x86_64.sh
RUN sh cmake-3.31.7-linux-x86_64.sh --prefix=/usr/local --skip-license

# Copy qsim files from the outside-Docker location to an inside-Docker location.
COPY ./ /qsim/
WORKDIR /qsim/

# Use venv to avoid collision between system packages (e.g., NumPy) and our deps
RUN python3 -m venv test_env

# Activate venv.
ENV PATH="test_env/bin:$PATH"

# Install dev requirements
RUN pip3 install -r dev-requirements.txt

# Install qsim from the local sources
RUN pip3 install .

# Run tests in a non-qsim directory
COPY ./qsimcirq_tests/ /test-install/

WORKDIR /test-install/

ENTRYPOINT python3 -m pytest ./
