#importing pyshark which allows python to parse pcap files
import pyshark

#parsing the file packets.pcapng and applying a filter so that it only looks for packets going across unencrypted ports
file = pyshark.FileCapture('packets.pcapng', display_filter = 'http || tcp.port == 20 || tcp.port == 21 || udp.port == 21 || '
    'tcp.port == 23 || tcp.port == 25 || udp.port == 69 || '
    'tcp.port == 80 || udp.port == 80 || tcp.port == 110 || '
    'tcp.port == 119 || tcp.port == 139 || tcp.port == 143 || '
    'udp.port == 143 || tcp.port == 161 || udp.port == 161 || '
    'tcp.port == 389 || udp.port == 389 || tcp.port == 445 || '
    'udp.port == 514 || tcp.port == 513 || tcp.port == 6667'
)

#initializing the variables to count how many of each TCP and UDP packets
tcpAmount = 0
udpAmount = 0

#going through each packet and seeing if it is a tcp or udp packet
for packet in file:
    if "TCP" in packet:
        tcpAmount += 1
    if "UDP" in packet:
        udpAmount += 1

#printing total amount
print("Total TCP packets going across unencrypted ports: ", tcpAmount)
print("Total UDP packets going across unencrypted ports: ", udpAmount)
