from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import matplotlib
import numpy as np
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from ui.ui_RR import Ui_RR


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)




class TestUiRR(QtWidgets.QWidget, Ui_RR):
    def __init__(self):
        super(TestUiRR, self).__init__()
        self.setupUi(self)
        self.numberIterator = NumberIterator()
        
        #here will be implemented data loadiong 
        self.p = 0.1
        self.T = 6
        self.Tmax = 150
        self.mean_int = 60
        
        #distribution params.I'll keep it here, possible good idea - move it to different object
        self.p_vec = []
        self.n_vec = []
        self.rng = rng = np.random.default_rng()
        
        #spinboxes settings
        self.pDoubleSpinBox.setMaximum(1.0)
        self.pDoubleSpinBox.setMinimum(0.0)
        self.pDoubleSpinBox.setDecimals(3)
        self.pDoubleSpinBox.setSingleStep(0.01)
        self.pDoubleSpinBox.setValue(self.p)
        
    
        
        self.nMaxSpinBox.setMinimum(1)
        self.nMaxSpinBox.setMaximum(3600)
        self.nMaxSpinBox.setValue(150)
        
        
        self.stopTimeSpinBox.setMinimum(1)
        self.stopTimeSpinBox.setMaximum(180)
        self.stopTimeSpinBox.setValue(60)
        
        self.stopTrialSpinBox.setMinimum(1)
        self.stopTrialSpinBox.setMaximum(999)
        self.stopTrialSpinBox.setValue(10)
        

        
        
        #spinboxes connection
        self.pDoubleSpinBox.valueChanged.connect(self.updateDistrParam)
        self.nMaxSpinBox.valueChanged.connect(self.updateDistrParam)
        
        
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
        
        self.generateSequence()
        self.generatePushButton.clicked.connect(self.generateSequence)
        
        
        self.startPushButton.clicked.connect(self.runNumberIterator)
        
    def generateSequence(self):
        self.sequence = self.rng.choice(self.n_vec, size = self.stopTrialSpinBox.value(), p=self.p_vec)
        self.riModel.setData(list(zip(["not_recorded"]*len(self.sequence), self.sequence)))
        ns, counts = np.unique(self.sequence, return_counts = True)
        freq_vec = counts/len(self.sequence)
        self._freq_ref.set_data(ns, freq_vec)
        self.sc.draw()
    
    def updateDistrParam(self):
        #move plot update to different place
        #also update plot for frequences
        #and do goood x y scaling
        self.p = self.pDoubleSpinBox.value()
        self.Nmax = self.nMaxSpinBox.value()
        self.riLabel.setText(f"{self.T/self.p:.1f}")
        self.n_vec = list(range(1, self.Nmax+1))
        self.p_vec = []
        for i in range(0, len(self.n_vec)):
            self.p_vec.append((1-sum(self.p_vec))*self.p)
        self.p_vec[-1] += (1 - sum(self.p_vec))
        self._plot_ref.set_data(self.n_vec, self.p_vec)
        self.sc.axes.set_xlim(0, self.Tmax+1.0)
        self.sc.axes.set_ylim(0, self.p + 0.1)
        self.sc.draw()
      
    def runNumberIterator(self):
        
        self.riModel.restart()
        
                
        self.numberIterator = NumberIterator(self.sequence) 
        
       
        
        
        
        self.numberIterator.countdown_started_signal.connect(lambda x: self.riModel.intervalStarted(x))
        
        
        self.numberIterator.countdown_ended_signal.connect(lambda x: self.riModel.intervalEnded(x))
        self.numberIterator.countdown_ended_signal.connect(self.parentWidget().parentWidget().parentWidget().parentWidget().catch_countdown_ended)
        
        
        self.numberIterator.pause_signal.connect(self.riModel.intervalPaused)
        self.numberIterator.resume_signal.connect(self.riModel.intervalResumed)
        
        
        
        
        
        
        self.numberIterator.finished_signal.connect(lambda x: self.riModel.intervalEnded(x))
        self.numberIterator.finished_signal.connect(self.numberIterator.deleteLater)
        self.startPushButton.setEnabled(False)
        self.numberIterator.finished_signal.connect( lambda: self.startPushButton.setEnabled(True))
        self.generatePushButton.setEnabled(False)
        self.numberIterator.finished_signal.connect( lambda: self.generatePushButton.setEnabled(True))
        
        self.numberIterator._start()
        
        self.stopPushButton.clicked.connect(self.numberIterator._stop)
        
        self.pausePushButton.setCheckable(True)
        self.pausePushButton.toggled.connect( lambda x: self.numberIterator._pause() if x else self.numberIterator._resume())
       
        self.numberIterator.countdown_started_signal.connect(lambda x: self.parentWidget().parentWidget().parentWidget().parentWidget().catch_timer(x))
        
        self.parentWidget().parentWidget().parentWidget().parentWidget().catch_start()
        self.numberIterator.pause_signal.connect(self.parentWidget().parentWidget().parentWidget().parentWidget().catch_pause)
        self.numberIterator.resume_signal.connect(self.parentWidget().parentWidget().parentWidget().parentWidget().catch_resume)
        self.stopPushButton.clicked.connect(self.parentWidget().parentWidget().parentWidget().parentWidget().catch_stop)
        
        self.numberIterator.countdown_shifted_signal.connect(lambda x: self.riModel.countdownShifted(x))
       
        
        
        
        
        
        
        



