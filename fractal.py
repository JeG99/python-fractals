import numpy as np
import matplotlib.pyplot as plt
import fvars

from PIL import Image
from pylab import imshow, show
from Mandelbrot import mandelbrot, mandelbrot
from Julia import julia

class Fractal():
    def __init__(self, fractal_type, iterations, dimensions, min_x, max_x, min_y, max_y, verbose=False):
        self.fractal_type = fractal_type
        
        fvars.fractal_vars['ITERATIONS'] = iterations
        self.iterations = fvars.fractal_vars['ITERATIONS']
        self.dimensions = dimensions

        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y

        self.verbose = verbose
        
        self.pixelHeight = (self.max_y - self.min_y) / float(self.dimensions[0])
        self.pixelWidth = (self.max_x - self.min_x) / float(self.dimensions[1])
        self.canvas = np.array(np.arange(1, dimensions[0] + 1)[:, None] * np.float(self.pixelHeight) * np.complex('j') + np.arange(1, dimensions[1] + 1) * np.float(self.pixelWidth))
        self.canvas += self.min_x + self.min_y * np.complex('j')

    def generate(self):
        if self.fractal_type == 'julia':
            func = np.vectorize(julia)
        elif self.fractal_type == 'mandelbrot':
            func = np.vectorize(mandelbrot)
        self.canvas = func(self.canvas).real.astype(np.uint8)
        
    def show_fractal(self):
        imshow(self.canvas)
        show()

    def save_fractal(self, file_name, file_format='png'):
        img = Image.fromarray(self.canvas)
        img.save(file_name + '.' + file_format)

    def get_canvas(self):
        return self.canvas
