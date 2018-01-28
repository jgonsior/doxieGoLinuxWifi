# doxieGoLinuxWifi
A python script for downloading scans from a Doxie Wifi Go scanner.

# Installation
[Pipenv](https://github.com/pypa/pipenv) is requiered for dependency management.

`pipenv install` should be sufficient to be able to execute the program with `python main.py`.

# Config
You need to have the following config file in `~/.config/doxieGoLinuxWifi/config`:

```ini
[DEFAULT]
doxieip = http://192.168.1.40:8080/
downloadLocation = ~/documents/inbox
```
