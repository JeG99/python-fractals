import numpy as np
import matplotlib.pyplot as plt
import fvars

from PIL import Image
from pylab import imshow, show
from Mandelbrot import mandel
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
    
        self.canvas = np.zeros(self.dimensions, dtype=np.uint8)
        self.pixelHeight = (self.max_y - self.min_y) / float(self.dimensions[0])
        self.pixelWidth = (self.max_x - self.min_x) / float(self.dimensions[1])

    def generate(self):
        for x in range(self.dimensions[1]):
            dx = x * self.pixelWidth
            a = self.min_x + dx
            for y in range(self.dimensions[0]):
                dy =  y * self.pixelHeight
                b = self.min_y + dy
                if self.fractal_type == 'julia':
                    self.canvas[x, y] = julia(a, b, self.iterations)
                elif self.fractal_type == 'mandelbrot':
                    self.canvas[y, x] = mandel(a, b, self.iterations)

    def show_fractal(self):
        imshow(self.canvas)
        show()

    def save_fractal(self, file_name, file_format='png'):
        img = Image.fromarray(self.canvas)
        img.save(file_name + '.' + file_format)

    def get_canvas(self):
        return self.canvas
