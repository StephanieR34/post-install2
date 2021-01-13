# post-install2

echo 

echo est une commande UNIX (également présente avec MS-DOS) qui permet d'afficher une chaîne de caractères passée en paramètre sur le terminal (sortie standard).

sudo apt-get update 

#Sudo (substitute user do) est un programme conçu pour permettre à un utilisateur d'exécuter une commande sous un autre.
#En général, on l'utilise pour autoriser certains utilisateurs à exécuter certaines commandes en tant que root.
#ainsi sudo est souvent considéré comme l’abréviation de Super-user do.
#apt-get update télécharge les listes de paquets des référentiels et les "met à jour" pour obtenir des informations sur les dernières versions des paquets et leurs dépendances.

sudo apt-get install --yes git git-extras python3-pip 

#ici on installe git avec les supplementation git-extras ainsi que pip pour python 3 

sudo snap install discord 

#on installe discord 
sudo snap install code --classic
#on instale visual studio code


pour le script en python on utilise la methode 
os.system() qui permet de transcrire n'importe quel language pour l'executer en python 
