apt update;
apt upgrade -y;

apt install python3 -y;
apt install python3-pip -y;

python3 -m pip install discord;
python3 -m pip install requests;
python3 -m pip install selenium;
python3 -m pip install geckodriver-autoinstaller;

python3 -m pip install pyvirtualdisplay pillow EasyProcess;

apt install x11-utils gnumeric -y;
apt install x11-utils firefox -y;
apt install firefox-geckodriver -y;
apt install xvfb xserver-xephyr tigervnc-standalone-server x11-utils gnumeric -y;

apt autoremove -y;
apt remove apache2 -y;