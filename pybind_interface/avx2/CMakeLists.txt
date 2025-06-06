cmake_minimum_required(VERSION 3.31)
project(qsim)

IF (WIN32)
    set(CMAKE_CXX_FLAGS "/arch:AVX2 /O2 /openmp")
ELSE()
    set(CMAKE_CXX_FLAGS "-mavx2 -mfma -O3")
ENDIF()

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
pybind11_add_module(qsim_avx2 pybind_main_avx2.cpp)

target_link_libraries(qsim_avx2 PUBLIC OpenMP::OpenMP_CXX)
