from ipaddress import*
net = ip_network('192.168.15.0/255.255.255.0')
for ip in net:
    print(ip)