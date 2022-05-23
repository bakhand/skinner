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




class TestUiRi(QtWidgets.QWidget, Ui_RI):
    def __init__(self):
        super(TestUiRi, self).__init__()
        self.setupUi(self)
        self.timerIterator = TimerIterator()
        
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
        
        self.generateSequence()
        self.generatePushButton.clicked.connect(self.generateSequence)
        
        
        self.startPushButton.clicked.connect(self.runTimerIterator)
        
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
      
    def runTimerIterator(self):
        self.parentWidget().parentWidget().catch_start()
        self.riModel.restart()
        # self.thread = QtCore.QThread()
        self.timerIterator = TimerIterator(self.sequence) #sequence кинь
        # self.timerIterator.moveToThread(self.thread)
        
        # self.thread.started.connect(self.timerIterator._start)
        # self.timerIterator.finished_signal.connect(self.thread.quit)
        self.timerIterator.finished_signal.connect(self.timerIterator.deleteLater)
        # self.thread.finished.connect(self.thread.deleteLater)
        # self.thread.start()
        # self.thread.exec()
        self.timerIterator.timer_started_signal.connect(lambda x: self.riModel.intervalStarted(x))
        
        
        self.timerIterator.timeout_signal.connect(lambda x: self.riModel.intervalEnded(x))
        
        
        
        self.timerIterator.pause_signal.connect(self.riModel.intervalPaused)
        self.timerIterator.resume_signal.connect(self.riModel.intervalResumed)
        
        
        
        
        
        
        self.timerIterator.finished_signal.connect(lambda x: self.riModel.intervalEnded(x))
        self.startPushButton.setEnabled(False)
        self.timerIterator.finished_signal.connect( lambda: self.startPushButton.setEnabled(True))
        self.generatePushButton.setEnabled(False)
        self.timerIterator.finished_signal.connect( lambda: self.generatePushButton.setEnabled(True))
        
        self.timerIterator._start()
        
        self.stopPushButton.clicked.connect(self.timerIterator._stop)
        
        self.pausePushButton.setCheckable(True)
        self.pausePushButton.toggled.connect( lambda x: self.timerIterator._pause() if x else self.timerIterator._resume())
       
        self.timerIterator.timer_started_signal.connect(lambda x: self.parentWidget().parentWidget().catch_timer(x))
        
        self.timerIterator.pause_signal.connect(self.parentWidget().parentWidget().catch_pause)
        self.timerIterator.resume_signal.connect(self.parentWidget().parentWidget().catch_resume)
        self.stopPushButton.clicked.connect(self.parentWidget().parentWidget().catch_stop)
        

       
        
        
        
        
        
        
        



class RIModel(QtCore.QAbstractListModel):
    #need to replace index calls and _index calls
    
    def __init__(self, intervals=None, *args, **kwargs):
        super(RIModel, self).__init__(*args, **kwargs)
        self.intervals = intervals or []
        statuses = ["got_food", "missed_food", "not_recorded", "paused", "recording_now", "recording_got"]
        self.iconPool = IconPool(statuses)
        self.last_started = -1
        self.status_before_pause = ""

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            status, text = self.intervals[index.row()]
            return f'{index.row() + 1}. {text} сек'
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
        
    
    def foodGiven(self):
        self.editStatus(_index(self.last_started), "recording_got")
    
    def intervalEnded(self,n):
        if self.getStatus(_index(n)) == "recording_now":
             self.editStatus(_index(n), "missed_food")
        else:
            if self.getStatus(_index(n)) == "recording_got":
                self.editStatus(_index(n), "got_food")
            
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

class FalsePassieArduino():
    def leverOut(self):
        print("Педаль выехала")
    def leverIn(self):
        print("Педаль уехала")
    def triggerOn(self):
        print("Auto ON")
    def triggerOff(self):
        print("Auto OFF")

     
        
class TimerIterator(QtCore.QObject):
    VEL = 1000 #10 times faster
    
    
    finished_signal = QtCore.pyqtSignal(int)
    timer_started_signal = QtCore.pyqtSignal(int)
    timeout_signal = QtCore.pyqtSignal(int)
    pause_signal = QtCore.pyqtSignal()
    resume_signal = QtCore.pyqtSignal()
    
    def __init__(self, time_sequence=[1,2,3]):
        super(TimerIterator, self).__init__()
        self.time_sequence = time_sequence
        self.current_index = 0
        self.max_index = len(self.time_sequence)-1
        
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.remaining_time = 0
        print("Timer iterator created")
        
    
    def _start(self):
        time = QtCore.QTime.currentTime()
        self.timer.timeout.connect(self._timeout)
        self.timer.start(self.time_sequence[self. current_index]*self.VEL) 
        self.timer_started_signal.emit(0)
        print(f"Timer iterator started {self.current_index}: {self.time_sequence[self. current_index]*self.VEL} " + time.toString("hh:mm:ss"))
        
    def _timeout(self):
        self.timeout_signal.emit(self.current_index)
        if self.current_index == self.max_index:
            self._stop()
            
        else:
            time = QtCore.QTime.currentTime()
            self.current_index += 1
            self.timer.start(self.time_sequence[self.current_index]*self.VEL)
            self.timer_started_signal.emit(self.current_index)
            print(f"Timer iterator went to {self.current_index}: {self.time_sequence[self. current_index]*self.VEL}" + time.toString("hh:mm:ss"))
        
    
    def _pause(self):
        self.remaining_time = self.timer.remainingTime()
        self.pause_signal.emit()
        self.timer.stop()
        print(self.remaining_time)
    
    def _resume(self):
        self.timer.start(self.remaining_time)
        self.resume_signal.emit()
        self.remaining_time = 0
    
    def _stop(self):
        print("THe END")
        self.timer.stop()
        self.finished_signal.emit(self.current_index)      
    
    
    
    


def main():
    app = QApplication(sys.argv)
    form = TestUiRi()
    form.show()
    app.exec_()



if __name__ == '__main__':
    main()
