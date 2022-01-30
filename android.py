import os

class Android:
    def __init__(self):
        pass

    def start_app(self, app, intent=None):
        if not intent == None:
            os.system('monkey -p {} 1'.format(app))
        else:
            os.system('monkey -p {} -c {} 1'.format(app, intent))
    
    def kill_program(self, program):
        os.system('killall -q {}'.format(program))
    
    def enable_overlay(self, overlay):
        os.system('cmd overlay enable {}'.format(overlay))

    def disable_overlay(self, overlay):
        os.system('cmd overlay disable {}'.format(overlay))
    
    def reboot(self):
        os.system('reboot')

    def shutdown(self):
        os.system('reboot -p')
    
    def tap(self, x, y):
        os.system('input tap {} {}'.format(x, y))
    
    def text_input(self, text):
        os.system('input text {}'.format(text))
    
    def swipe(self, x1, y1, x2, y2, duration):
        os.system('input swipe {} {} {} {} {}'.format(x1, y1, x2, y2, duration))

    def command(self, cmd):
        os.system(cmd)
    
    def setprop(self, name, value):
        os.system('setprop {} {}'.format(name, value))

    def keyevent(self, key):
        os.system('input keyevent {}'.format(key))

    def volume_change(self, updown):
        if updown == 'up':
            os.system('input keyevent VOLUME_UP')
        elif updown == 'down':
            os.system('input keyevent VOLUME_DOWN')
    
    def screenshot(self, location):
        os.system('screencap -p {}'.format(location))

    def install_apk(self, apk):
        os.system('pm install {}'.format(apk))
    
    def uninstall(self, pkg_name):
        os.system('pm uninstall {}'.format(pkg_name))
