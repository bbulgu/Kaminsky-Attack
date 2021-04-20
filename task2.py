from scapy.all import *
import random
import string

randstr = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
Qdsec = DNSQR(qname=randstr+".example.com")
dns = DNS(id=0xAAAA, qr=0, qdcount=1, ancount=0, nscount=0,arcount=0, qd=Qdsec)
ip = IP(dst="10.9.0.53", src="10.9.0.1")
udp = UDP(dport=53, sport=33333, chksum=0)
request = ip/udp/dns
send(request)

with open("ip_req.bin", "wb") as f:
	f.write(bytes(request))
