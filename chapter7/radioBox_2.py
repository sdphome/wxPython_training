# -*- coding: utf-8 -*-
import wx

class RadioBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Radio Example', size=(400, 200))
        panel = wx.Panel(self, -1)
        sampleList = ['zero', 'one', 'two', 'three', 'four', 'six', 'seven', 'eight']
        wx.RadioBox(panel, -1, "A Radio Box", (10, 10), wx.DefaultSize, sampleList, 2, wx.RA_SPECIFY_COLS)
        wx.RadioBox(panel, -1, "A Radio Box2", (150, 10), wx.DefaultSize, sampleList, 3, wx.RA_SPECIFY_COLS | wx.NO_BORDER)

        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = RadioBoxFrame()
    frame.Show(True)
    app.MainLoop()
