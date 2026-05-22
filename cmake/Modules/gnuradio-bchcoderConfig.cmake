find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_BCHCODER gnuradio-bchcoder)

FIND_PATH(
    GR_BCHCODER_INCLUDE_DIRS
    NAMES gnuradio/bchcoder/api.h
    HINTS $ENV{BCHCODER_DIR}/include
        ${PC_BCHCODER_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_BCHCODER_LIBRARIES
    NAMES gnuradio-bchcoder
    HINTS $ENV{BCHCODER_DIR}/lib
        ${PC_BCHCODER_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-bchcoderTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_BCHCODER DEFAULT_MSG GR_BCHCODER_LIBRARIES GR_BCHCODER_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_BCHCODER_LIBRARIES GR_BCHCODER_INCLUDE_DIRS)
