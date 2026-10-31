# ==========================================
# ACTIVIDAD FORMATIVA 3
# Diseño de Filtros Digitales
# Autor: Miguel Angel Hilario Lopez
# ==========================================

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# ==========================================
# 1. GENERACIÓN DE SEÑAL DE PRUEBA
# ==========================================

fs = 1000  # Frecuencia de muestreo (Hz)

t = np.linspace(0, 1, fs, endpoint=False)

# Señal compuesta por varias frecuencias
senal = (
    np.sin(2*np.pi*50*t)
    + 0.5*np.sin(2*np.pi*150*t)
    + 0.3*np.sin(2*np.pi*300*t)
)

# Generación de ruido blanco
ruido = 0.4 * np.random.randn(len(t))

# Señal con ruido
senal_ruidosa = senal + ruido

# ==========================================
# 2. DISEÑO FILTROS IIR BUTTERWORTH
# ==========================================

# Pasa bajos
b_lp, a_lp = signal.butter(
    4,
    100/(fs/2),
    btype='low'
)

# Pasa altos
b_hp, a_hp = signal.butter(
    4,
    100/(fs/2),
    btype='high'
)

# Pasa bandas
b_bp, a_bp = signal.butter(
    4,
    [100/(fs/2), 250/(fs/2)],
    btype='band'
)

# ==========================================
# 3. APLICAR FILTROS IIR
# ==========================================

senal_lp = signal.filtfilt(
    b_lp,
    a_lp,
    senal_ruidosa
)

senal_hp = signal.filtfilt(
    b_hp,
    a_hp,
    senal_ruidosa
)

senal_bp = signal.filtfilt(
    b_bp,
    a_bp,
    senal_ruidosa
)

# ==========================================
# 4. FILTRO FIR
# ==========================================

coef_fir = signal.firwin(
    numtaps=51,
    cutoff=100,
    fs=fs,
    window='hamming'
)

senal_fir = signal.lfilter(
    coef_fir,
    1,
    senal_ruidosa
)

# ==========================================
# 5. GRAFICAS DE SEÑALES
# ==========================================

plt.figure(figsize=(12,10))

plt.subplot(5,1,1)
plt.plot(t, senal_ruidosa)
plt.title("Señal con Ruido")
plt.grid()

plt.subplot(5,1,2)
plt.plot(t, senal_lp, color='green')
plt.title("Filtro Pasa Bajos (IIR)")
plt.grid()

plt.subplot(5,1,3)
plt.plot(t, senal_hp, color='red')
plt.title("Filtro Pasa Altos (IIR)")
plt.grid()

plt.subplot(5,1,4)
plt.plot(t, senal_bp, color='purple')
plt.title("Filtro Pasa Bandas (IIR)")
plt.grid()

plt.subplot(5,1,5)
plt.plot(t, senal_fir, color='orange')
plt.title("Filtro FIR")
plt.grid()

plt.tight_layout()

plt.savefig("comparacion_filtros.png")

plt.show()

# ==========================================
# 6. RESPUESTA EN FRECUENCIA
# ==========================================

w, h = signal.freqz(
    b_lp,
    a_lp
)

plt.figure(figsize=(8,5))

plt.plot(
    (w/np.pi)*(fs/2),
    20*np.log10(np.abs(h))
)

plt.title("Respuesta en Frecuencia - Pasa Bajos")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Ganancia (dB)")
plt.grid()

plt.savefig("respuesta_frecuencia.png")

plt.show()

print("Proceso terminado correctamente")
print("Imagenes guardadas:")
print("- comparacion_filtros.png")
print("- respuesta_frecuencia.png")