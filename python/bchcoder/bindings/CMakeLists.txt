# Copyright 2020 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

########################################################################
# Check if there is C++ code at all
########################################################################
if(NOT bchcoder_sources)
    message(STATUS "No C++ sources... skipping python bindings")
    return()
endif(NOT bchcoder_sources)

########################################################################
# Check for pygccxml
########################################################################
gr_python_check_module_raw("pygccxml" "import pygccxml" PYGCCXML_FOUND)

include(GrPybind)

########################################################################
# Python Bindings
########################################################################

list(APPEND bchcoder_python_files
    bchencoder_bb_python.cc
    bchdecoder_bb_python.cc python_bindings.cc)

gr_pybind_make_oot(bchcoder ../../.. gr::bchcoder "${bchcoder_python_files}")

# copy bindings extension for use in QA test module
add_custom_command(
    TARGET bchcoder_python
    POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:bchcoder_python>
            ${PROJECT_BINARY_DIR}/test_modules/gnuradio/bchcoder/)

install(
    TARGETS bchcoder_python
    DESTINATION ${GR_PYTHON_DIR}/gnuradio/bchcoder
    COMPONENT pythonapi)
