import wx

class StaticTextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Static Text Example', size=(400, 300))
        panel = wx.Panel(self, -1)
        wx.StaticText(panel, -1, "This is an example of static text", (100, 100))
        rev = wx.StaticText(panel, -1, "Static Text With Reversed Colors", (100, 30))
        rev.SetForegroundColour('White')
        rev.SetBackgroundColour('Black')
        center = wx.StaticText(panel, -1, "align center", (100, 50), (160, -1), wx.ALIGN_CENTER)
        center.SetForegroundColour('Black')
        center.SetBackgroundColour('White')
        str = "You can also change font."
        text = wx.StaticText(panel, -1, str, (20, 100))
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text.SetFont(font)
        wx.StaticText(panel, -1, "Your text\ncan be split\n"
                      "over multiple lines\nneven blank ones",
                      (20, 150))
        wx.StaticText(panel, -1, "Multi-line text\ncan also\n"
                      "be right aligned\nneven with a black",
                      (220, 150), style=wx.ALIGN_RIGHT)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = StaticTextFrame()
    frame.Show(True)
    app.MainLoop()
