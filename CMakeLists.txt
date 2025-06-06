set(CMAKE_CXX_STANDARD 11)
cmake_minimum_required(VERSION 3.31)

# Set prelimary value so that other variables we need are defined
project(qsim)

# Darwin + Arm64 => Apple Silicon, where we can't build Cuda, AVX or SSE features.
if(CMAKE_SYSTEM_NAME STREQUAL "Darwin" AND CMAKE_SYSTEM_PROCESSOR STREQUAL "arm64")
    set(APPLE_ARM TRUE)
else()
    set(APPLE_ARM FALSE)
endif()

# Set the project name and language more precisely
if(APPLE)
    project(qsim LANGUAGES CXX)
else()
    execute_process(COMMAND which nvcc OUTPUT_VARIABLE has_nvcc OUTPUT_STRIP_TRAILING_WHITESPACE)
    if(has_nvcc)
        project(qsim LANGUAGES CXX CUDA)
    else()
        execute_process(COMMAND which hipcc OUTPUT_VARIABLE has_hipcc OUTPUT_STRIP_TRAILING_WHITESPACE)
        if(has_hipcc)
            project(qsim LANGUAGES CXX HIP)
        else()
            project(qsim LANGUAGES CXX)
        endif()
    endif()
endif()

find_package(OpenMP REQUIRED)

# Add subdirectories based on the architecture or available compilers
ADD_SUBDIRECTORY(pybind_interface/basic)
ADD_SUBDIRECTORY(pybind_interface/decide)
if(NOT APPLE_ARM)
    if(has_nvcc)
        ADD_SUBDIRECTORY(pybind_interface/cuda)
        if(DEFINED ENV{CUQUANTUM_ROOT})
            ADD_SUBDIRECTORY(pybind_interface/custatevec)
        endif()
    elseif(has_hipcc)
        ADD_SUBDIRECTORY(pybind_interface/hip)
    endif()

    ADD_SUBDIRECTORY(pybind_interface/sse)
    ADD_SUBDIRECTORY(pybind_interface/avx512)
    ADD_SUBDIRECTORY(pybind_interface/avx2)
endif()
