import numpy as np
import fvars
import matplotlib.pyplot as plt

from multiprocessing import Pool, cpu_count
from PIL import Image
from pylab import imshow, show
from Mandelbrot import mandelbrot, mandelbrot
from Julia import julia


class Fractal():
    def __init__(self, fractal_type, iterations, dimensions, min_x, max_x, min_y, max_y, verbose=False):
        self.fractal_type = fractal_type
        
        fvars.ITERATIONS = iterations
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

        if self.fractal_type == 'julia':
            self.func = np.vectorize(julia)
        elif self.fractal_type == 'mandelbrot':
            self.func = np.vectorize(mandelbrot)

    def partial_calc(self, first_array, last_array):
        self.canvas[first_array:last_array] = self.func(self.canvas[first_array:last_array])
        print(self.canvas[first_array:last_array])

    def generate(self):
        print('Calculating...')
        self.canvas = self.func(self.canvas)
        self.canvas = self.canvas.real.astype(np.uint8)

    def show_fractal(self):
        imshow(self.canvas)
        show()

    def save_fractal(self, file_name, file_format='png'):
        cm = plt.get_cmap('nipy_spectral')
        # cm = plt.get_cmap('prism')
        colored_image = cm(self.canvas)
        Image.fromarray((colored_image[:, :, :3] * 255).astype(np.uint8)).save('{}.{}'.format(file_name, file_format))

    def get_canvas(self):
        return self.canvas
