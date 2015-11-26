from PythonCard import model
import win32api,win32con,win32com.client,wx


class MyVMSApp(model.Background):

    def on_BtnStartVMS_mouseClick(self, event):
        hkey = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,
                                        "Software\\View Engineering\\Voyager\\8.0\\Windows\\Video",
                                        0, win32con.KEY_ALL_ACCESS)
        
        self.VideoWindow = wx.Dialog(None,-1, "Video (Live) in Python",
                                     size=(int(win32api.RegQueryValueEx(hkey,"Height")[0]),
                                           int(win32api.RegQueryValueEx(hkey,"Width")[0])),
                                     style=wx.RESIZE_BORDER|wx.DEFAULT_DIALOG_STYLE)
        self.VideoWindow.Show(True)
        self.myVmsApplication =win32com.client.Dispatch("Vms.Application.1")
        self.myVmsApplication.SetExtOperatorUIHandle(self.VideoWindow.GetHandle(),
                                                        self.components.ResultWindow.GetHandle())
        self.myVmsApplication.Start(1)


    def on_BtnZero_mouseClick(self, event):
        self.myVmsApplication.ZeroStage()

    def on_BtnStopVMS_mouseClick(self, event):
        self.myVmsApplication.Stop()

    def on_BtnLoadProgram_mouseClick(self, event):
        self.myVmsPrg = win32com.client.Dispatch("Vms.Program.1")
        self.myVmsPrg.Open("Test2.voy",1)

    def on_ImgBtnMeasureCircle_mouseClick(self, event):
        self.myVmsPrg = win32com.client.Dispatch("Vms.Program.1")
        self.myVmsPrg.Open("MeasureCirle.voy",1)

    def on_ImgBtnMeasureLine_mouseClick(self, event):
        self.myVmsPrg = win32com.client.Dispatch("Vms.Program.1")
        self.myVmsPrg.Open("MeasureLine.voy",1)    

    def on_BtnRunProgram_mouseClick(self, event):
        self.myVmsPrg = win32com.client.Dispatch("Vms.Program.1")
        self.myVmsPrg.Start()

if __name__ == '__main__':
    app = model.Application(MyVMSApp)
    app.MainLoop()
