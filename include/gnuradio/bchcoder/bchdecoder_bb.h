/* -*- c++ -*- */
/*
 * Copyright 2026 gr-bchcoder author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_BCHCODER_BCHDECODER_BB_H
#define INCLUDED_BCHCODER_BCHDECODER_BB_H

#include <gnuradio/bchcoder/api.h>
#include <gnuradio/block.h>

namespace gr {
namespace bchcoder {

/*!
 * \brief <+description of block+>
 * \ingroup bchcoder
 *
 */
class BCHCODER_API bchdecoder_bb : virtual public gr::block
{
public:
    typedef std::shared_ptr<bchdecoder_bb> sptr;

    /*!
     * \brief Return a shared_ptr to a new instance of bchcoder::bchdecoder_bb.
     *
     * To avoid accidental use of raw pointers, bchcoder::bchdecoder_bb's
     * constructor is in a private implementation
     * class. bchcoder::bchdecoder_bb::make is the public interface for
     * creating new instances.
     */
    static sptr make(int length, int k, int t);
};

} // namespace bchcoder
} // namespace gr

#endif /* INCLUDED_BCHCODER_BCHDECODER_BB_H */
