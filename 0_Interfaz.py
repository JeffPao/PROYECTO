# Form implementation generated from reading ui file 'INTERFAZV2.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(444, 760)
        MainWindow.setBaseSize(QtCore.QSize(400, 500))
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
        self.button_comprimir.setGeometry(QtCore.QRect(60, 600, 161, 31))
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
        self.button_descomprimir.setGeometry(QtCore.QRect(230, 600, 161, 31))
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
        self.textEdit_DCT_UMBRAL = QtWidgets.QTextEdit(parent=self.tab_4)
        self.textEdit_DCT_UMBRAL.setGeometry(QtCore.QRect(270, 30, 91, 31))
        self.textEdit_DCT_UMBRAL.setObjectName("textEdit_DCT_UMBRAL")
        self.label_14 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(210, 20, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(10, 20, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.textEdit_DCT_AMPLIFICACION = QtWidgets.QTextEdit(parent=self.tab_4)
        self.textEdit_DCT_AMPLIFICACION.setGeometry(QtCore.QRect(110, 30, 91, 31))
        self.textEdit_DCT_AMPLIFICACION.setObjectName("textEdit_DCT_AMPLIFICACION")
        self.comboBox_tipo_de_filtro_DCT = QtWidgets.QComboBox(parent=self.tab_4)
        self.comboBox_tipo_de_filtro_DCT.setGeometry(QtCore.QRect(180, 110, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.comboBox_tipo_de_filtro_DCT.setFont(font)
        self.comboBox_tipo_de_filtro_DCT.setObjectName("comboBox_tipo_de_filtro_DCT")
        self.comboBox_tipo_de_filtro_DCT.addItem("")
        self.comboBox_tipo_de_filtro_DCT.addItem("")
        self.label_34 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_34.setGeometry(QtCore.QRect(90, 100, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.label_16 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(90, 60, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.textEdit_DCT_ORDEN = QtWidgets.QTextEdit(parent=self.tab_4)
        self.textEdit_DCT_ORDEN.setGeometry(QtCore.QRect(190, 70, 91, 31))
        self.textEdit_DCT_ORDEN.setObjectName("textEdit_DCT_ORDEN")
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
        self.textEdit_DWT_Umbral = QtWidgets.QTextEdit(parent=self.tab_7)
        self.textEdit_DWT_Umbral.setGeometry(QtCore.QRect(190, 40, 111, 31))
        self.textEdit_DWT_Umbral.setObjectName("textEdit_DWT_Umbral")
        self.textEdit_DWT_nivel = QtWidgets.QTextEdit(parent=self.tab_7)
        self.textEdit_DWT_nivel.setGeometry(QtCore.QRect(190, 80, 111, 31))
        self.textEdit_DWT_nivel.setObjectName("textEdit_DWT_nivel")
        self.label_17 = QtWidgets.QLabel(parent=self.tab_7)
        self.label_17.setGeometry(QtCore.QRect(130, 30, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(parent=self.tab_7)
        self.label_19.setGeometry(QtCore.QRect(80, 70, 111, 51))
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
        self.label_7.setGeometry(QtCore.QRect(160, 630, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textEdit_TAMANO_INICIAL = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_TAMANO_INICIAL.setEnabled(False)
        self.textEdit_TAMANO_INICIAL.setGeometry(QtCore.QRect(90, 680, 131, 31))
        self.textEdit_TAMANO_INICIAL.setObjectName("textEdit_TAMANO_INICIAL")
        self.textEdit_TAMANO_FINAL = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_TAMANO_FINAL.setEnabled(False)
        self.textEdit_TAMANO_FINAL.setGeometry(QtCore.QRect(230, 680, 131, 31))
        self.textEdit_TAMANO_FINAL.setObjectName("textEdit_TAMANO_FINAL")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(140, 650, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(280, 650, 41, 21))
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
        self.tabWidget.setCurrentIndex(2)
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
        self.label_15.setText(_translate("MainWindow", "Amplificacion"))
        self.comboBox_tipo_de_filtro_DCT.setItemText(0, _translate("MainWindow", "Filtro pasa bajo"))
        self.comboBox_tipo_de_filtro_DCT.setItemText(1, _translate("MainWindow", "Filtro pasa alto"))
        self.label_34.setText(_translate("MainWindow", "Tipo de filtro"))
        self.label_16.setText(_translate("MainWindow", "Orden de filtro"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "DCT"))
        self.label_6.setText(_translate("MainWindow", "Transformada de Wavelet"))
        self.label_17.setText(_translate("MainWindow", "Umbral"))
        self.label_19.setText(_translate("MainWindow", "Nivel de la DWT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "DWT"))
        self.label_4.setText(_translate("MainWindow", "PARAMETROS DE TRANSFORMADAS"))
        self.label_7.setText(_translate("MainWindow", "Tamaño del archivo"))
        self.label_8.setText(_translate("MainWindow", "Inicial"))
        self.label_9.setText(_translate("MainWindow", "Final"))
        self.button_Filtro.setText(_translate("MainWindow", "FILTRO"))
        self.label_21.setText(_translate("MainWindow", "PARAMETROS DE COMPRESION"))
        self.label_13.setText(_translate("MainWindow", "Sample rate"))
        self.label_12.setText(_translate("MainWindow", "Bitrate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
