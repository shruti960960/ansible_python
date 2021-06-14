
#!/usr/bin/python3
print("content-type: text/html")
print()

import os 
import getpass

os.system("tput setaf 1")
print("\t\tHello this is TUI project which will makes ur life simple")

os.system("tput setaf 7")
print("\t\t---------------------------------------------------------")

passwd = getpass.getpass("Enter ur password : ")
apass = "******"
if passwd != apass:
    print("authentication failure")
    exit()
    
while True:
    print("""
    Press 1  : To create file
    Press 2  : To remove file
    Press 3  : To create directory
    press 4  : To remove directory
    Press 5  : To copy files or directory
    Press 6  : To move files or directory
    Press 7  : To create user
    Press 8  : To delete user
    Press 9  : To download anything form google
    Press 10 : To configure web server
    Press 11 : To configure nfs
    Press 12 : To configure samba at server side
    Press 13 : To configure samba at client side
    Press 14 : To configure mariadb
    Press 15 : To exit
    """)   

    print("enter ur choice : ",end="")
    ch=input()
    print(ch)
    if int(ch) == 1:
        os.system("ansible-playbook create_file.yml")
    elif int(ch) == 2:
        os.system("ansible-playbook remove_file.yml")
    elif int(ch) == 3:
        os.system("ansible-playbook create_dir.yml")
    elif int(ch) == 4:
        os.system("ansible-playbook remove_dir.yml")
    elif int(ch) == 5:
        os.system("ansible-playbook copy_file.yml")
    elif int(ch) == 6:
        os.system("ansible-playbook move_file.yml")
    elif int(ch) == 7:
        os.system("ansible-playbook create_user.yml")
    elif int(ch) == 8:
        os.system("ansible-playbook remove_user.yml")
    elif int(ch) == 9:
        os.system("ansible-playbook download.yml")
    elif int(ch) == 10:
        os.system("ansible-playbook configure_webserver.yml")
    elif int(ch) == 11:
        os.system("ansible-playbook nfs.yml")
    elif int(ch) == 12:
        os.system("ansible-playbook samba_server.yml")
    elif int(ch) == 13:
        os.system("ansible-playbook samba_client.yml")
    elif int(ch) == 14:
        os.system("ansible-playbook mariadb.yml")
    elif int(ch) == 15:
        exit()
    else:
        print("Does not support")
