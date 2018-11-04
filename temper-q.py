#!/usr/bin/python3
import hidapi

def main():
    for dev_info in hidapi.enumerate(vendor_id=0x413d, product_id=0x2107):
        if(dev_info.interface_number != 1):
            continue
        dev = hidapi.Device(info=dev_info)
        dev.write(b'\x01\x80\x33\x01\x00\x00\x00\x00')
        temp_raw = dev.read(8)
        dev.close()
        print(dump_to_temperature(temp_raw[2:4]))
        exit(0)
    print('No temper thermometer found')
    exit(1)

def dump_to_temperature(bytes):
    temp = (bytes[0] <<8) + bytes[1]
    return float(temp) / 100

if __name__ == '__main__':
    main()
