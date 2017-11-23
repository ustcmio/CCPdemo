import wx

class Dialog_out(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"转出管理", pos=wx.DefaultPosition, size=wx.Size(450, 270),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour('white')

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        bSizer7.Add((0, 0), 1, wx.EXPAND, 5)

        gbSizer3 = wx.GridBagSizer(0, 0)
        gbSizer3.SetFlexibleDirection(wx.BOTH)
        gbSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText31 = wx.StaticText(self, wx.ID_ANY, u"党员编号：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        gbSizer3.Add(self.m_staticText31, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_textCtrl22 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_READONLY)
        gbSizer3.Add(self.m_textCtrl22, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText32 = wx.StaticText(self, wx.ID_ANY, u"姓名：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText32.Wrap(-1)
        gbSizer3.Add(self.m_staticText32, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl23 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_READONLY)
        gbSizer3.Add(self.m_textCtrl23, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText33 = wx.StaticText(self, wx.ID_ANY, u"身份证号：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText33.Wrap(-1)
        gbSizer3.Add(self.m_staticText33, wx.GBPosition(1, 2), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl24 = wx.TextCtrl(self, wx.ID_ANY, u"111111111111111111", wx.DefaultPosition, wx.Size(150, -1),
                                        wx.TE_READONLY)
        gbSizer3.Add(self.m_textCtrl24, wx.GBPosition(1, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText34 = wx.StaticText(self, wx.ID_ANY, u"转出时间：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText34.Wrap(-1)
        gbSizer3.Add(self.m_staticText34, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl25 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.m_textCtrl25, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText35 = wx.StaticText(self, wx.ID_ANY, u"转出地：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText35.Wrap(-1)
        gbSizer3.Add(self.m_staticText35, wx.GBPosition(2, 2), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl26 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.m_textCtrl26, wx.GBPosition(2, 3), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        bSizer7.Add(gbSizer3, 3, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer6.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button10 = wx.Button(self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_button10, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_button11, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        bSizer7.Add(bSizer6, 0, wx.EXPAND | wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class Dialog_in(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"转入管理", pos=wx.DefaultPosition, size=wx.Size(450, 270),
                           style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour('white')

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        gbSizer3 = wx.GridBagSizer(0, 0)
        gbSizer3.SetFlexibleDirection(wx.BOTH)
        gbSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText31 = wx.StaticText(self, wx.ID_ANY, u"党员编号：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        gbSizer3.Add(self.m_staticText31, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_dybh = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.m_dybh, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText32 = wx.StaticText(self, wx.ID_ANY, u"姓名：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText32.Wrap(-1)
        gbSizer3.Add(self.m_staticText32, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.m_name, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText33 = wx.StaticText(self, wx.ID_ANY, u"身份证号：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText33.Wrap(-1)
        gbSizer3.Add(self.m_staticText33, wx.GBPosition(1, 2), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_sfzh = wx.TextCtrl(self, wx.ID_ANY, u"111111111111111111", wx.DefaultPosition, wx.Size(150, -1), 0)
        gbSizer3.Add(self.m_sfzh, wx.GBPosition(1, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText34 = wx.StaticText(self, wx.ID_ANY, u"转入时间：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText34.Wrap(-1)
        gbSizer3.Add(self.m_staticText34, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_zrrq = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.m_zrrq, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText35 = wx.StaticText(self, wx.ID_ANY, u"转入地：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText35.Wrap(-1)
        gbSizer3.Add(self.m_staticText35, wx.GBPosition(2, 2), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_zrd = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.m_zrd, wx.GBPosition(2, 3), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.m_staticText36 = wx.StaticText(self, wx.ID_ANY, u"联系方式：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText36.Wrap(-1)
        gbSizer3.Add(self.m_staticText36, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_lxfs = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.m_lxfs, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.m_staticText37 = wx.StaticText(self, wx.ID_ANY, u"党费缴至：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText37.Wrap(-1)
        gbSizer3.Add(self.m_staticText37, wx.GBPosition(3, 2), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_dfjz = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.m_dfjz, wx.GBPosition(3, 3), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.msg = wx.StaticText(self, wx.ID_ANY, u"     ", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.msg,0, wx.EXPAND|wx.CENTER, 10)
        bSizer4.Add(gbSizer3, 3, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer6.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button10 = wx.Button(self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_button10, 0, wx.ALIGN_RIGHT | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_button11, 0, wx.ALIGN_RIGHT | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer4.Add(bSizer6, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class Dialog_ImportEXCEL(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(380, 160), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"导入Excel数据", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        bSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_filePicker = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                              wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        bSizer1.Add(self.m_filePicker, 0, wx.ALL | wx.EXPAND, 5)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_reset = wx.Button(self, wx.ID_ANY, u"重置", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.btn_reset, 0, wx.ALL, 10)

        self.btn_done = wx.Button(self, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.btn_done, 0, wx.ALL, 10)

        bSizer1.Add(bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
