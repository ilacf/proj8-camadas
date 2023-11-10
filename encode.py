#importe as bibliotecas
import suaBibSignal as sbs
import numpy as np
import sounddevice as sd
import time
import soundfile
import matplotlib.pyplot as plt
from scipy import signal

audio_original, samplerate = soundfile.read('swishes.wav')
# sd.play(amplitudes)
# time.sleep(5)

# valores adquiridos no matblab atraves da tf discreta com f sendo 1000:
a = 0.009235
b = 0.008398
c = 1
d = -1.734
e = 0.7521

audio_filtrado = [audio_original[0], audio_original[1]]
for k in range(2, len(audio_original)):
      Y = -d * audio_filtrado[k - 1] - e * audio_filtrado[k - 2] + a * audio_original[k - 1] + b * audio_original[k - 2]
      audio_filtrado.append(Y)
# sd.play(audio_filtrado)
# time.sleep(5)

audio_duration = len(audio_filtrado)/samplerate

t = np.linspace(0, audio_duration, len(audio_filtrado), endpoint=False)

w_portadora = 2 * np.pi * 14000
portadora = 1 * np.sin(w_portadora*t)

audio_modulado = audio_filtrado * portadora
maximo_absoluto = np.max(np.abs(audio_modulado))

audio_normalizado = audio_modulado/maximo_absoluto
# sd.play(audio_normalizado)
# time.sleep(5)

soundfile.write('modulado.wav', audio_normalizado, samplerate)

calculo_fourier = sbs.signalMeu()

# grafico 1
plt.plot(t, audio_normalizado)
plt.xlabel("tempo")
plt.ylabel("sinal de audio original normalizado")
plt.show()

# grafico 2
plt.plot(t, audio_filtrado)
plt.xlabel("tempo")
plt.ylabel("sinal de audio filtrado")
plt.show()

# grafico 3
calculo_fourier.plotFFT(audio_filtrado, samplerate)
plt.xlabel("frequencia")
plt.ylabel("sinal de audio filtrado")
plt.show()

# grafico 4
plt.plot(t, audio_modulado)
plt.xlabel("tempo")
plt.ylabel("sinal de audio modulado")
plt.show()

# grafico 5
calculo_fourier.plotFFT(audio_modulado, samplerate)
plt.xlabel("frequencia")
plt.ylabel("sinal de audio modulado")
plt.show()