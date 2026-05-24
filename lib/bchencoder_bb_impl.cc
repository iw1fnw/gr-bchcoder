/* -*- c++ -*- */
/*
 * Copyright 2020 gr-bchcoder author.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include "bchencoder_bb_impl.h"
#include <gnuradio/io_signature.h>


namespace gr {
  namespace bchcoder {

    bchencoder_bb::sptr bchencoder_bb::make(int length, int k, int t)
    {
        return gnuradio::make_block_sptr<bchencoder_bb_impl>(length, k, t);
    }


    /*
     * The private constructor
     */
    bchencoder_bb_impl::bchencoder_bb_impl(int length, int k, int t)
      : gr::block("bchencoder_bb",
              gr::io_signature::make(1, 1, sizeof(unsigned char)),
              gr::io_signature::make(1, 1, sizeof(unsigned char)))
            //mybchtype(bchtype)
    {
      bch=new BCHCode(length, k, t);
      set_output_multiple(bch->length);
    }

    /*
     * Our virtual destructor.
     */
    bchencoder_bb_impl::~bchencoder_bb_impl()
    {
        delete bch;
    }

    void
    bchencoder_bb_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      ninput_items_required[0] = (noutput_items*bch->k)/bch->length;
    }

    int
    bchencoder_bb_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      
      const unsigned char *in = (const unsigned char *) input_items[0];
      unsigned char *out = (unsigned char *) output_items[0];
      uint8_t blockinput[bch->k];
      uint8_t blockoutput[bch->length];
      // Do <+signal processing+>

      int blks = std::min(noutput_items / bch->length, ninput_items[0] / bch->k);
      printf("blocks: %d\n",blks);

      for (int i = 0; i < blks; i++) {
          for(int j=0;j < bch->k;j++){
            blockinput[j]=in[j+(i*bch->k)];
          }
          bch->encode(blockinput,blockoutput);
          for(int j=0;j < bch->length;j++){
            out[j+(i*bch->length)]=blockoutput[j];
          }
      }
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (blks*bch->k);


      // Tell runtime system how many output items we produced.
      return blks*bch->length;
    }

  } /* namespace bchcoder */
} /* namespace gr */

