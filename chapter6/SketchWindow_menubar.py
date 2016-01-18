#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx

class SketchWindow(wx.Window):
    def __init__(self, parent, ID):
        print("SketchWindow init")
        wx.Window.__init__(self, parent,  ID)
        self.SetBackgroundColour("White")
        self.color = "Black"
        self.thickness = 1
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)
        self.lines = []
        self.curLine = []
        self.pos = (0, 0)
        self.InitBuffer()

        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMotion)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def InitBuffer(self):
        print("InitBuffer")
        size = self.GetClientSize()
        self.buffer = wx.EmptyBitmap(size.width, size.height)
        dc = wx.BufferedDC(None, self.buffer)
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        self.DrawLines(dc)
        self.reInitBuffer = False

    def GetLinesData(self):
        print("GetLinesData")
        return self.lines[:]

    def SetLinesData(self, lines):
        print("SetLinesData")
        self.lines = lines[:]
        self.InitBuffer()
        self.Refresh()

    def OnLeftDown(self, event):
        print("OnLeftDown")
        self.curLine = []
        self.pos = event.GetPositionTuple() #得到鼠标位置
        self.CaptureMouse() #捕获鼠标

    def OnLeftUp(self, event):
        print("OnLeftUp")
        if self.HasCapture():
            self.lines.append((self.color,
                               self.thickness,
                               self.curLine))
            self.curLine = []
            self.ReleaseMouse() #释放鼠标

    def OnMotion(self, event):
        print("OnMotion")
        if event.Dragging() and event.LeftIsDown():
            dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
            self.drawMotion(dc, event)
        event.Skip()

    def drawMotion(self, dc, event):
        print("drawMotion")
        dc.SetPen(self.pen)
        newPos = event.GetPositionTuple()
        coords = self.pos + newPos
        dc.DrawLine(*coords)
        self.pos = newPos

    def OnSize(self, event):
        print("OnSize")
        self.reInitBuffer = True

    def OnIdle(self, event):
        print("OnIdle")
        if self.reInitBuffer:
            self.InitBuffer()
            self.Refresh(False)

    def OnPaint(self, event):
        print("OnPaint")
        dc = wx.BufferedPaintDC(self, self.buffer)

    def DrawLines(self, dc):
        print("DrawLines")
        for colour, thickness, line in self.lines:
            pen = ex.Pen(colour, thickness, wx.SOLID)
            dc.SetPen(pen)
            for coords in line:
                dc.DrawKine(*coords)

    def SetColor(self, color):
        print("SetColor")
        self.color = color
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)

    def SetThickness(self, num):
        print("SetThickness")
        self.thickness = num
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)

class SketchFrame(wx.Frame):
    def __init__(self, parent):
        print("SketchFrame init")
        wx.Frame.__init__(self, parent, -1, "Sketch Frame", size=(800, 600))
        self.sketch = SketchWindow(self, -1)
        self.sketch.Bind(wx.EVT_MOTION, self.OnSketchMotion)
        self.initStatusBar()
        self.createMenuBar()

    def initStatusBar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -3])

    def OnSketchMotion(self, event):
        self.statusbar.SetStatusText("Pos: %s" %str(event.GetPositionTuple()), 0)
        self.statusbar.SetStatusText("Current Pts: %s" %len(self.sketch.curLine), 1)
        self.statusbar.SetStatusText("Line Count:%s" %len(self.sketch.lines), 2)
        event.Skip()

    def menuData(self):
        return [("&File", (
                    ("New", "New sketch file", self.OnNew),
                    ("Open", "Open sketch file", self.OnOpen),
                    ("Save", "Save sketch file", self.OnSave),
                    ("", "", ""),
                ("Color", (
                    ("Black", "", self.OnColor, wx.ITEM_RADIO),
                    ("Red", "", self.OnColor, wx.ITEM_RADIO),
                    ("Green", "", self.OnColor, wx.ITEM_RADIO),
                    ("Blue", "", self.OnColor, wx.ITEM_RADIO))),
                    ("", "", ""),
                    ("Quit", "Quit", self.OnCloseWindow)))]

    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            menuBar.Append(self.createMenu(menuItems), menuLabel)
        self.SetMenuBar(menuBar)

    def createMenu(self, menuData):
        menu = wx.Menu()
        for eachItem in menuData:
            if len(eachItem) == 2:
                label = eachItem[0]
                subMenu = self.createMenu(eachItem[1])
                menu.AppendMenu(wx.NewId(), label, subMenu)
            else:
                self.createMenuItem(menu, *eachItem)
        return menu

    def createMenuItem(self, menu, label, status, handler, kind=wx.ITEM_NORMAL):
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(-1, label, status, kind)
        self.Bind(wx.EVT_MENU, handler, menuItem)

    def OnNew(self, event): pass
    def OnOpen(self, event): pass
    def OnSave(self, event): pass

    def OnColor(self, event):
        menubar = self.GetMenuBar()
        itemId = event.GetId()
        item = menubar.FindItemById(itemId)
        color = item.GetLabel()
        self.sketch.SetColor(color)

    def OnCloseWindow(self, event):
        self.Destroy()

if __name__ == '__main__':
    print("main")
    app = wx.PySimpleApp()
    frame = SketchFrame(None)
    frame.Show(True)
    app.MainLoop()
