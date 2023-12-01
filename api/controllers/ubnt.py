import paramiko
from api.controllers.helpers import get_new_ip, get_old_gateway, get_version_list
from api.controllers.mikrotik import connect_to_mikrotik, get_ip_addr, set_mkt

def connect_ssh(ip_host):

    #datos
    port = 1221
    username = 'adminrm'
    password = 'redmetro.27'

    #instancia ssh client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(ip_host, port, username, password)

    return ssh_client

#def find_version(ssh_client):
    stdout = ssh_client.exec_command('cat /etc/version')
    data = stdout.read().decode()
    return data

#def change_ip_ac(ssh_client, ip_host, count):
    #conexion al equipo
    try: 
        connect_ssh(ip_host)
        new_ip = get_new_ip(count)
        new_gateway = new_ip.replace('2', '1')

        #ejecutar comando
        #command = f"set interfaces ethernet br0 address {new_ip}"
        commands = [
            f'route add default gw {new_gateway}'
            f"ifconfig br0 {new_ip} netmask 255.255.255.0",
            ]
        for command in commands:
            stdin, stdout, stderr = ssh_client.exec_command(command)
        print('IP cambiada')
    except Exception as e:
        print('error en la conexion o config')

'''
def renum_ac(ip_addr_216, n):
   
    x_version = get_version_list(ip_addr_216)
    print(x_version)

    # Por cada ip en la lista ejecuto la accion
    for ip in x_version['ac']:
        # Información de conexión SSH
        username = 'adminrm'
        password = 'redmetro.27'
        port = 1221
        new_ip = get_new_ip(n)
        new_gateway = new_ip[:-1] + '2'
        old_gateway = get_old_gateway(ip)

        # Comandos para cambiar la dirección IP 
        commands = [
            f'sed -i "s/netconf.3.ip={ip}/netconf.3.ip={new_ip}/g" /tmp/system.cfg',
            '\n',
            f'sed -i "s/route.1.gateway={old_gateway}/route.1.gateway={new_gateway}/g" /tmp/system.cfg',
            '\n',
            'save',
            '\n',
            'cfgmtd -f /tmp/system.cfg -w',
            '\n',
            'reboot',
            '\n',
        ]
        client = paramiko.SSHClient()
        print(client)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(ip, username=username, password=password, port=port)
            print('Connected to', ip)
            
            for command in commands:
                print('Executing command:', command)
                stdin, stdout, stderr = client.exec_command(command, timeout=10)
                # Leer la salida y errores si es necesario
                output = stdout.read().decode('utf-8')
                error = stderr.read().decode('utf-8')
                
                if error:
                    print('Error:', error)
                else:
                    print('Output:', output)
            n += 1    
            print(f'Configuration changed on device {ip}')

        except paramiko.AuthenticationException:
            print(f'Error de autenticación en el dispositivo {ip}')
        except paramiko.SSHException as e:
            print(f'Error SSH en el dispositivo {ip}: {e}')
        except Exception as e:
            print(f'Error inesperado en el dispositivo {ip}: {e}')
        
        try:
            set_mkt(ip, new_ip)
        except Exception as e:
            print(f'Error inesperado en el dispositivo {ip}: {e}')

def renum_airm(ip_addr_216, n):
   
    x_version = get_version_list(ip_addr_216)
    print(x_version)

    # Por cada ip en la lista ejecuto la accion
    for ip in x_version['airm']:
        # Información de conexión SSH
        username = 'adminrm'
        password = 'bonsai'
        port = 1221
        new_ip = get_new_ip(n)
        new_gateway = new_ip[:-1] + '2'
        old_gateway = get_old_gateway(ip)

        # Comandos para cambiar la dirección IP 
        commands = [
            f'sed -i "s/netconf.3.ip={ip}/netconf.3.ip={new_ip}/g" /tmp/system.cfg',
            '\n',
            f'sed -i "s/route.1.gateway={old_gateway}/route.1.gateway={new_gateway}/g" /tmp/system.cfg',
            '\n',
            'save',
            '\n',
            'cfgmtd -f /tmp/system.cfg -w',
            '\n',
            'reboot',
            '\n',
        ]
        client = paramiko.SSHClient()
        print(client)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(ip, username=username, password=password, port=port)
            print('Connected to', ip)
            
            for command in commands:
                print('Executing command:', command)
                stdin, stdout, stderr = client.exec_command(command, timeout=10)
                # Leer la salida y errores si es necesario
                output = stdout.read().decode('utf-8')
                error = stderr.read().decode('utf-8')
                
                if error:
                    print('Error:', error)
                else:
                    print('Output:', output)
            n += 1    
            print(f'Configuration changed on device {ip}')

        except paramiko.AuthenticationException:
            print(f'Error de autenticación en el dispositivo {ip}')
        except paramiko.SSHException as e:
            print(f'Error SSH en el dispositivo {ip}: {e}')
        except Exception as e:
            print(f'Error inesperado en el dispositivo {ip}: {e}')
        
        try:
            set_mkt(ip, new_ip)
        except Exception as e:
            print(f'Error inesperado en el dispositivo {ip}: {e}')
'''











