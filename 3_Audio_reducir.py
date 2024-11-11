from pydub import AudioSegment
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ====== CARGAR AUDIO ORIGINAL ======
carpeta_principal = Path('Recursos')
nombre_archivo = 'In_Piano.wav'
ruta_archivo = carpeta_principal / nombre_archivo

if ruta_archivo.exists():
    # Cargar el archivo WAV original
    frecuencia_muestreo, datos_audio = wav.read(ruta_archivo)
    if len(datos_audio.shape) > 1:
        datos_audio = np.mean(datos_audio, axis=1)  # Promediar los dos canales
        datos_audio = np.int16(datos_audio)  # Convertir a enteros

    # ====== TRANSFORMADA DE FOURIER (Original) ======
    transformada_original = np.fft.fft(datos_audio)
    frecuencias_original = np.fft.fftfreq(len(transformada_original), d=1/frecuencia_muestreo)

    # ====== GUARDAR COMO WAV TEMPORAL ======
    nombre_archivo_temporal = ruta_archivo.with_name('Audio_Temporal.wav')
    wav.write(nombre_archivo_temporal, frecuencia_muestreo, datos_audio)

    # ====== CONVERTIR A MP3 ======
    nombre_archivo_mp3 = ruta_archivo.with_name('Audio_Reducido.mp3')
    audio = AudioSegment.from_wav(nombre_archivo_temporal)
    audio.export(nombre_archivo_mp3, format="mp3", bitrate="128k")
    print(f'Archivo guardado en formato MP3 en: {nombre_archivo_mp3}')

    # ====== CARGAR AUDIO COMPRIMIDO ======
    audio_comprimido = AudioSegment.from_mp3(nombre_archivo_mp3)
    nombre_archivo_comprimido_wav = ruta_archivo.with_name('Audio_Comprimido.wav')
    audio_comprimido.export(nombre_archivo_comprimido_wav, format="wav")
    frecuencia_muestreo_comprimido, datos_audio_comprimido = wav.read(nombre_archivo_comprimido_wav)
    
    if len(datos_audio_comprimido.shape) > 1:
        datos_audio_comprimido = np.mean(datos_audio_comprimido, axis=1)
        datos_audio_comprimido = np.int16(datos_audio_comprimido)

    # ====== TRANSFORMADA DE FOURIER (Comprimido) ======
    transformada_comprimido = np.fft.fft(datos_audio_comprimido)
    frecuencias_comprimido = np.fft.fftfreq(len(transformada_comprimido), d=1/frecuencia_muestreo_comprimido)

    # ====== GRAFICAR TRANSFORMADA DE FOURIER ======
    plt.figure(figsize=(10, 6))

    # Gráfica del audio original
    plt.subplot(2, 1, 1)
    plt.plot(frecuencias_original[:len(frecuencias_original)//2], np.abs(transformada_original)[:len(frecuencias_original)//2])
    plt.title('Transformada de Fourier del Audio Original')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud')
    plt.grid(True)

    # Gráfica del audio comprimido
    plt.subplot(2, 1, 2)
    plt.plot(frecuencias_comprimido[:len(frecuencias_comprimido)//2], np.abs(transformada_comprimido)[:len(frecuencias_comprimido)//2])
    plt.title('Transformada de Fourier del Audio Comprimido')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

else:
    print("El archivo no existe en la ruta especificada.")
