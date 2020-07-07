import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Drawing import Point, Color, ContentAlignment
from System.Windows.Forms import Application, Button, Form, Label, TextBox, Panel, BorderStyle, CheckBox, FlowLayoutPanel, AnchorStyles, DockStyle

class DatabaseRow(FlowLayoutPanel):
    def __init__(self, formParent, myIndex, strName, strID):
        self.initLabel()
        self.checkBox = CheckBox()
        self.lblName = Label()
        self.lblID = Label()
        self.formParent = formParent
        self.strName = strName
        self.strID = strID

        self.initCheckBox()
        self.initLabelName(strName)
        self.initLabelID(strID)

        self.Controls.Add(self.checkBox)
        self.Controls.Add(self.lblName)
        self.Controls.Add(self.lblID)
    
    def initLabel(self):
        self.BackColor = Color.White
        self.Width = 320
        self.Height = 30

    def initCheckBox(self):
        self.checkBox.Width = 36
        self.checkBox.Height = 30
        self.checkBox.CheckAlign = ContentAlignment.MiddleCenter
        self.checkBox.Click += self.checkBox_Clicked

    def initLabelName(self, strName):
        self.lblName.Width = 133
        self.lblName.Height = 30
        self.lblName.TextAlign = ContentAlignment.MiddleCenter
        self.lblName.Text = strName
    
    def initLabelID(self, strID):
        self.lblID.Width = 133
        self.lblID.Height = 30
        self.lblID.TextAlign = ContentAlignment.MiddleCenter
        self.lblID.Text = strID

    def checkBox_Clicked(self, sender, evtArgs):
        listPanel = self.formParent.getListPanel()

        if(self.checkBox.Checked):
            listRow = ListRow(self.strName, self.strID)
            listPanel.Add(listRow)
        else :
            i = 0
            for control in listPanel:
                print("Try to Remove : " + control.lblID.Text)
                if(control.lblID.Text == self.lblID.Text):
                    listPanel.RemoveAt(i)
                    print("Remove it !!!")
                    break
                i += 1

    def getMe(self):
        return self

class ListRow(FlowLayoutPanel):
    def __init__(self, strName, strID):
        print("Create ListRow")
        self.initLabel()

        self.lblName = Label()
        self.lblID = Label()
        self.tbNumber = TextBox()

        self.initTextBoxNumber()
        self.initLabelName(strName)
        self.initLabelID(strID)

        self.Controls.Add(self.lblName)
        self.Controls.Add(self.lblID)
        self.Controls.Add(self.tbNumber)

    def initLabel(self):
        self.BackColor = Color.White
        self.Width = 320
        self.Height = 30

    def initLabelName(self, strName):
        self.lblName.Width = 100.67
        self.lblName.Height = 30
        self.lblName.TextAlign = ContentAlignment.MiddleCenter
        self.lblName.Text = strName
    
    def initLabelID(self, strID):
        self.lblID.Width = 100.67
        self.lblID.Height = 30
        self.lblID.TextAlign = ContentAlignment.MiddleCenter
        self.lblID.Text = strID

    def initTextBoxNumber(self):        
        self.tbNumber.Width = 100.67
        self.tbNumber.Height = 30
        self.tbNumber.Dock = DockStyle.Fill