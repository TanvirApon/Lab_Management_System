import csv

'''Computer Lab Management Application using Python'''

def Add_PC():
    '''This Function is for Adding A PC Information'''
    with open('pc_record.csv','r') as file:
        csv_dict = [row for row in csv.DictReader(file)]
        if len(csv_dict)==0:
            print("\n")
            print("--------------------------Instructions-----------------------------")
            print("Please remember to input Number while you input the PC Number.")
            print("Please remember to input WORD while you input the PC OS and Status.")
            print("If you don't follow the above instruction it will give you an error.")
            print("--------------------------------------------------------------------\n")
            n=int(input("Enter the number of pc you want to input:"))
            #data rows as dictionary objects
            pc={
            "PC-Number":"",
            "OS-Installed":"",
            "PC-Status":"",
            }
     
            #fields names
            field =['PC-Number','OS-Installed','PC-Status'] 
            #name of csv file
            for i in range(n):
                pc_num=str(input("Enter the number of the pc: "))
                pc_os=str(input("Enter the os name install in pc: "))
                pc_status=str(input("Enter the status of the pc: "))
            
            pc["PC-Number"]=pc_num
            pc["OS-Installed"]=pc_os
            pc["PC-Status"]=pc_status
        
            with open("pc_record.csv","r+")as file:
             d_writer=csv.DictWriter(file,fieldnames=field)
             d_writer.writeheader()
             d_writer.writerow(pc)
             print("Data Stored\n")
        
        else:
             n=int(input("Enter the number of pc you want to input:"))
             #data rows as dictionary objects
             pc={
             "PC-Number":"",
             "OS-Installed":"",
             "PC-Status":"",
              }
     
            #fields names
             field =['PC-Number','OS-Installed','PC-Status'] 
             #name of csv file
             filenames="pc_record.csv" 
             for i in range(n):
                 pc_num=int(input("Enter the number of the pc: "))
                 pc_os=str(input("Enter the os name install in pc: "))
                 pc_status=str(input("Enter the status of the pc: "))
            
             pc["PC-Number"]=pc_num
             pc["OS-Installed"]=pc_os
             pc["PC-Status"]=pc_status
        
             with open("pc_record.csv","a")as file:
              p_writer=csv.DictWriter(file,fieldnames=field)
              p_writer.writerow(pc)
              print("Data Stored\n")
     
              
              
    
    
    

def Update_PC():
    '''This Function is for Updating the PC Information'''
    file=open('pc_record.csv','r')
    Reader=csv.DictReader(file)
    dict={}
    s=int(input("Enter the pc-number you want to update:"))
    found=False
    for item in Reader:
        if item['PC-Number']==str(s):
            found=True
            pc_os=str(input("Enter the os name install in pc: "))
            pc_status=str(input("Enter the status of the pc: "))
            item['OS-Installed']=pc_os
            item['PC-Status']=pc_status
        dict.append(item)
    file.close()
    if found:
        print("No Data Found !!!!")          
            
    else:
        file=open('pc_record.csv','w+',newline='')
        Writer=csv.writer(file)
        Writer.writerows(lst)
        file.seek(0)
        Reader=csv.reader(file)
        for row in Reader:
            print(row)
        file.close()           
               
            
           
    
    
                    
                            
            
            
    
    
    
















def Remove_PC():
    '''This Function is for Removing the PC Information'''
    
    
    
    
    
    
    
    
def Display_All_PC():
    '''This Function is for Displaying All PC Information'''
    try:
        with open("pc_record.csv","r")as file:
            d_reader = csv.DictReader(file)
            for i in d_reader:
                print("PC-Number: ",i["PC-Number"])
                print("PC-OS: ",i["OS-Installed"])
                print("PC-Status: ",i["PC-Status"])
                print("\n")
        
    except EOFError:
        print("No record found !!!") 
        
         









def Display_PC():
    '''This Function is for Displaying a specific PC Information'''















#Option Functionality
def Option():
    '''This Function for showing the option on the console. This function can be updated for further use'''    
    while True:   
     print("--------Welcome to the Computer Lab Management--------")
     print("1.Add a Computer Details")
     print("2.Update a Computer Details")
     print("3.Remove Computer Details")
     print("4.Display All Computer Details")
     print("5.Search Computer Details")
     print("6.Exit")
     print("-------------------------------------------------------")
     
     print("\n")
     
     choice=int(input("Enter the action you want:"))
     
     if choice==1:
         Add_PC()
         
     elif choice==2:
         Update_PC()    
     
     elif choice==3:
         Remove_PC()   
         
     elif choice==4:
         Display_All_PC()
           
     elif choice==5:
         Display_PC()
         
     elif choice==6:
         exit()
    
     else:
         print("Please input a legal action as described above") 





if __name__=="__main__":
    '''This Function is the main function where methods are called'''
    Option()
    
     
    
    
    
