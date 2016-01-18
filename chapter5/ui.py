#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
class RefactorExample(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Refactor Example', size=(300, 200))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour("White")   #默认背景色是灰色
        prevButton = wx.Button(panel, -1, "<<PREV", pos=(80, 0))
        self.Bind(wx.EVT_BUTTON, self.OnPrev, prevButton)
        nextButton = wx.Button(panel, -1, "NEXT>>", pos=(160, 0)) #button可以直接显示
        self.Bind(wx.EVT_BUTTON, self.OnPrev, nextButton)
        firstButton = wx.Button(panel, -1, "FIRST")
        self.Bind(wx.EVT_BUTTON, self.OnFirst, firstButton)
        lastButton = wx.Button(panel, -1, "LAST", pos=(240, 0))
        self.Bind(wx.EVT_BUTTON, self.OnLast, lastButton)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        menuBar = wx.MenuBar()      #创建一个目录
        menu1 = wx.Menu()           #目录标题项
        openMenuItem = menu1.Append(-1, "File", "Copy in status bar") #目录下拉显示
        self.Bind(wx.EVT_MENU, self.OnOpen, openMenuItem)
        quitMenuItem = menu1.Append(-1, "Quit", "Quit")
        self.Bind(wx.EVT_MENU, self.OnCloseWindow, quitMenuItem)
        menuBar.Append(menu1, "File")   #目录标题显示
        menu2 = wx.Menu()
        copyItem = menu2.Append(-1, "Copy", "Copy")
        self.Bind(wx.EVT_MENU, self.OnCopy, copyItem)
        cutItem = menu2.Append(-1, "Cut", "Cut")
        self.Bind(wx.EVT_MENU, self.OnCut, cutItem)
        pasteItem = menu2.Append(-1, "Paste", "Paste")
        self.Bind(wx.EVT_MENU, self.OnPaste, pasteItem)
        menuBar.Append(menu2, "Edit")
        self.SetMenuBar(menuBar)    #调用这个函数才会显示menu

        menu2.AppendSeparator()    #加一个分割线
        optItem = menu2.Append(-1, "Option", "Display Options")
        self.Bind(wx.EVT_MENU, self.OnOptions, optItem)

        static = wx.StaticText(panel, wx.NewId(), "First Name", pos=(10, 50))        #固定字
        static.SetBackgroundColour("White")
        text = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1)    , pos=(80, 50))  #文本框



        static = wx.StaticText(panel, wx.NewId(), "Last Name", pos=(10, 80))
        static.SetBackgroundColour("White")
        text = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1)    , pos=(80, 80))   #文本框 

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
