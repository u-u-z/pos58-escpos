from escpos.printer import Usb,Dummy,Serial
import os
import hashlib
#Print System usb id information
os.system("lsusb")
print("\n\n")
#Get user usbid
'''
vid = input("\nPlease input VendorID (e.g.:0x21a1):")
vid = int(vid,16)
pid = input("\nPlease input ProductID (e.g.:0x2123):")
pid = int(pid,16)
oep = input("\nPlease input ENDPOINT:")
oep = int(oep,16)
print("\nThe USB VendorID is ["+str(vid)+"] ProductID is ["+str(pid)+"]")
'''
i =0 
p = Usb(0x0483,0x070b,0,out_ep=0x2)
p.text("HELLO WORLD! I'M PRINTER!\n\n")
p.image("timg.jpg")
while True:
    pstr = str(hashlib.md5(i+123).hexdigest())
    p.text(pstr)
    i = i + 1