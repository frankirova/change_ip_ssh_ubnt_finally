import paramiko
from api.controllers.helpers import get_new_ip, get_old_gateway, get_version_list
from api.controllers.mikrotik import connect_to_mikrotik, get_ip_addr, set_mkt

# Lista de direcciones IP de los dispositivos
n = 10
api = connect_to_mikrotik()
ip_addr = get_ip_addr(api, '10.116')
ip_addr_216 = get_ip_addr(api, '10.216')
x_version = get_version_list(ip_addr)
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
        f'sed -i "s/netconf.1.ip={ip}/netconf.1.ip={new_ip}/g" /tmp/system.cfg',
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

##intento6
'''
import paramiko

# Información de conexión SSH
username = 'adminrm'
password = 'redmetro.27'
port = 1221
##new_ip = ['10.216.1.1', '10.216.2.1', '10.216.3.1']
new_ip = '10.216.1.1'
device_ip = '10.116.131.1'
# Lista de direcciones IP de los dispositivos
##device_ips = ['192.168.1.10', '10.116.', '10.116.138.1']  # Agrega las direcciones IP de tus dispositivos aquí

# Comandos para cambiar la dirección IP (ejemplo para dispositivos UniFi)
commands = [
    f'configure',
    f'set interfaces ethernet br0 address {new_ip}',
    f'commit',
    f'save',
    f'exit'
]
##for ip in device_ips:
client = paramiko.SSHClient()
print(client)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
        # Inicia una conexión SSH
        client.connect(device_ip, username=username, password=password, port=port)

        # Ejecuta los comandos para cambiar la dirección IP
        for command in commands:
            stdin, stdout, stderr = client.exec_command(command)
            # Puedes agregar lógica para manejar las respuestas o errores aquí

        print(f'Dirección IP cambiada en el dispositivo {device_ip}')

except paramiko.AuthenticationException:
    print(f'Error de autenticación en el dispositivo {device_ip}')
except paramiko.SSHException as e:
    print(f'Error SSH en el dispositivo {device_ip}: {e}')
except Exception as e:
    print(f'Error inesperado en el dispositivo {device_ip}: {e}')
##finally:
    #if client is not None:
     #   client.close()
'''

##intento5
'''
import paramiko

ip_host = '10.116.131.1'
port = 1221
username = 'adminrm'
password = 'redmetro.27'

file_path = '/tmp/system.cfg'
new_cfg = 'netconf.3.ip=10.216.1.1'

try:
    with paramiko.SSHClient() as client_ssh:
        client_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        client_ssh.connect(ip_host, port, username, password)
        print('Conexión establecida')

        stdin, stdout, stderr = client_ssh.exec_command(f'cat {file_path}')
        current_content = stdout.read().decode()
        print(current_content + 'hola')
        new_content = current_content + '\n' + new_cfg

#        with client_ssh.open_sftp() as sftp:
 #           with sftp.file(file_path, 'w') as remote_file:
  #              remote_file.write(new_content)
   #         print('Archivo modificado y guardado')

except paramiko.AuthenticationException:
    print('Error de autenticación')

except paramiko.SSHException as e:
    print(f'Error SSH: {e}')

except Exception as e:
    print(f'Error inesperado: {e}')
'''

#intento 4
'''
import paramiko

##datos
ip_host = '10.116.131.1'
port = 1221
username = 'adminrm'
password = 'redmetro.27'

##ruta al archivo
file_path = '/tmp/system.cfg'

##datos a añadir o modificar
new_cfg = 'netconf.3.ip=10.216.1.1'

client_ssh= None
try:
    ##conexion
    client_ssh = paramiko.SSHClient()
    client_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client_ssh.connect(ip_host, port, username, password)
    print('me conecte')
    ##leer contenido actual

    stdin, stdout, stderr = client_ssh.exec_command(f'cat {file_path}', timeout=10)
    contain = stdout.read().decode('utf-8')

    ##agrega o modificar
    new_cfg_completo = contain + new_cfg

    ##escribir en el archivo
    commands=[
        f'echo {new_cfg_completo} > {file_path}',
        'save'
    ]
    for com in commands:
        stdin, stdout, stderr = client_ssh.exec_command(com, timeout=10)

    ##cerramos conexion
    client_ssh.close()
    print('Archivo modificado con exito')

except paramiko.AuthenticationException:
    print('err auth')

except paramiko.SSHException as e:
    print(f'err SSH: {e}')

except Exception as e:
    print(f'err inesperado: {e}')
'''

