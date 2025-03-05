def do_ap():
    import network
    ap_if = network.WLAN(network.AP_IF)
    mac = ''.join('%02x' % b for b in ap_if.config('mac'))[-5:]
    if not network.WLAN(network.AP_IF).active() and not network.WLAN(network.STA_IF).isconnected():
        print("Config...")
        ap_if.config(essid='catalejo-'+mac, authmode=3, password='87654321')
        ap_if.active(True)
    print('WiFi name: ' + 'catalejo-' + mac)
    print('PASS: ' + '87654321')

def led_ctr(led, state):
    if led:
        if state != None:
            led.value(state)
        else:
            led.value(not led.value())

def but_ctr(but, logic):
    if but:
        return but.value() == logic
    else:
        return False

def removeMain():
    try:
        from machine import Pin
        import wifi_config
        import time
        if wifi_config.BUT != None and wifi_config.LBUT != None:
            but = Pin(wifi_config.BUT, Pin.IN)
            time.sleep(1.5)
            ret_but = but_ctr(but, wifi_config.LBUT)
            if ret_but:
                import os
                os.remove("main.py")
                print("main.py removed")
    except OSError as e:
        print(e)

def do_sta_connect():
    import network
    import wifi_config
    if not wifi_config.SSID or not wifi_config.PASS or not wifi_config.ATTE:
        return
    wlan = network.WLAN(network.STA_IF)
    mac = ''.join('%02x' % b for b in network.WLAN(network.AP_IF).config('mac'))[-5:]
    wlan.active(True)
    from machine import Pin
    import time
    led = None
    but = None
    ret_but = None
    if wifi_config.LED != None and wifi_config.LLED != None:
        led = Pin(wifi_config.LED, Pin.OUT)
    if wifi_config.BUT != None and wifi_config.LBUT != None:
        but = Pin(wifi_config.BUT, Pin.IN)
    led_ctr(led, wifi_config.LLED)
    time.sleep(0.5)
    ret_but = but_ctr(but, wifi_config.LBUT)
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(wifi_config.SSID, wifi_config.PASS)
        attemps = 0
        while not wlan.isconnected() and attemps < wifi_config.ATTE:
            led_ctr(led, wifi_config.LLED)
            time.sleep(0.1)
            led_ctr(led, not wifi_config.LLED)
            time.sleep(0.9)
            attemps += 1
    if wlan.isconnected(): 
        led_ctr(led, wifi_config.LLED)
        print("IP STA: ", wlan.ifconfig()[0])
        print("Dev: catalejo-" + mac)
        if ret_but :
            time.sleep(3)
            while not but_ctr(but, wifi_config.LBUT):
                led_ctr(led, None)
                print("IP STA: ", wlan.ifconfig()[0])
                print("Dev: catalejo-" + mac)
                time.sleep(1)
        if not wifi_config.AP:
            network.WLAN(network.AP_IF).active(False)
            print("AP_IF off")
    else:
        wlan.active(False)
        led_ctr(led, not wifi_config.LLED)
        print("Don't connect how a STA")
