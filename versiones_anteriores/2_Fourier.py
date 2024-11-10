from pathlib import Path
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np

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
    # Solo aplicamos el filtro en frecuencias mayores a 10 kHz
    frecuencia_corte = 10000  # 10 kHz
    transformada_filtrada = np.where(np.abs(frecuencias) > frecuencia_corte, 0, transformada)

    # ====== TRANSFORMADA INVERSA ======
    datos_filtrados = np.fft.ifft(transformada_filtrada).real
    datos_filtrados = np.int16(datos_filtrados)

    # ====== GUARDAR AUDIO RESULTANTE ======
    nombre_archivo_salida = 'Audio_Reducido.wav'
    ruta_salida = carpeta_principal / nombre_archivo_salida
    wav.write(ruta_salida, frecuencia_muestreo, datos_filtrados)
    print(f'Archivo reducido guardado en: {ruta_salida}')

    # ====== GRÁFICA AUDIO REDUCIDO ======
    duracion = len(datos_filtrados) / frecuencia_muestreo
    tiempo = np.linspace(0., duracion, len(datos_filtrados))
    plt.figure(figsize=(10, 8))
    plt.plot(tiempo, datos_filtrados, color='blue')
    plt.ylabel("Amplitud")
    plt.title("Forma de Onda del Audio Reducido con Filtro")
    plt.grid()
    plt.show()
else:
    print("El archivo no existe en la ruta especificada.")
