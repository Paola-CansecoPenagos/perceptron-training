import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QLineEdit, QTextEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from perceptron import procesar_archivo, entrenamiento, graficarNormaError, graficarEvolucionPesos

class SeleccionarArchivoCSV(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 550, 650)
        self.setWindowTitle('Perception')
        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 10, 450, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("FUNCIONES DE APROXIMACION")
        
        self.label_eta = QLabel('Tasa de aprendizaje:', self)
        self.label_eta.setGeometry(130, 50, 120, 20)
        self.entrada_eta = QLineEdit(self)
        self.entrada_eta.setGeometry(300, 50, 120, 20)

        self.label_epoca = QLabel('Epocas (Iteraciones):', self)
        self.label_epoca.setGeometry(130, 90, 120, 20)
        self.entrada_epoca = QLineEdit(self)
        self.entrada_epoca.setGeometry(300, 90, 120, 20)
        
        self.etiqueta_archivo = QLabel(self)
        self.etiqueta_archivo.setGeometry(80, 130, 480, 20)

        btn_cargar = QPushButton('Seleccionar Archivo CSV', self)
        btn_cargar.clicked.connect(self.abrirDialogo)
        btn_cargar.setGeometry(195, 160, 160, 30)

        btn_iniciar = QPushButton('Iniciar', self)
        btn_iniciar.clicked.connect(self.iniciarProcesamiento)
        btn_iniciar.setGeometry(175, 200, 200, 30)

        self.label_reporte = QLabel('REPORTE FINAL:', self)
        self.label_reporte.setGeometry(225, 240, 200, 20)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_reporte.setFont(font)
        self.reporte = QTextEdit(self)
        self.reporte.setEnabled(True)
        self.reporte.setGeometry(QtCore.QRect(125, 280, 300, 250))
        self.reporte.setObjectName("solucion") 

        graficaNormaError = QPushButton('Evolución de la norma \n del error |e|', self)
        graficaNormaError.setGeometry(100, 550, 160, 50)
        graficaNormaError.clicked.connect(self.mostrarGraficaNormaError)
        
        graficaEvolucion = QPushButton('Evolución del valor \n de los pesos (W)', self)
        graficaEvolucion.setGeometry(285, 550, 160, 50)
        graficaEvolucion.clicked.connect(self.mostrarGraficaEvolucionPeso)
        
        btn_reiniciar = QPushButton('Reiniciar', self)
        btn_reiniciar.clicked.connect(self.reiniciar)
        btn_reiniciar.setGeometry(235, 600, 80, 30)
        
        self.archivo_seleccionado = None

        self.show()
    
    def abrirDialogo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo CSV", "", "Archivos CSV (*.csv);;Todos los archivos (*)", options=options)

        if file_name:
            self.archivo_seleccionado = file_name
            self.etiqueta_archivo.setText(f"Archivo seleccionado: {file_name}")
            print(f"Archivo CSV seleccionado: {file_name}")

    def iniciarProcesamiento(self):
        if self.archivo_seleccionado:
            eta = float(self.entrada_eta.text())
            epocas = int(self.entrada_epoca.text())
            
            resultado = ""

            wIniciales, wFinales = entrenamiento(self.archivo_seleccionado, epocas, eta)
            resultado += f"Tasa de aprendizaje (eta): {eta}\n"
            resultado += f"Error permisible: 0\n"
            resultado += f"Cantidad de iteraciones: {epocas}\n\n"
            resultado += f"Pesos iniciales:\n{wIniciales}\n"
            resultado += f"Pesos finales:\n{wFinales}"
            self.reporte.setPlainText(resultado)
        else:
            print("Por favor, selecciona un archivo CSV antes de iniciar.")

    def mostrarGraficaNormaError(self):
        if self.archivo_seleccionado:
            epocas = int(self.entrada_epoca.text())
            graficarNormaError(epocas)
    
    def mostrarGraficaEvolucionPeso(self):
        if self.archivo_seleccionado:
            epocas = int(self.entrada_epoca.text())
            graficarEvolucionPesos(epocas)
            
    def reiniciar(self):
        self.entrada_eta.clear()
        self.entrada_epoca.clear()
        self.etiqueta_archivo.clear()
        self.reporte.clear()
