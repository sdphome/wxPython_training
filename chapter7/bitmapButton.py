# -*- coding: utf-8 -*-
import wx

class BitmapFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Button Example', size=(300, 150))
        panel = wx.Panel(self, -1)
        bmp = wx.Image("bitmap.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, bmp, pos=(10, 20))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()
        self.button2 = wx.BitmapButton(panel, -1, bmp, pos=(100, 20), style=0)
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button2)

    def OnClick(self, event):
        self.Destroy()

        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = BitmapFrame()
    frame.Show(True)
    app.MainLoop()
