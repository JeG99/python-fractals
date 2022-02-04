import numpy as np

from fvars import ITERATIONS
from numba import njit, vectorize, prange, complex128

@njit
def julia(complex_number):
    p = complex_number
    #p = complex(re, im)
    for i in prange(ITERATIONS):
        p = f(p)
        if (p.real*p.real + p.imag*p.imag) >= 4:
            return i
    return ITERATIONS

@vectorize([complex128(complex128)])
def f(z):
    #return z*z
    #return ((z * z + z) / np.log(z)) + complex(0.268, 0.060)
    #return z * np.exp(z) + 0.04
    #return z * z * np.exp(z) + 0.21
    #return z*z + 0.2555555555555555555555555555555555555555555555555
    return z*z + complex(-0.79, 0.15)
    #return z*z + complex(0.33, 0.008)