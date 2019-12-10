# houseplant watering stuff
these docs are not designed to be exact or perfect
- setup raspberry pi w/ssh
    - create/edit `wpa_supplicant.conf` for wifi
    - create file named `ssh`
- download docker, python3, mosquitto broker etc on pi
```
curl -sSL https://get.docker.com | sh
sudo apt-get update
sudo apt-get install -y python3 python-pip 
sudo apt-get install -y mosquitto mosquitto-clients
sudo systemctl enable mosquitto.service
```
- use rsync or similar to upload code to pi
```
rsync -av -e ssh --exclude="*.csv" <path> pi@<ip>:/home/pi/    
```

- make python scripts run on startup
  - create three files on the pi one for each of the services 
```
# /etc/systemd/system/<service>.service
[Unit]
Description=<Service>

[Service]
ExecStart=/usr/bin/python3 /home/pi/drippy/<service>/<service>.py
User=pi
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```
    - create ~/.aws/credentials file on pi
    - enable the services 
        - `sudo systemctl enable <service>`
    - `sudo reboot`
        - make sure all the services are running