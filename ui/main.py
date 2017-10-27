import wx
import wx.aui
import ui.panels
import ui.dialogs
import enty.member
import wx.dataview
from controler import Controller


class Screen(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"党员管理系统", pos=wx.DefaultPosition, size=wx.Size(1280, 800),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        # 数据源
        self.controller = Controller()

        # 布局
        self.layout()

        # 数据初始化
        self.initData()

        # 树形菜单事件绑定
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.onItemSelect)


    def layout(self):
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.nodetree1 = wx.TreeCtrl(self,id=wx.ID_ANY, pos=wx.DefaultPosition, size=(160,-1),
         style=wx.TR_DEFAULT_STYLE| wx.TR_HIDE_ROOT | wx.TR_NO_LINES | wx.TR_FULL_ROW_HIGHLIGHT | wx.TR_NO_BUTTONS, validator=wx.DefaultValidator,name=wx.TreeCtrlNameStr)

        node_root = self.nodetree1.AddRoot(u'根目录件')
        node_modi = self.nodetree1.AppendItem(node_root,u'党员信息')
        self.nodetree1.AppendItem(node_modi,u'信息维护')
        self.nodetree1.AppendItem(node_modi, u'转入转出')
        node_df = self.nodetree1.AppendItem(node_root, u'党费收缴')
        node_data= self.nodetree1.AppendItem(node_root, u'数据文件')
        self.nodetree1.AppendItem(node_data, u'数据备份')
        self.nodetree1.AppendItem(node_data, u'导入XLS')
        self.nodetree1.AppendItem(node_data, u'导出XLS')

        hSizer.Add(self.nodetree1, 0, wx.EXPAND | wx.ALL, 0)

        # 多标签页
        self.m_auinotebook = wx.aui.AuiNotebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                wx.aui.AUI_NB_DEFAULT_STYLE)
        self.currentPanel = ui.panels.Panel_info(self.m_auinotebook)
        self.m_auinotebook.AddPage(self.currentPanel, "党员信息", True, wx.NullBitmap)

        hSizer.Add(self.m_auinotebook, 3, wx.EXPAND | wx.ALL, 0)

        self.SetSizer(hSizer)
        self.Layout()

        self.Centre(wx.BOTH)


    def initData(self):
        print(self.controller.getAllData())
        self.currentPanel.showData(self.controller.getAllData())

    def __del__(self):
        pass


    def getPageIndex(self, label):
        count = self.m_auinotebook.GetPageCount()
        for index in range(count):
            if self.m_auinotebook.GetPageText(index) == label:
                return index
        return None

    def showPageWithData(self, label, data=None):

        current = self.m_auinotebook.GetSelection()
        index = self.getPageIndex(label)

        print(index, current)
        if index is None:
            if label == '党员信息':
                self.currentPanel = ui.panels.Panel_info(self.m_auinotebook)
            elif label == '信息维护':
                self.currentPanel = ui.panels.Panel_person_info(self.m_auinotebook)
            elif label == '党费收缴':
                self.currentPanel = ui.panels.Panel_df(self.m_auinotebook)
            elif label == '数据文件':
                self.currentPanel = ui.panels.Panel_print(self.m_auinotebook)
            else:
                return
            self.m_auinotebook.AddPage(self.currentPanel, label, True, wx.NullBitmap)
        else:
            if index is not current:
                self.m_auinotebook.SetSelection(index)
            self.currentPanel = self.m_auinotebook.GetPage(index)

        if data:
            self.currentPanel.showData(data)

    def onItemSelect(self,event):
        item = event.GetItem()
        title = self.nodetree1.GetItemText(item)
        print(title)
        self.showPageWithData(title)


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
