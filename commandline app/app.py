print("""
\t********************************
\t**** WELCOME TO DATAMANAGER ****
\t****         Menu           ****
\t*  1 List All     4 Delete ID  *
\t*  2 List ID      5 Update ID  *
\t*  3 List Name    6 Add        *
\t*  7 Exit                      *
\t********************************
""")

import csv,os

def read():
    '''Function For Read Csv File'''
    with open('data.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      return [row for row in csv_reader]

def write(data):
    '''Function For Read Write File'''
    with open('data.csv', mode='w') as csv_file:
      filewrite = csv.writer(csv_file, delimiter=',')
      filewrite.writerows(data)
    return len(data)

def printouput(data,action=False):
    '''Function For Print Output On screen For
         1 List All 
         2 List ID  
         3 List Name
     '''
    print(''.join(['_' for x in range(70)]),'\n')
    if not action:data = data[1:]
    print('\t',"\t\t".join(['Name','ID','Price','In Stock']))
    print(''.join(['_' for x in range(70)]),'\n')
    for x in data:print('\t',"\t\t".join(x))

def showoutput(action):
    '''Function For Perform Actions On Data For Following
         1 List All 
         2 List ID  
         3 List Name
    '''
    if action == 2:
        readby = input("Enter Product ID:- ")
        return printouput([x for x in read() if x[1] == readby],True)
    elif action == 3:
        readby = input("Enter Product Name:- ")
        return printouput([x for x in read() if x[0] == readby],True)
    else: return printouput(read())

def deleteupdate(action):
    ''' Function For Delete And Update Products In Database '''
    data = read()
    if action == 4:
        delete_key = input("Enter ID For Delete Product:- ")
        if len(data) != write([x for x in data if x[1] != delete_key]):
            print(f"Product With Id {delete_key} Is Deleted!")
        else:print(f"No Product Found With Id {delete_key}!")
    elif action == 5:
        update_key,updated = input("Enter ID For Update Product:- "),False
        def updatedata():
            '''Function For Return List Of Values Take From User'''
            nonlocal updated;updated = True
            return [input('Product Name:- '),input('Product ID:- '),input('Product Price:- '),input('Product In Stock:- ')]
        write([updatedata() if x[1] == update_key else x for x in data])
        if updated:print(f"Product With Id {update_key} Is Updated!")
        else:print(f"No Product Found With Id {update_key}!")

def addproduct():
    '''Function For Add New Product To Database'''
    values = [input('Product Name:- '),input('Product ID:- '),input('Product Price:- '),input('Product In Stock:- ')]
    data = read() ; data.append(values)
    write(data)
    print(f"{values[0]} Product Is Added To Database!")

def takeinput():
  '''Function For Take Input From User Between 1 to 7 Numbers'''
  try:
    value = int(input('\n>> '))
    if value > 7:print("Read Instruction From Begining Of Program")
    else:return value
  except:print("Read Instruction From Begining Of Program")
  
def startapp():
 ''' Command Line Tool Start Function '''
 value  = takeinput()
 if value != 7:
     if isinstance(value,int) and value < 4:showoutput(value)
     elif isinstance(value,int) and value < 6:deleteupdate(value)
     elif isinstance(value,int) and value == 6:addproduct()
     startapp()
 else:print('Exiting......')


if __name__ == "__main__":
    if not os.path.exists('data.csv'):
        with open('data.csv','w') as f:
            f.write('Name,ID,Price,In Stock\n') 
    startapp()