import wx
import wx.dataview



class Panel_info(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(600, 600),
                          style=wx.TAB_TRAVERSAL)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        radioBoxChoices = [u"所有党员", u"一支部", u"二支部", u"三支部", u"四支部"]
        self.radioBox = wx.RadioBox(self, wx.ID_ANY, u"支部选择", wx.DefaultPosition, wx.DefaultSize, radioBoxChoices, 6,
                                    wx.RA_SPECIFY_COLS)
        self.radioBox.SetSelection(4)
        bSizer3.Add(self.radioBox, 0, wx.ALL | wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_searchCtrl1 = wx.SearchCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_searchCtrl1.ShowSearchButton(True)
        self.m_searchCtrl1.ShowCancelButton(False)
        bSizer4.Add(self.m_searchCtrl1, 3, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.btn_reflash = wx.Button(self, wx.ID_ANY, u"刷  新", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.btn_reflash, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer3.Add(bSizer4, 0, wx.EXPAND, 5)

        self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                                wx.dataview.DV_HORIZ_RULES | wx.dataview.DV_VERT_RULES)
        self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.AppendToggleColumn(u"选择")
        self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.AppendTextColumn(u"序号")
        self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.AppendTextColumn(u"姓名")
        self.m_dataViewListColumn3 = self.m_dataViewListCtrl1.AppendTextColumn(u"性别")
        self.m_dataViewListColumn4 = self.m_dataViewListCtrl1.AppendTextColumn(u"身份证号")
        self.m_dataViewListColumn5 = self.m_dataViewListCtrl1.AppendTextColumn(u"所在支部")
        self.m_dataViewListColumn6 = self.m_dataViewListCtrl1.AppendTextColumn(u"入党年月")
        self.m_dataViewListColumn7 = self.m_dataViewListCtrl1.AppendTextColumn(u"转正时间")
        self.m_dataViewListColumn5 = self.m_dataViewListCtrl1.AppendTextColumn(u"所在支部")
        self.m_dataViewListColumn6 = self.m_dataViewListCtrl1.AppendTextColumn(u"入党年月")
        self.m_dataViewListColumn7 = self.m_dataViewListCtrl1.AppendTextColumn(u"转正时间")

        self.m_dataViewListCtrl1.AppendItem([True,1,2,3,4,5,6,7,8,9,10])
        self.m_dataViewListCtrl1.AppendItem([True,1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.m_dataViewListCtrl1.AppendItem([True,1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.m_dataViewListCtrl1.AppendItem([True,1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        bSizer3.Add(self.m_dataViewListCtrl1, 3, wx.ALL | wx.EXPAND, 5)

        self.Bind(wx.dataview.EVT_DATAVIEW_ITEM_CONTEXT_MENU, self.itemMenu)
        self.SetSizer(bSizer3)
        self.Layout()

        self.i_menu = wx.Menu()
        self.i_menu_item1 = wx.MenuItem(self.i_menu,wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL)
        self.i_menu_item2 = wx.MenuItem(self.i_menu,wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL)
        self.i_menu.Append(self.i_menu_item1)
        self.i_menu.Append(self.i_menu_item2)


    def __del__(self):
        pass

    def itemMenu(self, event):
        self.PopupMenu(self.i_menu, event.GetPosition())
        print(self.m_dataViewListCtrl1.ItemToRow(event.GetItem()))
