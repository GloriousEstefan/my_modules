from tkinter import *
from is_ip_valid_gui import is_ip_valid
from is_mac_valid_gui import is_mac_valid
from ssh_connection_gui import ios_ssh
from napalm_get_config_gui import napalm_get_config

root = Tk()

def search_func(ip, user, passw):
    device_ip = is_ip_valid(ip)
    ssh_connection = ios_ssh(device_ip, user, passw)
    config = napalm_get_config(ssh_connection)
    result_text.insert(END, config)

username_label = Label(root, text="Enter username:")
password_label = Label(root, text="Enter password:")
ip_label = Label(root, text="Enter IP address:")
mac_label = Label(root, text="Enter MAC address:")

username_entry = Entry(root, width=25)
password_entry = Entry(root, width=25)
ip_entry = Entry(root, width=25)
mac_entry = Entry(root, width=25)
ip_addr,mac_addr,username,password = ip_entry.get(),mac_entry.get(),username_entry.get(),password_entry.get()
print('hello')
search_button = Button(root, text="Search", command=search_func(ip_addr, username, password))
print('hello')
result_text = Text(root, height=5, width=52)

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