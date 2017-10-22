import wx
import wx.aui
import ui.panels

class Screen(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"党员管理系统", pos=wx.DefaultPosition, size=wx.Size(1280, 800),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.left_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.left_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        leftSizer = wx.BoxSizer(wx.VERTICAL)

        self.btn_info = wx.Button(self.left_panel, wx.ID_ANY, u"党员信息", wx.DefaultPosition, (150,30), 0)
        leftSizer.Add(self.btn_info, 0, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.btn_io = wx.Button(self.left_panel, wx.ID_ANY, u"转入转出", wx.DefaultPosition, (150,30), 0)
        leftSizer.Add(self.btn_io, 0, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.btn_df = wx.Button(self.left_panel, wx.ID_ANY, u"党费收缴", wx.DefaultPosition, (150,30), 0)
        leftSizer.Add(self.btn_df, 0, wx.TOP | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.btn_print = wx.Button(self.left_panel, wx.ID_ANY, u"信息导出", wx.DefaultPosition, (150,30), 0)
        leftSizer.Add(self.btn_print, 0, wx.TOP | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.left_panel.SetSizer(leftSizer)
        self.left_panel.Layout()
        leftSizer.Fit(self.left_panel)
        hSizer.Add(self.left_panel, 0, wx.EXPAND | wx.ALL, 0)

        self.m_auinotebook1 = wx.aui.AuiNotebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                 wx.aui.AUI_NB_DEFAULT_STYLE)

        hSizer.Add(self.m_auinotebook1, 3, wx.EXPAND | wx.ALL, 0)

        self.p_info = ui.panels.Panel_info(self.m_auinotebook1)
        self.m_auinotebook1.AddPage(self.p_info,'党员情况',False,wx.NullBitmap)

        self.p_person_info = ui.panels.Panel_person_info(self.m_auinotebook1)
        self.m_auinotebook1.AddPage(self.p_person_info, '个人基本信息', False, wx.NullBitmap)


        self.SetSizer(hSizer)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class MyApp(wx.App):
    def OnInit(self):
        s = Screen(None)
        s.CenterOnScreen()
        self.SetTopWindow(s)
        s.Show()
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
