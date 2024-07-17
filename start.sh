#!/bin/bash

# Chemin vers le fichier marqueur
FILE="/path/to/.script_executed_once"

# Vérifier si le fichier existe
if [ -f "$FILE" ]; then
    echo "Le script a déjà été exécuté. Sortie."
    exit 0
fi
/usr/bin/python3 /home/zombie/bot.py
/usr/bin/java  -Xmx6144M -Xms6144M -jar /home/zombie/server.jar nogui

touch "$FILE"
