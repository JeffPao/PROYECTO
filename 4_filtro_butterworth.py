from pathlib import Path
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, filtfilt
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

    # ====== FILTRADO DE PASO BAJO CON BUTTERWORTH ======
    frecuencia_corte = 20000  # Hz
    orden_filtro = 2 # Orden del filtro

    # Normalizar la frecuencia de corte en función de la frecuencia de muestreo
    nyquist = 0.5 * frecuencia_muestreo
    frecuencia_normalizada = frecuencia_corte / nyquist

    # Crear el filtro Butterworth
    b, a = butter(orden_filtro, frecuencia_normalizada, btype='low')
    datos_filtrados = filtfilt(b, a, datos_audio)
    datos_filtrados = np.int16(datos_filtrados)  # Convertir a enteros

    # ====== GUARDAR COMO WAV TEMPORAL ======
    nombre_archivo_temporal = ruta_archivo.with_name('Audio_Temporal.wav')
    wav.write(nombre_archivo_temporal, frecuencia_muestreo, datos_filtrados)

    # ====== CONVERTIR A MP3 ======
    nombre_archivo_mp3 = ruta_archivo.with_name('Audio_Reducido.mp3')
    audio = AudioSegment.from_wav(nombre_archivo_temporal)

    # Ajustes para reducir el tamaño
    bitrate = "32k"  # Cambia a un bitrate menor, como "64k" o "32k" para reducir el tamaño
    sample_rate = 16000  # Opcional: cambia a 16000 o 8000 para reducir aún más el tamaño y la calidad

    # Exportar el audio con ajustes
    audio.export(nombre_archivo_mp3, format="mp3", bitrate=bitrate, parameters=["-ar", str(sample_rate)])
    print(f'Archivo guardado en formato MP3 en: {nombre_archivo_mp3}')
    
    # ====== GRAFICAR TRANSFORMADA DE FOURIER ======
    transformada = np.fft.fft(datos_audio)
    frecuencias = np.fft.fftfreq(len(transformada), d=1/frecuencia_muestreo)

    plt.figure(figsize=(10, 6))
    plt.plot(frecuencias[:len(frecuencias)//2], np.abs(transformada)[:len(frecuencias)//2])  # Solo la mitad positiva del espectro
    plt.title('Transformada de Fourier del Audio')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.show()
else:
    print("El archivo no existe en la ruta especificada.")
