import sys
import usb.core
import usb.util

print(f"setting to GPIO={sys.argv[1]}")

VID = 0x2e8a
PID = 0x000c

dev = usb.core.find(idVendor=VID, idProduct=PID)
if dev is None:
    raise ValueError("Device not found")

out_endpoint = 0x04
data = [0x02, 0x03, int(sys.argv[1])]
dev.write(out_endpoint, data)

in_endpoint = 0x85
response = dev.read(in_endpoint, 64)  
print("Response:", response)
