# EDITH---Personal-Automation-assistant
This Automated personal assistant works through speech recognition process and automates your mundane tasks such as, searching the web, Wikipedia query, playing
music online etc.
This project makes use of pre-existing python libraries such as - speech_recognition, Pyttsx3 (version 2.71) and selenium.

PROBABLE ERRORS that you might face
1. while using Pyttsx3 module you might come accross 'module not found' error, this is caused by 32 bit dependencies in your 64bit python. Run 'pip install pypiwin32' 
in your terminal to get rid of the error.
2. Next error while using same module can be 'Key Error = none'. this is caused because Pyttsx version beyond 2.71 have compatibility issues with pypiwin32. Run 
'pip uninstall Pyttsx3' and then run 'pip install Pyttsx3=2.71'. Then your code will run fine.


