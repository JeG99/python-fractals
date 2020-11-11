from fractal import Fractal

dim = (1080, 1920) # resolucion de la imagen

#frac = Fractal('mandelbrot', 100, dim, -3.3, 1.9, -1.5, 1.5)

# el intento mamalon (8 horas)
#frac = Fractal('mandelbrot', 8000, dim, -3.3 + 0.693333, 1.9 - 0.693333, -1.1, 1.1)

# un julia set bien chido (pero no tan mamalon como el mandelbrot anterior)
frac = Fractal('julia', 8000, dim, -3.3 + 0.693333, 1.9 - 0.693333, -1.1, 1.1) 

frac.generate() # genera el fractal
frac.show_fractal() # muestra el fractal en una ventana
frac.save_fractal('fractal', 'png') # guarda el fractal con el nombre y tipo de imagen dados (si no se da el tipo se guarda en png automaticamente)
