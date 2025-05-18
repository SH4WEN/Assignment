# # ass 5
# import socket

# # Sample integers
# host_short = 12345      # 16-bit
# host_long = 123456789   # 32-bit

# # Convert host to network byte order
# net_short = socket.htons(host_short)
# net_long = socket.htonl(host_long)

# # Convert back from network to host byte order
# back_short = socket.ntohs(net_short)
# back_long = socket.ntohl(net_long)

# print(f"Original 16-bit value: {host_short}")
# print(f"Network byte order (16-bit): {net_short}")
# print(f"Back to host (16-bit): {back_short}")
# print()

# print(f"Original 32-bit value: {host_long}")
# print(f"Network byte order (32-bit): {net_long}")
# print(f"Back to host (32-bit): {back_long}\n")



# Assignment #5 - Network Byte Order Conversion
# Demonstrates converting integers between host and network byte order

import socket

def main():
    # Sample integers for demonstration
    host_short = 12345      # 16-bit integer (short)
    host_long = 123456789   # 32-bit integer (long)

    # Conversion to network byte order
    net_short = socket.htons(host_short)
    net_long = socket.htonl(host_long)

    # Conversion back to host byte order
    back_short = socket.ntohs(net_short)
    back_long = socket.ntohl(net_long)

    # Display results with additional hexadecimal representation
    print("16-bit Integer Conversion:")
    print(f"Original host value: {host_short} (0x{host_short:04x})")
    print(f"Network byte order:  {net_short} (0x{net_short:04x})")
    print(f"Converted back:      {back_short} (0x{back_short:04x})")
    print()

    print("32-bit Integer Conversion:")
    print(f"Original host value: {host_long} (0x{host_long:08x})")
    print(f"Network byte order:  {net_long} (0x{net_long:08x})")
    print(f"Converted back:      {back_long} (0x{back_long:08x})")
    print("\nAS PERFORMED BY Sherwin Sarmiento.")

if __name__ == "__main__":
    main()