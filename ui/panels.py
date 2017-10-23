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
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(1000, 700),
                          style=wx.TAB_TRAVERSAL)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_p_modify = wx.Button(self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.btn_p_modify, 0, wx.ALL, 3)

        self.btn_p_save = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.btn_p_save, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 3)

        self.btn_p_out = wx.Button(self, wx.ID_ANY, u"转出", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.btn_p_out, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 3)

        self.btn_p_in = wx.Button(self, wx.ID_ANY, u"转入", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.btn_p_in, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 3)

        bSizer1.Add(bSizer2, 0, wx.EXPAND, 5)

        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"个人基本信息", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_CENTRE)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(15, 70, 90, 92, False, wx.EmptyString))

        gbSizer1.Add(self.m_staticText1, wx.GBPosition(0, 0), wx.GBSpan(1, 8), wx.ALL | wx.EXPAND, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"姓名：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        gbSizer1.Add(self.m_staticText2, wx.GBPosition(1, 0), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.tC_name = wx.TextCtrl(self, wx.ID_ANY, u"张三三三", wx.DefaultPosition, wx.Size(-1, -1), 0)
        gbSizer1.Add(self.tC_name, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"姓别：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        gbSizer1.Add(self.m_staticText3, wx.GBPosition(1, 2), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        c_sexChoices = [u"男", u"女"]
        self.c_sex = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, c_sexChoices, 0)
        self.c_sex.SetSelection(0)
        gbSizer1.Add(self.c_sex, wx.GBPosition(1, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"民族：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        gbSizer1.Add(self.m_staticText4, wx.GBPosition(1, 4), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.tc_mz = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        gbSizer1.Add(self.tc_mz, wx.GBPosition(1, 5), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"学历：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        gbSizer1.Add(self.m_staticText5, wx.GBPosition(1, 6), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.tc_study = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1), 0)
        gbSizer1.Add(self.tc_study, wx.GBPosition(1, 7), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"身份证号：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        gbSizer1.Add(self.m_staticText6, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tc_pid = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.tc_pid, wx.GBPosition(2, 1), wx.GBSpan(1, 3), wx.ALL | wx.EXPAND, 5)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"人员类别：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        gbSizer1.Add(self.m_staticText7, wx.GBPosition(2, 4), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tc_type = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.tc_type, wx.GBPosition(2, 5), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"党员编号：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        gbSizer1.Add(self.m_staticText8, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tc_dybh = wx.TextCtrl(self, wx.ID_ANY, u"042300000", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.tc_dybh, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, u"类别：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        gbSizer1.Add(self.m_staticText9, wx.GBPosition(4, 0), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.m_staticText15 = wx.StaticText(self, wx.ID_ANY, u"家庭地址：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)
        gbSizer1.Add(self.m_staticText15, wx.GBPosition(5, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tc_jtzz = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.tc_jtzz, wx.GBPosition(5, 1), wx.GBSpan(1, 5), wx.ALL | wx.EXPAND, 5)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"联系方式：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        gbSizer1.Add(self.m_staticText17, wx.GBPosition(6, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tc_lxfs = wx.TextCtrl(self, wx.ID_ANY, u"051088888888", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.tc_lxfs, wx.GBPosition(6, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, u"手机号码：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)
        gbSizer1.Add(self.m_staticText18, wx.GBPosition(6, 2), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tc_sjhm = wx.TextCtrl(self, wx.ID_ANY, u"13000000000", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.tc_sjhm, wx.GBPosition(6, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText19 = wx.StaticText(self, wx.ID_ANY, u"工作单位：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText19.Wrap(-1)
        gbSizer1.Add(self.m_staticText19, wx.GBPosition(7, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tc_gzdw = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.tc_gzdw, wx.GBPosition(7, 1), wx.GBSpan(1, 5), wx.ALL | wx.EXPAND, 5)

        self.m_staticText28 = wx.StaticText(self, wx.ID_ANY, u"党籍状态信息", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText28.Wrap(-1)
        self.m_staticText28.SetFont(wx.Font(15, 70, 90, 92, False, wx.EmptyString))

        gbSizer1.Add(self.m_staticText28, wx.GBPosition(8, 0), wx.GBSpan(1, 8), wx.ALL | wx.EXPAND, 5)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"所在支部：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        gbSizer1.Add(self.m_staticText10, wx.GBPosition(3, 2), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.m_staticText21 = wx.StaticText(self, wx.ID_ANY, u"党籍状态：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        gbSizer1.Add(self.m_staticText21, wx.GBPosition(9, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_radioBtn2 = wx.RadioButton(self, wx.ID_ANY, u"正常", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        gbSizer1.Add(self.m_radioBtn2, wx.GBPosition(9, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_radioBtn3 = wx.RadioButton(self, wx.ID_ANY, u"不正常", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_radioBtn3, wx.GBPosition(9, 2), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText22 = wx.StaticText(self, wx.ID_ANY, u"是否失联：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        gbSizer1.Add(self.m_staticText22, wx.GBPosition(10, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_radioBtn4 = wx.RadioButton(self, wx.ID_ANY, u"否", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        gbSizer1.Add(self.m_radioBtn4, wx.GBPosition(10, 1), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_radioBtn5 = wx.RadioButton(self, wx.ID_ANY, u"是", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_radioBtn5, wx.GBPosition(11, 1), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText24 = wx.StaticText(self, wx.ID_ANY, u"失联日期：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText24.Wrap(-1)
        gbSizer1.Add(self.m_staticText24, wx.GBPosition(11, 2), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tc_slrq = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.tc_slrq, wx.GBPosition(11, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText25 = wx.StaticText(self, wx.ID_ANY, u"是否流动：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText25.Wrap(-1)
        gbSizer1.Add(self.m_staticText25, wx.GBPosition(12, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_radioBtn6 = wx.RadioButton(self, wx.ID_ANY, u"否", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        gbSizer1.Add(self.m_radioBtn6, wx.GBPosition(12, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_radioBtn7 = wx.RadioButton(self, wx.ID_ANY, u"是", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_radioBtn7, wx.GBPosition(13, 1), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText26 = wx.StaticText(self, wx.ID_ANY, u"外出流向：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText26.Wrap(-1)
        gbSizer1.Add(self.m_staticText26, wx.GBPosition(13, 2), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tc_wclx = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.tc_wclx, wx.GBPosition(13, 3), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.m_listCtrl1 = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(800, 180),
                                       wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
        self.m_listCtrl1.AppendColumn("序号",wx.LIST_FORMAT_CENTER,50)
        self.m_listCtrl1.AppendColumn("时间",wx.LIST_FORMAT_CENTER, width=120)
        self.m_listCtrl1.AppendColumn("转入/转出",wx.LIST_FORMAT_CENTER, width=80)
        self.m_listCtrl1.AppendColumn("转入地/转出地",wx.LIST_FORMAT_CENTER,width=300)
        self.m_listCtrl1.AppendColumn("备注", wx.LIST_FORMAT_CENTER,width=250)
        gbSizer1.Add(self.m_listCtrl1, wx.GBPosition(15, 0), wx.GBSpan(1, 8), wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_staticText27 = wx.StaticText(self, wx.ID_ANY, u"党员关系转接", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText27.Wrap(-1)
        self.m_staticText27.SetFont(wx.Font(15, 70, 90, 92, False, wx.EmptyString))

        gbSizer1.Add(self.m_staticText27, wx.GBPosition(14, 0), wx.GBSpan(1, 8), wx.ALL | wx.EXPAND, 5)

        c_szzbChoices = [u"柏庄社区第一支部", u"柏庄社区第二支部", u"柏庄社区第三支部", u"柏庄社区第四支部"]
        self.c_szzb = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), c_szzbChoices, 0)
        self.c_szzb.SetSelection(0)
        gbSizer1.Add(self.c_szzb, wx.GBPosition(3, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText13 = wx.StaticText(self, wx.ID_ANY, u"党内职务：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)
        gbSizer1.Add(self.m_staticText13, wx.GBPosition(3, 4), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        c_dnzwChoices = [u"无", u"支部书记", u"党小组长"]
        self.c_dnzw = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, c_dnzwChoices, 0)
        self.c_dnzw.SetSelection(0)
        gbSizer1.Add(self.c_dnzw, wx.GBPosition(3, 5), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText16 = wx.StaticText(self, wx.ID_ANY, u"党费交至：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)
        gbSizer1.Add(self.m_staticText16, wx.GBPosition(3, 6), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tc_dfjz = wx.TextCtrl(self, wx.ID_ANY, u"2017/06/01", wx.DefaultPosition, wx.Size(100, -1), 0)
        gbSizer1.Add(self.tc_dfjz, wx.GBPosition(3, 7), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"入党日期：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        gbSizer1.Add(self.m_staticText11, wx.GBPosition(4, 2), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tc_rdrq = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.tc_rdrq, wx.GBPosition(4, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, u"转正日期：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        gbSizer1.Add(self.m_staticText12, wx.GBPosition(4, 4), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tc_zzrq = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.tc_zzrq, wx.GBPosition(4, 5), wx.GBSpan(1, 1), wx.ALL, 5)

        c_lxChoices = [u"预备党员", u"正式党员"]
        self.c_lx = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, c_lxChoices, 0)
        self.c_lx.SetSelection(0)
        gbSizer1.Add(self.c_lx, wx.GBPosition(4, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        bSizer1.Add(gbSizer1, 3, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 3)

        self.SetSizer(bSizer1)
        self.Layout()

    def __del__(self):
        pass
