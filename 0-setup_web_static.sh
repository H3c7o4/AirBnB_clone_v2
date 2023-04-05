#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

# verify if nginx is installed
nginx -v &> /dev/null
folder="/data/"
s_foler="/data/web_static/"
s_folder_0="/data/web_static/releases/"
s_folder_1="/data/web_static/shared/"
ss_folder="/data/web_static/releases/test/"
html_file="/data/web_static/releases/test/index.html"
link_target="/data/web_static/releases/test/"
link_name="/data/web_static/current"

# If the previous command return an error nginx isn't installed
if [ $? -ne 0 ]
then
	sudo apt update -y && apt upgrade -y
	sudo apt install nginx -y

	sudo nginx -t && sudo /etc/init.d/nginx reload
fi

# Create the folder /data/ if it doesn’t already exist
if [ ! -d "$folder" ]
then
	mkdir "$folder"
fi

# Create the folder /data/web_static/ if it doesn’t already exist
if [ ! -d "$s_folder" ]
then
        sudo mkdir "$s_folder"
fi

# Create the folder /data/web_static/releases/ if it doesn’t already exist
if [ ! -d "$s_folder_0" ]
then
        sudo mkdir "$s_folder_0"
fi

# Create the folder /data/web_static/shared/ if it doesn’t already exist
if [ ! -d "$s_folder_1" ]
then
        sudo mkdir "$s_folder_1"
fi

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
if [ ! -d "$ss_folder" ]
then
        sudo mkdir "$ss_folder"
fi

# Create a fake HTML file /data/web_static/releases/test/index.html
# (with simple content, to test your Nginx configuration)
if [ ! -e "$html_file" ]
then
	sudo touch "$html_file"
	echo "<!DOCTYPE html>" > $html_file
	echo "<html lang=\"en\">" >> 
	echo "<head>" >> $html_file
	echo "  <meta charset=\"UTF-8\">" >> $html_file
	echo "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">" >> $html_file
	echo "  <title>Exemple de page</title>" >> $html_file
	echo "</head>" >> $html_file
	echo "<body>" >> $html_file
	echo "  <h1>Bonjour, bienvenue sur ma page !</h1>" >> $html_file
	echo "</body>" >> $html_file
	echo "</html>" >> $html_file

fi

# Create a symbolic link. If the symbolic link already exists,
# it should be deleted and recreated every time the script is ran.
if [ -L "$link_name" ]
then
	sudo rm "$link_name"
else
	sudo ln -s "$link_target" "$link_name"
fi

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update nginx configuration
sudo sed -i '/location \/hbnb_static/d' /etc/nginx/sites-available/default
sudo sed -i '/alias \/data\/web_static\/current\/;/d' /etc/nginx/sites-available/default
sudo sed -i '/}/i \\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}' /etc/nginx/sites-available/default

exit 0
