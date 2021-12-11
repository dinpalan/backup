#! /usr/bin/env python3
#SHEBANG

#import modules with methods in this space
try:
    from netmiko import ConnectHandler
except:
    print("Please run 'pip install netmiko'")
try:
    import csv
except:
    print("Please run 'pip install csv'")   

def automatic():
        print("You choosen the Automatic backup option")
        print("Please make sure 'device.csv' file is updated")
        a=0
        no=input("Please enter the number of devices from which you need to take Automatic backup:")
        while a<int(no):
            with open('devices.csv', 'r') as f:
                reader = csv.reader(f)
                the_whole_file = list(reader)
                row = a
                column1 = 0
                ips = the_whole_file[row][column1]
                column2 = 1
                usernames = the_whole_file[row][column2]
                column3 = 2
                passwords = the_whole_file[row][column3]
                column4 = 3
                secrets = the_whole_file[row][column4]
                detail = {
                    'device_type':'cisco_ios',
                    'ip': ips,
                    'username': usernames,
                    'password': passwords,
                    'secret': secrets,
                    }
                print(f"successfully SSH into the {ips} \n Login details are shown below:")   
                print(detail)
                vty = ConnectHandler(**detail)    
                vty.enable()
                output4 = vty.send_command("show running-config")
                save_file = open(f"running{a}.txt","w")
                save_file.write(output4)
                save_file.close()
                print(f"Please check the 'running{a}.txt' file for running configuration")
                vty.disconnect()
                a=int(a)+1;
                print(f"Please copy and save the device running{a} config file into a safe folder")
            
                   
def manual():    
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
            print(f"successfully SSH into the {ipl} \n Login details are shown below:")   
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
            print(f"Please copy and save the device running{i} config file into a safe folder")
                          

def dikupabackup():
#write your main function here 
       try:           
            print("Wecome to Network Backup Application\nPress 'ctrl+c' to exit anytime during process");   
            back=input("Please type yes for manual backup or no for Automatic backup(yes/no):")
            backup=back.lower()
            try:
                try:
                    if backup == 'no':     
                        automatic()
                    if backup == 'yes':
                        manual()
                 except:
                    print("Problem occured! Please check the ssh connection to the devices from putty")
            except:
                print("Please type only yes or no");
                dikupabackup();
                
                     
       except KeyboardInterrupt:
              print("Exiting because of program interpreted by user"); print("Thanks for using my application");       
              
if __name__=='__main__':
       dikupabackup()   

