**Design Your Own Custom Game Controller Using Micro: bit**


1) Upload microbit_Uart_data.hex on microbit.

2) Install LightBlue app if using Mac OS (Microbit is not visible in the Bluetooth menu), It has not been tested on Windows as of now.
   
3) Install Nordic NRF connect on your mobile phone and pair micro: bit using pairing mode. (only the first time you upload the Bluetooth code). It will help you to check what all services are running on microbit. Once you see all micro: bit required Bluetooth services are up then you can disconnect

4) Install below library:
    
    pip install bleak ( optional if installing Kaspermicrobit library(**wrapper of bleak library**))
    
    pip install kaspersmicrobit
 
    pip install keyboard

    pip install pyobjc  –upgrade

5) run the code Game_controller.py and read the values
