# If on linux, be sure to do:
#   sudo apt-get install python3-tk
# https://stackoverflow.com/questions/56656777/userwarning-matplotlib-is-currently-using-agg-which-is-a-non-gui-backend-so

from fractal import Fractal

#dim = (1080, 1920) # resolucion de la imagen
#frac = Fractal('mandelbrot', 100, dim, -3.3, 1.9, -1.5, 1.5)

dim = (768, 1024)
frac = Fractal('mandelbrot', 100, dim, -0.73786069063659, -0.73753744616721, -0.17466298343187, -0.17442055007983)

#frac = Fractal('mandelbrot', 8000, dim, -3.3 + 0.693333, 1.9 - 0.693333, -1.1, 1.1)
#frac = Fractal('julia', 8000, dim, -3.3 + 0.693333, 1.9 - 0.693333, -1.1, 1.1) 

frac.generate() # genera el fractal
#frac.show_fractal() # muestra el fractal en una ventana
#frac.save_fractal('fractal', 'png') # guarda el fractal con el nombre y tipo de imagen dados (si no se da el tipo se guarda en png automaticamente)
