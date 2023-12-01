from api.controllers.mikrotik import set_mkt

ips = '10.116.131.1'
new_ips = '10.216.1.1'
for ip in ips:
    response = set_mkt(ip, new_ips)



'''
ips = ['10.116.131.1', '10.116.134.1', '10.116.138.1']
x_version = get_version_list(ips)
print(x_version['ac'])
print(x_version['airm'])
'''


'''def get_new_ip(n):

    ips = []
    base_ip = "10.216."
    fourth_octet = ".1"

    for i in range(n):  # Cambiado el rango para incluir el tercer octeto desde 16 hasta 116
        ip = base_ip + str(i) + fourth_octet
        ips.append(ip)

    print(ips)
get_new_ip()
'''
'''
def get_new_ip(n):
    base_ip = "10.216."
    fourth_octet = ".1"
    ip = base_ip + str(n) + fourth_octet

    return ip
'''
