cmake_minimum_required(VERSION 3.31)
project(qsim LANGUAGES CXX CUDA)

if(WIN32)
    set(CMAKE_CXX_FLAGS "/O2 /openmp")
else()
    set(CMAKE_CXX_FLAGS "-O3")
endif()

if(APPLE)
    set(CMAKE_CXX_STANDARD 14)
    include_directories(
      "/usr/local/include"
      "/usr/local/opt/llvm/include"
      "/opt/homebrew/include"
      "/opt/homebrew/opt/llvm@19/include"
    )
    link_directories(
      "/usr/local/lib"
      "/usr/local/opt/llvm/lib"
      "/opt/homebrew/lib"
      "/opt/homebrew/opt/llvm@19/lib"
    )
endif()

INCLUDE(../GetPybind11.cmake)
find_package(PythonLibs 3.7 REQUIRED)
find_package(CUDA REQUIRED)

include_directories(${PYTHON_INCLUDE_DIRS})
if(pybind11_FOUND)
    include_directories(${pybind11_INCLUDE_DIRS})
else()  # means pybind11 has been fetched in GetPybind11.cmake
    include_directories(${pybind11_SOURCE_DIR}/include)
endif()

cuda_add_library(qsim_cuda MODULE pybind_main_cuda.cpp)
set_target_properties(qsim_cuda PROPERTIES
    CUDA_ARCHITECTURES "$ENV{CUDAARCHS}"
    PREFIX "${PYTHON_MODULE_PREFIX}"
    SUFFIX "${PYTHON_MODULE_EXTENSION}"
)
set_source_files_properties(pybind_main_cuda.cpp PROPERTIES LANGUAGE CUDA)

target_link_libraries(qsim_cuda OpenMP::OpenMP_CXX)
