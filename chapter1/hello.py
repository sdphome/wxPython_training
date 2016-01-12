#!/usr/bin/env python
import wx
'''Hello, we will display the image.'''

class Frame(wx.Frame):
    '''Frame class that displays an image.'''
    def __init__(self, image, parent=None, id=-1,
                 pos=wx.DefaultPosition,
                 title='Hello, LoveLog!'):
        '''Create a Frame instance and display image.'''
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)

class App(wx.App):
    def OnInit(self):
        image = wx.Image('lovelylog.png', wx.BITMAP_TYPE_PNG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

def main():
    app = App()
    app.MainLoop()

if __name__ == '__main__':
    main()

