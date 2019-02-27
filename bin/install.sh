#!/usr/bin/env bash

if [ $# = 0 ]; then
    printf "\e[33mNeed to specify the name of the new command: \e[37m\e[44minstall.sh <command>\e[0m"
else # do install
    # verify profile for bin PATH
    verify_profile=$(cat ~/.profile | grep "$1 command registry")
    if [ "$verify_profile" != "" ]; then
        printf "\e[42m\e[97m$1\e[49m\e[92m command already installed in your PATH. \e[1mRIGHT ON!!\e[0m\n"
    else
        bin_pwd=$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )
        printf "\e[33minstalling $1...\e[0m\n"
        echo "PATH=\"$bin_pwd:\$PATH\" # $1 command registry" >> ~/.profile
        cp $bin_pwd/internal/.base $bin_pwd/$1
        chmod +x $bin_pwd/$1
        printf "\e[32mInstalled. Remember to \e[44m\e[97msource ~/.profile\e[49m\e[32m or re-login your terminal. \e[1mHAVE FUN!!\e[0m\n"
    fi
    # verify host
    verify_hosts=$(cat /etc/hosts | grep "$1 command registry")
    if [ "$verify_hosts" != "" ]; then
        echo "already in hosts: ${verify_hosts}"
    else
        while true; do
            read -rp "Type url base (for base.local) to use [empty to use '$1.local']: " REPLY
            if [ "$REPLY" != "" ]; then
                url_base=$REPLY
                read -rp "Using $url_base.local. confirm? [y/n]: " REPLY
                if [[ ${REPLY,,} =~ ^(y|yes|j|ja|s|si|o|oui)$ ]]; then
                    echo "127.0.0.1  $url_base.local # $1 command registry" | sudo tee -a /etc/hosts
                    break
                fi
            else
                echo "127.0.0.1  $1.local # $1 command registry" | sudo tee -a /etc/hosts
                break
            fi
        done
    fi
fi
printf "\n"
