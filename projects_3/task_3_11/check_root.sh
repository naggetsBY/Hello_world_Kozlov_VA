#!/bin/bash

check_root() {
 if [ "$EUID" -ne 0 ]; then
echo "[ERROR] Скрипт должен быть запущен от root!"
 fi 
}

check_root 
