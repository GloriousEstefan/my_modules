import json
from tkinter import *
from is_ip_valid_gui import is_ip_valid
from is_mac_valid_gui import is_mac_valid
from ssh_connection_gui import ios_ssh
from napalm_get_config_gui import napalm_get_config

root = Tk()
login_frame = Frame(root)
input_frame = Frame(root)
output_frame = Frame(root)
func_frame = Frame(root)

def search_func(ip, mac, user, passw):
    
    device_ip = is_ip_valid(ip)
    ssh_connection = ios_ssh(ip, user, passw)
    config = napalm_get_config(ssh_connection)
    result_text.insert(END, json.dumps(config))

def search_butt():
    
    ip_addr,mac_addr,username,password = ip_entry.get(),mac_entry.get(),username_entry.get(),password_entry.get()
    search = search_func(ip_addr, mac_addr, username, password)

username_label = Label(login_frame, text="Enter username:")
password_label = Label(login_frame, text="Enter password:")
ip_label = Label(root, text="Enter IP address:")
mac_label = Label(root, text="Enter MAC address:")

username_entry = Entry(login_frame, width=25)
password_entry = Entry(login_frame, width=25)
ip_entry = Entry(root, width=25)
mac_entry = Entry(root, width=25)

search_button = Button(root, text="Search", command=search_butt)
result_text = Text(root, height=100, width=100)

login_frame.pack(side=LEFT)
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
ip_label.pack()
ip_entry.pack()
mac_label.pack()
mac_entry.pack()
search_button.pack()
result_text.pack()


root.mainloop()