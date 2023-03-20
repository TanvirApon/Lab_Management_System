import json

'''Computer Lab Management Application using Python'''




#Add the PC Details in JSON file
def Add_PC():
    '''This Function is for Adding A PC Information'''
    print("\n")
    print("--------------------------Instructions-----------------------------")
    print("Please remember to input Number while you input the PC Number.")
    print("Please remember to input WORD while you input the PC OS and Status.")
    print("If you don't follow the above instruction it will give you an error.")
    print("--------------------------------------------------------------------\n") 
    
    pc_num=str(input("Enter the number of the pc: "))
    check(pc_num)
    pos=str(input("Enter the os name install in pc: "))
    pstatus=str(input("Enter the status of the pc: ")) 
     
    pc={
        
        "pc-number: ":pc_num,
        "pc-os: " :pos,
        "pc-status: ":pstatus     
    }
    
    with open("pc_record.json","r") as getdata:
        data = json.load(getdata)
        
        data[pc_num]=pc
        
        with open("pc_record.json","w") as save:
            json.dump(data, save)
            print("Data Stored")
            

#Update the PC-OS and PC-Status
def Update_PC():
    '''This Function is for Updating the PC Information'''
    no=input("Enter the pc number: ")
    with open("pc_record.json","r") as getdata:
        data=json.load(getdata)
        if no in data:
            pos=str(input("Enter the os name install in pc: "))
            pstatus=str(input("Enter the status of the pc: "))
            
            pc={
                "pc-number: ":no,
                "pc-os: " :pos,
                "pc-status: ":pstatus    
            }
            
            data[no]=pc
            with open("pc_record.json","w")as update:
                json.dump(data, update)
                print("Updated Data") 
                   
    

#Remove a specific PC
def Remove_PC():
    Display_All_PC()
    '''This Function is for Removing the PC Information'''
    no=input("Enter the pc number: ")
    
    with open("pc_record.json","r") as getdata:
        data = json.load(getdata)
        if no in data:
            data.pop(no)
            
            with open("pc_record.json","w") as delete:
                data1=json.dump(data, delete)
                print("Data Deleted")
                
        else:
            print("No data found !")
      
    
    
#Display All the PC
def Display_All_PC():
    '''This Function is for Displaying All PC Information'''
    with open('pc_record.json','r')as view:
        data=json.load(view) 
        for i,m in data.items():
            for x,n in m.items():
                print(x,n)
            print("\n")
                
   

#Check the pc number is already taken or not
def check(pc_num):
    '''This function is for checking pc number'''
    
    with open("pc_record.json","r") as getdata:
        data = json.load(getdata)
        for i,m in data.items():
            if i == pc_num:
                print("Pc Number already exits")
                Add_PC()



#Display Specific PC
def Display_PC():
    '''This Function is for Displaying a specific PC Information'''
    no=input("Enter the pc number: ")
    with open("pc_record.json","r") as getdata:
        data = json.load(getdata)
        for i,m in data.items():
            if i == no:
                for x,n in m.items():
                    print(x,n)
                print("\n") 
                       


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
    
     
    
    
    
