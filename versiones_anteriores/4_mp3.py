from pathlib import Path
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment

# ====== CARGAR AUDIO ======
carpeta_principal = Path('Recursos')
nombre_archivo = 'In_Piano.wav'
ruta_archivo = carpeta_principal / nombre_archivo

if ruta_archivo.exists():
    frecuencia_muestreo, datos_audio = wav.read(ruta_archivo)
    if len(datos_audio.shape) > 1:
        datos_audio = np.mean(datos_audio, axis=1)  # Promediar los dos canales
        datos_audio = np.int16(datos_audio)  # Convertir a enteros

    # ====== TRANSFORMADA DE FOURIER ======
    transformada = np.fft.fft(datos_audio)
    frecuencias = np.fft.fftfreq(len(transformada), d=1/frecuencia_muestreo)

    # ====== FILTRADO DE PASO BAJO ======
    frecuencia_corte = 10000  # 10 kHz
    transformada_filtrada = np.where(np.abs(frecuencias) > frecuencia_corte, 0, transformada)

    # ====== TRANSFORMADA INVERSA ======
    datos_filtrados = np.fft.ifft(transformada_filtrada).real
    datos_filtrados = np.int16(datos_filtrados)

    # ====== GUARDAR COMO WAV TEMPORAL ======
    nombre_archivo_temporal = 'Audio_Temporal.wav'
    wav.write(nombre_archivo_temporal, frecuencia_muestreo, datos_filtrados)

    # ====== CONVERTIR A MP3 ======
    nombre_archivo_mp3 = 'Audio_Reducido.mp3'
    ruta_salida_mp3 = carpeta_principal / nombre_archivo_mp3
    audio = AudioSegment.from_wav(nombre_archivo_temporal)
    audio.export(ruta_salida_mp3, format="mp3", bitrate="128k")
    print(f'Archivo guardado en formato MP3 en: {ruta_salida_mp3}')

else:
    print("El archivo no existe en la ruta especificada.")