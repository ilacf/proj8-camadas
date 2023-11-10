#Importe todas as bibliotecas
import suaBibSignal as sbs
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time
import soundfile

audio_modulado, samplerate = soundfile.read('modulado.wav')

calculo_fourier = sbs.signalMeu()
calculo_fourier.plotFFT(audio_modulado, samplerate)
plt.xlabel("frequencia")
plt.ylabel("sinal de audio modulado")
plt.show()

# demodular audio
audio_duration = len(audio_modulado)/samplerate
t = np.linspace(0, audio_duration, len(audio_modulado), endpoint=False)

w = 2 * np.pi * 14000
portadora = 1 * np.sin(w*t)

audio_demodulado = audio_modulado * portadora

# filtrar frequencias
a = 0.009235
b = 0.008398
c = 1
d = -1.734
e = 0.7521

audio_filtrado = [audio_demodulado[0], audio_demodulado[1]]
for k in range(2, len(audio_demodulado)):
      Y = -d * audio_filtrado[k - 1] - e * audio_filtrado[k - 2] + a * audio_demodulado[k - 1] + b * audio_demodulado[k - 2]
      audio_filtrado.append(Y)

# grafico 5
plt.plot(t, audio_demodulado)
plt.xlabel("tempo")
plt.ylabel("sinal de audio demodulado")
plt.show()

# grafico 6
calculo_fourier.plotFFT(audio_demodulado, samplerate)
plt.xlabel("frequencia")
plt.ylabel("sinal de audio demodulado")
plt.show()

# grafico 7
calculo_fourier.plotFFT(audio_filtrado, samplerate)
plt.xlabel("frequencia")
plt.ylabel("sinal de audio demodulado e filtrado")
plt.show()