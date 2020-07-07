import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Drawing import Point, Color, ContentAlignment
from System.Windows.Forms import Application, Button, Form, Label, TextBox, Panel, BorderStyle, CheckBox, FlowLayoutPanel, AnchorStyles, DockStyle

class StatusRow(FlowLayoutPanel):
    def __init__(self, formParent, strName, strID, strNumber, strStatus):
        self.initLabel()

        self.lblName = Label()
        self.lblID = Label()
        self.lblNumber = Label()
        self.lblStatus = Label()
        
        self.formParent = formParent

        self.strName = strName
        self.strID = strID
        self.strNumber = strNumber
        self.strStatus = strStatus

        self.initLabelName(strName)
        self.initLabelID(strID)
        self.initLabelNumber(strNumber)
        self.initLabelStatus(strStatus)

        self.Controls.Add(self.lblName)
        self.Controls.Add(self.lblID)
        self.Controls.Add(self.lblNumber)
        self.Controls.Add(self.lblStatus)
    
    def initLabel(self):
        self.BackColor = Color.White
        self.Width = 300
        self.Height = 20

    def initLabelName(self, strName):
        self.lblName.Width = 70
        self.lblName.Height = 20
        self.lblName.TextAlign = ContentAlignment.MiddleCenter
        self.lblName.Text = strName
    
    def initLabelID(self, strID):
        self.lblID.Width = 70
        self.lblID.Height = 20
        self.lblID.TextAlign = ContentAlignment.MiddleCenter
        self.lblID.Text = strID

    def initLabelNumber(self, strNumber):
        self.lblNumber.Width = 70
        self.lblNumber.Height = 20
        self.lblNumber.TextAlign = ContentAlignment.MiddleCenter
        self.lblNumber.Text = strNumber

    def initLabelStatus(self, strStatus):
        self.lblStatus.Width = 50
        self.lblStatus.Height = 20
        self.lblStatus.TextAlign = ContentAlignment.MiddleCenter
        self.lblStatus.Text = strStatus
