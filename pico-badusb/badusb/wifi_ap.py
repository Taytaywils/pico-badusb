import wifi
import socketpool

def start():
    wifi.radio.start_ap (
        ssid="Picow",
        password="Picow"
    )
    
    return socketpool.SocketPool(wifi.radio)
