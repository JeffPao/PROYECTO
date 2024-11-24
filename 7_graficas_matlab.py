import numpy as np
import matplotlib.pyplot as plt

from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap
import sys



"""
AL FINAL SOLO ES UN PLOT Y YA
"""
# Crear datos
x = np.arange(0, 10.1, 0.1)  # Similar a 0:0.1:10 en MATLAB
y = np.sin(x)

# Crear el gráfico
plt.plot(x, y)
plt.title('Ejemplo de gráfico Python')  # Título
plt.xlabel('Eje X')  # Etiqueta del eje X
plt.ylabel('Eje Y')  # Etiqueta del eje Y

# Guardar el gráfico como archivo PNG
plt.savefig('grafico.png')  # Similar a saveas(gcf, 'grafico.png') en MATLAB

# Mostrar el gráfico (opcional)
plt.show()



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráfico MATLAB en PyQt6")
        
        # Crear un diseño
        layout = QVBoxLayout()
        
        # Cargar la imagen exportada de MATLAB
        pixmap = QPixmap("grafico.png")
        label = QLabel()
        label.setPixmap(pixmap)
        
        # Agregar la imagen al diseño
        layout.addWidget(label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
