import socket

def toggle_socket_blocking():
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Check default blocking mode (True = blocking, False = non-blocking)
    default_blocking = sock.getblocking()
    print(f"Default Blocking Mode: {'Blocking' if default_blocking else 'Non-Blocking'}")

    # Set to NON-BLOCKING mode
    sock.setblocking(False)
    print("Socket set to NON-BLOCKING mode")

    # Try a non-blocking operation (will raise an error if no data is ready)
    try:
        data = sock.recv(1024)  # This would fail immediately if no data
        print("Received data (unlikely in this example):", data)
    except socket.error as e:
        print(f"Non-blocking recv() error (expected): {e}")

    # Set back to BLOCKING mode
    sock.setblocking(True)
    print("Socket set back to BLOCKING mode")

    sock.close()

if __name__ == "__main__":
    toggle_socket_blocking()