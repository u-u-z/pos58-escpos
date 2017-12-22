import usb.core
import usb.util
import sys

dev = usb.core.find(idVendor=0x0483 ,idProduct=0x070b)

cfg = dev.get_active_configuration()

intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf, \
    custom_match = \
    lambda e: \
    usb.util.endpoint_direction(e.bEndpointAddress) == \
    usb.util.ENDPOINT_OUT
)
print ep
dev.reset()
