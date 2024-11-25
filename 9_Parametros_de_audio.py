import os
from scipy.io import wavfile
from pydub import AudioSegment
import numpy as np
from pathlib import Path

# ====== CARGAR AUDIO ======
carpeta_principal = Path('Recursos')
nombre_archivo = 'In_Piano.wav'
nombre_archivo_mp3 = 'Audio_Reducido.mp3'  # Define nombre_archivo_mp3 aquí
ruta_archivo_wav = carpeta_principal / nombre_archivo
ruta_archivo_mp3 = carpeta_principal / nombre_archivo_mp3

# ====== CARGAR AUDIO ORIGINAL ======
frecuencia_muestreo, datos_audio_original = wavfile.read(ruta_archivo_wav)

# Convertir a mono si es estéreo
if len(datos_audio_original.shape) > 1:
    datos_audio_original = np.mean(datos_audio_original, axis=1).astype(np.int16)

# ====== CARGAR AUDIO COMPRIMIDO ======
audio_mp3 = AudioSegment.from_mp3(ruta_archivo_mp3)
datos_audio_mp3 = np.array(audio_mp3.get_array_of_samples())

# Convertir a mono si es estéreo
if audio_mp3.channels > 1:
    datos_audio_mp3 = np.mean(datos_audio_mp3.reshape(-1, audio_mp3.channels), axis=1).astype(np.int16)

# ====== CALCULAR TAMAÑO Y TASA DE BITS ======
tamaño_wav = os.path.getsize(ruta_archivo_wav)
tamaño_mp3 = os.path.getsize(ruta_archivo_mp3)
duración_segundos = len(datos_audio_original) / frecuencia_muestreo

tasa_bits_wav = (tamaño_wav * 8) / duración_segundos
tasa_bits_mp3 = (tamaño_mp3 * 8) / duración_segundos

# ====== CALCULAR RELACIÓN DE COMPRESIÓN ======
relacion_compresion = tamaño_wav / tamaño_mp3

# ====== CALCULAR EL ERROR CUADRÁTICO MEDIO (ECM) ======
# Alinear tamaños de los arreglos
min_len = min(len(datos_audio_original), len(datos_audio_mp3))
datos_audio_original = datos_audio_original[:min_len]
datos_audio_mp3 = datos_audio_mp3[:min_len]

# Calcular ECM
ecm = np.mean((datos_audio_original - datos_audio_mp3) ** 2)

# ====== IMPRIMIR RESULTADOS ======
print("Tamaño del archivo WAV original:", tamaño_wav, "bytes")
print("Tamaño del archivo MP3 comprimido:", tamaño_mp3, "bytes")
print("Tasa de bits WAV:", tasa_bits_wav, "bps")
print("Tasa de bits MP3:", tasa_bits_mp3, "bps")
print("Relación de compresión:", relacion_compresion)
print("Error Cuadrático Medio (ECM) entre las señales:", ecm)
