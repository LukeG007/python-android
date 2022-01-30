# Python for Android
## Info
A way to install python on a rooted android device. It also comes with a module that makes it easier to interract with the device from python

## Requirements
The device must be rooted.

## Setup
Run this on the computer that is connected to the android device as root
```sh
git clone https://github.com/LukeG007/python-android
adb push python-android /data/python-android
adb shell chmod 755 /data/python-android/setup.sh
adb shell "su -c '/data/python-android/setup.sh'"
```

## Examples
### Unlock Device
```python
from android import Android

def unlock():
    droid.keyevent('HOME')
    droid.swipe(700, 2400, 700, 320, 500)
    droid.text_input('password')
    droid.keyevent(66)

droid = Android()

unlock()
```
### Take a screenshot
```python
from android import Android

droid = Android()

droid.screenshot('/storage/emulated/0/Pictures')
```
### Reboot
```python
from android import Android

droid = Android()

droid.reboot()
```
