cmake_minimum_required(VERSION 3.31)
project(qsim)


IF (WIN32)
    set(CMAKE_CXX_FLAGS "/arch:AVX512 /O2 /openmp")
ELSE()
    set(CMAKE_CXX_FLAGS "-mavx512f -mbmi2 -O3")
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
pybind11_add_module(qsim_avx512 pybind_main_avx512.cpp)

target_link_libraries(qsim_avx512 PUBLIC OpenMP::OpenMP_CXX)
