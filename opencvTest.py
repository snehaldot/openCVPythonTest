import wxversion
wxversion.select('2.8')

import wx
import cv2.cv as cv
#from cv2.cv import highgui as gui
#import cv2.highgui as gui
#from cv2 import *

class CvDisplayPanel(wx.Panel):
    def __init__(self, parent, img):
        wx.Panel.__init__(self, parent, -1)
        # Convert the raw image data to something wxpython can handle.
        #cv.CvtColor(img, img, cv.CV_BGR2RGB)
        #self.bmp = wx.BitmapFromBuffer(img.width, img.height	)
        # Display the resulting image
        #sbmp = wx.StaticBitmap(self, -1, bitmap=self.bmp)

if __name__=="__main__":
    imageToDisplay = cv.LoadImage("new.jpg")
    app = wx.App()
    app.RestoreStdio()
    frame = wx.Frame(None, -1, size=(imageToDisplay.width, imageToDisplay.height))
    CvDisplayPanel(frame, imageToDisplay)
    frame.Show(True)
    app.MainLoop()
