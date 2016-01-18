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
        self.statusbar = self.CreateStatusBar()
        self.sketch.Bind(wx.EVT_MOTION, self.OnSketchMotion)

    def OnSketchMotion(self, event):
        self.statusbar.SetStatusText(str(event.GetPositionTuple()))

if __name__ == '__main__':
    print("main")
    app = wx.PySimpleApp()
    frame = SketchFrame(None)
    frame.Show(True)
    app.MainLoop()
