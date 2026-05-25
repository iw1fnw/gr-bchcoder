#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 gr-bchcoder author.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr, gr_unittest
from gnuradio import blocks
import time
try:
    from gnuradio.bchcoder import bchencoder_bb
except ImportError:
    import os
    import sys
    dirname, filename = os.path.split(os.path.abspath(__file__))
    sys.path.append(os.path.join(dirname, "bindings"))
    from gnuradio.bchcoder import bchencoder_bb

# -----------------------------
# Test Codeword for BCH(15,11,1)
# -----------------------------
codeword_15_11 = [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0]

# -----------------------------
# Test Codeword for BCH(30,15,3)
# -----------------------------
codeword_30_15 = [0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0] # Reversed

# -----------------------------
# Test Codeword for BCH(125,104,3)
# -----------------------------
codeword_125_104_1 = [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
                      1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0,
                      0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1] # Reversed
codeword_125_104_2 = [1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0,
                      1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1,
                      1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0,
                      1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1,
                      1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0,
                      0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0] # Reversed

class qa_bchencoder_bb(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None


    def test_encode_one_frame(self):
        src_data        = codeword_15_11[4:]
        expected_result = codeword_15_11
        src   = blocks.vector_source_b(src_data)
        encod = bchencoder_bb(15, 11, 1)
        dst   = blocks.vector_sink_b()
        self.tb.connect(src, encod)
        self.tb.connect(encod, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertListEqual(expected_result, result_data)


    def test_encode_two_frames(self):
        src_data        = codeword_15_11[4:] + codeword_15_11[4:]
        expected_result = codeword_15_11 + codeword_15_11
        src   = blocks.vector_source_b(src_data)
        encod = bchencoder_bb(15, 11, 1)
        dst   = blocks.vector_sink_b()
        self.tb.connect(src, encod)
        self.tb.connect(encod, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertListEqual(expected_result, result_data)


    def test_encode_one_frame_short(self):
        src_data        = codeword_30_15[15:]
        expected_result = codeword_30_15
        src   = blocks.vector_source_b(src_data)
        encod = bchencoder_bb(30, 15, 3)
        dst   = blocks.vector_sink_b()
        self.tb.connect(src, encod)
        self.tb.connect(encod, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertListEqual(expected_result, result_data)


if __name__ == '__main__':
    gr_unittest.run(qa_bchencoder_bb)
