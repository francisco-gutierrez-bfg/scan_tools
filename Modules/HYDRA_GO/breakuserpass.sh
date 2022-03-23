#!/bin/bash
# Desarrolado por:
# Francisco Javier Gutierrez G.
# Hexacta 2021
        if [ -z "${1}" ]; then
        echo ""
        echo "${0} 'IP o host' 'Protocolo'"
        echo ""
        exit
        fi

        PASSFILE="diccionarios/wordlists/passwords.lst"
        LOGIN="diccionarios/wordlists/users.lst"
        IP="${1}"
        PROTO="${2}"
        mayus=`echo $PROTO |tr [a-z] [A-Z]`
        if [ $mayus = "FTP" ]; then
        PORT="21"
        elif [ $mayus = "SSH" ]; then
        PORT="22"
        elif [ $mayus = "HTTP" ]; then
        PORT="80"
        elif [ $mayus = "HTTPS" ]; then
        PORT="443"
        elif [ $mayus = "RDP" ]; then
        PORT="3389"
        fi

        echo "Testing: $1"
        sudo ncat ${1} ${PORT} -w 2 < /dev/null
        ST="$?"
        if [ $ST = "0" ]; then
                hydra -L ${LOGIN} -P ${PASSFILE} ${1} ${PROTO}
        fi
