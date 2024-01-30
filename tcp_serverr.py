import socket
import os

Server_Host = "192.168.1.102"
Server_Port = 8090

server = socket.socket()
server.bind((Server_Host, Server_Port))
print('[+] Server Started')
print('[+] Listening')
server.listen(1)

print('[+] Server   ')

client, addr = server.accept()
print(f'[+]{addr}Client Connected to the server')

commands = {"ipconfig": "Check client ip address",
            "dir": "List directory",
            "tasklist": "Current running tasks list",
            "systeminfo": "Show system information",
            "netstat": "Print network statistics",
            "whoami": "Print current user info"
            }
print("Available commands:")
for key, value in commands.items():
    print(f"{key}: {value}")
while True:
    command = input("\nEnter a command (type 'help' for options):")
    if command == "help":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Available commands:")
        for key, value in commands.items():
            print(f"{key}: {value}")
        continue
    if command not in commands.keys():
        print("Invalid command \n Enter help options:")
        continue
    command = command.encode()
    client.send(command)
    print('\n[+] Sent command to client \n')

    output = client.recv(4096).decode()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Output: {output}")
