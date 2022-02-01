message=$( curl -s https://am.i.mullvad.net/connected )
status=$( echo $message | cut -d" " -f3 )
dateandtime=$( date +"%Y-%m-%d %T" )
conno=$( tail -n1 log.txt | cut -d"[" -f2 | cut -d"]" -f1 )

if [ $status = not ]; then
	echo $message; echo "Type 'mullvad' if you need to start the vpn."
	uod=down
else
	echo $message; uod=$( echo "up" )
fi
echo "$dateandtime ($USER) CHECK connection[$conno]: $uod" >> log.txt

