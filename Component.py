import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Drawing import Point, Color
from System.Windows.Forms import Application, Button, Form, Label, TextBox, Panel, BorderStyle

def CreatePanel(width, height, pointX, pointY):
    panel = Panel()
    panel.BackColor = Color.White
    panel.Width = width
    panel.Height = height
    panel.Location = Point(pointX, pointY)
    panel.BorderStyle = BorderStyle.FixedSingle

    return panel

def CreateLabel(text, posX, posY):
    label = Label()
    label.Text = text
    label.Location = Point(posX, posY)

    return label

def CreateButton(text, posX, posY):
    button = Button()
    button.Text = text
    button.Width = 360
    button.Location = Point(posX, posY)

    return button