
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 800, 800, 800)  
        self.setWindowTitle('INI-Maker V1.01')

        # ---------- Menun bar add ---------------
        # Create new action INI Open
        iniopen_action = QAction('&INI Open', self)
        iniopen_action.setShortcut('Ctrl+I')
        iniopen_action.setStatusTip('INI File OPEN')
        iniopen_action.triggered.connect(self.ini_opencall)

        # Map Open new action
        mapopen_action = QAction('&Map Open', self)
        mapopen_action.setShortcut('Ctrl+M')
        mapopen_action.setStatusTip('MAP File OPEN')
        mapopen_action.triggered.connect(self.map_opencall)

        savefile_action = QAction('&Save File', self)
        savefile_action.setShortcut('Ctrl+S')
        savefile_action.setStatusTip('Save File Path')
        savefile_action.triggered.connect(self.savefile_call)

        # Exit action
        close_action = QAction('&Exit', self)
        close_action.setShortcut('Ctrl+Q')
        close_action.setStatusTip('EXIT')
        close_action.triggered.connect(self.menu_closecall)

        # Info action
        info_action = QAction('&Info', self)
        #info_action.setShortcut('Ctrl+Q')
        info_action.setStatusTip('Info')
        info_action.triggered.connect(self.menu_infocall)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(iniopen_action)
        file_menu.addAction(mapopen_action)
        file_menu.addAction(savefile_action)
        file_menu.addAction(close_action)

        file_menu = menu_bar.addMenu('&Info')
        file_menu.addAction(info_action)
        self.setupUI()
    

    def setupUI(self):

        self.ta1 = QTableWidget(self)
        self.ta1.setGeometry(0, 40, 500, 500)  
        self.ta1.resize(600, 600)
        self.ta1.setColumnCount(3)
        self.ta1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ta1.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
    
        action1 = QAction("메뉴1" , self.ta1)
        action2 = QAction("메뉴2" , self.ta1)

        action1.triggered.connect(self.action1_fun)
        action2.triggered.connect(self.action2_fun)


        self.ta1.addAction(action1)
        self.ta1.addAction(action2)

        table_column=["첫번째 열" , "두번째 열" , "Third 열"]
        self.ta1.setHorizontalHeaderLabels(table_column)

        
        #행 2개 추가
        self.ta1.setRowCount(2)
        
        #추가된 행에 데이터 채워넣음
        self.ta1.setItem(0, 0, QTableWidgetItem("(0,0)"))
        self.ta1.setItem(0, 1, QTableWidgetItem("(0,1)"))
        self.ta1.setItem(1, 0, QTableWidgetItem("(1,0)"))
        self.ta1.setItem(1, 1, QTableWidgetItem("(1,1)"))     

    def action1_fun(self):
        print("action1 메뉴 선택")

    def action2_fun(self):
        print("action2 메뉴 선택")

    def ini_opencall(self):
        #print('ini call')
        global ininame 
        ininame = QFileDialog.getOpenFileName(self, 'Open File', '',
                                            'INI File(*.ini)')
        self.pathLabel.setText('INI File Path : '+ininame[0])
        if len(ininame[0]) == 0 :
            ininame = None
        self.button_set()

    
    # map open 함수 호출
    def map_opencall(self):
        #print('map call')      
        global mapname  
        mapname = QFileDialog.getOpenFileName(self, 'Open File', '',
                                            'MAP File(*.map)')
        self.pathLabe2.setText('MAP File Path : '+mapname[0])
        if len(mapname[0]) == 0 :
            mapname = None
        self.button_set()
        #print(mapname[0])

    # save file 함수 호출
    def savefile_call(self):
        #print('save open call')
        global savename
        savename = QFileDialog.getSaveFileName(self, 'Save File', '',
                                            'INI File(*.ini)')
        self.pathLabe3.setText('SAVE Path : '+savename[0])
        if len(savename[0]) == 0 :
            savename = None
        self.button_set()
        #print(savename[0])
    
    def menu_infocall(self):
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle('Info')
        self.msg.setText('Question: jadu9000142@rinnai.co.kr')
        self.msg.setStandardButtons(QMessageBox.Ok)
        retval = self.msg.exec_()
        #print('QMessageBox 리턴값 ', retval)
        if retval == QMessageBox.Ok :
            print('messagebox ok : ', retval)   

    def menu_closecall(self):
        #print('exit menu call')
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()