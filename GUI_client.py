import tkinter
from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo
from PIL import ImageTk, Image
import client
from functools import partial
from tkinter.filedialog import asksaveasfile

class ClientGUI:
    def __init__(self, master):
        self.buff = None
        self.master = master
        self.master.title("Client")
        self.master.geometry('240x330')


        self.lbl_IP_input = Label(self.master, text = "IP: ")
        self.lbl_IP_input.grid(column = 0, row = 0)

        self.txt_IP_input = Entry(self.master, width = 20)
        self.txt_IP_input.focus()
        self.txt_IP_input.grid(column = 1, row = 0)

        self.btn_connect = Button(self.master, text="Connect", command = self.connect)
        self.btn_connect.grid(column=2, row=0)

        self.btn_screenshot = Button(self.master, text = "Screenshot", width = 20, height = 2, command = self.screenshot)
        self.btn_screenshot.grid(column = 1, row = 2)

        self.btn_process_running = Button(self.master, text = "Process running", width = 20, height = 2, command = self.runningProcess)
        self.btn_process_running.grid(column = 1, row = 3)

        self.btn_app_running = Button(self.master, text = "App running", width = 20, height = 2, command = self.runningApp)
        self.btn_app_running.grid(column = 1, row = 4)

        self.btn_keystroke = Button(self.master, text = "Keystroke", width = 20, height = 2, command=self.keystroke)
        self.btn_keystroke.grid(column = 1, row = 5)

        self.btn_edit_registry = Button(self.master, text = "Edit registry", width = 20, height = 2, command = self.editRegistry)
        self.btn_edit_registry.grid(column = 1, row = 6)

        self.btn_shutdown = Button(self.master, text = "Shutdown", width = 20, height = 2, command = self.shutdown)
        self.btn_shutdown.grid(column = 1, row = 7)

        self.btn_exit = Button(self.master, text = "Exit", width = 20, height = 2, command = self.exit)
        self.btn_exit.grid(column = 1, row = 8)
    
    def connect(self):
        self.buff = client.connectServer('temp')

    def screenshot(self):
        if self.buff == None:
            showerror(title = 'Error', message = 'Not connected to the server.')
            return
        window_screenshot = Toplevel()
        screenshotGUI(window_screenshot, self.buff)
        window_screenshot.mainloop()

    def runningProcess(self):
        if self.buff == None:
            showerror(title = 'Error', message = 'Not connected to the server.')
            return        
        window_runningProcess = Toplevel()
        runningProcessGUI(window_runningProcess, self.buff)
        window_runningProcess.mainloop()

    def runningApp(self):
        if self.buff == None:
            showerror(title = 'Error', message = 'Not connected to the server.')
            return        
        window_runningApp = Toplevel()
        runningAppGUI(window_runningApp, self.buff)
        window_runningApp.mainloop()

    def keystroke(self):
        if self.buff == None:
            showerror(title = 'Error', message = 'Not connected to the server.')
            return        
        window_keystroke = Toplevel()
        keystrokeGUI(window_keystroke, self.buff)
        window_keystroke.mainloop()

    def editRegistry(self):
        if self.buff == None:
            showerror(title = 'Error', message = 'Not connected to the server.')
            return        
        window_editRegistry = Toplevel()
        editRegistryGUI(window_editRegistry, self.buff)
        window_editRegistry.mainloop()
    def shutdown(self):
        showinfo(title='Shutdown', message='Shutdown request sent.')

    def exit(self):
        self.master.destroy()
    
class screenshotGUI:
    def __init__(self, master, buff):
        self.buff = buff
        self.master = master
        self.image = None
        self.render = None
        self.master.title("Screenshot")
        self.master.geometry('700x500')
        self.master.focus()
        self.master.grab_set()
        
        self.canvas = Canvas(self.master, width = 600, height = 400)  
        self.canvas.grid(column = 0, row = 0)
        self.imgOnCanvas = self.canvas.create_image(0, 0, anchor = NW)

        self.btn_cap = Button(self.master, text = "Capture", width = 10, height = 2, command = self.capture)
        self.btn_cap.grid(column = 0, row= 1)

        self.btn_save = Button(self.master, text = "Save", width = 10, height = 2, command = self.save)
        self.btn_save.grid(column = 1, row = 1)
        
        self.capture()

    def capture(self):
        self.image = client.getScreenShot(self.buff)

        imageShow = self.image.resize((600, 400), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(imageShow)
        self.canvas.itemconfig(self.imgOnCanvas, image = self.render)

    def save(self):
        f = asksaveasfile(mode='w', initialfile = 'screenshot.png', defaultextension=".png",filetypes=[("PNG Files", "*.png")])
        self.image.save(f.name)

class runningProcessGUI:
    def __init__(self, master, buff):
        self.buff = buff
        self.master = master
        self.master.title("Running process")
        self.master.geometry('320x200')
        self.master.focus()
        self.master.grab_set()

        self.btn_kill = Button(self.master, text = "Kill", width = 10, height = 2, command = self.kill)
        self.btn_kill.grid(column = 0, row = 0)

        self.btn_show = Button(self.master, text = "Show", width = 10, height = 2, command = self.show)
        self.btn_show.grid(column = 1, row = 0)

        self.btn_hide = Button(self.master, text = "Hide", width = 10, height = 2, command = self.hide)
        self.btn_hide.grid(column = 2, row = 0)

        self.btn_start = Button(self.master, text = "Start", width = 10, height = 2, command = self.start)
        self.btn_start.grid(column = 3, row = 0)

    def kill(self):
        pass
    def show(self):
        pass
    def hide(self):
        pass
    def start(self):
        pass

class runningAppGUI:
    def __init__(self, master, buff):
        self.buff = buff
        self.master = master
        self.master.title("Running app")
        self.master.geometry('300x200')
        self.master.focus()
        self.master.grab_set()

class keystrokeGUI:
    def __init__(self, master, buff):
        self.buff = buff
        self.master = master
        self.master.title("Keystroke")
        self.master.geometry('300x200')
        self.master.focus()
        self.master.grab_set()    

class editRegistryGUI:
    def __init__(self, master, buff):
        self.buff = buff
        self.master = master
        self.master.title("Edit registry")
        self.master.geometry('300x200')
        self.master.focus()
        self.master.grab_set()    


window_client = Tk()
a = ClientGUI(window_client)
window_client.mainloop()