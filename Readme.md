Steps:
 - Install "Raspberry Pi OS Lite" (2021-10-30 at the time of writing)
 - Upgrade using apt
 - `sudo apt install vim git build-essential cmake python3-opencv python3-pip`
 - `git clone https://github.com/jgarff/rpi_ws281x.git`
 - use cmake to build / install
 - `sudo sh -c 'echo "blacklist snd_bcm2835" > /etc/modprobe.d/snd-blacklist.conf'`
 - `sudo pip install rpi_ws281x`
 - `sudo python3 ws2812_play_movie.py movie.mp4`
