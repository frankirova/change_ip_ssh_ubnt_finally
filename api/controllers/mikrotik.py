import routeros_api
import os

from dotenv import load_dotenv

def connect_to_mikrotik():
    try:
        load_dotenv()
        IP_MIKROTIK = os.getenv('IP_MIKROTIK')
        PASS_MIKROTIK = os.getenv('PASS_MIKROTIK')
        USER_MIKROTIK = os.getenv('USER_MIKROTIK')
        # conexion con la api Miktoik
        connection = routeros_api.RouterOsApiPool(IP_MIKROTIK, username=USER_MIKROTIK, password=PASS_MIKROTIK, plaintext_login=True)
        api = connection.get_api()
        return api
    except Exception as e:
        # Manejo de la excepción
        print("Ocurrió un error:", str(e))
        ##raise HTTPException(status_code=500, detail='Error en mikrotik')

def get_ip_addr(api, range_ip):

    #ip_addresses = api.get_resource('/ip/address').get()
    ip_addresses = api.get_resource('/ip/address').get()
    filtered_ip_addresses = [ip for ip in ip_addresses if range_ip in ip['address']]

    ip_addr = []
    for ip in filtered_ip_addresses:
        item = (ip['address'])
        ip_addr.append(item[:-3].replace('2','1'))
    return ip_addr


def get_ip(ip_addr):
    ip_piola = []
    for ip in ip_addr:
        item = ip.replace('2','1')
        ip_piola.append(item)


def set_mkt(ip, new_ip):
    api = connect_to_mikrotik()

    ##queues
    old_target = ip[:-1] + '0' + '/30'
    print('old_target: ' + old_target)

    new_ip_queues = new_ip[:-1] + '0/30'
    print(new_ip_queues)

    id_queue = api.get_resource('/queue/simple').get(target = old_target)[0]['id']
    print(id_queue)

    api.get_resource('/queue/simple').set(id = id_queue, target = new_ip_queues)

    ##addr
    old_addr = ip[:-1] + '2/30'
    print(old_addr)

    addr = new_ip[:-1] + '2/30'
    print(addr)

    network = new_ip[:-1] + '0'
    print(network)

    id_addr = api.get_resource('/ip/address').get(address = old_addr)[0]['id']
    print(id_addr)

    api.get_resource('/ip/address').set(id = id_addr, address = addr, network=network, interface='ether5')

    ##firewall_addr_list
    id_firewall_addr_list = api.get_resource('/ip/firewall/address-list').get(address = ip)[0]['id']
    print(id_firewall_addr_list)

    api.get_resource('/ip/firewall/address-list').set(id = id_firewall_addr_list, address = new_ip)