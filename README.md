# IntercomProject
Intercom Project using Raspberry Pi 3 and Pi Zeros to act as an intercom system. It sets up the Raspberry Pi3 as a network access point, which then connects to the Pi Zeros over ethernet. Using the Waveshare Audio Hat for Raspberry Pi, it creates a system that broadcasts audio between the Pis when a button is pressed. Sound is played back by all connected Pis (but not the one recording the audio to prevent feedback loops). 

In its current form, this project does not work. It's still usable; the only issue is that the Raspberry Pi Zeros cut out periodically. In order to fix it, I planned to switch the pi zero's to a RTOS system. However, I have not had the time at this point to do so. Setup instructions are found in the PDF file and the python code is included. It provides minimal delay due to network. I had the system down to a couple of milliseconds of delay between recording and playback. 

This project helped me learn how to debug systems, from the order in which everything needs to be setup, to all the little tweaks it needed to make it work. I hope someone finds this useful. 
