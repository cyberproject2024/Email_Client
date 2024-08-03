# This is where we will start to write the Python for creating the client. 
# To install Kivy for windows in Visual Studio
# 1: Open the terminal in Visual Studio
# 2: type pip install kivy[full] and hit enter

## imports basic app stuff from Kivy
from kivy.app import *
from kivy.uix.label import *


class Cyber_Sec_EmailApp(App):
    def build(self):
        label = Label(text='Cyber Email')
        return label
app = Cyber_Sec_EmailApp()
app.run()
