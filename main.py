from fractal import Fractal

dim = (1080, 1080) # resolucion de la imagen
mandel = Fractal('mandelbrot', 20, dim, -2, 2, -2, 2) # '<julia | mandelbrot>, iteraciones, tupla de dimensiones, minimo en X, maximo en X, minimo en Y, maximo en Y'

mandel.generate() # genera el fractal
mandel.show_fractal() # muestra el fractal en una ventana
mandel.save_fractal('fractal vergon', 'jpg') # guarda el fractal con el nombre y tipo de imagen dados (si no se da el tipo se guarda en png automaticamente)