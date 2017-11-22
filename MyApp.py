import wx
from ui.mainScreen import MainScreen

class MyApp(wx.App):
    def OnInit(self):
        s = MainScreen(None)
        s.CenterOnScreen()
        self.SetTopWindow(s)
        s.Show()
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
