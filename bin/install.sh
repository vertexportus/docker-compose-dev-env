#!/usr/bin/env bash

if [ $# = 0 ]; then
    printf "\e[33mNeed to specify the name of the new command: \e[37m\e[44minstall.sh <command>\e[0m"
else # do install
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
fi
