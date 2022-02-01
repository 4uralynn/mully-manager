#!/usr/bin/env python3
import os
import sys
import re
import subprocess
import signal
import shutil
import time

#Reads files in the vpn folder, does a regex search for country initials 
#and writes then successively appends them list argument
def write_initial_list(initial_list, path):
    for name in os.listdir(path):
        filename = os.path.join(path, name)
        initials = re.search(r"_([a-z]{2})_a", filename)
        if initials is None:
            pass
        elif not os.path.isdir(filename):
            initial_list.append(initials[1])

#Uses the argument from the system to choose country. 
#Default is Sweden
#Also provides a help message or initiates a disconnect
def sel_country(initial_list, conn_info):
    ccode = str
    if len(sys.argv) < 2:
        ccode = "se"
        #filename = sel_country(initial_list, ccode)
    elif sys.argv[1] == "disco":
        return disconnect(conn_info[0], conn_info[1])
    elif sys.argv[1] == "--help":
        print("Valid country options are:  " + ", ".join(initial_list))
        return 0
    elif len(sys.argv[1]) == 2 and sys.argv[1].lower() in initial_list:
        ccode = sys.argv[1]
        #filename = sel_country(initial_list, ccode)
    else:
        print("'{}' is not a valid option. Type 'mullvad --help' to " 
                "see country list.".format(sys.argv[1]))
        return 0
    return ccode 

#Pulls the PID number and status from the 'log.txt' file using regex
def logscrape(conn_info):
    pattern=r"\[(\d+)\]:\s([a-z]+)$"
    with open("log.txt") as file:
        for line in file.readlines():
            sresult = re.search(pattern, line)
    file.close()
    conn_info.append(sresult.group(1))
    conn_info.append(sresult.group(2))

#Calls the 'connect' bash script. If already connected, the PID for the
#current connection recieves a kill signal and then reconnects.
def connect(conn_no, status):
    if "down" in status:
        print("Starting Mullvad VPN...\n")
    elif "up" in status:
        print("Resetting with new country code...\n")
        os.kill(int(conn_no), signal.SIGTERM)
        time.sleep(5)
    else: 
        return 1
    mully = subprocess.call("./connect.sh &", shell=True)
    return 0

#If the retrieved log status is already down, it prints that
#if not, it sends a kill signal to the current connection PID
def disconnect(conn_no, status):
    if "down" in status:
        print("Mullvad VPN is already disconnected.")
    elif "up" in status:
        print("Disconnecting Mullvad VPN...\n")
        os.kill(int(conn_no), signal.SIGTERM)
        time.sleep(5)
        print("\nMullvad VPN has been disconnected.")
    return 0

#Based on the country selected by the user, the main config file
#is overwritten by that country's config file.
def lockin_config(path, ccode):
    os.chdir(path)
    file_src = "mullvad_" + ccode + "_all.conf"
    f_src = open(file_src, 'rb')
    file_dest = "mullvad_current.conf"
    f_dest = open(file_dest, "wb")
    shutil.copyfileobj(f_src, f_dest) 
    print("Country code '{}' is loaded.".format(ccode))
    os.chdir(os.path.dirname(os.path.abspath(__file__)))


#The main function changes the program path to the current directory
#and calls functions to setup a list of country initials, scrape the
#log.txt file for info, facilitates the user's input (help, disc, 
#or country) update the vpn configuration file based on those 
#choices, and connects to the vpn.
def main():
    path = "/etc/openvpn"  ##Input vpn config file location
    initial_list = []
    write_initial_list(initial_list, path)
    conn_info = []
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    logscrape(conn_info)
    ccode = sel_country(initial_list, conn_info)
    if ccode == 0:
        sys.exit(1)
        return
    lockin_config(path, ccode)
    result = connect(conn_info[0], conn_info[1])
    sys.exit(0)
    return result

main()
