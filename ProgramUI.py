import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Drawing import Point, Color
from System.Windows.Forms import Application, Button, Form, Label, TextBox, Panel, BorderStyle

import Component
import DBTBL

class SimpleTextBoxForm(Form):
    def __init__(self):
        startX = 30
        self.Text = "Program2 (Page1)"
        self.Width = 440
        self.Height = 620
        
        self.DatabasePanel = Component.CreatePanel(360, 230, startX, 30)
        self.databaseTable = DBTBL.DatabaseTable()
        self.DatabasePanel.Controls.Add(self.databaseTable.getTable())

        self.Controls.Add(Component.CreateLabel("Database", startX, 5))
        self.Controls.Add(self.DatabasePanel)
        self.Controls.Add(Component.CreateLabel("List", startX, 265))
        self.Controls.Add(Component.CreatePanel(360, 230, startX, 295))
        self.Controls.Add(Component.CreateButton("Next to page 2", startX, 540))

form = SimpleTextBoxForm()

Application.Run(form)