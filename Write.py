import xlrd
import xlwt
import xlutils.copy
from xlutils.copy import copy
def Write(path,contracts):
    old = xlrd.open_workbook(path,formatting_info=True);
    new=copy(old)
    read=old.sheet_by_index(1)
    sheet1=new.get_sheet(1)
    for i in range( read.nrows ):
        if(type(read.cell(i,0).value)==type(1) or type(read.cell(i,0).value)==type(1.0)):
            for j in range(len(contracts)):
                if(contracts[j].isSame(read.cell(i,0).value)):
                    sheet1.write(i,6,int(contracts[j].price))
                    break
                
    new.save('book2.xls')  

    
    
