import paramiko
from getpass import getpass
vm_pass = getpass("Enterrootpassword: ")

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh_client.connect(hostname="x.x.x.x", username='root', password=vm_pass)
print("Connected successfully!")

stdin, stdout, stderr = ssh_client.exec_command( 'ping -c 2 8.8.8.8')
output = stdout.read().decode()
print("Command output:")
print(output)

    # Close the SSH connection
ssh_client.close()
print("Connection closed.")