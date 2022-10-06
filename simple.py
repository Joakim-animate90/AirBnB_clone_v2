#!/usr/bin/python
"""Generates a .tgz archive from the
contents of the web_static folder
Distributes an archive to a web server"""

from fabric.operations import local, run, put
from datetime import datetime
import os
from fabric.api import env
import re
import fabric
env.use_ssh_config = True
env.hosts = ['3.236.56.179']
env.user = 'ubuntu'
def do_pack():

    """Function to compress files in an archive"""
    result =  run("whoami")

    if result.failed:
        return None
    return result

