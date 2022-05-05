from threading import Thread, Event
import numpy as np
import sounddevice as sd

class StreamThread(Thread):

    def __init__(self, app):
        super().__init__()        
        self.dispoitivo_input = 1
        self.dispoitivo_output = 3
        self.tamano_bloque = 8000
        self.frecuencia_muestreo = 44100
        self.canales = 1
        self.tipo_dato = np.int16
        self.latencia = "low"
        self.app = app

    def callback_stream(self, indata, outdata, frames, time, status):

        data = indata[:,0]
        transformada = np.fft.rfft(data)
        periodo_muestreo = 1/self.frecuencia_muestreo
        frecuencias = np.fft.rfftfreq(len(data), periodo_muestreo)
        frecuencia_fundamental = frecuencias[np.argmax(np.abs(transformada))]
        print("frecuencia fundamental: " + str(frecuencias[np.argmax(np.abs(transformada))]))

        if frecuencia_fundamental >= 27 and frecuencia_fundamental <= 28:
            print("La (A0)")
        if frecuencia_fundamental >= 28.5 and frecuencia_fundamental <= 29.5:
            print("La sostenido / Si bemol (A#0/Bb0)")
        if frecuencia_fundamental >= 29.51 and frecuencia_fundamental <= 31.4:
            print("Si (B0)")
        if frecuencia_fundamental >= 31.42 and frecuencia_fundamental <= 33.5:
            print("Do (C1)")
        if frecuencia_fundamental >= 33.6 and frecuencia_fundamental <= 35:
            print("Do sostenido / Re bemol (C#1/Db1)")
        if frecuencia_fundamental >= 35.1 and frecuencia_fundamental <= 37.5:
            print("Re (D1)")
        if frecuencia_fundamental >= 37.6 and frecuencia_fundamental <= 39.6:
            print("Re sostenido / Mi bemol (D#1/Eb1)")
        if frecuencia_fundamental >= 39.7 and frecuencia_fundamental <= 42:
            print("Mi (E1)")
        if frecuencia_fundamental >= 42.1 and frecuencia_fundamental <= 45:
            print("Fa (F1)")
        if frecuencia_fundamental >= 45.1 and frecuencia_fundamental <= 47.5:
            print("Fa sostenido/ Sol bemol (F#1/Gb1)")
        if frecuencia_fundamental >= 47.51 and frecuencia_fundamental <= 50:
            print("Sol (G1)")
        if frecuencia_fundamental >= 50.1 and frecuencia_fundamental <= 52.5:
            print("Sol sostenido / La bemol (G#1/Ab1)")
        if frecuencia_fundamental >= 52.5 and frecuencia_fundamental <= 57.5:
            print("La (A1)")
        if frecuencia_fundamental >= 57.6 and frecuencia_fundamental <= 60:
            print("La sostenido / Si bemol (A#1/Bb1)")
        if frecuencia_fundamental >= 60.1 and frecuencia_fundamental <= 63:
            print("Si (B1)")
        if frecuencia_fundamental >= 63.1 and frecuencia_fundamental <= 67:
            print("Do (C2)")
        if frecuencia_fundamental >= 67.1 and frecuencia_fundamental <= 71:
            print("Do sostenido / Re bemol (C#2/Db2)")
        if frecuencia_fundamental >= 71.1 and frecuencia_fundamental <= 75:
            print("Re (D2)")
        if frecuencia_fundamental >= 75.1 and frecuencia_fundamental <= 79.5:
            print("Re sostenido / Mi bemol (D#2/Eb2)")
        if frecuencia_fundamental >= 79.6 and frecuencia_fundamental <= 84:
            print("Mi (E2)")
        if frecuencia_fundamental >= 84.1 and frecuencia_fundamental <= 90:
            print("Fa (F2)")
        if frecuencia_fundamental >= 90.1 and frecuencia_fundamental <= 94.9:
            print("Fa sostenido/ Sol bemol (F#2/Gb2)")
        if frecuencia_fundamental >= 95 and frecuencia_fundamental <= 100:
            print("Sol (G2)")
        if frecuencia_fundamental >= 100.1 and frecuencia_fundamental <= 106:
            print("Sol sostenido / La bemol (G#2/Ab2)")
        if frecuencia_fundamental >= 106.1 and frecuencia_fundamental <= 113:
            print("La (A2)")
        if frecuencia_fundamental >= 113.1 and frecuencia_fundamental <= 119:
            print("La sostenido / Si bemol (A#2/Bb2)")
        if frecuencia_fundamental >= 119.1 and frecuencia_fundamental <= 126:
            print("Si (B2)")
        if frecuencia_fundamental >= 126.1 and frecuencia_fundamental <= 134:
            print("Do (C3)")
        if frecuencia_fundamental >= 134.1 and frecuencia_fundamental <= 141:
            print("Do sostenido / Re bemol (C#3/Db3)")
        if frecuencia_fundamental >= 141.1 and frecuencia_fundamental <= 151:
            print("Re (D3)")
        if frecuencia_fundamental >= 151.1 and frecuencia_fundamental <= 160:
            print("Re sostenido / Mi bemol (D#3/Eb3)")
        if frecuencia_fundamental >= 160.1 and frecuencia_fundamental <= 169:
            print("Mi (E3)")
        if frecuencia_fundamental >= 169.1 and frecuencia_fundamental <= 179:
            print("Fa (F3)")
        if frecuencia_fundamental >= 179.1 and frecuencia_fundamental <= 190:
            print("Fa sostenido/ Sol bemol (F#3/Gb3)")
        if frecuencia_fundamental >= 190.1  and frecuencia_fundamental <= 200.9:
            print("Sol (G3)")
        if frecuencia_fundamental >= 201 and frecuencia_fundamental <= 213.6:
            print("Sol sostenido / La bemol (G#3/Ab3)")
        if frecuencia_fundamental >= 213.7 and frecuencia_fundamental <= 225.5:
            print("La (A3)")
        if frecuencia_fundamental >= 225.6 and frecuencia_fundamental <= 238.08:
            print("La sostenido / Si bemol (A#3/Bb3)")
        if frecuencia_fundamental >= 238.09 and frecuencia_fundamental <= 251.9 :
            print("Si (B3)")
        if frecuencia_fundamental >= 252 and frecuencia_fundamental <= 266.6:
            print("Do (C4)")
        if frecuencia_fundamental >= 266.7 and frecuencia_fundamental <= 282.2:
            print("Do sostenido / Re bemol (C#4/Db4)")
        if frecuencia_fundamental >= 282.3 and frecuencia_fundamental <= 295.6:
            print("Re (D4)")
        if frecuencia_fundamental >= 295.7 and frecuencia_fundamental <= 316.2:
            print("Re sostenido / Mi bemol (D#4/Eb4)")
        if frecuencia_fundamental >=316.3  and frecuencia_fundamental <= 334.6:
            print("Mi (E4)")
        if frecuencia_fundamental >= 334.7 and frecuencia_fundamental <= 354.3:
            print("Fa (F4)")
        if frecuencia_fundamental >= 354.4 and frecuencia_fundamental <= 375:
            print("Fa sostenido/ Sol bemol (F#4/Gb4)")
        if frecuencia_fundamental >= 375.1 and frecuencia_fundamental <= 397:
            print("Sol (G4)")
        if frecuencia_fundamental >= 397.1 and frecuencia_fundamental <= 420.4:
            print("Sol sostenido / La bemol (G#4/Ab4)")
        if frecuencia_fundamental >= 420.5 and frecuencia_fundamental <= 455:
            print("La(A4)")
        if frecuencia_fundamental >= 455.1 and frecuencia_fundamental <= 476.2:
            print("La sostenido / Si bemol (A#4/Bb4)")
        if frecuencia_fundamental >= 476.3 and frecuencia_fundamental <= 504:
            print("Si (B4)")
        if frecuencia_fundamental >= 504.1 and frecuencia_fundamental <= 533.3:
            print("Do (C5)")
        if frecuencia_fundamental >= 533.4 and frecuencia_fundamental <= 564.4:
            print("Do sostenido / Re bemol (C#5/Db5)")
        if frecuencia_fundamental >= 564.5 and frecuencia_fundamental <= 597.4:
            print("Re (D5)")
        if frecuencia_fundamental >= 597.5 and frecuencia_fundamental <= 632.3:
            print("Re sostenido / Mi bemol (D#5/Eb5)")
        if frecuencia_fundamental >= 632.4 and frecuencia_fundamental <= 669.3:
            print("Mi (E5)")
        if frecuencia_fundamental >= 669.4 and frecuencia_fundamental <= 708.5:
            print("Fa(F5)")
        if frecuencia_fundamental >= 708.6 and frecuencia_fundamental <= 750:
            print("Fa sostenido/ Sol bemol (F#5/Gb5)")
        if frecuencia_fundamental >= 750.1 and frecuencia_fundamental <= 799:
            print("Sol (G5)")
        if frecuencia_fundamental >= 799.1 and frecuencia_fundamental <= 845.6:
            print("Sol sostenido / La bemol (G#5/Ab5)")
        if frecuencia_fundamental >= 845.7 and frecuencia_fundamental <= 900:
            print("La (A5)")
        if frecuencia_fundamental >= 900.1 and frecuencia_fundamental <= 950:
            print("La sostenido / Si bemol (A#5/Bb5)")
        if frecuencia_fundamental >= 950.1 and frecuencia_fundamental <= 1010:
            print("Si (B5)")
        if frecuencia_fundamental >= 1010.1 and frecuencia_fundamental <= 1070:
            print("Do (C6)")
        if frecuencia_fundamental >= 1070.1 and frecuencia_fundamental <= 1140:
            print("Do sostenido / Re bemol (C#6/Db6)")
        if frecuencia_fundamental >= 1140.1 and frecuencia_fundamental <= 1205:
            print("Re (D6)")
        if frecuencia_fundamental >= 1205.1 and frecuencia_fundamental <= 1280:
            print("Re sostenido / Mi bemol (D#6/Eb6)")
        if frecuencia_fundamental >= 1280.1 and frecuencia_fundamental <= 1350:
            print("Mi (E6)")
        if frecuencia_fundamental >= 1350.1 and frecuencia_fundamental <= 1430:
            print("Fa (F6)")
        if frecuencia_fundamental >= 1430.1 and frecuencia_fundamental <= 1510:
            print("Fa sostenido/ Sol bemol (F#6/Gb6)")
        if frecuencia_fundamental >= 1510.1 and frecuencia_fundamental <= 1610:
            print("Sol (G6)")
        if frecuencia_fundamental >= 1610.1 and frecuencia_fundamental <= 1710:
            print("Sol sostenido / La bemol (G#6/Ab6)")
        if frecuencia_fundamental >= 1710.1 and frecuencia_fundamental <= 1805:
            print("La (A6)")
        if frecuencia_fundamental >= 1805.1 and frecuencia_fundamental <= 1920:
            print("La sostenido / Si bemol (A#6/Bb6)")
        if frecuencia_fundamental >= 1920.1 and frecuencia_fundamental <= 2030:
            print("Si (B6)")
        if frecuencia_fundamental >= 2030.1 and frecuencia_fundamental <= 2150:
            print("Do (C7)")
        if frecuencia_fundamental >= 2150.1 and frecuencia_fundamental <= 2280:
            print("Do sostenido / Re bemol (C#7/Db7)")
        if frecuencia_fundamental >= 2280.1 and frecuencia_fundamental <= 2410:
            print("Re (D7)")
        if frecuencia_fundamental >= 2410.1 and frecuencia_fundamental <= 2530:
            print("Re sostenido / Mi bemol (D#7/Eb7)")
        if frecuencia_fundamental >= 2530.1 and frecuencia_fundamental <= 2700:
            print("Mi (E7)")
        if frecuencia_fundamental >= 2700.1 and frecuencia_fundamental <= 2860:
            print("Fa (F7)")
        if frecuencia_fundamental >= 2860.1 and frecuencia_fundamental <= 3050:
            print("Fa sostenido/ Sol bemol (F#7/Gb7)")
        if frecuencia_fundamental >= 3050.1 and frecuencia_fundamental <= 3250:
            print("Sol (G7)")
        if frecuencia_fundamental >= 3250.1 and frecuencia_fundamental <= 3420:
            print("Sol sostenido / La bemol (G#7/Ab7)")
        if frecuencia_fundamental >= 3420.1 and frecuencia_fundamental <= 3650:
            print("La (A7")
        if frecuencia_fundamental >= 3650.1 and frecuencia_fundamental <= 3820:
            print("La sostenido / Si bemol (A#7/Bb7)")
        if frecuencia_fundamental >= 3820.1 and frecuencia_fundamental <= 4020:
            print("Si (B7)")
        if frecuencia_fundamental >= 4020.1 and frecuencia_fundamental <= 4250:
            print("Do (C8)")


        if frecuencia_fundamental >= 27 and frecuencia_fundamental <= 31.41:
            print("Octava 0")
            print("")
        if frecuencia_fundamental >= 31.42 and frecuencia_fundamental <= 63:
            print("Primera octava")
            print("")
        if frecuencia_fundamental >= 63.1 and frecuencia_fundamental <= 126:
            print("Segunda octava")
            print("")
        if frecuencia_fundamental >= 126.1 and frecuencia_fundamental <= 251.9:
            print("Tercera octava")
            print("")
        if frecuencia_fundamental >= 252 and frecuencia_fundamental <= 504:
            print("Cuarta octava")
            print("")
        if frecuencia_fundamental >= 504.1 and frecuencia_fundamental <= 1010:
            print("Quinta octava")
            print("")
        if frecuencia_fundamental >= 1010.1 and frecuencia_fundamental <= 2030:
            print("Sexta octava")
            print("")
        if frecuencia_fundamental >= 2030.1 and frecuencia_fundamental <= 4020:
            print("Septima octava")
            print("")
        if frecuencia_fundamental >= 4020.1 and frecuencia_fundamental <= 4250:
            print("Ultima octava")
            print("")

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

