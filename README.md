Starting the Mincecraft Server on Raspberry Pi 3
===

This script start/stop the Minecraft server running raspberry pi.
## Requirement
* python >= 3.6
* screen 4.05

## Device specifications(Raspberry Pi 3 )
* CPU: 4× ARM Cortex-A53, 1.2GHz
* GPU: Broadcom VideoCore IV
* RAM: 1GB LPDDR2 (900 MHz)

## Usage
Check out the collect script for infomation about different options.
```
python ctl_minecraft_server.py --help
usage: ctl_minecraft_server.py [-h] [-e {start,stop}]

optional arguments:
  -h, --help            show this help message and exit
  -e {start,stop}, --execute {start,stop}
                        Type of execution controlling Minecraft Server
```
## JVM arguments
Default setting JVM arguments as follows in table below.
All variables which can be overridden are stored in script.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `server_file` | minecraft_server.1.13.1.jar | Server file name |
| `session_name` | minecraft | Screen's session name |
| `options` | -Xms800M<br>-Xmx800M<br>-Xmn128M<br>-XX:+UseNUMA<br>-XX:+DisableExplicitGC<br>-XX:+CMSClassUnloadingEnabled<br>-XX:+UseConcMarkSweepGC<br>-XX:+UseParNewGC<br>-XX:NewRatio=2 | JVM option |
