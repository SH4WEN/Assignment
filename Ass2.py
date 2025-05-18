# CODE EDITING, RUN AND EXECUTION FOR -  Retrieving a remote machine's IP address
# ASSIGN 2
import socket

# Function to get the IP address of a given domain
remote_host = 'www.youtube.com'

try:
   # Get the IP address of the remote host
    ip_address = socket.gethostbyname(remote_host)
    print(f"IP address of {remote_host}: {ip_address}")
except socket.gaierror:
    print(f"Failed to resolve host: {remote_host}")
# Output the desired format
#print(f"AS PERFORMED BY Sarmiento Sherwin")
print(f"AS PERFORMED BY Sarmiento Sherwin")


