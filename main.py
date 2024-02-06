import sys
from PyQt5.QtWidgets import QApplication
from view import SeleccionarArchivoCSV

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = SeleccionarArchivoCSV()
    sys.exit(app.exec_())
 