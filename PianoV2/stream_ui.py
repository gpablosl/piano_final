import tkinter as tk
import sounddevice as sd
import numpy as np
from threading import Thread, Event

class StreamThread(Thread):
    def __init__(self):
        super().__init__()
        self.dispoitivo_input = 1
        self.dispoitivo_output = 3
        self.tamano_bloque = 5500
        self.frecuencia_muestreo = 44100
        self.canales = 1
        self.tipo_dato = np.int16
        self.latencia = "low"

    def callback_stream(self, indata, outdata, frames, time, status):
        global app
        app.etiqueta_valor_estado["text"] = "Grabando"
        data = indata[:,0]
        transformada = np.fft.rfft(data)
        periodo_muestreo = 1/self.frecuencia_muestreo
        frecuencias = np.fft.rfftfreq(len(data), periodo_muestreo)
        frecuencia_fundamental = frecuencias[np.argmax(np.abs(transformada))]

        app.etiqueta_valor_ff["text"] = frecuencia_fundamental
        

        
        if frecuencia_fundamental >= 27 and frecuencia_fundamental <= 28:
            app.etiqueta_nota["text"] = "La (A0)"
        if frecuencia_fundamental >= 28.5 and frecuencia_fundamental <= 29.5:
            app.etiqueta_nota["text"] =  "A#0/Bb0)"
        if frecuencia_fundamental >= 29.51 and frecuencia_fundamental <= 31.4:
            app.etiqueta_nota["text"] = "Si (B0)"
        if frecuencia_fundamental >= 31.42 and frecuencia_fundamental <= 33.5:
           app.etiqueta_nota["text"] = "Do (C1)"
        if frecuencia_fundamental >= 33.6 and frecuencia_fundamental <= 35:
            app.etiqueta_nota["text"] = "Do sostenido / Re bemol (C#1/Db1)"
        if frecuencia_fundamental >= 35.1 and frecuencia_fundamental <= 37.5:
           app.etiqueta_nota["text"] = "Re (D1)"
        if frecuencia_fundamental >= 37.6 and frecuencia_fundamental <= 39.6:
            app.etiqueta_nota["text"] = "Re sostenido / Mi bemol (D#1/Eb1)"
        if frecuencia_fundamental >= 39.7 and frecuencia_fundamental <= 42:
            app.etiqueta_nota["text"] = "Mi (E1)"
        if frecuencia_fundamental >= 42.1 and frecuencia_fundamental <= 45:
            app.etiqueta_nota["text"] = "Fa (F1)"
        if frecuencia_fundamental >= 45.1 and frecuencia_fundamental <= 47.5:
           app.etiqueta_nota["text"] = "Fa sostenido/ Sol bemol (F#1/Gb1)"
        if frecuencia_fundamental >= 47.51 and frecuencia_fundamental <= 50:
           app.etiqueta_nota["text"] = "Sol (G1)"
        if frecuencia_fundamental >= 50.1 and frecuencia_fundamental <= 52.5:
            app.etiqueta_nota["text"] = "Sol sostenido / La bemol (G#1/Ab1)"
        if frecuencia_fundamental >= 52.5 and frecuencia_fundamental <= 57.5:
            app.etiqueta_nota["text"] = "La (A1)"
        if frecuencia_fundamental >= 57.6 and frecuencia_fundamental <= 60:
            app.etiqueta_nota["text"] = "La sostenido / Si bemol (A#1/Bb1)"
        if frecuencia_fundamental >= 60.1 and frecuencia_fundamental <= 63:
           app.etiqueta_nota["text"] = "Si (B1)"
        if frecuencia_fundamental >= 63.1 and frecuencia_fundamental <= 67:
            app.etiqueta_nota["text"] = "Do (C2)"
        if frecuencia_fundamental >= 67.1 and frecuencia_fundamental <= 71:
            app.etiqueta_nota["text"] = "Do sostenido / Re bemol (C#2/Db2)"
        if frecuencia_fundamental >= 71.1 and frecuencia_fundamental <= 75:
           app.etiqueta_nota["text"] = "Re (D2)"
        if frecuencia_fundamental >= 75.1 and frecuencia_fundamental <= 79.5:
            app.etiqueta_nota["text"] = "Re sostenido / Mi bemol (D#2/Eb2)"
        if frecuencia_fundamental >= 79.6 and frecuencia_fundamental <= 84:
            app.etiqueta_nota["text"] = "Mi (E2)"
        if frecuencia_fundamental >= 84.1 and frecuencia_fundamental <= 90:
            app.etiqueta_nota["text"] = "Fa (F2)"
        if frecuencia_fundamental >= 90.1 and frecuencia_fundamental <= 94.9:
            app.etiqueta_nota["text"] = "Fa sostenido/ Sol bemol (F#2/Gb2)"
        if frecuencia_fundamental >= 95 and frecuencia_fundamental <= 100:
            app.etiqueta_nota["text"] = "Sol (G2)"
        if frecuencia_fundamental >= 100.1 and frecuencia_fundamental <= 106:
            app.etiqueta_nota["text"] = "Sol sostenido / La bemol (G#2/Ab2)"
        if frecuencia_fundamental >= 106.1 and frecuencia_fundamental <= 113:
            app.etiqueta_nota["text"] = "La (A2)"
        if frecuencia_fundamental >= 113.1 and frecuencia_fundamental <= 119:
            app.etiqueta_nota["text"] = "La sostenido / Si bemol (A#2/Bb2)"
        if frecuencia_fundamental >= 119.1 and frecuencia_fundamental <= 126:
            app.etiqueta_nota["text"] = "Si (B2)"
        if frecuencia_fundamental >= 126.1 and frecuencia_fundamental <= 134:
            app.etiqueta_nota["text"] = "Do (C3)"
        if frecuencia_fundamental >= 134.1 and frecuencia_fundamental <= 141:
            app.etiqueta_nota["text"] = "Do sostenido / Re bemol (C#3/Db3)"
        if frecuencia_fundamental >= 141.1 and frecuencia_fundamental <= 151:
            app.etiqueta_nota["text"] = "Re (D3)"
        if frecuencia_fundamental >= 151.1 and frecuencia_fundamental <= 160:
           app.etiqueta_nota["text"] = "Re sostenido / Mi bemol (D#3/Eb3)"
        if frecuencia_fundamental >= 160.1 and frecuencia_fundamental <= 169:
           app.etiqueta_nota["text"] = "Mi (E3)"
        if frecuencia_fundamental >= 169.1 and frecuencia_fundamental <= 179:
            app.etiqueta_nota["text"] = "Fa (F3)"
        if frecuencia_fundamental >= 179.1 and frecuencia_fundamental <= 190:
            app.etiqueta_nota["text"] = "Fa sostenido/ Sol bemol (F#3/Gb3)"
        if frecuencia_fundamental >= 190.1  and frecuencia_fundamental <= 200.9:
            app.etiqueta_nota["text"] = "Sol (G3)"
        if frecuencia_fundamental >= 201 and frecuencia_fundamental <= 213.6:
            app.etiqueta_nota["text"] = "Sol sostenido / La bemol (G#3/Ab3)"
        if frecuencia_fundamental >= 213.7 and frecuencia_fundamental <= 225.5:
            app.etiqueta_nota["text"] = "La (A3)"
        if frecuencia_fundamental >= 225.6 and frecuencia_fundamental <= 238.08:
            app.etiqueta_nota["text"] = "La sostenido / Si bemol (A#3/Bb3)"
        if frecuencia_fundamental >= 238.09 and frecuencia_fundamental <= 251.9 :
            app.etiqueta_nota["text"] = "Si (B3)"
        if frecuencia_fundamental >= 252 and frecuencia_fundamental <= 266.6:
            app.etiqueta_nota["text"] = "Do (C4)"
        if frecuencia_fundamental >= 266.7 and frecuencia_fundamental <= 282.2:
           app.etiqueta_nota["text"] = "Do sostenido / Re bemol (C#4/Db4)"
        if frecuencia_fundamental >= 282.3 and frecuencia_fundamental <= 295.6:
            app.etiqueta_nota["text"] = "Re (D4)"
        if frecuencia_fundamental >= 295.7 and frecuencia_fundamental <= 316.2:
            app.etiqueta_nota["text"] = "Re sostenido / Mi bemol (D#4/Eb4)"
        if frecuencia_fundamental >=316.3  and frecuencia_fundamental <= 334.6:
            app.etiqueta_nota["text"] = "Mi (E4)"
        if frecuencia_fundamental >= 334.7 and frecuencia_fundamental <= 354.3:
            app.etiqueta_nota["text"] = "Fa (F4)"
        if frecuencia_fundamental >= 354.4 and frecuencia_fundamental <= 375:
           app.etiqueta_nota["text"] = "Fa sostenido/ Sol bemol (F#4/Gb4)"
        if frecuencia_fundamental >= 375.1 and frecuencia_fundamental <= 397:
            app.etiqueta_nota["text"] = "Sol (G4)"
        if frecuencia_fundamental >= 397.1 and frecuencia_fundamental <= 420.4:
            app.etiqueta_nota["text"] = "Sol sostenido / La bemol (G#4/Ab4)"
        if frecuencia_fundamental >= 420.5 and frecuencia_fundamental <= 455:
            app.etiqueta_nota["text"] = "La(A4)"
        if frecuencia_fundamental >= 455.1 and frecuencia_fundamental <= 476.2:
            app.etiqueta_nota["text"] = "La sostenido / Si bemol (A#4/Bb4)"
        if frecuencia_fundamental >= 476.3 and frecuencia_fundamental <= 504:
            app.etiqueta_nota["text"] = "Si (B4)"
        if frecuencia_fundamental >= 504.1 and frecuencia_fundamental <= 533.3:
            app.etiqueta_nota["text"] = "Do (C5)"
        if frecuencia_fundamental >= 533.4 and frecuencia_fundamental <= 564.4:
           app.etiqueta_nota["text"] = "Do sostenido / Re bemol (C#5/Db5)"
        if frecuencia_fundamental >= 564.5 and frecuencia_fundamental <= 597.4:
            app.etiqueta_nota["text"] = "Re (D5)"
        if frecuencia_fundamental >= 597.5 and frecuencia_fundamental <= 632.3:
           app.etiqueta_nota["text"] = "Re sostenido / Mi bemol (D#5/Eb5)"
        if frecuencia_fundamental >= 632.4 and frecuencia_fundamental <= 669.3:
            app.etiqueta_nota["text"] = "Mi (E5)"
        if frecuencia_fundamental >= 669.4 and frecuencia_fundamental <= 708.5:
            app.etiqueta_nota["text"] = "Fa(F5)"
        if frecuencia_fundamental >= 708.6 and frecuencia_fundamental <= 750:
            app.etiqueta_nota["text"] = "Fa sostenido/ Sol bemol (F#5/Gb5)"
        if frecuencia_fundamental >= 750.1 and frecuencia_fundamental <= 799:
            app.etiqueta_nota["text"] = "Sol (G5)"
        if frecuencia_fundamental >= 799.1 and frecuencia_fundamental <= 845.6:
            app.etiqueta_nota["text"] = "Sol sostenido / La bemol (G#5/Ab5)"
        if frecuencia_fundamental >= 845.7 and frecuencia_fundamental <= 900:
            app.etiqueta_nota["text"] = "La (A5)"
        if frecuencia_fundamental >= 900.1 and frecuencia_fundamental <= 950:
            app.etiqueta_nota["text"] = "La sostenido / Si bemol (A#5/Bb5)"
        if frecuencia_fundamental >= 950.1 and frecuencia_fundamental <= 1010:
           app.etiqueta_nota["text"] = "Si (B5)"
        if frecuencia_fundamental >= 1010.1 and frecuencia_fundamental <= 1070:
            app.etiqueta_nota["text"] = "Do (C6)"
        if frecuencia_fundamental >= 1070.1 and frecuencia_fundamental <= 1140:
            app.etiqueta_nota["text"] = "Do sostenido / Re bemol (C#6/Db6)"
        if frecuencia_fundamental >= 1140.1 and frecuencia_fundamental <= 1205:
            app.etiqueta_nota["text"] = "Re (D6)"
        if frecuencia_fundamental >= 1205.1 and frecuencia_fundamental <= 1280:
            app.etiqueta_nota["text"] = "Re sostenido / Mi bemol (D#6/Eb6)"
        if frecuencia_fundamental >= 1280.1 and frecuencia_fundamental <= 1350:
            app.etiqueta_nota["text"] = "Mi (E6)"
        if frecuencia_fundamental >= 1350.1 and frecuencia_fundamental <= 1430:
            app.etiqueta_nota["text"] = "Fa (F6)"
        if frecuencia_fundamental >= 1430.1 and frecuencia_fundamental <= 1510:
            app.etiqueta_nota["text"] = "Fa sostenido/ Sol bemol (F#6/Gb6)"
        if frecuencia_fundamental >= 1510.1 and frecuencia_fundamental <= 1610:
            app.etiqueta_nota["text"] = "Sol (G6)"
        if frecuencia_fundamental >= 1610.1 and frecuencia_fundamental <= 1710:
            app.etiqueta_nota["text"] = "Sol sostenido / La bemol (G#6/Ab6)"
        if frecuencia_fundamental >= 1710.1 and frecuencia_fundamental <= 1805:
            app.etiqueta_nota["text"] = "La (A6)"
        if frecuencia_fundamental >= 1805.1 and frecuencia_fundamental <= 1920:
            app.etiqueta_nota["text"] = "La sostenido / Si bemol (A#6/Bb6)"
        if frecuencia_fundamental >= 1920.1 and frecuencia_fundamental <= 2030:
           app.etiqueta_nota["text"] = "Si (B6)"
        if frecuencia_fundamental >= 2030.1 and frecuencia_fundamental <= 2150:
            app.etiqueta_nota["text"] = "Do (C7)"
        if frecuencia_fundamental >= 2150.1 and frecuencia_fundamental <= 2280:
            app.etiqueta_nota["text"] = "Do sostenido / Re bemol (C#7/Db7)"
        if frecuencia_fundamental >= 2280.1 and frecuencia_fundamental <= 2410:
            app.etiqueta_nota["text"] = "Re (D7)"
        if frecuencia_fundamental >= 2410.1 and frecuencia_fundamental <= 2530:
            app.etiqueta_nota["text"] = "Re sostenido / Mi bemol (D#7/Eb7)"
        if frecuencia_fundamental >= 2530.1 and frecuencia_fundamental <= 2700:
            app.etiqueta_nota["text"] = "Mi (E7)"
        if frecuencia_fundamental >= 2700.1 and frecuencia_fundamental <= 2860:
            app.etiqueta_nota["text"] = "Fa (F7)"
        if frecuencia_fundamental >= 2860.1 and frecuencia_fundamental <= 3050:
            app.etiqueta_nota["text"] = "Fa sostenido/ Sol bemol (F#7/Gb7)"
        if frecuencia_fundamental >= 3050.1 and frecuencia_fundamental <= 3250:
            app.etiqueta_nota["text"] = "Sol (G7)"
        if frecuencia_fundamental >= 3250.1 and frecuencia_fundamental <= 3420:
            app.etiqueta_nota["text"] = "Sol sostenido / La bemol (G#7/Ab7)"
        if frecuencia_fundamental >= 3420.1 and frecuencia_fundamental <= 3650:
            app.etiqueta_nota["text"] = "La (A7"
        if frecuencia_fundamental >= 3650.1 and frecuencia_fundamental <= 3820:
            app.etiqueta_nota["text"] = "La sostenido / Si bemol (A#7/Bb7)"
        if frecuencia_fundamental >= 3820.1 and frecuencia_fundamental <= 4020:
            app.etiqueta_nota["text"] ="Si (B7)"
        if frecuencia_fundamental >= 4020.1 and frecuencia_fundamental <= 4250:
            app.etiqueta_nota["text"] = "Do (C8)"


        if frecuencia_fundamental >= 27 and frecuencia_fundamental <= 31.41:
            app.etiqueta_Octava["text"] = "Octava 0"
        if frecuencia_fundamental >= 31.42 and frecuencia_fundamental <= 63:
            app.etiqueta_Octava["text"] = "Primera octava"
        if frecuencia_fundamental >= 63.1 and frecuencia_fundamental <= 126:
            app.etiqueta_Octava["text"] = "Segunda octava"
        if frecuencia_fundamental >= 126.1 and frecuencia_fundamental <= 251.9:
            app.etiqueta_Octava["text"] = "Tercera octava"
        if frecuencia_fundamental >= 252 and frecuencia_fundamental <= 504:
            app.etiqueta_Octava["text"] = "Cuarta octava"
        if frecuencia_fundamental >= 504.1 and frecuencia_fundamental <= 1010:
            app.etiqueta_Octava["text"] = "Quinta octava"
        if frecuencia_fundamental >= 1010.1 and frecuencia_fundamental <= 2030:
            app.etiqueta_Octava["text"] = "Sexta octava"
        if frecuencia_fundamental >= 2030.1 and frecuencia_fundamental <= 4020:
            app.etiqueta_Octava["text"] = "Septima octava"
        if frecuencia_fundamental >= 4020.1 and frecuencia_fundamental <= 4250:
            app.etiqueta_Octava["text"] = "Ultima octava"

        return

    def run(self):
        try:
            self.event = Event()
            with sd.Stream(
                device=(self.dispoitivo_input, self.dispoitivo_output), #Se eligen dispositivos (entrada, salida)
                blocksize= self.tamano_bloque, # 0 significa que la tarjeta de sonido decide el mejor tamaño
                samplerate= self.frecuencia_muestreo, # frecuencia de muestreo
                channels= self.canales, #numero de canales1
                dtype= self.tipo_dato, #Tipo de dato (profundidad de bits)
                latency=self.latencia, # Latencia, que tanto tiempo pasa desde entrada hasta la salida
                callback= self.callback_stream
            ) as self.stream:
                self.event.wait()

        except Exception as e:
            print(str(e))



