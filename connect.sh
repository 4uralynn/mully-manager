status=$( tail -n1 log.txt | grep down | cut -d" " -f6 )	
dateandtime=$( date +"%Y-%m-%d %T" )
if [ $status ]; then 
	sudo ip rule add from 10.0.0.113 table 128
	sudo ip route add table 128 to 10.0.0.113/32 dev eth0
	sudo ip route add table 128 default via 10.0.0.1
	currprocess=$( ps all | tail -n1 | tr -s " " | cut -d" " -f3 )
	mullprocess=$(($currprocess+1))
	echo "$dateandtime ($USER) NEW connection[$mullprocess]: up" >> log.txt
	sudo openvpn --config /etc/openvpn/mullvad_current.conf --ca /etc/openvpn/mullvad_ca.crt --auth-user-pass /etc/openvpn/mullvad_userpass.txt
else
	echo " "
	echo "There is already an open connection."
	echo " "
fi
echo " "
./statuscheck.sh
