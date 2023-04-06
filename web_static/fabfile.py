#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """generates a .tgz archive"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}".format(archive_name)

    if not os.path.exists("versions"):
        os.mkdir("versions")

    local("tar -czvf {} web_static".format(archive_path))

    if os.path.exists(archive_path):
        return archive_path
    else:
        return None
