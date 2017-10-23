import wx
import wx.aui
import ui.panels
import ui.dialogs

class Screen(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"党员管理系统", pos=wx.DefaultPosition, size=wx.Size(1280, 800),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.left_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.left_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        leftSizer = wx.BoxSizer(wx.VERTICAL)

        # 党员列表button
        self.btn_info = wx.Button(self.left_panel, wx.ID_ANY, u"党员列表", wx.DefaultPosition, (150,30), 0)
        leftSizer.Add(self.btn_info, 0, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        # 信息维护button
        self.btn_io = wx.Button(self.left_panel, wx.ID_ANY, u"信息维护", wx.DefaultPosition, (150,30), 0)
        leftSizer.Add(self.btn_io, 0, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        # 党费收缴button
        self.btn_df = wx.Button(self.left_panel, wx.ID_ANY, u"党费收缴", wx.DefaultPosition, (150,30), 0)
        leftSizer.Add(self.btn_df, 0, wx.TOP | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        # 信息导出button
        self.btn_print = wx.Button(self.left_panel, wx.ID_ANY, u"信息导出", wx.DefaultPosition, (150,30), 0)
        leftSizer.Add(self.btn_print, 0, wx.TOP | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.left_panel.SetSizer(leftSizer)
        self.left_panel.Layout()
        leftSizer.Fit(self.left_panel)
        hSizer.Add(self.left_panel, 0, wx.EXPAND | wx.ALL, 0)

        # 多标签页
        self.m_auinotebook = wx.aui.AuiNotebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                 wx.aui.AUI_NB_DEFAULT_STYLE)

        hSizer.Add(self.m_auinotebook, 3, wx.EXPAND | wx.ALL, 0)

        self.p = ui.panels.Panel_info(self.m_auinotebook)
        self.m_auinotebook.AddPage(self.p,'党员列表',True,wx.NullBitmap)

        self.SetSizer(hSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        self.Bind(wx.EVT_BUTTON, self.onClick)

    def __del__(self):
        pass

    def onClick(self, event):
        btn = event.GetEventObject()
        index = self.getPageIndex(btn.GetLabel())
        current = self.m_auinotebook.GetSelection()

        print(index , current)
        if index == current:
            return
        if index is not None:
            self.m_auinotebook.SetSelection(index)
        else:
            if btn is self.btn_info:
                self.p = ui.panels.Panel_info(self.m_auinotebook)
            if btn is self.btn_io:
                self.p = ui.panels.Panel_person_info(self.m_auinotebook)
            if btn is self.btn_df:
                self.p = ui.panels.Panel_df(self.m_auinotebook)
            if btn is self.btn_print:
                self.p = ui.panels.Panel_print(self.m_auinotebook)
            self.m_auinotebook.AddPage(self.p, btn.GetLabel(), True, wx.NullBitmap)


    def getPageIndex(self, label):
        count = self.m_auinotebook.GetPageCount()
        for index in range(count):
            if self.m_auinotebook.GetPageText(index) == label:
                return index
        return None

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
