import socket
import pickle

def receive_array_udp(ip='127.0.0.1', port=12345):
    """
    Receives a Python array over UDP.
    :param ip: The IP address to bind to.
    :param port: The port to listen on.
    """
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    print(f"Listening for data on {ip}:{port}...")
    # Receive data (max buffer size 4096 bytes)
    data, addr = sock.recvfrom(4096)
    print(f"Received data from {addr}")
    # Deserialize the array using pickle
    array = pickle.loads(data)
    print(f"Received array: {array}")
    # Close the socket
    sock.close()
    return array

def send_array_udp(array, ip='10.192.202.1', port=5005):
    """
    Sends a Python array over UDP.
    :param array: The array to send.
    :param ip: The IP address of the receiving end.
    :param port: The port of the receiving end.
    """
    # Serialize the array using pickle
    # array = [0,1,1,1,1,0]
    serialized_data = pickle.dumps(array)
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Send the serialized data
    sock.sendto(serialized_data, (ip, port))
    print(f"Sent array: {array} to {ip}:{port}")
    # Close the socket
    sock.close()

# Example array to send

if __name__ == '__main__':
    # Start receiving
    received_array = receive_array_udp()

    array_to_send = [1, 2, 3, 4, 5]
    send_array_udp(array_to_send)