#importe as bibliotecas
import suaBibSignal as sbs
import numpy as np
import sounddevice as sd
import time
import soundfile
import matplotlib.pyplot as plt
from scipy import signal

amplitudes, samplerate = soundfile.read('swishes.wav')
# sd.play(amplitudes)
# time.sleep(5)

maximo = amplitudes.max()
minimo = amplitudes.min()
print(f"Valores antes da normalizacao: minimo {minimo} e maximo {maximo} \n")

diferenca = maximo - minimo # para deixar o minimo como 0

audio_normalizado = []
for amplitude in amplitudes:
      audio_normalizado.append((amplitude-minimo)/diferenca)
sd.play(audio_normalizado)
time.sleep(5)

maximo2 = max(audio_normalizado)
minimo2 = min(audio_normalizado)
print(f"Checando se foi normalizado: minimo {minimo2} e maximo {maximo2}")

nyq_rate = samplerate/2
width = 5.0/nyq_rate
ripple_db = 60.0 #dB
N , beta = signal.kaiserord(ripple_db, width)
cutoff_hz = 4000.0
taps = signal.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))

audio_filtrado = signal.lfilter(taps, 1.0, audio_normalizado)
sd.play(audio_filtrado)
time.sleep(5)

audio_duration = len(audio_filtrado)/samplerate

t = np.linspace(0, audio_duration, len(audio_filtrado), endpoint=False)
w = 2 * np.pi * 14000
portadora = 1 * np.sin(w*t)

audio_modulado = audio_filtrado * portadora
maximo_absoluto = np.max(np.abs(audio_modulado))
audio_normalizado2 = audio_modulado/maximo_absoluto
# sd.play(audio_normalizado2)
# time.sleep(5)

soundfile.write('modulado.wav', audio_normalizado2, samplerate)

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