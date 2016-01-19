# -*- coding: utf-8 -*-
import wx

class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example', size=(300, 100))
        panel = wx.Panel(self, -1)
        basicLabel = wx.StaticText(panel, -1, "Basic Control:")
        basicText = wx.TextCtrl(panel, -1, "I've entered some text!", size=(175, -1))#, style=wx.TE_READONLY)
        basicText.SetInsertionPoint(0)  #设置输入位置
        pwdLabel = wx.StaticText(panel, -1, "Password:")
        pwdText = wx.TextCtrl(panel, -1, "password", size=(175, -1),
                              style=wx.TE_PASSWORD) #可以将密码显示为...
        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([basicLabel, basicText, pwdLabel, pwdText])
        panel.SetSizer(sizer)
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = TextFrame()
    frame.Show(True)
    app.MainLoop()
