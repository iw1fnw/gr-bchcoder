#!/usr/bin/env python
# -*- coding: utf-8 -*-
#                     GNU GENERAL PUBLIC LICENSE
#                        Version 3, 29 June 2007
#
#  Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
#  Everyone is permitted to copy and distribute verbatim copies
#  of this license document, but changing it is not allowed.
#
#

from itertools import combinations
from gnuradio import gr, gr_unittest
from gnuradio import blocks
try:
    from gnuradio.bchcoder import bchdecoder_bb
except ImportError:
    import os
    import sys
    dirname, filename = os.path.split(os.path.abspath(__file__))
    sys.path.append(os.path.join(dirname, "bindings"))
    from gnuradio.bchcoder import bchdecoder_bb

class qa_bchdecoder_bb(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_no_errors(self):
        src_data=[0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0]
        expected_result=[0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0]
        src = blocks.vector_source_b(src_data)
        decod= bchdecoder_bb(15, 11, 1)
        dst = blocks.vector_sink_b()
        self.tb.connect(src, decod)
        self.tb.connect(decod, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertListEqual(expected_result, result_data,
            msg=f"Failed to decode corrected sequence")

    def test_one_error(self):
        src_data=[0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0]
        expected_result=[0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0]
        for error_pos in range(len(src_data)):
            with self.subTest(error_pos=error_pos):
                corrupted_data = src_data.copy()
                corrupted_data[error_pos] ^= 1
                src = blocks.vector_source_b(corrupted_data)
                decod= bchdecoder_bb(15, 11, 1)
                dst = blocks.vector_sink_b()
                self.tb.connect(src, decod)
                self.tb.connect(decod, dst)
                self.tb.run()
                result_data = dst.data()
                self.assertListEqual(expected_result, result_data,
                    msg=f"Failed to correct single-bit error at position {error_pos}")

    def test_two_errors(self):
        src_data=[0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0]
        expected_result=[0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0]
        for pos1, pos2 in combinations(range(len(src_data)), 2):
            with self.subTest(pos1=pos1, pos2=pos2):
                corrupted_data = src_data.copy()
                corrupted_data[pos1] ^= 1
                corrupted_data[pos2] ^= 1     
                src = blocks.vector_source_b(corrupted_data)
                decod= bchdecoder_bb(15, 11, 1)
                dst = blocks.vector_sink_b()
                self.tb.connect(src, decod)
                self.tb.connect(decod, dst)
                self.tb.run()
                result_data = dst.data()
                self.assertNotEqual(expected_result, result_data,
                    msg=f"Unexpectedly corrected double-bit error at positions {pos1}, {pos2}")


if __name__ == '__main__':
    gr_unittest.run(qa_bchdecoder_bb)

