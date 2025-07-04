#!/bin/bash


read -p $' name for AP (max=16): ' AP_name
read -p $' directory name : ' wordlist_name
printf " number of AP's: 100\n"
printf " directory made  >\e[1;32m $(pwd)/$wordlist_name\e[0m\n"

for i in {1.};
do 
	echo "$AP_name-$i"; 
done > $wordlist_name