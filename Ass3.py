# IPv4 Address Conversion Tool
# Converts an IPv4 address to binary, octal, hexadecimal, and packed integer formats.
# ASSIGN 3 - Sherwin Sarmiento

import socket
import struct

def convert_ipv4(ip):
    try:
        # Validate IP format
        socket.inet_aton(ip)  # Raises error for invalid IPs
        
        octets = ip.split('.')
        
        # Binary: Pad each octet to 8 bits (e.g., 192 -> '11000000')
        binary = '.'.join(f"{int(octet):08b}" for octet in octets)
        
        # Octal: Pad each octet to 3 digits (e.g., 168 -> '250')
        octal = '.'.join(f"{int(octet):03o}" for octet in octets)
        
        # Hex: Pad each octet to 2 uppercase hex digits (e.g., 1 -> '01')
        hexa = '.'.join(f"{int(octet):02X}" for octet in octets)
        
        # Packed 32-bit integer (network byte order)
        packed_ip = struct.unpack("!I", socket.inet_aton(ip))[0]
        
        return {
            "Original IP": ip,
            "Binary": binary,
            "Octal": octal,
            "Hexadecimal": hexa,
            "Integer": packed_ip
        }
    except socket.error:
        raise ValueError("Invalid IPv4 address format")

if __name__ == "__main__":
    # Example usage
    ip = "192.168.1.2"  # Replace with any IPv4 address
    try:
        results = convert_ipv4(ip)
        for key, value in results.items():
            print(f"{key:<12}: {value}")
        print("\nAS PERFORMED BY Sherwin Sarmiento")
    except ValueError as e:
        print(f"Error: {e}")