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

#ifndef INCLUDED_BCHCLASS_H
#define INCLUDED_BCHCLASS_H

#include <stdint.h>
#include <stdio.h>

class BCHCode {
public:
    int m, n, length, k, t, d;  // d may not be needed here. Used only withing gen_poly().
    uint32_t prim_poly;
    
    BCHCode(int length_p, int k_p, int t_p,
            uint32_t prim_poly_p = 0,
            uint32_t gen_poly_p = 0);
    
    void encode( uint8_t datai[],uint8_t datao[], bool msb_first = true);

    int decode( uint8_t datai[],uint8_t datao[], bool msb_first = true);

private:

    int p[21];
    int alpha_to[1048576], index_of[1048576], g[548576];

    static constexpr uint32_t prim_poly_table[] = {
        0,        // m=0  (unused)
        0x3,      // m=1  x + 1
        0x7,      // m=2  x^2 + x + 1
        0xB,      // m=3  x^3 + x + 1
        0x13,     // m=4  x^4 + x + 1
        0x25,     // m=5  x^5 + x^2 + 1
        0x43,     // m=6  x^6 + x + 1
        0x89,     // m=7  x^7 + x^3 + 1
        0x11D,    // m=8  x^8 + x^4 + x^3 + x^2 + 1
        0x211,    // m=9  x^9 + x^4 + 1
        0x409,    // m=10 x^10 + x^3 + 1
        0x805,    // m=11 x^11 + x^2 + 1
        0x1053,   // m=12 x^12 + x^6 + x^4 + x + 1
        0x201B,   // m=13 x^13 + x^4 + x^3 + x + 1
        0x4443,   // m=14 x^14 + x^10 + x^6 + x + 1
        0x8003,   // m=15 x^15 + x + 1
        0x1002D,  // m=16 x^16 + x^5 + x^3 + x^2 + 1
        0x20009,  // m=17 x^17 + x^3 + 1
        0x40027,  // m=18 x^18 + x^5 + x^2 + x + 1
        0x80027,  // m=19 x^19 + x^5 + x^2 + x + 1
        0x100009, // m=20 x^20 + x^3 + 1  
    };
  
    void generate_gf();
    /*
     * Generate field GF(2**m) from the irreducible polynomial p(X) with
     * coefficients in p[0]..p[m].
     *
     * Lookup tables:
     *   index->polynomial form: alpha_to[] contains j=alpha^i;
     *   polynomial form -> index form:     index_of[j=alpha^i] = i
     *
     * alpha=2 is the primitive element of GF(2**m)
     */

    void gen_poly();
    /*
     * Compute the generator polynomial of a binary BCH code. Fist generate the
     *   cycle sets modulo 2**m - 1, cycle[][] =  (i, 2*i, 4*i, ..., 2^l*i). Then
     *   determine those cycle sets that contain integers in the set of (d-1)
     *   consecutive integers {1..(d-1)}. The generator polynomial is calculated
     *   as the product of linear factors of the form (x+alpha^i), for every i in
     *   the above cycle sets.
     */

};

#endif /* INCLUDED_BCHCLASS_H */
