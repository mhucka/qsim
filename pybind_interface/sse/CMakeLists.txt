cmake_minimum_required(VERSION 3.31)
project(qsim)

IF (WIN32)
    set(CMAKE_CXX_FLAGS "/O2 /openmp")
ELSE()
    set(CMAKE_CXX_FLAGS "-msse4.1 -O3")
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
pybind11_add_module(qsim_sse pybind_main_sse.cpp)

target_link_libraries(qsim_sse PUBLIC OpenMP::OpenMP_CXX)
