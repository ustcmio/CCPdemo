import wx
import wx.aui
import ui.panels
import ui.dialogs
import wx.dataview
from controler import Controller
import ui.dialogs

# 主界面布局
class MainScreen(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"党员管理系统", pos=wx.DefaultPosition, size=wx.Size(1280, 800),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # 一、布局
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        # 1、左侧树形结构,wx.TR_HIDE_ROOT：隐藏根节点
        self.leftnodetree = wx.TreeCtrl(self, id=wx.ID_ANY, pos=wx.DefaultPosition, size=(200, -1),
                                     style=wx.TR_DEFAULT_STYLE | wx.TR_HIDE_ROOT | wx.TR_NO_LINES | wx.TR_FULL_ROW_HIGHLIGHT | wx.TR_NO_BUTTONS,
                                     validator=wx.DefaultValidator, name=wx.TreeCtrlNameStr)

        node_root = self.leftnodetree.AddRoot(u'根目录')
        self.node_all = self.leftnodetree.AppendItem(node_root, u'党员列表')
        node_modify = self.leftnodetree.AppendItem(node_root, u'党员管理')
        self.leftnodetree.AppendItem(node_modify, u'信息维护')
        self.leftnodetree.AppendItem(node_modify, u'转入转出')
        node_df = self.leftnodetree.AppendItem(node_root, u'党费收缴')
        node_data = self.leftnodetree.AppendItem(node_root, u'数据管理')
        self.leftnodetree.AppendItem(node_data, u'数据备份')
        self.leftnodetree.AppendItem(node_data, u'导入Excel')
        self.leftnodetree.AppendItem(node_data, u'导出Excel')
        self.leftnodetree.ExpandAll()

        hSizer.Add(self.leftnodetree, 0, wx.EXPAND | wx.ALL, 0)

        # 2、右侧多标签页
        self.m_auinotebook = wx.aui.AuiNotebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                wx.aui.AUI_NB_DEFAULT_STYLE)

        hSizer.Add(self.m_auinotebook, 3, wx.EXPAND | wx.ALL, 0)

        self.SetSizer(hSizer)
        self.Layout()

        self.Centre(wx.BOTH)


        # 二、加载数据信息
        self.db = Controller()

        # 获取所有支部名称
        self.setParty()
        # 当前面板
        self.currentPanel = None
        # 默认显示党员信息
        # self.showPageWithData(u'党员列表', self.db.getAllData())

        # 三、绑定各类事件
        # 树形菜单事件绑定
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.onItemSelect)

        self.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSED,self.onPageClosed, self.m_auinotebook)


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

        if index is None:
            if label == '党员列表':
                self.currentPanel = ui.panels.Panel_info(self.m_auinotebook)
            elif label == '信息维护':
                self.currentPanel = ui.panels.Panel_person_info(self.m_auinotebook, self.db.getChoices())
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
        title = self.leftnodetree.GetItemText(item)

        # 显示数据库为空的提示
        msgdlg = None
        if title=='党员列表' and not self.db.getAllData():
            msgdlg = wx.MessageDialog(self,"数据库为空！",style=wx.OK | wx.CANCEL)

        if title == u'党员列表':
            self.showPageWithData(title,data=self.db.getAllData())
        elif title in self.db.getChoices():
            self.showPageWithData(u'党员列表', data = self.db.getAllData(szzb=title))
        elif title == u'信息维护':
            self.showPageWithData(title)
        elif title == u'转入转出':
            pass
        elif title == u'党费缴至':
            self.showPageWithData(title)
        elif title == u'数据备份':
            pass
        elif title == '导入Excel':
            self.import_Excel()
        elif title == '导出Excel':
            pass
        else:
            return

        # 提示数据库为空
        if msgdlg:
            msgdlg.ShowModal()

    def onPageClosed(self,event):
        # print('close')
        self.leftnodetree.UnselectAll()

    def import_Excel(self):
        msgdlg = wx.MessageDialog(self,"导入Excel将清空原有数据，请确认已备份原有数据。",style=wx.OK | wx.CANCEL)
        if msgdlg.ShowModal() == wx.ID_OK:
            filesFilter = "Excel (*.xls;*.xlsx)|*.xls;*.xlsx|" "All files (*.*)|*.*"
            dlg = wx.FileDialog(self, '选择Excel文件', defaultDir='.', wildcard=filesFilter, style=wx.FD_OPEN)
            if dlg.ShowModal() == wx.ID_OK:
                self.db.dataFromExcel(dlg.GetPath())
        self.setParty()
        self.currentPanel.showData(self.db.getAllData())

    def setParty(self):
        choices = self.db.getChoices()
        if choices:
            for choice in choices:
                self.leftnodetree.AppendItem(self.node_all, choice)
            self.leftnodetree.ExpandAll()
