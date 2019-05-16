import xlrd
from Contract import *

def Load(location):
        contracts=[]
        flag=0
        book=xlrd.open_workbook(location)
        sheet1=book.sheet_by_index(1)
        for i in range(1,sheet1.nrows):
                if(type(sheet1.cell(i,0).value)==type(1) or type(sheet1.cell(i,0).value)==type(1.0)):
                        if(len(contracts)!=0):
                                for j in range(len(contracts)):
                                        
                                        if(contracts[j].isSame(sheet1.cell(i,0).value)):
                                                flag=1
                                                break
                        if(flag==0 and type(sheet1.cell(i,15).value)!=type("dd") and sheet1.cell(i,6).value=="总分"):
                                newc=Contract(sheet1.cell(i,0).value)
                                newc.addPrice(sheet1.cell(i,15).value,1)
                                newc.addName(sheet1.cell(i,3).value)
                                contracts.append(newc)
                        flag=0
        return contracts
    
