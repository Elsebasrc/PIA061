#!/bin/bash
#
# Script <superscan.sh> 
# <06/03/2022> - < Brian Reyna Castillo> 
#Menu en BASH
#
date

    echo "|"
    echo "|---------------------------|"
    echo "|   Menu Principal          |"
    echo "|---------------------------|"
    echo "|1. Net Discover"
    echo "|2. Portscanv1"
    echo "|3. Welcome"
    echo "|4. Exit"
    echo "|"
read -p "Opción  [ 1 - 4 ] " c

case $c in
        1) $HOME/netdiscover.sh;;
        2) $HOME/portscanv1.sh $1;;
        3) $HOME/welcome.sh;;
        4) echo "Bye!"; exit 0;;
esac
