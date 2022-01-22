import socket
#pada client kita harus mencari ip target serta port target sehingga dapat berkomunikasi
target_host = "0.0.0.0"
target_port = 1010
#sama seperti server, kita membuat socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
#setelah connect dengan target server pada line berikut akan dikirim string "Test"
client.send(b"Alpha")

response = client.recv(4096)

print (response)

# REFERENCE: Chapter 1 - Network Programming Basic