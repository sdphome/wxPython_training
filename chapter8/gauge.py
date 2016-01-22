# -*- coding: utf-8 -*-
import wx

class GaugeFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Gauge Example', size=(350, 150))
        panel = wx.Panel(self, -1)
        self.count = 0
        self.gauge = wx.Gauge(panel, -1, 50, (20, 50), (250, 25))
        self.gauge.SetBezelFace(3)
        self.gauge.SetShadowWidth(3)
        self.Bind(wx.EVT_IDLE, self.OnIdle)

    def OnIdle(self, event):
        self.count = self.count + 1
        if self.count == 100:
            self.count = 0
        self.gauge.SetValue(self.count)   #显示进度条
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = GaugeFrame()
    frame.Show(True)
    app.MainLoop()