#intento 3
'''
import paramiko
import time
from api.controllers.helpers import get_new_ip
from api.controllers.ubnt import connect_ssh, find_version
from api.controllers.mikrotik import connect_to_mikrotik, get_ip_addr

# Función para realizar operaciones SSH
def perform_ssh_operations(ip_host, new_ip, new_gateway):
    ssh_client = connect_ssh(ip_host)
    
    stdin, stdout, stderr = ssh_client.exec_command('cat /etc/version')
    x_version = stdout.read().decode('utf-8').strip()
    print(x_version)

    if 'XM' in x_version:
        commands = [
            f"ifconfig ath0 {new_ip} netmask 255.255.255.0",
            f'route add default gw {new_gateway}'
        ]
    #else:
    if 'WA' in x_version:
        commands = [
            f"ifconfig br0 {new_ip} netmask 255.255.255.0",
            f'route add default gw {new_gateway}'
        ]

    for command in commands:
        stdin, stdout, stderr = ssh_client.exec_command(command)
    
    ssh_client.close()

n = 1
api = connect_to_mikrotik()
ip_addr = get_ip_addr(api)

iterations = len(ip_addr)  # Número de iteraciones
delay_between_iterations = 5  # Tiempo en segundos entre cada iteración

for ip_host in ip_addr:
    new_ip = get_new_ip(n)
    new_gateway = new_ip[:-1] + '2'
    print(ip_host)
    print(new_gateway)
    print(new_ip)
    print(n)
    
    perform_ssh_operations(ip_host, new_ip, new_gateway)
    
    if n < iterations:
        print(f"Esperando {delay_between_iterations} segundos antes de la siguiente iteración...")
        time.sleep(delay_between_iterations)
    
    n += 1
'''




##CODIGO INTENTO 2
'''
import paramiko
from api.controllers.helpers import get_new_ip
from api.controllers.ubnt import connect_ssh
from api.controllers.mikrotik import connect_to_mikrotik, get_ip_addr

n = 1
api = connect_to_mikrotik()
ip_addr = get_ip_addr(api)

for ip_host in ip_addr:
    new_ip = get_new_ip(n)
    new_gateway = new_ip[:-1] + '2'
    print(ip_host)
    print(new_gateway)
    print(new_ip)
    print(n)
    ssh_client = connect_ssh(ip_host)
    #ssh_client.connect(ip_host, port, username, password)
    stdin, stdout, stderr = ssh_client.exec_command('cat /etc/version')
    #x_version = stdout.read().decode('utf-8')
    x_version = stdout.read().decode('utf-8').strip()
    print(x_version)
    #data = find_version(ssh_client)
    if 'XM' in x_version:
        commands = [
            f"ifconfig ath0 {new_ip} netmask 255.255.255.0",
            f'route add default gw {new_gateway}',
            'save'
            ]
        for command in commands:
                stdin, stdout, stderr = ssh_client.exec_command(command)
    #else:
    if 'WA' in x_version:
        commands = [
            f"ifconfig br0 {new_ip} netmask 255.255.255.0",
            f'route add default gw {new_gateway}',
            'save'
            ]
        for command in commands:
            try:
                stdin, stdout, stderr = ssh_client.exec_command(command, timeout=10)  # Agrega un tiempo de espera de 10 segundos
        # Agrega mensajes de depuración aquí
            except paramiko.SSHException as e:
                print("Error al ejecutar el comando:", e)

    ssh_client.close()
    n += 1
'''


#CODIGO INTENTO 1#
'''
# Resto de tu código...
#ips news
new_gateway_host = []
new_ips = ['10.216.16.1', '10.216.17.1']

for ip in new_ips:
    item = ip[:-1] + '2'
    new_gateway_host.append(item)

ip_host = ['10.116.134.1', '192.168.116.201']

#datos
port = 1221
username = 'adminrm'
password = 'redmetro.27'

#instancia ssh client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

x_air_max = []
x_ac = []
for ip in ip_host:
    try:
        ssh_client.connect(ip, port, username, password)
        print('Conexión exitosa')
        stdin, stdout, stderr = ssh_client.exec_command('cat /etc/version')
        data = stdout.read().decode('utf-8')

        if 'XM' in data:
            x_air_max.append(ip)
        if 'XW' in data:
            x_air_max.append(ip)
        if 'WA' in data:
            x_ac.append(ip)

    except Exception as e:
        print(f'Error en la conexión o configuración para el host {ip}')
    finally:
        ssh_client.close()

print(x_air_max)
print(x_ac)
'''



'''
# Asegurémonos de que las tres listas tengan la misma cantidad de elementos
if len(ip_host) == len(new_ips) == len(new_gateway_host):
    for i in range(len(ip_host)):
        current_host_ip = ip_host[i]
        new_host_ip = new_ips[i]
        new_host_gateway = new_gateway_host[i]

        try:
            ssh_client.connect(current_host_ip, port, username, password)
            print(f'Conexión exitosa con el host {current_host_ip}')

            commands = [
                f"ifconfig ath0 {new_host_ip} netmask 255.255.255.0",
                f'route add default gw {new_host_gateway}'
            ]

            for command in commands:
                stdin, stdout, stderr = ssh_client.exec_command(command)

            print(f'Configuración cambiada para el host {current_host_ip}')
        except Exception as e:
            print(f'Error en la conexión o configuración para el host {current_host_ip}')
        finally:
            ssh_client.close()
else:
    print("Las listas no tienen la misma cantidad de elementos")

'''

