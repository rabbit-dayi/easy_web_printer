import win32print
import tempfile
import win32api
def print_file(filename,printer):
    
    str1=win32print.GetDefaultPrinter()
    if printer=="":
        device_name=win32print.GetDefaultPrinter()
    win32print.SetDefaultPrinter(device_name)
    open(filename,"r")
    win32api.ShellExecute(0, "print", filename, None, ".", 0)

    #win32api.ShellExecute(
    #    0,
    #    "print",
    #    filename,
     #   '/d:"%s"' % + str1,
     #   ".",
     #   0
    #)

print(win32print.GetDefaultPrinter())

print_file("C:/2.pdf","")