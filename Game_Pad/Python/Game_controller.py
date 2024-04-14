import logging
import time
import keyboard

from kaspersmicrobit import KaspersMicrobit

logging.basicConfig(level=logging.INFO)

def print_received_string(string: str):
    global rider

    print(f"Received from microbit: '{string}'")
    rider = string

    res = rider.split(",", 3)
    print("Accelerometer:", res[0], "Touch_pad1 :", res[1], "Touch_pad2:", res[2])
    if res[1] == "true":
        keyboard.press('up')
        time.sleep(0.1)
        keyboard.release('up')

    elif res[2] == "true":
        keyboard.press('down')
        time.sleep(0.1)
        keyboard.release('down')

    elif res[0] >= "500":
        keyboard.press('right')
        time.sleep(0.1)
        keyboard.release('right')
    elif res[0] < "0":
        keyboard.press('left')
        time.sleep(0.1)
        keyboard.release('left')
    else:
        print("jumbo")


with KaspersMicrobit.find_one_microbit() as microbit:
    microbit.uart.receive_string(print_received_string)


    time.sleep(20)