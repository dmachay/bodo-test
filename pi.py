#!/usr/bin/env python3

from decimal import Decimal, getcontext
import sys

def pi(prec):
    """Compute Pi to the given precision.
       Adapted from Decimal docs
    """
    getcontext().prec = prec+2  # extra digits for intermediate steps
    three = Decimal(3)          # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    getcontext().prec = prec
    return +s                   # unary plus applies the new precision

if len(sys.argv) <= 1:
    prec = 30
else:
    prec = int(sys.argv[1])

print( pi(prec) )
