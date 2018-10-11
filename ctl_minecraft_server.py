# -*- coding: utf-8 -*-
##########################################################################
#
# Start/Stop your own Minecraft Server
#
##########################################################################

"""
This script start/stop the Minecraft server.
"""

import argparse
import subprocess
import sys
from logging import getLogger, StreamHandler, DEBUG, Formatter

##########################################################################
# JVM arguments
##########################################################################
# Server file
server_file = "minecraft_server.1.13.1.jar"
# screen's session name
session_name = "minecraft"
# java commandline option
options = (
        "-Xms800M",
        "-Xmx800M",
        "-Xmn128M",
        "-XX:+UseNUMA",
        "-XX:+DisableExplicitGC",
        "-XX:+CMSClassUnloadingEnabled",
        "-XX:+UseConcMarkSweepGC",
        "-XX:+UseParNewGC",
        "-XX:NewRatio=2",
        )

# argparse
parser = argparse.ArgumentParser()
parser.add_argument('-e', '--execute',
                    help='Type of execution controlling Minecraft Server',
                    choices=['start', 'stop'])
args = parser.parse_args()

# logging massage
logger = getLogger(__name__)
logger.setLevel(DEBUG)
stream_handler = StreamHandler()
stream_handler.setLevel = (DEBUG)
handler_format = Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
stream_handler.setFormatter(handler_format)
logger.addHandler(stream_handler)

def check_proc():
    """
    Check minecraft server proccesses.
    """
    cmd = "screen -ls | grep -sq minecraft"
    rc = subprocess.run(cmd, shell=True)
    # If already started Minecraft server process.
    if rc.returncode == 0 :
        logger.info("Minecraft server has already been launched.")
        sys.exit()

def main():
    """
    Main process.
    """
    # Starting the Minecraft server
    if args.execute == "start":
        # check started process.
        check_proc()
        logger.info("Starting Minecraft Server...")
        # Generate command
        screen_cmd = "screen -dmS {}".format(session_name)
        option = " ".join(options)
        java_run_cmd = "java -server {0} -jar {1} nogui" \
                    .format(option, server_file)
        exe_cmd = "{0} {1}".format(screen_cmd, java_run_cmd)
        # Starting server
        try:
            subprocess.check_call(exe_cmd, shell=True)
        except subprocess.CalledProcessError as e:
            logger.error(e)
            sys.exit(8)
        else:
            logger.info("Successfully start-uped server.")
    # Stopping the Minecraft server
    elif args.execute == "stop":
        # Generate command
        logger.info("Stopping Mincecraft Server...")
        screen_cmd = "screen -S {} -X stuff '/stop^M'".format(session_name)
        # Stopping server
        try:
            subprocess.check_call(screen_cmd, shell=True)
        except subprocess.CalledProcessError as e:
            logger.error(e)
            sys.exit(8)
        else:
            logger.info("Successfully stopped server.")

if __name__ == "__main__":
    main()
