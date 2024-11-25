#LIBRERIAS
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
from pathlib import Path
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
from datetime import datetime
from scipy.signal import butter, filtfilt
from scipy.fft import fft, ifft
from scipy.fftpack import dct, idct
import pywt


#Parametros base del programa
archivo_cargado = None
bitrate = "32k" 
frecuencia_de_corte = 500
sample_rate = 16000
orden_filtro = 2
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(444, 809)
        MainWindow.setBaseSize(QtCore.QSize(400, 500))
        # Deshabilitar maximización
        MainWindow.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint | QtCore.Qt.WindowType.WindowMinimizeButtonHint)
        MainWindow.setFixedSize(MainWindow.size())
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cbx_transformada = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cbx_transformada.setGeometry(QtCore.QRect(140, 110, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        self.cbx_transformada.setFont(font)
        self.cbx_transformada.setObjectName("cbx_transformada")
        self.cbx_transformada.addItem("")
        self.cbx_transformada.addItem("")
        self.cbx_transformada.addItem("")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 90, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.button_comprimir = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_comprimir.setGeometry(QtCore.QRect(60, 610, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.button_comprimir.setFont(font)
        self.button_comprimir.setCheckable(False)
        self.button_comprimir.setObjectName("button_comprimir")
        self.cargar_button = QtWidgets.QToolButton(parent=self.centralwidget)
        self.cargar_button.setGeometry(QtCore.QRect(280, 40, 71, 31))
        self.cargar_button.setObjectName("cargar_button")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.texteditor1 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.texteditor1.setEnabled(False)
        self.texteditor1.setGeometry(QtCore.QRect(120, 40, 151, 31))
        self.texteditor1.setObjectName("texteditor1")
        self.button_descomprimir = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_descomprimir.setGeometry(QtCore.QRect(230, 610, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.button_descomprimir.setFont(font)
        self.button_descomprimir.setCheckable(False)
        self.button_descomprimir.setObjectName("button_descomprimir")
        self.button_analisis = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_analisis.setGeometry(QtCore.QRect(150, 140, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.button_analisis.setFont(font)
        self.button_analisis.setCheckable(False)
        self.button_analisis.setObjectName("button_analisis")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 210, 391, 191))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit_DFT_Orden = QtWidgets.QTextEdit(parent=self.tab_3)
        self.textEdit_DFT_Orden.setGeometry(QtCore.QRect(210, 70, 101, 31))
        self.textEdit_DFT_Orden.setObjectName("textEdit_DFT_Orden")
        self.label_3 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(110, 0, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit_DFT_f_corte = QtWidgets.QTextEdit(parent=self.tab_3)
        self.textEdit_DFT_f_corte.setGeometry(QtCore.QRect(210, 30, 101, 31))
        self.textEdit_DFT_f_corte.setObjectName("textEdit_DFT_f_corte")
        self.label_10 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(60, 20, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(80, 60, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_20 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(80, 100, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.comboBox_tipo_de_filtro_dft = QtWidgets.QComboBox(parent=self.tab_3)
        self.comboBox_tipo_de_filtro_dft.setGeometry(QtCore.QRect(180, 110, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.comboBox_tipo_de_filtro_dft.setFont(font)
        self.comboBox_tipo_de_filtro_dft.setObjectName("comboBox_tipo_de_filtro_dft")
        self.comboBox_tipo_de_filtro_dft.addItem("")
        self.comboBox_tipo_de_filtro_dft.addItem("")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_5 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(70, 0, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit_DCT_Umbral_de_corte = QtWidgets.QTextEdit(parent=self.tab_4)
        self.textEdit_DCT_Umbral_de_corte.setGeometry(QtCore.QRect(190, 40, 61, 31))
        self.textEdit_DCT_Umbral_de_corte.setObjectName("textEdit_DCT_Umbral_de_corte")
        self.label_14 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(130, 30, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.textEdit_DCT_bitrate = QtWidgets.QTextEdit(parent=self.tab_4)
        self.textEdit_DCT_bitrate.setGeometry(QtCore.QRect(190, 90, 61, 31))
        self.textEdit_DCT_bitrate.setObjectName("textEdit_DCT_bitrate")
        self.label_15 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(100, 120, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(140, 80, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.textEdit_DCT_samplerate_ = QtWidgets.QTextEdit(parent=self.tab_4)
        self.textEdit_DCT_samplerate_.setGeometry(QtCore.QRect(190, 130, 61, 31))
        self.textEdit_DCT_samplerate_.setObjectName("textEdit_DCT_samplerate_")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.label_6 = QtWidgets.QLabel(parent=self.tab_7)
        self.label_6.setGeometry(QtCore.QRect(100, 0, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit_DWT_Umbral_de_corte = QtWidgets.QTextEdit(parent=self.tab_7)
        self.textEdit_DWT_Umbral_de_corte.setGeometry(QtCore.QRect(200, 40, 61, 31))
        self.textEdit_DWT_Umbral_de_corte.setObjectName("textEdit_DWT_Umbral_de_corte")
        self.textEdit_DWR_samplerate = QtWidgets.QTextEdit(parent=self.tab_7)
        self.textEdit_DWR_samplerate.setGeometry(QtCore.QRect(200, 130, 61, 31))
        self.textEdit_DWR_samplerate.setObjectName("textEdit_DWR_samplerate")
        self.textEdit_DWT_bitrate = QtWidgets.QTextEdit(parent=self.tab_7)
        self.textEdit_DWT_bitrate.setGeometry(QtCore.QRect(200, 90, 61, 31))
        self.textEdit_DWT_bitrate.setObjectName("textEdit_DWT_bitrate")
        self.label_17 = QtWidgets.QLabel(parent=self.tab_7)
        self.label_17.setGeometry(QtCore.QRect(140, 30, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.tab_7)
        self.label_18.setGeometry(QtCore.QRect(110, 120, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(parent=self.tab_7)
        self.label_19.setGeometry(QtCore.QRect(150, 80, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.tabWidget.addTab(self.tab_7, "")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 190, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 660, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textEdit_TAMANO_INICIAL = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_TAMANO_INICIAL.setEnabled(False)
        self.textEdit_TAMANO_INICIAL.setGeometry(QtCore.QRect(90, 710, 131, 31))
        self.textEdit_TAMANO_INICIAL.setObjectName("textEdit_TAMANO_INICIAL")
        self.textEdit_TAMANO_FINAL = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_TAMANO_FINAL.setEnabled(False)
        self.textEdit_TAMANO_FINAL.setGeometry(QtCore.QRect(230, 710, 131, 31))
        self.textEdit_TAMANO_FINAL.setObjectName("textEdit_TAMANO_FINAL")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(140, 680, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(280, 680, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.button_Filtro = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_Filtro.setGeometry(QtCore.QRect(180, 410, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.button_Filtro.setFont(font)
        self.button_Filtro.setCheckable(False)
        self.button_Filtro.setObjectName("button_Filtro")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 450, 391, 141))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_21 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(100, 10, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.textEdit_samplerate = QtWidgets.QTextEdit(parent=self.groupBox)
        self.textEdit_samplerate.setGeometry(QtCore.QRect(200, 40, 111, 31))
        self.textEdit_samplerate.setObjectName("textEdit_samplerate")
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(100, 30, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(130, 80, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.textEdit_bitrate = QtWidgets.QTextEdit(parent=self.groupBox)
        self.textEdit_bitrate.setGeometry(QtCore.QRect(200, 80, 111, 31))
        self.textEdit_bitrate.setObjectName("textEdit_bitrate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 444, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Compresor de audio"))
        self.cbx_transformada.setItemText(0, _translate("MainWindow", "Fourier"))
        self.cbx_transformada.setItemText(1, _translate("MainWindow", "Coseno discreto"))
        self.cbx_transformada.setItemText(2, _translate("MainWindow", "Wavelet"))
        self.label.setText(_translate("MainWindow", "Tipo de transformada"))
        self.button_comprimir.setText(_translate("MainWindow", "COMPRIMIR"))
        self.cargar_button.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Cargar archivo.wav"))
        self.button_descomprimir.setText(_translate("MainWindow", "DESCOMPRIMIR"))
        self.button_analisis.setText(_translate("MainWindow", "ANALISIS"))
        self.label_3.setText(_translate("MainWindow", "Transformada de Fourier"))
        self.label_10.setText(_translate("MainWindow", "Frecuencia de corte"))
        self.label_11.setText(_translate("MainWindow", "Orden de filtro"))
        self.label_20.setText(_translate("MainWindow", "Tipo de filtro"))
        self.comboBox_tipo_de_filtro_dft.setItemText(0, _translate("MainWindow", "Filtro pasa bajo"))
        self.comboBox_tipo_de_filtro_dft.setItemText(1, _translate("MainWindow", "Filtro pasa alto"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "DFT"))
        self.label_5.setText(_translate("MainWindow", "Transformada de Discreta del Coseno"))
        self.label_14.setText(_translate("MainWindow", "Umbral"))
        self.label_15.setText(_translate("MainWindow", "Sample rate"))
        self.label_16.setText(_translate("MainWindow", "Bitrate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "DCT"))
        self.label_6.setText(_translate("MainWindow", "Transformada de Wavelet"))
        self.label_17.setText(_translate("MainWindow", "Umbral"))
        self.label_18.setText(_translate("MainWindow", "Sample rate"))
        self.label_19.setText(_translate("MainWindow", "Bitrate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "DWT"))
        self.label_4.setText(_translate("MainWindow", "PARAMETROS DE TRANSFORMADAS"))
        self.label_7.setText(_translate("MainWindow", "Tamaño del archivo"))
        self.label_8.setText(_translate("MainWindow", "Inicial"))
        self.label_9.setText(_translate("MainWindow", "Final"))
        self.button_Filtro.setText(_translate("MainWindow", "FILTRO"))
        self.label_21.setText(_translate("MainWindow", "PARAMETROS DE COMPRESION"))
        self.label_13.setText(_translate("MainWindow", "Sample rate"))
        self.label_12.setText(_translate("MainWindow", "Bitrate"))


        #PROGRAMA
        self.cargar_button.clicked.connect(self.cargar_archivo)
        self.button_analisis.clicked.connect(self.graficas)
        self.button_Filtro.clicked.connect(self.filtro)
        self.button_comprimir.clicked.connect(self.compresion)
        
        

    def cargar_archivo(self):
        # Abrir el cuadro de diálogo de archivos y obtener la ruta del archivo seleccionado
        global archivo_cargado
        archivo_cargado, _ = QFileDialog.getOpenFileName(
            None, "Seleccionar archivo", "", "Archivos WAV (*.wav);;Todos los archivos (*)"
        )
        if archivo_cargado:
            print(f"Archivo seleccionado: {Path(archivo_cargado).name}")
            # Actualizar el texteditor1 con el nombre del archivo cargado
            nombre_archivo = Path(archivo_cargado).name  # Obtiene solo el nombre del archivo
            self.texteditor1.setPlainText(nombre_archivo)  # Muestra el nombre del archivo en el QTextEdit

    def graficas(self):
        global archivo_cargado
        if not archivo_cargado:
            print("No se ha seleccionado ningún archivo.")
            return
        
        if Path(archivo_cargado).exists():
            archivo_ruta = Path(archivo_cargado)
            carpeta_salida = archivo_ruta.parent  # Usar la carpeta donde se encuentra el archivo cargado
            # Evaluación de la transformada seleccionada en el combo box
            transformada = self.cbx_transformada.currentText()

            # Leer el archivo WAV
            frecuencia_muestreo, datos_audio = wav.read(archivo_ruta)
            if len(datos_audio.shape) > 1:
                datos_audio = np.mean(datos_audio, axis=1)  # Promediar los dos canales
                datos_audio = np.int16(datos_audio)  # Convertir a enteros

            # Obtener la transformada seleccionada
            transformada = self.cbx_transformada.currentText()

            # ---------- TRANSFORMADAS ----------
            # ====== GRAFICAR TRANSFORMADA DE FOURIER ======
            transformada_fft = fft(datos_audio)
            frecuencias = np.fft.fftfreq(len(transformada_fft), d=1/frecuencia_muestreo)

            # Submuestreo para graficar menos puntos
            factor_submuestreo = 100  # Cambia este valor según tu necesidad
            frecuencias_sub = frecuencias[::factor_submuestreo]
            fft_magnitud_sub = np.abs(transformada_fft[::factor_submuestreo])

            # ====== GRAFICA TRANSFORMADA DEL COSENO DISCRETA ======
            dct_data = dct(datos_audio, type=2, norm='ortho')
            # ====== TRANSFORMADA WAVELET ======
            coeffs = pywt.wavedec(datos_audio, 'haar', level=7)

            def graficar_coefs_wavelet(coeffs, nivel):
                    """
                    Grafica los coeficientes de la DWT (originales o filtrados).
                    """
                    fig, axes = plt.subplots(len(coeffs), 1, figsize=(10, 8))
                    fig.suptitle('Coeficientes de la Transformada Wavelet', fontsize=16)
                    
                    for i, coef in enumerate(coeffs):
                        if i == 0:
                            title = "Aproximación (Nivel {})".format(nivel)
                        else:
                            title = "Detalle (Nivel {})".format(nivel - i + 1)
                        axes[i].plot(coef, color='blue')
                        axes[i].set_title(title, fontsize=10)
                        axes[i].set_xlim(0, len(coef))
                        axes[i].tick_params(axis='x', which='both', bottom=False, labelbottom=False)
                    
                    plt.tight_layout()
                    plt.subplots_adjust(top=0.9)
                    plt.show()

            if transformada == "Fourier":
                print("Realizando Transformada de Fourier (DFT)")
                plt.figure(figsize=(10, 6))
                plt.plot(frecuencias_sub, fft_magnitud_sub)
                plt.title('Transformada de Fourier del Audio')
                plt.xlabel('Frecuencia (Hz)')
                plt.ylabel('Amplitud')
                plt.grid(True)
                plt.show()

            elif transformada == "Coseno discreto":
                print("Realizando Transformada Coseno Discreto (DCT)")
                # Parámetro para reducir puntos en la gráfica (submuestreo)
                grafica_puntos = 2000  # Número de puntos máximo para graficar (ajústalo según tu necesidad)
                # Crear índices de submuestreo para graficar
                dct_indices = np.linspace(0, len(dct_data) - 1, grafica_puntos, dtype=int)
                # Graficar los coeficientes DCT
                plt.figure(figsize=(10, 6))
                plt.stem(dct_indices, dct_data[dct_indices], linefmt='b-', markerfmt='bo', basefmt=" ", label='Coeficientes DCT')
                plt.title('Coeficientes DCT (Dominio de la Frecuencia)')
                plt.xlabel('Índice de Frecuencia')
                plt.ylabel('Amplitud')
                plt.grid(True)
                plt.legend()
                plt.tight_layout()
                plt.show()

            elif transformada == "Wavelet":
                print("Realizando Transformada Wavelet (DWT)")
                graficar_coefs_wavelet(coeffs, 7)
        else:
            print("El archivo no existe.")
             
    def filtro(self):
        global archivo_cargado, bitrate, frecuencia_de_corte, sample_rate, orden_filtro

        if not archivo_cargado:
            print("No se ha seleccionado ningun archivo")
        else:
            print("El archivo seleccionado es:",Path(archivo_cargado).name)

            if self.cbx_transformada.currentText() == "Fourier":
                #VALIDACION DE PARAMETROS
                print("Tranformada de fourier")
                self.validar_dft()
                self.dft()

            if self.cbx_transformada.currentText() == "Coseno discreto":
                #VALIDACION DE PARAMETROS
                print("Transformada del coseno discreta")
                self.validar_dct()
                

            if self.cbx_transformada.currentText() == "Wavelet":
                #VALIDACION DE PARAMETREOS
                print("Transformada de Wavelet")
                self.validar_dwt()
                
    def compresion(self):
        global sample_rate, bitrate, archivo_cargado
        # ====== Verificar archivo cargado ======
        if not archivo_cargado or not Path(archivo_cargado).exists():
            print("Error: No se encontró el archivo WAV cargado.")
            return

        # Validar los parámetros antes de continuar
        if not self.validar_P_compresion():
            return

        try:
            # Cargar valores de las cajas de texto
            sample_rate = int(self.textEdit_samplerate.toPlainText().strip())
            bitrate = int(self.textEdit_bitrate.toPlainText().strip())
            print(f"Muestreo: {sample_rate}, Bitrate: {bitrate}")
        except ValueError:
            print("Error: Uno o más valores no son válidos.")
            return

        

        # ====== CONVERTIR A MP3 ======
        archivo_ruta = Path(archivo_cargado)
        carpeta_salida = archivo_ruta.parent

        nombre_archivo_mp3 = carpeta_salida / f"{archivo_ruta.stem}_Reducido.mp3"
        audio = AudioSegment.from_wav(archivo_cargado)
        audio.export(nombre_archivo_mp3, format="mp3", bitrate="32k")
        print(f'Archivo guardado en formato MP3 en: {nombre_archivo_mp3}')


            
            
            





    """________ VALIDACIONES DE RECUADROS VACIOS ________"""
    def validar_dft(self):
        # Lista de cuadros de texto a validar
        Cuadros_texto = [self.textEdit_DFT_f_corte, self.textEdit_DFT_Orden]

        # Verificar si alguno está vacío
        campos_vacios = [field for field in Cuadros_texto if not field.toPlainText().strip()]

        if campos_vacios:
            print("Advertencia", "Hay uno o más campos vacíos. Por favor, complételos.")
        else:
            print("Éxito", "Todos los campos están llenos.")

    def validar_dct(self):
        # Lista de cuadros de texto a validar
        Cuadros_texto = [self.textEdit_DCT_Umbral_de_corte, self.textEdit_DCT_bitrate, self.textEdit_DCT_samplerate_]

        # Verificar si alguno está vacío
        campos_vacios = [field for field in Cuadros_texto if not field.toPlainText().strip()]

        if campos_vacios:
            print("Advertencia", "Hay uno o más campos vacíos. Por favor, complételos.")
        else:
            print("Éxito", "Todos los campos están llenos.")

    def validar_dwt(self):
        # Lista de cuadros de texto a validar
        Cuadros_texto = [self.textEdit_DWT_Umbral_de_corte, self.textEdit_DWT_bitrate, self.textEdit_DWR_samplerate]

        # Verificar si alguno está vacío
        campos_vacios = [field for field in Cuadros_texto if not field.toPlainText().strip()]

        if campos_vacios:
            print("Advertencia", "Hay uno o más campos vacíos. Por favor, complételos.")
        else:
            print("Éxito", "Todos los campos están llenos.")
    
    def validar_P_compresion(self):
        """
        Valida que los cuadros de texto requeridos para la compresión no estén vacíos.

        Returns:
            bool: True si todos los campos están llenos, False si alguno está vacío.
        """
        # Lista de cuadros de texto a validar
        Cuadros_texto = [self.textEdit_samplerate, self.textEdit_bitrate]

        # Verificar si alguno está vacío
        campos_vacios = [field for field in Cuadros_texto if not field.toPlainText().strip()]

        if campos_vacios:
            print("Error: Hay uno o más campos vacíos. Por favor, complételos.")
            return False  # Falla la validación
        else:
            print("Validación exitosa: Todos los campos están llenos.")
            return True  # Validación exitosa

    """ _________________________________________________"""









    """__________________ TRANSFORMADAS __________________"""
    def dft(self):
        global frecuencia_de_corte, orden_filtro, archivo_cargado

        # Leer el archivo de audio
        fre_muestreo, datos_audio = wav.read(archivo_cargado)

        try:
            # Cargar valores de las cajas de texto
            frecuencia_de_corte = float(self.textEdit_DFT_f_corte.toPlainText().strip())
            orden_filtro = int(self.textEdit_DFT_Orden.toPlainText().strip())
            print(f"Frecuencia de corte: {frecuencia_de_corte}, Orden del filtro: {orden_filtro}")

        except ValueError:
            print("Error: Uno o más valores no son válidos.")
            return

        # Comprobar que la frecuencia de corte es válida
        nyquist = 0.5 * fre_muestreo
        if frecuencia_de_corte >= nyquist:
            print("Error: La frecuencia de corte no puede ser mayor o igual a la frecuencia de Nyquist.")
            return

        # Convertir a mono si el audio tiene más de un canal
        if len(datos_audio.shape) > 1:
            datos_audio = np.mean(datos_audio, axis=1)
            datos_audio = np.int16(datos_audio)

        # Calcular la FFT de la señal
        ff_audio = fft(datos_audio)
        T = 1 / fre_muestreo
        freq = np.fft.fftfreq(len(datos_audio), T)
        freq = np.abs(freq)  # Tomar magnitud para evitar problemas con frecuencias negativas


        tipo_filtro = self.comboBox_tipo_de_filtro_dft.currentText()
        # Crear el filtro Butterworth en el dominio de la frecuencia
        if tipo_filtro == "Filtro pasa bajo":
            filtro = 1 / (1 + (freq / frecuencia_de_corte) ** (2 * orden_filtro))
        elif tipo_filtro == "Filtro pasa alto":
            filtro = 1 / (1 + (frecuencia_de_corte / np.maximum(freq, 1e-10)) ** (2 * orden_filtro))

        # Aplicar el filtro a la FFT
        fft_filtrado = ff_audio * filtro

        # Transformada inversa para volver al dominio temporal
        data_filtrada = np.real(ifft(fft_filtrado))

        # Normalizar y convertir a enteros
        data_filtrada = data_filtrada / np.max(np.abs(data_filtrada)) * np.max(np.abs(datos_audio))
        data_filtrada = np.int16(data_filtrada)

        # Guardar el archivo filtrado
        fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")  # Formato: AAAAMMDD_HHMMSS
        nombre_con_fecha = f"Audio_DFT_{fecha_hora}{Path(archivo_cargado).suffix}"
        name_archivo = Path(archivo_cargado).with_name(nombre_con_fecha)
        wav.write(name_archivo, fre_muestreo, data_filtrada)

        print(f"Archivo filtrado guardado en: {name_archivo}")

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
