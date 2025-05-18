# # ass 6
# import socket

# # Set the default timeout (in seconds)
# socket.setdefaulttimeout(10.0)

# # Get the current default timeout
# current_timeout = socket.getdefaulttimeout()

# print(f"Default socket timeout is set to: {current_timeout} seconds\n")




# Assignment #6 - Socket Timeout Configuration
# Demonstrates setting and getting default socket timeout

import socket

def demonstrate_socket_timeout():
    # Create a new socket
    test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Show default timeout (usually None initially)
    default_timeout = test_socket.gettimeout()
    print(f"Default socket timeout: {default_timeout}")

    # Set a new timeout (5 seconds)
    new_timeout = 5.0
    test_socket.settimeout(new_timeout)
    print(f"\nSetting new timeout: {new_timeout} seconds")

    # Verify the new timeout
    current_timeout = test_socket.gettimeout()
    print(f"Current socket timeout: {current_timeout} seconds")

    #  Demonstrate timeout behavior (commented safety wrapper)
    print("\nAttempting connection with timeout (will raise if no connection)...")
    try:
        # This will timeout if no connection is established
        test_socket.connect(("10.255.255.1", 80))  # Unreachable IP
    except socket.timeout:
        print("✓ Timeout occurred as expected!")
    except Exception as e:
        print(f"✗ Unexpected error: {type(e).__name__}: {e}")
    finally:
        test_socket.close()
        print("\nSocket closed. Demonstration complete.")
        print("AS PERFORMED BY Sherwin Sarmiento")

if __name__ == "__main__":
    demonstrate_socket_timeout()