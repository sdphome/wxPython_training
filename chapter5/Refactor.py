#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx

class RefactorExample(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Reactor Example', size=(368, 200))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour("White")
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.createMenuBar()
        self.createButtonBar(panel)
        self.createTextFields(panel)

    def menuData(self):
        return(("&File",
               ("&Open", "Open in status bar", self.OnOpen),
               ("&Quit", "Quit", self.OnCloseWindow)),
               ("&Edit",
               ("&Copy", "Copy", self.OnCopy),
               ("&Cut", "Cut", self.OnCut),
               ("&Paste", "Paste", self.OnPaste),
               ("", "", ""),
               ("&Options", "DisplayOptions", self.OnOptions)))

    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]     #menu框的名字
            menuItems = eachMenuData[1:]
            menuBar.Append(self.createMenu(menuItems), menuLabel)
        self.SetMenuBar(menuBar)  #只有调用了SetMenuBar才可以显示menu

    def createMenu(self, menuData):
        menu = wx.Menu()
        for eachLabel, eachStatus, eachHandler in menuData:
            if not eachLabel:
                menu.AppendSeparator()  #给目录下拉框加一条分界线
                continue
            menuItem = menu.Append(-1, eachLabel, eachStatus)  #目录的下拉菜单创建，按照先后顺序
            self.Bind(wx.EVT_MENU, eachHandler, menuItem)  #给目录点击事件绑定一个处理函数
        return menu

    def buttonData(self):
        return (("First", self.OnFirst),
                ("<< PREV", self.OnPrev),
                ("NEXT >>", self.OnNext),
                ("Last", self.OnLast))

    def createButtonBar(self, panel, yPos=0):
        xPos = 0
        for eachLabel, eachHandler in self.buttonData():
            pos = (xPos, yPos)
            button = self.buildOneButton(panel, eachLabel, eachHandler, pos)
            xPos += button.GetSize().width

    def buildOneButton(self, parent, label, handler, pos=(0, 0)):
        button = wx.Button(parent, -1, label, pos)   #创建一个按钮，label即为按钮上的文字
        self.Bind(wx.EVT_BUTTON, handler, button)    #给按钮事件绑定一个处理函数
        return button

    def textFieldData(self):
        return(("First Name", (10, 50)),
               ("Last Name", (10, 80)))

    def createTextFields(self, panel):
        for eachLabel, eachPos in self.textFieldData():
            self.createCaptionedText(panel, eachLabel, eachPos)

    def createCaptionedText(self, panel, label, pos):
        static = wx.StaticText(panel, wx.NewId(), label, pos)  #显示软件上固定的文字
        static.SetBackgroundColour("White")
        textPos = (pos[0] + 75, pos[1])
        wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1), pos=textPos) # 显示文本框

    def OnPrev(self, event): pass
    def OnNext(self, event): pass
    def OnLast(self, event): pass
    def OnFirst(self, event): pass
    def OnOpen(self, event): pass
    def OnCopy(self, event): pass
    def OnCut(self, event): pass
    def OnPaste(self, event): pass
    def OnOptions(self, event): pass
    def OnCloseWindow(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = RefactorExample(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