'''
#ips news
new_gateway_host = []
new_ips = [
    '10.216.16.1', '10.216.17.1', '10.216.18.1', '10.216.19.1', '10.216.20.1', '10.216.21.1', '10.216.22.1', '10.216.23.1', '10.216.24.1', '10.216.25.1', '10.216.26.1', '10.216.27.1', '10.216.28.1', '10.216.29.1', '10.216.30.1', '10.216.31.1', '10.216.32.1', '10.216.33.1', '10.216.34.1', '10.216.35.1', '10.216.36.1', '10.216.37.1', '10.216.38.1', '10.216.39.1', '10.216.40.1', '10.216.41.1', '10.216.42.1', '10.216.43.1', '10.216.44.1', '10.216.45.1', '10.216.46.1', '10.216.47.1', '10.216.48.1', '10.216.49.1', '10.216.50.1', '10.216.51.1', '10.216.52.1', '10.216.53.1', '10.216.54.1', '10.216.55.1', '10.216.56.1', '10.216.57.1', '10.216.58.1', '10.216.59.1', '10.216.60.1', '10.216.61.1', '10.216.62.1', '10.216.63.1', '10.216.64.1', '10.216.65.1', '10.216.66.1', '10.216.67.1', '10.216.68.1', '10.216.69.1', '10.216.70.1', '10.216.71.1', '10.216.72.1', '10.216.73.1', '10.216.74.1', '10.216.75.1', '10.216.76.1', '10.216.77.1', '10.216.78.1', '10.216.79.1', '10.216.80.1', '10.216.81.1', '10.216.82.1', '10.216.83.1', '10.216.84.1', '10.216.85.1', '10.216.86.1', '10.216.87.1', '10.216.88.1', '10.216.89.1', '10.216.90.1', '10.216.91.1', '10.216.92.1', '10.216.93.1', '10.216.94.1', '10.216.95.1', '10.216.96.1', '10.216.97.1', '10.216.98.1', '10.216.99.1', '10.216.100.1', '10.216.101.1', '10.216.102.1', '10.216.103.1', '10.216.104.1', '10.216.105.1', '10.216.106.1', '10.216.107.1', '10.216.108.1', '10.216.109.1', '10.216.110.1', '10.216.111.1', '10.216.112.1', '10.216.113.1', '10.216.114.1', '10.216.115.1', '10.216.116.1'
]
new_ips = ['10.216.16.1', '10.216.17.1', '10.216.18.1', '10.216.19.1',]
for ip in new_ips:
    item = ip[:-1] + '2'
    new_gateway_host.append(item)
print(new_gateway_host)

##ip_host = ['10.116.131.1', '10.116.133.1', '10.116.134.1', '10.116.138.1', '10.116.137.1', '10.116.139.1', '10.116.141.1', '10.116.141.1', '10.116.143.1', '10.116.145.1', '10.116.146.1', '10.116.150.1', '10.116.151.1', '10.116.153.1', '10.116.154.1', '10.116.155.1', '10.116.156.1', '10.116.157.1', '10.116.158.1', '10.116.160.1', '10.116.161.1', '10.116.161.1', '10.116.167.1', '10.116.171.1', '10.116.173.1', '10.116.174.1', '10.116.176.1', '10.116.177.1', '10.116.179.1', '10.116.178.1', '10.116.180.1', '10.116.181.1', '10.116.181.1', '10.116.183.1', '10.116.184.1', '10.116.189.1', '10.116.191.1', '10.116.191.1', '10.116.193.1', '10.116.194.1', '10.116.195.1', '10.116.196.1', '10.116.197.1', '10.116.198.1', '10.116.199.1', '10.116.100.1', '10.116.101.1', '10.116.101.1', '10.116.103.1', '10.116.104.1', '10.116.105.1', '10.116.106.1', '10.116.107.1', '10.116.108.1', '10.116.109.1', '10.116.110.1', '10.116.111.1', '10.116.111.1', '10.116.113.1', '10.116.114.1', '10.116.115.1', '10.116.117.1', '10.116.119.1', '10.116.118.1', '10.116.110.1', '10.116.111.1', '10.116.111.1', '10.116.113.1', '10.116.114.1', '10.116.115.1', '10.116.116.1', '10.116.117.1', '10.116.118.1', '10.116.130.1', '10.116.131.1', '10.116.131.1', '10.116.133.1', '10.116.134.1', '10.116.135.1', '10.116.136.1', '10.116.140.1', '10.116.143.1', '10.116.144.1', '10.116.145.1', '10.116.146.1', '10.116.147.1', '10.116.148.1', '10.116.149.1', '10.116.150.1', '10.116.151.1']
ip_host = ['10.116.131.1', '10.116.133.1', '10.116.134.1','10.116.138.1']

#datos
hostname = '192.168.2.250'
port = 22
username = 'adminrm'
password = 'redmetro.27'

#nueva direccion IP
new_ip = '192.168.2.254'
new_gateway = '192.168.2.1'

#instancia ssh client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#conexion al equipo
try: 
    ssh_client.connect(hostname, port, username, password)
    print('conexion exitosa')

    #ejecutar comando
    #command = f"set interfaces ethernet br0 address {new_ip}"
    commands = [
        f"ifconfig br0 {new_ip} netmask 255.255.255.0",
        f'route add default gw {new_gateway}'
        ]
    for command in commands:
        stdin, stdout, stderr = ssh_client.exec_command(command)

    print('IP cambiada')
except Exception as e:
    print('error en la conexion o config')
finally:
    #cerrar conexion ssh
    ssh_client.close()
'''

