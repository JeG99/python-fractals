# If on linux, be sure to do:
#   sudo apt-get install python3-tk
# https://stackoverflow.com/questions/56656777/userwarning-matplotlib-is-currently-using-agg-which-is-a-non-gui-backend-so

from fractal import Fractal

#dim = (1080, 1920) # resolucion de la imagen 

if __name__ == '__main__':
    r = 1
    dim = (768 * r, 1024 * r)
    # frac = Fractal('mandelbrot', 2500, dim, -3.3, 1.9, -1.5, 1.5) # fucked up mandelbrot
    frac = Fractal('julia', 2500, dim, -2, 2, -1.5, 1.5)
    # frac = Fractal('mandelbrot', 2500, dim, -0.73786069063659, -0.73753744616721, -0.17466298343187, -0.17442055007983) # tentacle
    frac.generate()
    # frac.show_fractal()
    frac.save_fractal('fractal', 'png')
