import os

def listFolderData():
    X, y = list(), list()
    # r=root, d=directories, f = files
    for r, d, f in os.walk("./data"):        
        for file in f:        
            if ".png" in file:            
                strEqu = file[0:len(file)-4]      #e.g 7+1
                intPlusIdx = strEqu.index('+')
                num1 = strEqu[0:intPlusIdx]
                num2 = strEqu[intPlusIdx+1:None]
                X.append([int(num1),int(num2)])   # [[7, 1], [4, 6], 
                y.append(int(num1) + int(num2))   # [8, 10,            
    return X, y
         


