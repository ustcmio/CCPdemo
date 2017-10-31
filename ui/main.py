import wx
import wx.aui
import ui.panels
import ui.dialogs
import enty.member
import wx.dataview
from controler import Controller
import ui.dialogs


class Screen(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"党员管理系统", pos=wx.DefaultPosition, size=wx.Size(1280, 800),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        # 数据源
        self.db = Controller()
        # 获取所有支部名称
        self.choices = self.db.getChoices()

        # 当前面板
        self.currentPanel = None

        # 布局
        self.layout()

        # 默认显示党员信息
        self.showPageWithData(u'党员列表', self.db.getAllData())

        # 树形菜单事件绑定
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.onItemSelect)

        self.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSED,self.onPageClosed, self.m_auinotebook)


    def layout(self):
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.nodetree1 = wx.TreeCtrl(self,id=wx.ID_ANY, pos=wx.DefaultPosition, size=(160,-1),
         style=wx.TR_DEFAULT_STYLE| wx.TR_HIDE_ROOT | wx.TR_NO_LINES | wx.TR_FULL_ROW_HIGHLIGHT | wx.TR_NO_BUTTONS, validator=wx.DefaultValidator,name=wx.TreeCtrlNameStr)

        node_root = self.nodetree1.AddRoot(u'根目录件')
        node_modi = self.nodetree1.AppendItem(node_root,u'党员信息')
        self.nodetree1.AppendItem(node_modi, u'党员列表')
        self.nodetree1.AppendItem(node_modi,u'信息维护')
        self.nodetree1.AppendItem(node_modi, u'转入转出')
        node_df = self.nodetree1.AppendItem(node_root, u'党费收缴')
        node_data= self.nodetree1.AppendItem(node_root, u'数据文件')
        self.nodetree1.AppendItem(node_data, u'数据备份')
        self.nodetree1.AppendItem(node_data, u'导入Excel')
        self.nodetree1.AppendItem(node_data, u'导出Excel')

        hSizer.Add(self.nodetree1, 0, wx.EXPAND | wx.ALL, 0)

        # 多标签页
        self.m_auinotebook = wx.aui.AuiNotebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                wx.aui.AUI_NB_DEFAULT_STYLE)


        hSizer.Add(self.m_auinotebook, 3, wx.EXPAND | wx.ALL, 0)

        self.SetSizer(hSizer)
        self.Layout()

        self.Centre(wx.BOTH)


    def __del__(self):
        self.db.saveToDatabase()
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
            if label == '党员列表':
                self.currentPanel = ui.panels.Panel_info(self.m_auinotebook,self.choices)
                self.currentPanel.showData(self.db.getAllData())
            elif label == '信息维护':
                self.currentPanel = ui.panels.Panel_person_info(self.m_auinotebook,self.choices)
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
        if title == '导入Excel':
            self.import_Excel()
        elif title == '导出Excel':
            pass
        else:
            self.showPageWithData(title)

    def onPageClosed(self,event):
        # print('close')
        self.nodetree1.UnselectAll()

    def import_Excel(self):
        msgdlg = wx.MessageDialog(self,"导入Excel将清空原有数据，请确认已备份原有数据。",style=wx.OK | wx.CANCEL)
        if msgdlg.ShowModal() == wx.ID_OK:
            filesFilter = "Excel (*.xls;*.xlsx)|*.xls;*.xlsx|" "All files (*.*)|*.*"
            dlg = wx.FileDialog(self, '选择Excel文件', defaultDir='.', wildcard=filesFilter, style=wx.FD_OPEN)
            if dlg.ShowModal() == wx.ID_OK:
                self.db.dataFromExcel(dlg.GetPath())
                self.showPageWithData('党员列表',self.db.getAllData())



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
