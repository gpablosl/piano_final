#Comandos para librerías
#pip install pyopengl
#pip install glfw

#Importar librerias

from cmath import cos, pi, sin
import dis
from OpenGL.GL import *
import glfw
import math
import random
from StreamThread import *

class App:

    def main(self):
        global app

        #iniciar StreamThread
        self.stream_thread = StreamThread(self)
        self.stream_thread.daemon = True
        self.stream_thread.start()


if __name__ == "__main__":
    app = App()
    app.main()
