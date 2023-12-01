import paramiko


def get_new_ip(n):
    base_ip = "10.216."
    fourth_octet = ".1"
    ip = base_ip + str(n) + fourth_octet
    return ip


def get_old_gateway(host_ip):
    for ip in host_ip:
        item = ip[:-1] + '2'
        return item
    
    
def get_version(client, ip_host):
    username = 'adminrm'
    password = 'redmetro.27'
    port = 1221 

    client = paramiko.SSHClient()
    client.connect(ip_host, username=username, password=password, port=port)
    print('Connected to', ip_host)

    stdout, stderr = client.exec_command('cat /etc/version')
    x_version = stdout.read().decode('utf-8').strip()
    error = stderr.read().decode('utf-8')

    if error:
        print('Error:', error)
    else:
        print('Output:', x_version)
        
    return x_version


def get_pass(ip_host):
    username = 'adminrm'
    password = 'redmetro.27'
    port = 1221 
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(ip_host, username=username, password=password, port=port)
        # Si la conexión se establece exitosamente
        client.close()  # Cerrar la conexión después de usarla
        return True
    except paramiko.AuthenticationException:
        # En caso de error de autenticación, agregar a la lista y retornar False
        return False
    except Exception as e:
        # En caso de cualquier otra excepción, manejarla según sea necesario
        print(f"Error en la conexión a {ip_host}: {str(e)}")
        return False
    

def get_version_list(ips):
    x_xm = []
    x_ac = []
    for ip in ips:
        response = get_pass(str(ip))
        if response  is False:
            x_xm.append(ip)
        else:
            x_ac.append(ip)
            
    return {'ac':x_ac, 'airm': x_xm}
