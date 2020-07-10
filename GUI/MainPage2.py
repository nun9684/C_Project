import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Drawing import Point, Color, ContentAlignment
from System.Windows.Forms import Application, Button, Form, Label, TextBox, Panel, BorderStyle, FlowDirection, FlowLayoutPanel, AutoSizeMode
from GUI.Page2 import TBL_Generator
import subprocess
import threading
import os
import time

class Page2(Form):
    def __init__(self):
        print("Create Page2")
        startX = 30
        self.Text = "Program2 (Page2)"
        self.Width = 440
        self.Height = 620

        self.cameraPanel = Panel()
        self.cameraPanel.Width = 360
        self.cameraPanel.Height = 360
        self.cameraPanel.Location = Point(30, 30)
        self.cameraPanel.BorderStyle = BorderStyle.FixedSingle

        self.lblLabel = Label()
        self.lblLabel.Width = 360
        self.lblLabel.Height = 50
        self.lblLabel.Location = Point(30, 400)
        self.lblLabel.BorderStyle = BorderStyle.FixedSingle

        self.statusContainer = Panel()
        self.statusContainer.Width = 310
        self.statusContainer.Height = 100
        self.statusContainer.Location = Point(30, 460)
        self.statusContainer.BorderStyle = BorderStyle.FixedSingle
        self.initHeaderForStatusPanel()
        self.statusContainer.Controls.Add(self.headerStatusPanel)

        self.btnPrint = Button()
        self.btnPrint.Width = 45
        self.btnPrint.Height = 100
        self.btnPrint.Location = Point(345, 460)
        self.btnPrint.Text = "Print"
        self.btnPrint.TextAlign = ContentAlignment.MiddleCenter

        self.initStatusContainer()
        self.initStatusPanel()
        # for x in range(10):
        #     databaseRow = TBL_Generator.StatusRow(self, "Chatchawan", str(12345 + x), "2/2", "OK")
        #     self.statusPanel.Controls.Add(databaseRow)

        self.statusContainer.Controls.Add(self.statusPanel)

        self.Controls.Add(self.cameraPanel)
        self.Controls.Add(self.lblLabel)
        self.Controls.Add(self.statusContainer)
        self.Controls.Add(self.btnPrint)
    
        self.inThreadObjDec = internalThreadCallObjDetection()
        self.inThreadObjDec.start()
        self.inThreadUpdateCtrls = internalThreadUpdateControls(self.statusPanel)
        self.inThreadUpdateCtrls.start()
        print('Create subprocess finish')
        self.FormClosed += self.formClose
    
    def initStatusPanel(self):
        path = os.getcwd() + r'\GUI\Camera\Value.txt'
        f = None
        try :
            f = open(path, "r")
            for text in f:
                val = text.split(",")
                databaseRow = TBL_Generator.StatusRow(self, val[0], val[1], val[2], val[3])
                self.statusPanel.Controls.Add(databaseRow)
        finally:
            if f is not None:
                f.close()
                
    def formClose(self, sender, evtArgs):
        print('form closed')
        self.inThreadObjDec.terminate()
        self.inThreadUpdateCtrls.terminate()
    
    def initHeaderForStatusPanel(self):
        self.headerStatusPanel = Panel()
        self.headerStatusPanel.BackColor = Color.White
        self.headerStatusPanel.Width = 310
        self.headerStatusPanel.Height = 20
        self.headerStatusPanel.Location = Point(0, 0)

        self.lblName = Label()
        self.lblName.Width = 70
        self.lblName.Height = 20
        self.lblName.Location = Point(6,0)
        self.lblName.TextAlign = ContentAlignment.MiddleCenter
        self.lblName.Text = "Name"

        self.lblID = Label()
        self.lblID.Width = 70
        self.lblID.Height = 20
        self.lblID.Location = Point(82,0)
        self.lblID.TextAlign = ContentAlignment.MiddleCenter
        self.lblID.Text = "ID"

        self.lblNumber = Label()
        self.lblNumber.Width = 70
        self.lblNumber.Height = 20
        self.lblNumber.Location = Point(158,0)
        self.lblNumber.TextAlign = ContentAlignment.MiddleCenter
        self.lblNumber.Text = "Number"   

        self.lblStatus = Label()
        self.lblStatus.Width = 70
        self.lblStatus.Height = 20
        self.lblStatus.Location = Point(225,0)
        self.lblStatus.TextAlign = ContentAlignment.MiddleCenter
        self.lblStatus.Text = "Status"  

        self.headerStatusPanel.Controls.Add(self.lblName)
        self.headerStatusPanel.Controls.Add(self.lblID)
        self.headerStatusPanel.Controls.Add(self.lblNumber)
        self.headerStatusPanel.Controls.Add(self.lblStatus)

    def initStatusContainer(self):
        self.statusPanel = FlowLayoutPanel()
        self.statusPanel.BackColor = Color.White
        self.statusPanel.Width = 310
        self.statusPanel.Height = 98
        self.statusPanel.Location = Point(0, 20)
        self.statusPanel.FlowDirection = FlowDirection.TopDown
        self.statusPanel.AutoScroll = True
        self.statusPanel.WrapContents = False
        self.statusPanel.HorizontalScroll.Visible = False
        self.statusPanel.HorizontalScroll.Enabled = False
        
class internalThreadCallObjDetection(threading.Thread):
    def __init__(self):
        print('Start new thread')
        threading.Thread.__init__(self)
    
    def run(self):
        path = os.getcwd()
        path = path + r'\GUI\Camera\Object_Detection.py'
        subprocess.call(path, shell=True)
        
    def terminate(self):
        self._running = False
        return

class internalThreadUpdateControls(threading.Thread):
    def __init__(self, listControls):
        self.lstControls = listControls
        self.listText = []
        threading.Thread.__init__(self)
        
    def run(self):
        self.path = os.getcwd() + r'\GUI\Camera\Value.txt'
        self._running = True
        self.readFile()
        
    def terminate(self):
        self._running = False
        return
        
    def readFile(self):
        while self._running :
            self.file = None
            try :
                self.file = open(self.path, "r")
                for f in self.file:
                    self.listText.Add(f.split(","))
                    
            except NameError:
                self.file = None
            finally :
                if self.file is not None:
                    self.file.close()
                    
            if len(self.listText) > 0:
                self.updateList()
            time.sleep(0.5)
            
    def updateList(self):
        print('Try to update list')
        i = 0
        for text in self.listText:
            for control in self.lstControls.Controls:
                control.Controls[0].Text = text[0]
                control.Controls[1].Text = text[1]
                control.Controls[2].Text = text[2]
                control.Controls[3].Text = text[3]
            i = i + 1
        