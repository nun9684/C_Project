import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Drawing import Point, Color, ContentAlignment
from System.Windows.Forms import Application, Button, Form, Label, TextBox, Panel, BorderStyle, FlowDirection, FlowLayoutPanel, MessageBox, AutoSizeMode

from GUI.Page1 import TBL_Generator
from GUI.MainPage2 import Page2

class Page1(Form):
    def __init__(self):
        startX = 30
        self.Text = "Program2 (Page1)"
        self.Width = 440
        self.Height = 620

        self.databaseContainer = Panel()
        self.databaseContainer.Width = 360
        self.databaseContainer.Height = 225
        self.databaseContainer.Location = Point(30,30)
        self.databaseContainer.BorderStyle = BorderStyle.FixedSingle

        self.listContainer = Panel()
        self.listContainer.Width = 360
        self.listContainer.Height = 225
        self.listContainer.Location = Point(30,295)
        self.listContainer.BorderStyle = BorderStyle.FixedSingle

        self.btnNextPage = Button()
        self.btnNextPage.Width = 360
        self.btnNextPage.Height = 30
        self.btnNextPage.Location = Point(30,530)
        self.btnNextPage.Text = "Next to Page 2"
        self.btnNextPage.Enabled = True
        self.btnNextPage.Click += self.btnNextPage_Clicked

        self.initHeaderForDatabasePanel()
        self.initDatabasePanel()
        self.initHeaderForListPanel()
        self.initListPanel()

        for x in range(10):
            databaseRow = TBL_Generator.DatabaseRow(self, x, "Chatchawan", str(12345 + x))
            self.DatabasePanel.Controls.Add(databaseRow)

        self.databaseContainer.Controls.Add(self.headerDBPanel)
        self.databaseContainer.Controls.Add(self.DatabasePanel)

        self.listContainer.Controls.Add(self.ListPanel)
        self.listContainer.Controls.Add(self.headerListPanel)

        self.Controls.Add(self.databaseContainer)
        self.Controls.Add(self.listContainer)
        self.Controls.Add(self.btnNextPage)

    def getListPanel(self):
        return self.ListPanel.Controls

    def btnNextPage_Clicked(self, sender, evtArgs):
        if(self.recursivevTextBoxCheck()):
            p2 = Page2()
            p2.Show()            

    def recursivevTextBoxCheck(self):
        isOK = True
        if(len(self.ListPanel.Controls) == 0):
            isOK = isOK & False
            MessageBox.Show("Please select list !")
        else:
            for panel in self.ListPanel.Controls:
                for control in panel.Controls :
                    if (control.GetType() == type(TextBox())):
                        if control.Text == "":
                            isOK = isOK & False
                            MessageBox.Show("Please fill in number input box !")
                            break
        return isOK

    def initDatabasePanel(self):
        self.DatabasePanel = FlowLayoutPanel()
        self.DatabasePanel.BackColor = Color.White
        self.DatabasePanel.Width = 360
        self.DatabasePanel.Height = 195
        self.DatabasePanel.Location = Point(0, 30)
        self.DatabasePanel.FlowDirection = FlowDirection.TopDown
        self.DatabasePanel.AutoScroll = True
        self.DatabasePanel.WrapContents = False
        self.DatabasePanel.HorizontalScroll.Visible = False
        self.DatabasePanel.HorizontalScroll.Enabled = False
    
    def initHeaderForDatabasePanel(self):
        self.headerDBPanel = Panel()
        self.headerDBPanel.BackColor = Color.White
        self.headerDBPanel.Width = 360
        self.headerDBPanel.Height = 30
        self.headerDBPanel.Location = Point(0, 0)

        self.lblName = Label()
        self.lblName.Width = 133
        self.lblName.Height = 30
        self.lblName.Location = Point(49,0)
        self.lblName.TextAlign = ContentAlignment.MiddleCenter
        self.lblName.Text = "Name"

        self.lblID = Label()
        self.lblID.Width = 133
        self.lblID.Height = 30
        self.lblID.Location = Point(188,0)
        self.lblID.TextAlign = ContentAlignment.MiddleCenter
        self.lblID.Text = "ID"

        self.headerDBPanel.Controls.Add(self.lblName)
        self.headerDBPanel.Controls.Add(self.lblID)

    def initListPanel(self):
        self.ListPanel = FlowLayoutPanel()
        self.ListPanel.BackColor = Color.White
        self.ListPanel.Width = 360
        self.ListPanel.Height = 195
        self.ListPanel.Location = Point(0, 30)
        self.ListPanel.FlowDirection = FlowDirection.TopDown
        self.ListPanel.AutoScroll = True
        self.ListPanel.WrapContents = False
        self.ListPanel.HorizontalScroll.Visible = False
        self.ListPanel.HorizontalScroll.Enabled = False

    def initHeaderForListPanel(self):
        self.headerListPanel = Panel()
        self.headerListPanel.BackColor = Color.White
        self.headerListPanel.Width = 360
        self.headerListPanel.Height = 30
        self.headerListPanel.Location = Point(0, 0)

        self.lblName = Label()
        self.lblName.Width = 100.67
        self.lblName.Height = 30
        self.lblName.Location = Point(0,0)
        self.lblName.TextAlign = ContentAlignment.MiddleCenter
        self.lblName.Text = "Name"

        self.lblID = Label()
        self.lblID.Width = 100.67
        self.lblID.Height = 30
        self.lblID.Location = Point(109,0)
        self.lblID.TextAlign = ContentAlignment.MiddleCenter
        self.lblID.Text = "ID"

        self.lblNumber = Label()
        self.lblNumber.Width = 100.67
        self.lblNumber.Height = 30
        self.lblNumber.Location = Point(218,0)
        self.lblNumber.TextAlign = ContentAlignment.MiddleCenter
        self.lblNumber.Text = "Number"   

        self.headerListPanel.Controls.Add(self.lblName)
        self.headerListPanel.Controls.Add(self.lblID)
        self.headerListPanel.Controls.Add(self.lblNumber)
