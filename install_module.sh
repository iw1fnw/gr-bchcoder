#!/bin/bash
# Script to install a module in gnuradio.
# Run it in the main folder of the OOT module

DO_TEST=false
DO_INSTALL=false
DO_CLEAN=false
for arg in "$@"; do
    case "$arg" in
        --test)    DO_TEST=true ;;
        --install) DO_INSTALL=true ;;
        --clean) DO_CLEAN=true ;;
        *)
            echo "Unknown option: $arg"
            echo "Usage: $0 [--make] [--test] [--install] [--clean]"
            echo "  (none)    : configure and build only"
            echo "  --test    : configure, build and run tests"
            echo "  --install : configure, build and install"
            echo "  --clean   : clean the build/build_test folders"
            exit 1
        ;;
    esac
done

if $DO_CLEAN; then rm -rf build; fi
mkdir -p build
cd build
cmake ../ -DCMAKE_INSTALL_PREFIX=~/prefix -Wno-dev
make
if $DO_TEST; then make test; fi
if $DO_INSTALL; then make install; sudo ldconfig; fi
cd ..
