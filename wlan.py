def do_connect():
    import network
    import time
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network')
        wlan.connect('swap','seeyousoon')
        print('....')
        while wlan.isconnected() == False:
            print('Waiting for connection...')
            time.sleep(1)
            
    print('connected to network',wlan.ifconfig()[0])
    ip = wlan.ifconfig()[0]
    return wlan.ifconfig()[0]