# houseplant watering stuff
these docs are not designed to be exact or perfect
- setup raspberry pi w/ssh
    - create/edit `wpa_supplicant.conf` for wifi
    - create file named `ssh`
- download docker, python3, etc on pi
```
curl -sSL https://get.docker.com | sh
sudo apt-get update
sudo apt-get install -y python3 python-pip
```
- use rsync or similar to upload code to pi
```
rsync -av -e ssh --exclude="*.csv" <path> pi@<ip>:/home/pi/    
```
- start mqtt broker on pi
```
docker run -d -p 1883:1883 eclipse-mosquitto
```
- start data publisher
```
# make sure to use python 3.x
python drippy/publisher.py
```
- start server
```
python drippy/server.py
```