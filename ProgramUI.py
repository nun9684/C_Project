import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
import sys
import os
sys.path.append(os.path.dirname(__file__))
print(os.path.dirname(__file__))
from System.Windows.Forms import Application
from GUI.MainPage1 import Page1

form = Page1()
Application.Run(form)