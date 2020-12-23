import fvars

def mandel(re, im, max_iter):
    c = complex(re, im)
    z = 0.0j

    for i in range(fvars.fractal_vars['ITERATIONS']):
        z = z * z + c
        if (z.real * z.real + z.imag * z.imag) >= 4:
            return i
    return fvars.fractal_vars['ITERATIONS']

