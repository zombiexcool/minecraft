# minecraft
A Ubuntu based minecraft server with a discord bot

# installation 
## Machine hôte : Debian based distro
````
sudo apt update
sudo apt upgrade
sudo apt install openjdk-22-jdk
wget https://piston-data.mojang.com/v1/objects/450698d1863ab5180c25d7c804ef0fe6369dd1ba/server.jar
java -Xmx1024M -Xms1024M -jar minecraft_server.1.21.jar nogui # 1024M = 1Go. Changez a votre guise.
nano eula.txt # mettre true
java -Xmx1024M -Xms1024M -jar minecraft_server.1.21.jar nogui 
````
## mettre en place les script 
placer tout dans votre /home, sauf le daemon (script.service)
````
sudo apt install python3-is-python
sudo apt install python3-discord
git clone https://github.com/zombiexcool/minecraft
sudo chmod +x start.sh
sudo chmod +x stop.sh 
````

## Ouvrir les ports ( port forwarding ) 
````
Machine serveur ( hote )
sudo ufw allow 25565/tcp
````
Configurer votre routeur pour rediriger le port 25565 vers celui de votre serveur.
