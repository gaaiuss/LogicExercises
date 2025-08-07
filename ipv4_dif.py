# Print the diference in valid ip addresses between two diferent ips
# EX: 10.0.0.1 - 10.0.0.50 = 50
# 10.0.1.0 - 10.0.0.0 = 256

def ipv4_dif(first, last):
    def ip_to_int(ip):
        parts = list(map(int, ip.split('.')))
        return (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8) + parts[3]
    return abs(ip_to_int(first) - ip_to_int(last))


first = '10.0.1.0'
last = '10.0.0.0'

print(ipv4_dif(first, last))
