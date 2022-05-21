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
        
        #distribution params.I'll keep it here, possible good idea - move it to different object
        self.p_vec = []
        self.t_vec = []
        self.rng = rng = np.random.default_rng()
        
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
        
        
        self.stopTimeSpinBox.setMinimum(1)
        self.stopTimeSpinBox.setMaximum(180)
        self.stopTimeSpinBox.setValue(60)
        
        self.stopTrialSpinBox.setMinimum(1)
        self.stopTrialSpinBox.setMaximum(999)
        self.stopTrialSpinBox.setValue(10)
        
        self.stopRewardSpinBox.setMinimum(1)
        self.stopRewardSpinBox.setMaximum(999)
        self.stopRewardSpinBox.setValue(100)
        
        
        #spinboxes connection
        self.pDoubleSpinBox.valueChanged.connect(self.updateDistrParam)
        self.tSpinBox.valueChanged.connect(self.updateDistrParam)
        self.tMaxSpinBox.valueChanged.connect(self.updateDistrParam)
        
        
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.sc)
        self._freq_ref = self.sc.axes.plot([],[], 'xr')[0]
        self._plot_ref = self.sc.axes.plot([], [], '-ok')[0]
        
        self.mplWidget.setLayout(layout)
        
        #riLabel initial value and initial plot
        self.updateDistrParam()
        
        self.riModel = RIModel()
        self.listView.setModel(self.riModel)
        
        self.sequence = self.generateSequence()
        self.generatePushButton.clicked.connect(self.generateSequence)
        
    def generateSequence(self):
        self.sequence = self.rng.choice(self.t_vec, size = self.stopTrialSpinBox.value(), p=self.p_vec)
        self.riModel.setData(list(zip(["not_recorded"]*len(self.sequence), self.sequence)))
        times, counts = np.unique(self.sequence, return_counts = True)
        freq_vec = counts/len(self.sequence)
        self._freq_ref.set_data(times, freq_vec)
        self.sc.draw()
    
    def updateDistrParam(self):
        #move plot update to different place
        #also update plot for frequences
        #and do goood x y scaling
        self.p = self.pDoubleSpinBox.value()
        self.T = self.tSpinBox.value()
        self.Tmax = self.tMaxSpinBox.value()
        self.riLabel.setText(f"{self.T/self.p:.1f}")
        self.t_vec = np.arange(self.T, self.Tmax, self.T)
        self.p_vec = []
        for i in range(0, len(self.t_vec)):
            self.p_vec.append((1-sum(self.p_vec))*self.p)
        self.p_vec[-1] += (1 - sum(self.p_vec))
        self._plot_ref.set_data(self.t_vec, self.p_vec)
        self.sc.axes.set_xlim(0, self.Tmax+1.0)
        self.sc.axes.set_ylim(0, self.p + 0.1)
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
            return str(text)
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

                
                
                
        return list(zip(["not_recorded"]*100, [1]*100))

def main():
    app = QApplication(sys.argv)
    form = TestUiRi()
    form.show()
    app.exec_()



if __name__ == '__main__':
    main()
