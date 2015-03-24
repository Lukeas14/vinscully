# vinscully
A Raspberry Pi / Python app that will play Vin Scully's "It's time for Dodger Baseball" at the start of every Dodger game.

# Get Started

1. Clone repository
  
  ```
  cd ~/
  git clone https://github.com/Lukeas14/vinscully.git
  cd vinscully
  ```

2. Install pip
  
  ```
  sudo apt-get install python-pip
  ````

3. Install Python package pytz
 
  ```
  sudo pip install pytz
  ```
  
4. Make sure your audio is set to the correct output (HDMI or 3.5mm jack).
  
  Follow the instructions here: http://www.raspberrypi.org/documentation/configuration/audio-config.md

5. Run program

  ```
  python vinscully.py
  ```
