#! /usr/bin/env python3
#SHEBANG

#import modules with methods in this space
try:
    from netmiko import ConnectHandler
except:
    print("Please run 'pip install netmiko'")    

def network():
    print("Wecome to Network Backup Application\nPress 'ctrl+c' to exit anytime during process");   
    back=input("Please type yes for manual backup or no for Automatic backup(yes/no):")
    backup=back.lower()
    if backup == 'no':
        print("You choosen the Automatic backup option")
        print("Sorry for the inconvience. I am currently working on this project. Will add this feature soon. Please use manual backup as per now.")
        input("Press enter to use backup application or Press ctrl+c to exit")
        network()
        #print("Please make sure 'device.csv' file is updated")
    if backup == 'yes':
        print("You choosen the Manual backup option")
        no=input("Please enter the number of devices from which you need to take manual backup:")
        i=0
        while i<int(no):
            print(i)
            ipl = input("Please enter device IP:")  
            details = {
                'device_type':'cisco_ios',
                'ip': ipl,
                'username': input("Please enter the username for login:"),
                'password': input("Please enter the password for login:"),
                'secret': input("Please enter the secret password for enable:"),
                }
            print("successfully SSH into the router using Netmiko \n Login details are shown below:")   
            print(details)
            vty = ConnectHandler(**details)    
            vty.enable()
            output4 = vty.send_command("show running-config")
            save_file = open(f"running{i}.txt","w")
            save_file.write(output4)
            save_file.close()
            print(f"Please check the 'running{i}.txt' file for running configuration")
            vty.disconnect()
            i=int(i)+1;    
    else:
        print("Please type only yes or no");
        network();

def main():
#write your main function here 
       try:            
              network()
                     
       except KeyboardInterrupt:
              print("Exiting because of program interpreted by user"); print("Thanks for using my application");       
              
if __name__=='__main__':
       main()   

