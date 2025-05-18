# Assignment #7 - Graceful Socket Error Handling
# Demonstrates comprehensive error handling for socket operations

import socket
import sys
from time import sleep

def socket_operation_with_retry(host="example.com", port=80, max_retries=3):
    """
    Demonstrates socket operations with graceful error handling and retry logic
    """
    retry_count = 0
    last_error = None
    
    while retry_count < max_retries:
        try:
            # Create and configure socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)  # Set reasonable timeout
            
            print(f"\nAttempt {retry_count + 1}/{max_retries}: Connecting to {host}:{port}")
            
            # Attempt connection
            sock.connect((host, port))
            print("✓ Connection established successfully!")
            
            # Simulate data exchange
            try:
                sock.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
                response = sock.recv(1024)
                print("✓ Received response (first 1024 bytes)")
                return True
                
            except socket.error as e:
                print(f"⚠ Data exchange error: {str(e)}")
                last_error = e
                
            finally:
                sock.close()
                print("Socket closed properly")
                return True
                
        except socket.timeout:
            last_error = "Connection timed out"
            print(f"⚠ {last_error}")
            
        except socket.gaierror as e:
            last_error = f"Address-related error: {str(e)}"
            print(f"⚠ {last_error}")
            break  # No point retrying if address is invalid
            
        except ConnectionRefusedError:
            last_error = "Connection refused by server"
            print(f"⚠ {last_error}")
            
        except socket.error as e:
            last_error = f"General socket error: {str(e)}"
            print(f"⚠ {last_error}")
            
        except Exception as e:
            last_error = f"Unexpected error: {type(e).__name__}: {str(e)}"
            print(f"⚠ {last_error}")
            break  # Don't retry on unknown errors
            
        retry_count += 1
        if retry_count < max_retries:
            sleep(2 ** retry_count)  # Exponential backoff
            print("Retrying...")
    
    print(f"\n❌ Operation failed after {max_retries} attempts")
    if last_error:
        print(f"Last error: {last_error}")
    return False

def main():
    print("=== Socket Error Handling Demonstration ===")
    print("Testing connection to different scenarios:\n")
    
    # Test cases
    test_cases = [
        ("example.com", 80),      # Should succeed
        ("nonexistent.domain", 80), # Will fail with gaierror
        ("localhost", 9999),       # Connection refused
        ("192.0.2.1", 80)         # Unreachable address (TEST-NET)
    ]
    
    for host, port in test_cases:
        print(f"\n{'='*50}")
        print(f"TEST CASE: {host}:{port}")
        print(f"{'='*50}")
        
        success = socket_operation_with_retry(host, port)
        print(f"Result: {'SUCCESS' if success else 'FAILURE'}")
        print(f"AS PERFORMED BY Sherwin Sarmiento")

if __name__ == "__main__":
    main()