# Python for Android
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
