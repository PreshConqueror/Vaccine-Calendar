#CALLING SOURCE CODE

#IMPORT FROM PYQT5
import sys 
from VaccineCalendarCalculation import * 
from PyQt5.QtWidgets import * 
 
class MyForm(QtWidgets.QDialog):
    def __init__(self, pixmap, parent=None):
        QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonCalculate.clicked.connect(self.calc)

        self.scene = QGraphicsScene(self)
        item=QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item) 
        self.ui.graphicsView.setScene(self.scene)
        
    def calc(self):
        todaysDate = self.ui.calendarWidget_current.selectedDate()
        vaccineDate = self.ui.calendarWidget_future.selectedDate()
        self.ui.label_NumberOfDays.setText("The number of days until your COVID vaccination is: "+str((vaccineDate.toPyDate()-todaysDate.toPyDate()).days) + "days")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    pixmap= QtGui.QPixmap()
    pixmap.load("vaccined.jpg")

    myapp = MyForm(pixmap)
    myapp.show()
    sys.exit(app.exec_())

