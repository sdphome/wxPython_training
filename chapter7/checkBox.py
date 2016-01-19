# -*- coding: utf-8 -*-
import wx

class CheckBox(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Gauge Example', size=(200, 200))
        panel = wx.Panel(self, -1)
        wx.CheckBox(panel, -1, "Alpha", (35, 40), (150, 20))
        wx.CheckBox(panel, -1, "Beta", (35, 60), (150, 20))
        wx.CheckBox(panel, -1, "Gamma", (35, 80), (150, 20))
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CheckBox()
    frame.Show(True)
    app.MainLoop()
