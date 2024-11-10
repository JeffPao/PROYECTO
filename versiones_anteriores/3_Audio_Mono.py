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
    
    # ====== CONVERTIR A MONO ======
    if len(datos_audio.shape) > 1:
        datos_audio = np.mean(datos_audio, axis=1)  # Promediar los dos canales
        datos_audio = np.int16(datos_audio)  # Convertir a enteros
    
    # ====== GUARDAR EL AUDIO MONO ======
    nombre_archivo_mono = 'InPianoMONO.wav'
    ruta_salida = carpeta_principal / nombre_archivo_mono
    wav.write(ruta_salida, frecuencia_muestreo, datos_audio)
    print(f'Archivo en mono guardado en: {ruta_salida}')

    # ====== GRÁFICA DEL AUDIO MONO ======
    duracion = len(datos_audio) / frecuencia_muestreo
    tiempo = np.linspace(0., duracion, len(datos_audio))
    plt.figure(figsize=(10, 8))
    plt.plot(tiempo, datos_audio, color='blue')
    plt.ylabel("Amplitud")
    plt.title("Forma de Onda del Audio en Mono")
    plt.grid()
    plt.show()
else:
    print("El archivo no existe en la ruta especificada.")