#Heredamos de Tk para hacer una ventana
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #Establecer tiutlo de la ventana
        self.title("Aplicación de audio")
        #Establecemos tamaño
        self.geometry("400x300")

        boton_iniciar = tk.Button(self, width=20, text ="Iniciar grabación", command=lambda: self.click_boton_iniciar())
        boton_iniciar.grid(column=0, row= 0)

        boton_detener = tk.Button(self, width=20, text="Detener grabación", command= lambda: self.click_boton_detener())
        boton_detener.grid(column=1, row=0)

        etiqueta_estado = tk.Label(text="Estado: ")
        etiqueta_estado.grid(column=0, row=1)

        self.etiqueta_valor_estado = tk.Label(text="-")
        self.etiqueta_valor_estado.grid(column=1, row=1)

        etiqueta_frecuencia_fundamental = tk.Label(text= "Frecuencia fundamental: ")
        etiqueta_frecuencia_fundamental.grid(column=0, row= 2)

        self.etiqueta_valor_ff = tk.Label(text="-")
        self.etiqueta_valor_ff.grid(column=1, row= 2)

        etiqueta_Nombre_Nota = tk.Label(text= "Nota: ")
        etiqueta_Nombre_Nota.grid(column=0, row= 3)

        self.etiqueta_nota= tk.Label(text="-")
        self.etiqueta_nota.grid(column=1, row= 3)

        etiqueta_nombre_Octava = tk.Label(text= "Octava: ")
        etiqueta_nombre_Octava.grid(column=0, row= 4)

        self.etiqueta_Octava= tk.Label(text="-")
        self.etiqueta_Octava.grid(column=1, row= 4)

        self.stream_thread = StreamThread()

    def click_boton_iniciar(self):
        if not self.stream_thread.is_alive():
            self.stream_thread.daemon = True
            self.stream_thread.start()
        
    
    def click_boton_detener(self):
        if self.stream_thread.is_alive():
            self.etiqueta_valor_estado["text"] = "Grabación detenida"
            self.stream_thread.stream.abort()
            self.stream_thread.event.set()
            self.stream_thread.join()

app = App()
def main():
    app.mainloop()

if __name__ == "__main__":
    main()