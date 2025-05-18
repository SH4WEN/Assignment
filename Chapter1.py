# CHAPTER 1- Sockets, IPv4, and Simple Client Server Programming - CODE INSPECTIONS RUN sample 
#
import socket

# Function to get the IP address of a given domain
def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        return f"Error resolving domain: {e}"

# Main function
def main():
    domain = "www.youtube.com"
    ip_address = get_ip_address(domain)

    # Output the desired format
    print(f"IP address of {domain}: {ip_address}")
    print(f"AS PERFORMED BY Sarmiento Sherwin")
    print(f"BSIT-3D-SD ")


# Run the main function
if __name__ == "__main__":
    main()