from time import *
import os

###... (    ALL VARIABLES ARE DEFINED BELOW    ) ...###

project_name = str(time()).split('.')[0]
log_file_name = "/home/anant/Desktop/Wireless_Network_Optimization_Results/" + project_name + "/logs.txt"

###... (    ALL VARIABLES ARE DEFINED ABOVE    ) ...###


def make_project():
    os.system("mkdir -p ~/Desktop/Wireless_Network_Optimization_Results/" + project_name)
    dir_notification = "Directory created  :-  ~/Desktop/Wireless_Network_Optimization_Results/" + project_name
    print(dir_notification)

    os.system("touch " + log_file_name)
    log_notification = " File created  :-  /home/anant/Desktop/Wireless_Network_Optimization_Results/" + project_name + "/logs.txt"
    print(log_notification)

    on_start(dir_notification)


def add_log(data):
    c_time = ctime()
    log_file = open(log_file_name , 'a')
    log_file.writelines("\n" + str(c_time) + " - " + str(time()) + " - " + data + "\n")
    log_file.flush()
    log_file.close()


def on_start(data):
    add_log(data)


def on_finish(data):
    add_log(data)