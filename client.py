import platform,socket,cpuinfo,psutil

nome_usuario = input("Nome do usuário da máquina: ")

cpu = cpuinfo.get_cpu_info()
win = platform.platform() + ' ' + platform.win32_edition()
nome_maquina = socket.gethostname()
ip_maquina = socket.gethostbyname(nome_maquina)
nome_processador = cpu['brand_raw']
memoria = str(round(psutil.virtual_memory().total / (1024.0 **3))) + 'GB'

hdd = psutil.disk_usage('/')
hd = hdd.total / (2**30)

# arquivo = open(f'{nome_usuario}.txt', 'w')
# arquivo.write('Nome usuario: ' + nome_usuario + '\n' )
# arquivo.write('Nome maquina: ' + nome_maquina + '\n' )
# arquivo.write('Processador: ' + nome_processador + '\n' )
# arquivo.write('Win: ' + win + '\n' )
# arquivo.write('Memoria: ' + memoria + '\n' )
# arquivo.write("HD: " + '\n' )
# arquivo.write('Ip: ' + ip_maquina + '\n' )
# arquivo.close()

print('Nome usuario: ' + nome_usuario + '\n' )
print('Nome maquina: ' + nome_maquina + '\n' )
print('Processador: ' + nome_processador + '\n' )
print('Win: ' + win + '\n' )
print('Memoria: ' + memoria + '\n' )
print("HD: " + '\n' )
print('Ip: ' + ip_maquina + '\n' )