from fvars import ITERATIONS
from numba import njit, prange

@njit
def mandelbrot(complex_number):
    c = complex_number
    #c = complex(re, im)
    z = 0.0j

    for i in prange(ITERATIONS):
        z = z * z + c
        if (z.real * z.real + z.imag * z.imag) >= 4:
            return i
    return ITERATIONS