class RIModel(QtCore.QAbstractListModel):
    #need to replace index calls and _index calls
    
    def __init__(self, intervals=None, *args, **kwargs):
        super(RIModel, self).__init__(*args, **kwargs)
        self.intervals = intervals or []
        statuses = ["got_food", "not_recorded", "paused", "recording_now"]
        self.iconPool = IconPool(statuses)
        self.last_started = -1
        self.status_before_pause = ""

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            status, text = self.intervals[index.row()]
            return f'{index.row() + 1}. {text} раз'
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
        
    def getStatus(self, index):
        status, value = self.intervals[index.row()] 
        return status  
    
        
    def intervalStarted(self, n):
        self.last_started = n
        self.editStatus(_index(n), "recording_now")
        
    def intervalPaused(self):
        self.status_before_pause = self.getStatus(_index(self.last_started))
        self.editStatus(_index(self.last_started), "paused")
        
    def intervalResumed(self):
        self.editStatus(_index(self.last_started), self.status_before_pause)
        
    
    def intervalEnded(self,n):
        self.editStatus(_index(n), "got_food")
        
    def countdownShifted(self, n):
        pass
            
    def restart(self):
        self.last_started = -1
        for i in range(0,len(self.intervals)):
            self.editStatus(_index(i), "not_recorded")
        

        
        
    

    
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

       


class _index:
    def __init__(self,r):
        self.r = r
            
    def row(self):
        return self.r
     
        
class NumberIterator(QtCore.QObject):
    
    
    finished_signal = QtCore.pyqtSignal(int)
    countdown_started_signal = QtCore.pyqtSignal(int)
    countdown_ended_signal = QtCore.pyqtSignal(int)
    countdown_shifted_signal = QtCore.pyqtSignal(int)
    pause_signal = QtCore.pyqtSignal()
    resume_signal = QtCore.pyqtSignal()
    
    def __init__(self, counter_sequence=[1,2,3]):
        super(NumberIterator, self).__init__()
        self.counter_sequence = counter_sequence
        self.index = 0
        self.max_index = len(self.counter_sequence)-1
        
        self.counter = self.counter_sequence[self.index]
        self.active = False
        self.pause = False
        print("Counter iterator created")
        
    
    def _start(self):
        self.countdown_started_signal.emit(0)
        self.active = True
        print(f"Counter iterator started {self.index}: {self.counter_sequence[self.index]}")
        
    
    def _pause(self):
        self.pause = True
        self.pause_signal.emit()
        print("Пауза началась")
    
    def _resume(self):
        self.pause = False
        self.resume_signal.emit()
        print("Пауза закончилась")
    
    def _stop(self):
        print("THe END")
        self.active = False
        self.finished_signal.emit(self.index)
        
    def _lever_hook(self):
        if self.active and not self.pause:
            self.counter -= 1
            self.countdown_shifted_signal.emit(self.counter)
            print(self.counter)
            if self.counter == 0:
                self.countdown_ended_signal.emit(self.index)
                if self.index == self.max_index:
                    self._stop()
                else:
                    self.index += 1
                    self.counter = self.counter_sequence[self.index]
                    self.countdown_started_signal.emit(self.index)
                    
        
    
    
    
    


def main():
    app = QApplication(sys.argv)
    form = TestUiRR()
    form.show()
    app.exec_()



if __name__ == '__main__':
    main()
