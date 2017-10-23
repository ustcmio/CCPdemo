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

        bSizer4.Add((0, 0), 1, wx.EXPAND, 5)

        gbSizer3 = wx.GridBagSizer(0, 0)
        gbSizer3.SetFlexibleDirection(wx.BOTH)
        gbSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText31 = wx.StaticText(self, wx.ID_ANY, u"党员编号：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        gbSizer3.Add(self.m_staticText31, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_textCtrl22 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.m_textCtrl22, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText32 = wx.StaticText(self, wx.ID_ANY, u"姓名：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText32.Wrap(-1)
        gbSizer3.Add(self.m_staticText32, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl23 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.m_textCtrl23, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText33 = wx.StaticText(self, wx.ID_ANY, u"身份证号：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText33.Wrap(-1)
        gbSizer3.Add(self.m_staticText33, wx.GBPosition(1, 2), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl24 = wx.TextCtrl(self, wx.ID_ANY, u"111111111111111111", wx.DefaultPosition, wx.Size(150, -1), 0)
        gbSizer3.Add(self.m_textCtrl24, wx.GBPosition(1, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText34 = wx.StaticText(self, wx.ID_ANY, u"转入时间：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText34.Wrap(-1)
        gbSizer3.Add(self.m_staticText34, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl25 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.m_textCtrl25, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText35 = wx.StaticText(self, wx.ID_ANY, u"转入地：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText35.Wrap(-1)
        gbSizer3.Add(self.m_staticText35, wx.GBPosition(2, 2), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl26 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.m_textCtrl26, wx.GBPosition(2, 3), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

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
