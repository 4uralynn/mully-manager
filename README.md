Mully Manager
===============

***If using Mullvad VPN,*** this program utilizes Python and bash scripts to facilitate quick server changes from within a terminal. This program
could probably be modified to accommodate any VPN service utilizing openvpn, but it was made to work with Mullvad.


**Instructions for use (more details to come):**
  + In order for these scripts to be usable, **you must have openvpn installed and Mullvad VPN already configured**.
    - Instructions and configuration files for your machine can be found at: https://mullvad.net/it/help/linux-openvpn-installation/
  + If you are looking to try this script out, you can clone the repository anywhere on your machine. Currently, the following commands *must* executed before the scripts will run.
    - First create a **log.txt** in the directory using this command: `echo "0000-00-00 00:00:00 (root) CHECK connection[000000]: down" > log.txt`
    - Next make the scripts executable: `sudo chmod +x connect.sh && sudo chmod +x mullmanage.py && sudo chmod +x statuscheck.sh`
    - For multiple users to access the scripts, permissions for **connect.sh**, **mullmanage.py**, **statuscheck.sh**, and **log.txt** will need to be updated for those users as well. 
  + After the above steps are completed, the script **mullmanage.py** will work to connect you to mullvad. It will connect to Sweden by default, but allows options by typing `mullmanage.py [option]`
    - The `--help` option will show a list of country codes, which can be typed in as options.
    - The `disco` option will disconnect from the VPN if you are connected.
  + For simple use, the files in the *to_bin* folder can be utilized by copying them to your binaries directory. 
    - First, update the paths in each file to the correct directory on your system.
    - Next, use the command `sudo chmod +x /to_bin/mullvad && sudo chmod +x /to_bin/vpnstatus && sudo cp to_bin/* /usr/bin/`
    - Afterwards, the program will run by typing `mullvad [option]`, and you can check the connection at any time using `vpnstatus`
