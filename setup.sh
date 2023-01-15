#!/system/bin/sh

mount -o rw,remount /
mount -o rw,remount /system
cp android.py python/system/python3.4.2/lib/python3.4
cp -r python/system /
chmod 755 /system/bin/python3
chmod 755 /system/python3.4.2/bin/*
