import winreg
import wmi




IP_addresses = open ("C:/Users/tkn/Desktop/Python_scripts/IP_adrese.txt","r")

def enable_remote_reg():

    outputs={}
    c = wmi.WMI()

    for IP in IP_addresses:

         info = IP.split()

         try:
             c = wmi.WMI(computer=info[0], user=info[1], password=info[2])
             print(info[0]+'-->'+"Connection established")
             c.Win32_Process.Create(CommandLine='cmd.exe /c sc start remoteregistry start=auto')
             
        
         except Exception as e:
             print(info[0]+'-->'+"Could not connect to machine")
             print(e)
             
 
             
    
         outputs[c]=[]
   
    return outputs





outputs = enable_remote_reg()
