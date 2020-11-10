import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from pylab import imshow, show

class Fractal():
    def __init__(self, fractal_type, iterations, dimensions, min_x, max_x, min_y, max_y, verbose=False):
        self.fractal_type = fractal_type
        self.iterations = iterations
        self.dimensions = dimensions

        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y

        self.verbose = verbose
    
        self.canvas = np.zeros(self.dimensions, dtype=np.uint8)
        self.pixelHeight = (self.max_y - self.min_y) / float(self.dimensions[0])
        self.pixelWidth = (self.max_x - self.min_x) / float(self.dimensions[1])

    def f(self, z):
        #return z*z
        #return ((z * z + z) / np.log(z)) + complex(0.268, 0.060)
        #return z * np.exp(z) + 0.04
        #return z * z * np.exp(z) + 0.21
        #return z*z + 0.2555555555555555555555555555555555555555555555555
        return z*z + complex(-0.79, 0.15)
        #return z*z + complex(0.33, 0.008)

    def julia(self, re, im, max_iter):
        p = complex(re, im)
        for i in range(self.iterations):
            p = self.f(p)
            if (p.real*p.real + p.imag*p.imag) >= 4:
                return i
        return self.iterations

    def mandelbrot(self, re, im, max_iter):
        c = complex(re, im)
        z = 0.0j

        for i in range(self.iterations):
            z = z * z + c
            if (z.real * z.real + z.imag * z.imag) >= 4:
                return i
        return self.iterations

    def generate(self):
        for x in range(self.dimensions[1]):
            dx = x * self.pixelWidth
            a = self.min_x + dx
            for y in range(self.dimensions[0]):
                dy =  y * self.pixelHeight
                b = self.min_y + dy
                if self.fractal_type == 'julia':
                    self.canvas[x, y] = self.julia(a, b, self.iterations)
                elif self.fractal_type == 'mandelbrot':
                    self.canvas[y, x] = self.mandelbrot(a, b, self.iterations)

    def show_fractal(self):
        imshow(self.canvas)
        show()

    def save_fractal(self, file_name, file_format='png'):
        img = Image.fromarray(self.canvas)
        img.save(file_name + '.' + file_format)

    def get_canvas(self):
        return self.canvas
