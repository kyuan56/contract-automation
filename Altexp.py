import xlrd
import tkinter.filedialog
from AltLoad import *
from AltWrite import Write
def main():
    path=tkinter.filedialog.askopenfilename()
    contracts=Load(path)
    print (len(contracts))
    path1=tkinter.filedialog.askopenfilename()
    Write(path1,contracts)


main()
