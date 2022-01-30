from android import Android

def unlock(password):
    droid.keyevent('HOME')
    droid.swipe(700, 2400, 700, 320, 500)
    droid.text_input(password)
    droid.keyevent(66)

droid = Android()

unlock(input('Password?: '))
