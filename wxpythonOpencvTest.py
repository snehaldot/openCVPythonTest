'''How to integrate openCV and wxpython.

This program loads an image file using openCV, converts it to a format
which wxpython can handle and displays the resulting image in a
wx.Frame.'''

# Select the version of wxpython to use.
import wxversion
wxversion.select('2.8')

import wx
import cv as cv
#import opencv.highgui as gui


class CvDisplayPanel(wx.Panel):
    def __init__(self, parent, img):
        wx.Panel.__init__(self, parent, -1)
        # Convert the raw image data to something wxpython can handle.
        cv.cvCvtColor(img, img, cv.CV_BGR2RGB)
        self.bmp = wx.BitmapFromBuffer(img.width, img.height,\
                                       img.imageData)
        # Display the resulting image
        sbmp = wx.StaticBitmap(self, -1, bitmap=self.bmp)

if __name__=="__main__":
    imageToDisplay = cv.LoadImage("new.jpg")
    app = wx.App()
    app.RestoreStdio()
    frame = wx.Frame(None, -1, size=(imageToDisplay.width, imageToDisplay.height))
    CvDisplayPanel(frame, imageToDisplay)
    frame.Show(True)
    app.MainLoop()

