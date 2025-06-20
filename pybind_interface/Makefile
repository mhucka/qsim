# The names of the shared libraries that result after compiling qsim for Pybind11
QSIMLIB_BASIC = ../qsimcirq/qsim_basic`python3-config --extension-suffix`
QSIMLIB_SSE = ../qsimcirq/qsim_sse`python3-config --extension-suffix`
QSIMLIB_AVX2 = ../qsimcirq/qsim_avx2`python3-config --extension-suffix`
QSIMLIB_AVX512 = ../qsimcirq/qsim_avx512`python3-config --extension-suffix`
QSIMLIB_CUDA = ../qsimcirq/qsim_cuda`python3-config --extension-suffix`
QSIMLIB_CUSTATEVEC = ../qsimcirq/qsim_custatevec`python3-config --extension-suffix`
QSIMLIB_HIP = ../qsimcirq/qsim_hip`python3-config --extension-suffix`
QSIMLIB_DECIDE = ../qsimcirq/qsim_decide`python3-config --extension-suffix`

# The flags for the compilation of the simd-specific Pybind11 interfaces
PYBINDFLAGS_BASIC = -Wall -shared -std=c++17 -fPIC `pybind11-config --includes`
PYBINDFLAGS_SSE = -msse4.1 -Wall -shared -std=c++17 -fPIC `pybind11-config --includes`
PYBINDFLAGS_AVX2 = -mavx2 -mfma -Wall -shared -std=c++17 -fPIC `pybind11-config --includes`
PYBINDFLAGS_AVX512 = -mavx512f -mbmi2 -Wall -shared -std=c++17 -fPIC `pybind11-config --includes`

# The flags for the compilation of CUDA-specific Pybind11 interfaces
PYBINDFLAGS_CUDA = -std=c++17 -x cu -Xcompiler "-Wall -shared -fPIC `pybind11-config --includes`"

# The flags for the compilation of cuStateVec-specific Pybind11 interfaces
PYBINDFLAGS_CUSTATEVEC = $(CUSTATEVECFLAGS) $(PYBINDFLAGS_CUDA)

# The flags for the compilation of HIP-specific Pybind11 interfaces
PYBINDFLAGS_HIP = -std=c++17 -Wall -shared -fPIC `pybind11-config --includes`

# Check for nvcc to decide compilation mode.
ifeq ($(shell which $(NVCC)),)
# Check for hipcc to decide compilation mode.
ifeq ($(shell which $(HIPCC)),)
pybind: pybind-cpu decide-cpu
else
pybind: pybind-hip decide-hip
endif
else
# Check for the cuStateVec library.
ifeq ($(CUQUANTUM_ROOT),)
pybind: pybind-cpu pybind-cuda decide-cuda
else
pybind: pybind-cpu pybind-cuda pybind-custatevec decide-custatevec
endif
endif

.PHONY: pybind-cpu
pybind-cpu:
	$(CXX) basic/pybind_main_basic.cpp -o $(QSIMLIB_BASIC) $(CXXFLAGS) $(PYBINDFLAGS_BASIC)
	$(CXX) sse/pybind_main_sse.cpp -o $(QSIMLIB_SSE) $(CXXFLAGS) $(PYBINDFLAGS_SSE)
	$(CXX) avx2/pybind_main_avx2.cpp -o $(QSIMLIB_AVX2) $(CXXFLAGS) $(PYBINDFLAGS_AVX2)
	$(CXX) avx512/pybind_main_avx512.cpp -o $(QSIMLIB_AVX512) $(CXXFLAGS) $(PYBINDFLAGS_AVX512)

.PHONY: decide-cpu
decide-cpu:
	echo "building decide-cpu"
	$(CXX) decide/decide.cpp -o $(QSIMLIB_DECIDE) $(CXXFLAGS) $(PYBINDFLAGS_BASIC)

.PHONY: pybind-cuda
pybind-cuda:
	$(NVCC) cuda/pybind_main_cuda.cpp -o $(QSIMLIB_CUDA) $(NVCCFLAGS) $(PYBINDFLAGS_CUDA)

.PHONY: decide-cuda
decide-cuda:
	$(NVCC) decide/decide.cpp -o $(QSIMLIB_DECIDE) $(NVCCFLAGS) $(PYBINDFLAGS_CUDA)

.PHONY: pybind-custatevec
pybind-custatevec:
	$(NVCC) custatevec/pybind_main_custatevec.cpp -o $(QSIMLIB_CUSTATEVEC) $(NVCCFLAGS) $(PYBINDFLAGS_CUSTATEVEC)

.PHONY: decide-custatevec
decide-custatevec:
	$(NVCC) decide/decide.cpp -D__CUSTATEVEC__ -o $(QSIMLIB_DECIDE) $(NVCCFLAGS) $(PYBINDFLAGS_CUDA)

.PHONY: pybind-hip
pybind-hip:
	$(HIPCC) basic/pybind_main_basic.cpp -o $(QSIMLIB_BASIC) $(CXXFLAGS) $(PYBINDFLAGS_BASIC)
	$(HIPCC) sse/pybind_main_sse.cpp -o $(QSIMLIB_SSE) $(CXXFLAGS) $(PYBINDFLAGS_SSE)
	$(HIPCC) avx2/pybind_main_avx2.cpp -o $(QSIMLIB_AVX2) $(CXXFLAGS) $(PYBINDFLAGS_AVX2)
	$(HIPCC) avx512/pybind_main_avx512.cpp -o $(QSIMLIB_AVX512) $(CXXFLAGS) $(PYBINDFLAGS_AVX512)
	$(HIPCC) hip/pybind_main_hip.cpp -o $(QSIMLIB_HIP) $(HIPCCFLAGS) $(PYBINDFLAGS_HIP)

.PHONY: decide-hip
decide-hip:
	$(HIPCC) decide/decide.cpp -o $(QSIMLIB_DECIDE) $(HIPCCFLAGS) $(PYBINDFLAGS_HIP)

.PHONY: clean
clean:
	-rm -f ./basic/*.x ./basic/*.a ./basic/*.so ./basic/*.mod $(QSIMLIB_BASIC)
	-rm -f ./sse/*.x ./sse/*.a ./sse/*.so ./sse/*.mod $(QSIMLIB_SSE)
	-rm -f ./avx2/*.x ./avx2/*.a ./avx2/*.so ./avx2/*.mod $(QSIMLIB_AVX2)
	-rm -f ./avx512/*.x ./avx512/*.a ./avx512/*.so ./avx512/*.mod $(QSIMLIB_AVX512)
	-rm -f ./cuda/*.x ./cuda/*.a ./cuda/*.so ./cuda/*.mod $(QSIMLIB_CUDA)
	-rm -f ./hip/*.x ./hip/*.a ./hip/*.so ./hip/*.mod $(QSIMLIB_HIP)
	-rm -f ./custatevec/*.x ./custatevec/*.a ./custatevec/*.so ./custatevec/*.mod $(QSIMLIB_CUSTATEVEC)
	-rm -f ./decide/*.x ./decide/*.a ./decide/*.so ./decide/*.mod $(QSIMLIB_DECIDE)
