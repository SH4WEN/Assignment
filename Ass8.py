# CODE EDITING, RUN AND EXECUTION FOR - Modifying a socket's send/receive buffer size
#  ASSIGN 8


import socket

def modify_socket_buffers():
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Default buffer sizes
    default_send = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    default_recv = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print(f"Default Send Buffer Size: {default_send} bytes")
    print(f"Default Receive Buffer Size: {default_recv} bytes")

    # Set new buffer sizes (e.g., 8192 bytes)
    new_size = 8192
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, new_size)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, new_size)

    # Verify changes
    updated_send = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    updated_recv = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print(f"Updated Send Buffer Size: {updated_send} bytes")
    print(f"Updated Receive Buffer Size: {updated_recv} bytes")
    print(f'AS PERFORMED BY Sherwin Sarmiento')

    sock.close()

if __name__ == "__main__":
    modify_socket_buffers()