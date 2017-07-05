import wx
import subprocess
import os
import io
import time

k=0
gamePath1 = 0
gamePath2 = 0
gamePath3 = 0
gamePath4 = 0
gamePath5 = 0

app = wx.App()
aBitmap = wx.Image(name = "splash.jpg").ConvertToBitmap()
splashDuration = 900

splash = wx.SplashScreen(aBitmap, wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT,
                                 splashDuration, None)
splash.Show()       
app.MainLoop()
                   
class windowClass(wx.Frame):
    def __init__ (self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()
       
    def basicGUI(self):
        self.Center()
        global panel, gamePath1, gamePath2, gamePath3, gamePath4, windowDetect, MySnapshot
        panel = wx.Panel(self, size=(300,220))
        menuBar = wx.MenuBar()
        menuFile = wx.Menu()
        MySnapshot = time.strftime("%Y_%m_%d_%H_%M_%S")
        self.SetTitle("Click Tester 10 Second Challenge")
            
        gameTitle1 = wx.StaticText(panel, -1, pos=((110,5)))
        gameTitle2 = wx.StaticText(panel, -1, pos=((0,57)))
        gameTitle5 = wx.StaticText(panel, -1, pos=((110,150)))
        
        launchTitle1 = wx.Button(panel, id=wx.ID_ANY, label="Start",pos=(0, 0))
        launchTitle2 = wx.Button(panel, id=wx.ID_ANY, label="Show Results",pos=(0, 26))
        launchTitle3 = wx.Button(panel, id=wx.ID_ANY, label="Screenshot Results",pos=(0, 174))
        launchTitle5 = wx.Button(panel, id=wx.ID_ANY, label="Click",pos=(154,174))
        windowDetect = "False"
        
        def launch5 (event):
            global k, windowDetect
            if windowDetect == "True" :
                k += 1
                gameTitle5.SetLabel(str(k))
            if windowDetect == "False" :
                gameTitle5.SetLabel(str(k))

        def launch2 (event):
            global k
            clicksPer = int(k)/10
            gameTitle2.SetLabel("Clicks Total: "+str(k)+"\n"+"Time: 10 sec\n"+"Clicks per second "+str(clicksPer))
            
        def launch3 (event):
            global MySnapshot
            import ImageGrab
            xold, yold = self.GetPosition()
            xnew, ynew = self.GetPosition()
            xold = xold + 2
            yold = yold + 2
            xnew = xnew + 248
            ynew = ynew + 248
            snapshot = ImageGrab.grab(bbox=(xold, yold, xnew, ynew))
            save_path = "Snapshots\\"+str(MySnapshot)+".jpg"
            snapshot.save(save_path)


        def launch1 (event):
            from threading import Thread
            def countdown(p,q):
                global windowDetect
                j=q
                while True:  
                    gameTitle1.SetLabel(str(j))
                    
                    j -= 1
                    time.sleep(1)
                    if(j==-1):
                        gameTitle1.SetLabel("Start!")
                        time.sleep(0.3)
                        break
                if(j==-1):
                    global windowDetect
                    windowDetect = "True"
                    def closeWinTimer(p,h):
                        w=h
                        while True:  
                            gameTitle1.SetLabel(str(w))
                    
                            w -= 1
                            time.sleep(1)
                            if(w==0):
                                global windowDetect
                                windowDetect = "False"
                                gameTitle1.SetLabel("Finish!")
                                break
                    closeWinTimer(1,10)

            for i in range(15):
                
                t = Thread(target=countdown, args=(1,5))
                t.start()
                
        launchTitle1.Bind(wx.EVT_BUTTON, launch1)
        launchTitle2.Bind(wx.EVT_BUTTON, launch2)
        launchTitle3.Bind(wx.EVT_BUTTON, launch3)
        launchTitle5.Bind(wx.EVT_BUTTON, launch5)



        def closewindow(event):
            self.Close()
        

        exitItem = menuFile.Append(wx.ID_EXIT, 'Exit', 'Close the App')
        
        menuBar.Append(menuFile, 'File')
        
        
        self.SetMenuBar(menuBar)
        
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        



        self.Show(True)

    def Quit(self, e):
        self.Close()   
def main():

    app = wx.App()
    windowClass(None, style = wx.CAPTION | wx.CLIP_CHILDREN | wx.MINIMIZE_BOX , size=((250, 250)))
    app.MainLoop()

main()
        
