import paramiko
from getpass import getpass

# Function to SSH into a VM and execute a command
def ssh_to_vm(hostname, username, password, command):
    try:
        # Create SSH client
        ssh_client = paramiko.SSHClient()
        
        # Automatically add host keys for unknown hosts
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        print(f"\nConnecting to {hostname}...")
        # Establish connection
        ssh_client.connect(hostname=hostname, username=username, password=password)
        print(f"Successfully connected to {hostname}")
        
        # Execute the command
        stdin, stdout, stderr = ssh_client.exec_command(command)
        
        # Read and print output and errors
        output = stdout.read().decode()
        errors = stderr.read().decode()
        
        if output:
            print(f"Output from {hostname}:\n{output}")
        if errors:
            print(f"Errors from {hostname}:\n{errors}")
    
    except paramiko.AuthenticationException:
        print(f"Authentication failed for {hostname}. Please check your credentials.")
    except paramiko.SSHException as ssh_error:
        print(f"SSH error while connecting to {hostname}: {ssh_error}")
    except Exception as e:
        print(f"An error occurred while connecting to {hostname}: {e}")
    finally:
        # Close the connection
        ssh_client.close()
        print(f"Connection to {hostname} closed.")

# Main function for processing multiple VMs
if __name__ == "__main__":
    # List of VMs to connect to
    vm_list = [
        {"hostname": "x.x.x.x", "username": "pt"},
        {"hostname": "x.x.x.x", "username": "root"},
    ]
    
    # Prompt for the SSH password (assuming the same password for all VMs)
    password = getpass("Enter the SSH password: ")
    
    # Command to execute on each VM
    command = ('ping -c 2 8.8.8.8') 
    #input("Enter the command to execute on all VMs: ")
    
    
    # Loop through each VM and execute the SSH command
    for vm in vm_list:
        ssh_to_vm(vm["hostname"], vm["username"], password, command)
