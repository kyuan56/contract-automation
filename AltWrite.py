import xlrd
import xlwt
import xlutils.copy
from xlutils.copy import copy
def Write(path,contracts):
    old = xlrd.open_workbook(path,formatting_info=True);
    new=copy(old)
    read=old.sheet_by_index(1)
    sheet1=new.get_sheet(1)
    for j in range(len(contracts)):
        sheet1.write(j,1,int(contracts[j].num))
        sheet1.write(j,2,contracts[j].name)
        sheet1.write(j,3,int(contracts[j].price))
            
                
    new.save('book3.xls')  

    
    
