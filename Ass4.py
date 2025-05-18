import socket

def find_service_name(port, protocol):
    """
    Find the service name for a given port and protocol.
    
    Args:
        port (int): The port number to look up
        protocol (str): The protocol ('tcp' or 'udp')
        
    Returns:
        str: The service name or an error message if not found
    """
    try:
        protocol = protocol.lower()
        if protocol not in ['tcp', 'udp']:
            return "Protocol must be either 'tcp' or 'udp'"
            
        service_name = socket.getservbyport(port, protocol)
        return f"Port {port}/{protocol.upper()} is associated with service: {service_name}"
    
    except socket.error as e:
        return f"No service found for port {port}/{protocol.upper()}: {str(e)}"

# Example usage
if __name__ == "__main__":
    print("Service Name Finder by Port and Protocol")
    print("----------------------------------------")
    
    try:
        port = int(input("Enter the port number: "))
        protocol = input("Enter the protocol (tcp/udp): ").strip().lower()
        
        result = find_service_name(port, protocol)
        print(result)
    except ValueError:
        print("Error: Port must be a valid integer.")