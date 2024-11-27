import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import scipy.io.wavfile as wav
from scipy.signal import butter

# ====== CARGAR AUDIO ======
carpeta_principal = Path('Recursos')
nombre_archivo = 'Centro_comercial.wav'
ruta_archivo = carpeta_principal / nombre_archivo

# Leer el archivo WAV
frecuencia_muestreo, datos_audio = wav.read(ruta_archivo)

# Calcular la duración del audio (en segundos)
d = len(datos_audio) / frecuencia_muestreo

# Si el audio es estéreo (2 canales), combinar los canales para convertirlo a mono
if len(datos_audio.shape) > 1:  # Verifica si es estéreo
    datos_audio = 0.5 * (datos_audio[:, 0] + datos_audio[:, 1])  # Promedio de ambos canales
else:
    datos_audio = datos_audio  # Si ya es mono, no hacer nada

# ====== TRANSFORMADA DE FOURIER ======
transformada = np.fft.fft(datos_audio)  # Usar `datos_audio` para asegurar que es mono
frecuencias = np.fft.fftfreq(len(transformada), d=1/frecuencia_muestreo)

# Normalización de la transformada de Fourier entre 0 y 1
max_amplitud = np.max(np.abs(transformada))  # Valor máximo absoluto en el espectro
transformada_normalizada = np.abs(transformada) / max_amplitud  # Normalizar entre 0 y 1

# Definir la frecuencia de corte del filtro Butterworth (en Hz)
frecuencia_corte = 1000  # Hz

# Crear el filtro Butterworth (sobre todo el espectro)
nyquist = 0.5 * frecuencia_muestreo
frecuencia_normalizada = frecuencia_corte / nyquist
orden_filtro = 2 # Orden del filtro
b, a = butter(orden_filtro, frecuencia_normalizada, btype='low')

# Filtrar la transformada de Fourier (espectro de frecuencias)
# Para aplicar el filtro, multiplicamos el filtro con las frecuencias de la transformada
# Creamos un filtro de paso bajo en el dominio de la frecuencia
filtro_pasa_bajo = np.zeros_like(frecuencias)
filtro_pasa_bajo[np.abs(frecuencias) <= frecuencia_corte] = 1  # Frecuencias menores o iguales a la corte

# Aplicar el filtro al espectro de la transformada
transformada_filtrada = transformada * filtro_pasa_bajo

# Aplicar la transformada inversa de Fourier para obtener la señal filtrada en el dominio del tiempo
audio_filtrado = np.fft.ifft(transformada_filtrada)
audio_filtrado = np.real(audio_filtrado)  # Tomar la parte real (despreciando cualquier pequeña parte imaginaria)

# ====== GRAFICAS ======
# Crear subgráficas (4 en una figura)
fig, ax = plt.subplots(4, 1, figsize=(10, 8))

# Gráfica de la señal de audio original en el dominio del tiempo
ax[0].plot(np.linspace(0, d, len(datos_audio)), datos_audio)
ax[0].set_title('Señal de audio original')
ax[0].set_xlabel('Tiempo [s]')
ax[0].set_ylabel('Amplitud')
ax[0].grid(True)

# Gráfica de la transformada de Fourier original
ax[1].plot(frecuencias, transformada_normalizada, label='Transformada de Fourier Original')
ax[1].set_title('Transformada de Fourier del Audio (Original)')
ax[1].set_xlabel('Frecuencia [Hz]')
ax[1].set_ylabel('Amplitud Normalizada')
ax[1].grid(True)
ax[1].legend()

# Gráfica de la transformada de Fourier filtrada
ax[2].plot(frecuencias, np.abs(transformada_filtrada) / max_amplitud, label='Transformada Filtrada')
ax[2].set_title('Transformada de Fourier Filtrada')
ax[2].set_xlabel('Frecuencia [Hz]')
ax[2].set_ylabel('Amplitud Normalizada')
ax[2].grid(True)
ax[2].legend()

# Gráfica de la señal de audio filtrada en el dominio del tiempo
ax[3].plot(np.linspace(0, d, len(audio_filtrado)), audio_filtrado)
ax[3].set_title('Señal Filtrada (Dominio del Tiempo)')
ax[3].set_xlabel('Tiempo [s]')
ax[3].set_ylabel('Amplitud')
ax[3].grid(True)

# Mostrar gráficas
plt.tight_layout()
plt.show()

# ====== GUARDAR AUDIO FILTRADO ======
nombre_archivo_filtrado = ruta_archivo.with_name('Audio_Filtrado_centro.wav')
wav.write(nombre_archivo_filtrado, frecuencia_muestreo, np.int16(audio_filtrado))  # Guardamos el archivo filtrado
print(f'Archivo de audio filtrado guardado en: {nombre_archivo_filtrado}')
