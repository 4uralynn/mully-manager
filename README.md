Mully Manager
===============

***If using Mullvad VPN,*** this program utilizes Python and bash scripts to facilitate quick server changes from within a terminal. This program
could probably be modified to accommodate any VPN service utilizing openvpn, but it was made to work with Mullvad.


**More details to come:**

  + If you are looking to try this script out, you can clone the repository anywhere on your machine. Currently, the following commands *must* executed before the scripts will run.
    - First create a **log.txt** in the directory using this command: `echo "0000-00-00 00:00:00 (root) CHECK connection[000000]: down" > log.txt`
    - Next make the scripts executable: `chmod +x connect.sh && chmod +x mullmanage.py && chmod +x statuscheck.sh`
    - For multiple users to access the scripts, permissions for **connect.sh**, **mullmanage.py**, **statuscheck.sh**, and **log.txt** will need to be updated for those users as well. 
