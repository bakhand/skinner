from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import matplotlib
import numpy as np
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from ui.ui_RI import Ui_RI


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class _index:
    def __init__(self,r):
        self.r = r
            
    def row(self):
        return self.r

class TestUiRi(QtWidgets.QWidget, Ui_RI):
    def __init__(self, parent=None):
        super(TestUiRi, self).__init__(parent)
        self.setupUi(self)
        
        #here will be implemented data loadiong 
        self.p = 0.1
        self.T = 6
        self.Tmax = 150
        self.mean_int = 60
        
        
        #spinboxes settings
        self.pDoubleSpinBox.setMaximum(1.0)
        self.pDoubleSpinBox.setMinimum(0.0)
        self.pDoubleSpinBox.setDecimals(3)
        self.pDoubleSpinBox.setSingleStep(0.01)
        self.pDoubleSpinBox.setValue(self.p)
        
        
        self.tSpinBox.setMinimum(1)
        self.tSpinBox.setMaximum(999)
        self.tSpinBox.setValue(self.T)
        
        self.tMaxSpinBox.setMinimum(1)
        self.tMaxSpinBox.setMaximum(3600)
        self.tMaxSpinBox.setValue(150)
        
        
        #spinboxes connection
        self.pDoubleSpinBox.valueChanged.connect(self.updateDistrParam)
        self.tSpinBox.valueChanged.connect(self.updateDistrParam)
        self.tMaxSpinBox.valueChanged.connect(self.updateDistrParam)
        
      
        
        
        
        
        
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        #self.sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.sc)
        self._plot_ref = self.sc.axes.plot([], [], '-ok')
        self.mplWidget.setLayout(layout)
        
        #riLabel initial value and initial plot
        self.updateDistrParam()
        
        
        self.risg = RISequenceGenerator()
        self.sequence = self.risg.generate()
        self.riModel = RIModel(self.sequence)
        self.listView.setModel(self.riModel)
        self.generatePushButton.clicked.connect(lambda x: self.riModel.editStatus(_index(3), "got_food"))
    
    def updateDistrParam(self):
        self.p = self.pDoubleSpinBox.value()
        self.T = self.tSpinBox.value()
        self.Tmax = self.tMaxSpinBox.value()
        self.riLabel.setText(str(self.p))
        t_vec = np.arange(self.T, self.Tmax, self.T)
        p_vec = []
        for i in range(0, len(t_vec)):
            p_vec.append((1-sum(p_vec))*self.p)
        #p_vec[-1] += sum(p_vec))
        #https://www.pythonguis.com/tutorials/plotting-matplotlib/ here I'm trying to do in-replace draw, but still failing
        self._plot_ref[0].set_data(t_vec, p_vec)
        self.sc.draw()



class RIModel(QtCore.QAbstractListModel):
    
    def __init__(self, intervals=None, *args, **kwargs):
        super(RIModel, self).__init__(*args, **kwargs)
        self.intervals = intervals or []
        statuses = ["got_food", "missed_food", "not_recorded", "paused", "recording_now", "recording_got"]
        self.iconPool = IconPool(statuses)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            status, text = self.intervals[index.row()]
            return text
        if role == QtCore.Qt.DecorationRole:
            status, _ = self.intervals[index.row()]
            return self.iconPool.getIcon(status)

    def rowCount(self, index):
        return len(self.intervals)
    
    def clear(self):
        self.intervals = ()
        self.layoutChanged.emit()
    
    def setData(self, intervals):
        self.intervals = intervals
        self.layoutChanged.emit()
    
    def editData(self, data, index):
        self.intervals[index.row()] = data
        #self.dataChanged.emit() indexes...
        self.layoutChanged.emit()
        
    
    def editStatus(self, index, status):
        _, value = self.intervals[index.row()] 
        self.intervals[index.row()] = (status, value)
        self.layoutChanged.emit()

    
class IconPool():
    def __init__(self, icon_list=[]):
        self.icons = {}
        icon_list.append("no_icon")
        self.icon_list = icon_list
        for icon_name in self.icon_list:
            self.icons[icon_name] = QtGui.QImage("./ui/res/img/" + icon_name + ".png")
    
    def getIcon(self, icon_name=""):
        if icon_name in self.icon_list:
            return self.icons[icon_name]
        else:
            return self.icons['no_icon']



class RISequenceGenerator():
    def calculateMean():
        pass
    
    def generate(self, p=1, T=1, Tmax = 100):
        return list(zip(["not_recorded"]*100, [1]*100))

def main():
    app = QApplication(sys.argv)
    form = TestUiRi()
    form.show()
    app.exec_()



if __name__ == '__main__':
    main()
