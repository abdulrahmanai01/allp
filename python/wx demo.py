# import wxPython
import wx

app = wx.App()

# create frame using Frame() constructor
frame = wx.Frame(None, id = 10, title ="Frame", 
					pos = wx.DefaultPosition,
						size = wx.DefaultSize, 
				style = wx.DEFAULT_FRAME_STYLE,
							name = "frame")

# show frame
frame.Show(True)

app.MainLoop()
