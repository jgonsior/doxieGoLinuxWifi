# doxieGoLinuxWifi
A python script for downloading scans from a Doxie Wifi Go scanner.

# Installation
You need to have [Pipenv](https://github.com/pypa/pipenv) installed.
After that you just need to run `pipenv install` to install all needed dependencies and are then free to go.

# Config
You need to have the following config file in `~/.config/doxieGoLinuxWifi/config`:

```ini
[DEFAULT]
doxieip = http://192.168.1.40:8080/
downloadLocation = ~/documents/inbox
```
