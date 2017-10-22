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
        self.radioBox.SetSelection(0)
        bSizer3.Add(self.radioBox, 0, wx.ALL | wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_searchCtrl1 = wx.SearchCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_searchCtrl1.ShowSearchButton(True)
        self.m_searchCtrl1.ShowCancelButton(False)
        bSizer4.Add(self.m_searchCtrl1, 3, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.btn_reflash = wx.Button(self, wx.ID_ANY, u"刷  新", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.btn_reflash, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer3.Add(bSizer4, 0, wx.EXPAND, 5)

        self.dvList = wx.dataview.DataViewListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.dataview.DV_HORIZ_RULES | wx.dataview.DV_VERT_RULES)
        self.dvListCol_id = self.dvList.AppendTextColumn(u"序号", width=40, align=wx.ALIGN_CENTER)
        self.dvListCol_party = self.dvList.AppendTextColumn(u"所在支部", width=60, align=wx.ALIGN_CENTER)
        self.dvListCol_isprob = self.dvList.AppendTextColumn(u"预备/正式", width=70, align=wx.ALIGN_CENTER)
        self.dvListCol_name = self.dvList.AppendTextColumn(u"姓  名", width=50, align=wx.ALIGN_CENTER)
        self.dvListCol_sex = self.dvList.AppendTextColumn(u"性别", width=40, align=wx.ALIGN_CENTER)
        self.dvListCol_pid = self.dvList.AppendTextColumn(u"身份证号", width=150, align=wx.ALIGN_CENTER)
        self.dvListCol_addr = self.dvList.AppendTextColumn(u"住址", width=250, align=wx.ALIGN_CENTER)
        self.dvListCol_phone = self.dvList.AppendTextColumn(u"座机", width=100, align=wx.ALIGN_CENTER)
        self.dvListCol_tel = self.dvList.AppendTextColumn(u"手机", width=100, align=wx.ALIGN_CENTER)
        self.dvListCol_dfjz = self.dvList.AppendTextColumn(u"党费交至", width=80, align=wx.ALIGN_CENTER)
        self.dvListCol_other = self.dvList.AppendTextColumn(u"备注", width=140, align=wx.ALIGN_CENTER)
        # self.dvListCol_date1 = self.dvList.AppendTextColumn(u"入党年月")
        # self.dvListCol_date2 = self.dvList.AppendTextColumn(u"转正时间")
        # self.dvListCol_date_in = self.dvList.AppendTextColumn(u"转入时间")
        # self.dvListCol_from = self.dvList.AppendTextColumn(u"转入地")

        self.dvList.AppendItem(
            [1, '一支部', '正式', '张张三', '男', '11111111111111111X', '锡山区东亭街道柏庄社区柏木南苑12-1201', '88708888', '13088888888',
             '201706', '党小组长'], data=11111111)

        bSizer3.Add(self.dvList, 3, wx.ALL | wx.EXPAND, 5)

        self.Bind(wx.dataview.EVT_DATAVIEW_ITEM_CONTEXT_MENU, self.itemMenu)
        self.SetSizer(bSizer3)
        self.Layout()

        self.i_menu = wx.Menu()
        self.i_menu_item1 = wx.MenuItem(self.i_menu, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL)
        self.i_menu_item2 = wx.MenuItem(self.i_menu, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL)
        self.i_menu.Append(self.i_menu_item1)
        self.i_menu.Append(self.i_menu_item2)

    def __del__(self):
        pass

    def itemMenu(self, event):
        self.PopupMenu(self.i_menu, event.GetPosition())
        print(self.dvList.ItemToRow(event.GetItem()))
        print(self.dvList.GetItemData(event.GetItem()))


class Panel_person_info(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(1100, 800),
                          style=wx.TAB_TRAVERSAL)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button3, 0, wx.ALL, 2)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button4, 0, wx.ALL, 2)

        bSizer1.Add(bSizer2, 0, wx.EXPAND, 2)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"个人基本信息", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_CENTRE)
        self.m_staticText1.Wrap(-1)
        bSizer3.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)

        gbSizer1 = wx.GridBagSizer(3, 5)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"姓  名：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        gbSizer1.Add(self.m_staticText3, wx.GBPosition(0, 0), wx.GBSpan(1, 1),
                     wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.t_name = wx.TextCtrl(self, wx.ID_ANY, u"张三三", wx.DefaultPosition, wx.Size(80, -1), wx.TE_CENTRE)
        gbSizer1.Add(self.t_name, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.ALL,
                     5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"姓  别：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        gbSizer1.Add(self.m_staticText4, wx.GBPosition(0, 2), wx.GBSpan(1, 1),
                     wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.ALIGN_RIGHT, 5)

        m_choice1Choices = [u"男", u"女"]
        self.m_choice1 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        gbSizer1.Add(self.m_choice1, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"民族：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        gbSizer1.Add(self.m_staticText5, wx.GBPosition(0, 4), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.t_race = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(70, -1), 0)
        gbSizer1.Add(self.t_race, wx.GBPosition(0, 5), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.EXPAND,
                     5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"公民身份证号：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        gbSizer1.Add(self.m_staticText6, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_textCtrl3, wx.GBPosition(1, 1), wx.GBSpan(1, 5),
                     wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.ALL, 5)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"学  历：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        gbSizer1.Add(self.m_staticText7, wx.GBPosition(0, 6), wx.GBSpan(1, 1),
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_textCtrl4, wx.GBPosition(0, 7), wx.GBSpan(1, 1),
                     wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.ALL, 5)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"人员类别：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        gbSizer1.Add(self.m_staticText8, wx.GBPosition(1, 6), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl6 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_textCtrl6, wx.GBPosition(1, 7), wx.GBSpan(1, 1),
                     wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, u"所在党支部：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        gbSizer1.Add(self.m_staticText9, wx.GBPosition(2, 0), wx.GBSpan(1, 1),
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_textCtrl7 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_textCtrl7, wx.GBPosition(2, 1), wx.GBSpan(1, 5), wx.ALL | wx.EXPAND, 5)

        self.m_staticText24 = wx.StaticText(self, wx.ID_ANY, u"党内职务：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText24.Wrap(-1)
        gbSizer1.Add(self.m_staticText24, wx.GBPosition(2, 6), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        m_choice2Choices = [u"无", u"支部书记", u"党小组长"]
        self.m_choice2 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(110, -1), m_choice2Choices, 0)
        self.m_choice2.SetSelection(0)
        gbSizer1.Add(self.m_choice2, wx.GBPosition(2, 7), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_radioBtn7 = wx.RadioButton(self, wx.ID_ANY, u"预备党员", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        gbSizer1.Add(self.m_radioBtn7, wx.GBPosition(3, 6), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_radioBtn8 = wx.RadioButton(self, wx.ID_ANY, u"正式党员", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_radioBtn8, wx.GBPosition(3, 7), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"入党日期：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        gbSizer1.Add(self.m_staticText10, wx.GBPosition(3, 0), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText13 = wx.StaticText(self, wx.ID_ANY, u"工作岗位：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)
        gbSizer1.Add(self.m_staticText13, wx.GBPosition(4, 0), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText14 = wx.StaticText(self, wx.ID_ANY, u"联系电话：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)
        gbSizer1.Add(self.m_staticText14, wx.GBPosition(5, 0), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText16 = wx.StaticText(self, wx.ID_ANY, u"手机号码：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)
        gbSizer1.Add(self.m_staticText16, wx.GBPosition(5, 3), wx.GBSpan(1, 2),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl12 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_textCtrl12, wx.GBPosition(5, 5), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"家庭地址：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        gbSizer1.Add(self.m_staticText17, wx.GBPosition(6, 0), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, u"党籍状态：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)
        gbSizer1.Add(self.m_staticText18, wx.GBPosition(8, 0), wx.GBSpan(1, 2),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER, 5)

        self.m_radioBtn1 = wx.RadioButton(self, wx.ID_ANY, u"正常", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        gbSizer1.Add(self.m_radioBtn1, wx.GBPosition(8, 2), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_radioBtn2 = wx.RadioButton(self, wx.ID_ANY, u"不正常", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_radioBtn2.SetValue(True)
        gbSizer1.Add(self.m_radioBtn2, wx.GBPosition(8, 3), wx.GBSpan(1, 2), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText19 = wx.StaticText(self, wx.ID_ANY, u"是否失联：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText19.Wrap(-1)
        gbSizer1.Add(self.m_staticText19, wx.GBPosition(9, 0), wx.GBSpan(2, 2), wx.ALL | wx.ALIGN_CENTER, 5)

        self.m_radioBtn3 = wx.RadioButton(self, wx.ID_ANY, u"否", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        gbSizer1.Add(self.m_radioBtn3, wx.GBPosition(9, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_radioBtn4 = wx.RadioButton(self, wx.ID_ANY, u"是", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_radioBtn4, wx.GBPosition(10, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText21 = wx.StaticText(self, wx.ID_ANY, u"失联日期：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        gbSizer1.Add(self.m_staticText21, wx.GBPosition(10, 3), wx.GBSpan(1, 2), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl15 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_textCtrl15, wx.GBPosition(10, 5), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.m_staticText22 = wx.StaticText(self, wx.ID_ANY, u"是否流动：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        gbSizer1.Add(self.m_staticText22, wx.GBPosition(11, 0), wx.GBSpan(1, 2),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER, 5)

        self.m_radioBtn5 = wx.RadioButton(self, wx.ID_ANY, u"否", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        gbSizer1.Add(self.m_radioBtn5, wx.GBPosition(11, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_listCtrl1 = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, (-1,150),
                                       wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
        self.m_listCtrl1.AppendColumn('序号', width=50)
        self.m_listCtrl1.AppendColumn('日期',width=100)
        self.m_listCtrl1.AppendColumn('类型', width=100)
        self.m_listCtrl1.AppendColumn('转入地/转出地', width=200)
        self.m_listCtrl1.AppendColumn('备注', width=200)
        gbSizer1.Add(self.m_listCtrl1, wx.GBPosition(14, 0), wx.GBSpan(1, 8),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_radioBtn6 = wx.RadioButton(self, wx.ID_ANY, u"是", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_radioBtn6, wx.GBPosition(12, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText23 = wx.StaticText(self, wx.ID_ANY, u"外出流向：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText23.Wrap(-1)
        gbSizer1.Add(self.m_staticText23, wx.GBPosition(12, 3), wx.GBSpan(1, 2), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl16 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_textCtrl16, wx.GBPosition(12, 5), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.m_staticText27 = wx.StaticText(self, wx.ID_ANY, u"转入转出信息", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText27.Wrap(-1)
        gbSizer1.Add(self.m_staticText27, wx.GBPosition(13, 0), wx.GBSpan(1, 8), wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl13 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_textCtrl13, wx.GBPosition(6, 1), wx.GBSpan(1, 6), wx.ALL | wx.EXPAND, 5)

        self.m_staticText26 = wx.StaticText(self, wx.ID_ANY, u"党籍状态信息", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText26.Wrap(-1)
        gbSizer1.Add(self.m_staticText26, wx.GBPosition(7, 0), wx.GBSpan(1, 8),
                     wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl11 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_textCtrl11, wx.GBPosition(5, 1), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl10 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_textCtrl10, wx.GBPosition(4, 1), wx.GBSpan(1, 6), wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl8 = wx.TextCtrl(self, wx.ID_ANY, u"2017/10/22", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE)
        gbSizer1.Add(self.m_textCtrl8, wx.GBPosition(3, 1), wx.GBSpan(1, 1),
                     wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 5)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"转正日期：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        gbSizer1.Add(self.m_staticText11, wx.GBPosition(3, 2), wx.GBSpan(1, 2),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.m_textCtrl9 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_textCtrl9, wx.GBPosition(3, 4), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        bSizer3.Add(gbSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer1.Add(bSizer3, 3, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

    def __del__(self):
        pass
