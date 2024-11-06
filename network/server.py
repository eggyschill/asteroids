import socket

# Creating socket server for rpi5 cnonection

HOST = "127.0.0.1" #Creating host, standard loopback interface address (localhost)
PORT = 44444

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server is listening")

    conn, addr = s.accept()
    print(f"Connection accepted by {addr}")

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                print("No data received, closing connection")
                break
            print(f"Received data: {data.decode()}") 
            conn.sendall(data)

