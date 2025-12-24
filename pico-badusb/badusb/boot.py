from board import GP1
from digitalio import DigitalInOut, Pull
from storage import disable_usb_drive
import wifi_ap

# Boot handler class
class Boot:
    
    # Initial setup
    def __init__(self) -> None:
        gp1 = DigitalInOut(GP1)
        gp1.switch_to_input(pull=Pull.UP)
        
        if not gp1.value:
            disable_usb_drive()

    def start_wifi(self):
        self.pool = wifi_ap.start()
