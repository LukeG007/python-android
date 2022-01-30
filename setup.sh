#!/system/bin/sh

mount -o rw,remount /
mount -o rw,remount /system
cp android.py python/lib
cp -r python/ /system/python
ln -s /system/python/bin/python3 /system/bin/python3
chmod 755 /system/bin/python3.9
chmod 755 /system/python/bin/*
