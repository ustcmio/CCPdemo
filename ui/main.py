import wx
import wx.aui
import ui.panels
import ui.dialogs
import enty.member
import wx.dataview

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

        # self.panels = {
        #     '党员列表': ui.panels.Panel_info(self.m_auinotebook),
        #     '信息维护': ui.panels.Panel_person_info(self.m_auinotebook),
        #     '党费收缴': ui.panels.Panel_df(self.m_auinotebook),
        #     '信息导出': ui.panels.Panel_print(self.m_auinotebook)
        # }

        # for label,panel in self.panels.items():
        #     panel.Hide()

        self.currentPanel = ui.panels.Panel_info(self.m_auinotebook)
        self.m_auinotebook.AddPage(self.currentPanel,self.btn_info.GetLabel(),True,wx.NullBitmap)

        self.SetSizer(hSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        self.Bind(wx.EVT_BUTTON, self.onClick)

        self.initData()

        self.Bind(wx.EVT_MENU, self.menu)

    def initData(self):
        self.orgni = [enty.member.Member('张三','111111111111111111','0402302338'),enty.member.Member('李四','111111111111111111','0402302339')]
        self.currentPanel.showData(self.orgni)

    def __del__(self):
        pass

    def menu(self,event):
        print(event.GetId())

    def onClick(self, event):
        btn = event.GetEventObject()
        if btn is self.btn_info:
            self.showPageWithData(btn.GetLabel(),self.orgni)
        else:
            self.showPageWithData(btn.GetLabel())


    def getPageIndex(self, label):
        count = self.m_auinotebook.GetPageCount()
        for index in range(count):
            if self.m_auinotebook.GetPageText(index) == label:
                return index
        return None

    def showPageWithData(self,label,data=None):

        current = self.m_auinotebook.GetSelection()
        index = self.getPageIndex(label)

        print(index,current)
        if index is None:
            if label == '党员列表':
                self.currentPanel = ui.panels.Panel_info(self.m_auinotebook)
            elif label == '信息维护':
                self.currentPanel = ui.panels.Panel_person_info(self.m_auinotebook)
            elif label == '党费收缴':
                self.currentPanel = ui.panels.Panel_df(self.m_auinotebook)
            else:
                self.currentPanel = ui.panels.Panel_print(self.m_auinotebook)
            self.m_auinotebook.AddPage(self.currentPanel,label,True,wx.NullBitmap)
        else:
            if index is not current:
                self.m_auinotebook.SetSelection(index)
            self.currentPanel = self.m_auinotebook.GetPage(index)
        self.currentPanel.showData(data)


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
