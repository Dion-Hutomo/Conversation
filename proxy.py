import socket

def proxy_handler(client_socket,target_host,target_port):
    remote_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    remote_socket.connect((target_host,target_port))
    
    #pertama diterima message dari client
    local_buffer = client_socket.recv(4096)

    #validasi yang saya gunakan adalah jika string dari client lebih atau sama dengan 5 karakter
    if len(local_buffer) >= 5:
        print ("[<==] Received %d from client" % len(local_buffer))
        #pada line berikut message akan diiteruskan pada server jika true
        remote_socket.send(local_buffer)
        print ("[==>] Sent to remote")    
    elif len(local_buffer) < 5:
        print ("[client] String is less than 5")

    #kemudian akan diterima balasan dari server
    remote_buffer = remote_socket.recv(4096)

    #validasi balasan dari server sama seperti validasi kiriman dari client
    if len(remote_buffer) >= 5:
        print ("[<==] Received %d from server" % len(remote_buffer))
        client_socket.send(remote_buffer)
        print ("[<==] Sent to localhost")
    elif len(remote_buffer) < 5:
        print ("[server] String is less than 5")

    #kemudian koneksi akan ditutup
    client_socket.close()
    remote_socket.close()
    print("[*] No more data. Closing connections")       

def server_loop():
    #bind ip dan port dari client
    bind_ip = "0.0.0.0"
    bind_port = 1010
    #target ip dan port menuju ke server untuk diteruskan
    target_host = "0.0.0.0"
    target_port = 7568
    
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        server.bind((bind_ip,bind_port))
    except:
        print ("[!!] Failed to listen on %s:%d" % (bind_ip,bind_port))
        print ("[!!] Check for other listening sockets or correct permissions.")
    
    print ("[*] Listening on %s:%d"% (bind_ip,bind_port))

    server.listen()

    client_socket, addr = server.accept()

    print ("[==>] Received incoming connection from %s:%d" % (addr[0],addr[1]))

    proxy_handler(client_socket,target_host,target_port)

server_loop()

# REFERENCE: Chapter 2-3 - Socket Network Program Advanced