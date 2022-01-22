#Import socket supaya dapat membuat socket object
import socket

#pilih ip dan port yang random untuk dijadikan server
bind_ip = "0.0.0.0"
bind_port = 7568

#membuat socket object dengan socket dan AF_INET dan SOCK_STREAM(Karena ini TCP pakai SOCK_STREAM) serta bind IP dan PORT
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
#pada line ini kita listen dari client yang mengirim message
server.listen()

print ("Listening on %s:%d" % (bind_ip,bind_port))

client, addr = server.accept()
req = client.recv(4096)

print ("Received: %s"% req)
#setelah menerima message dari client, server akan send message ACK!, pada kode ini ditambahkan b supaya dapat diterima sebagai string
#kemudian kita tutup kembali servernya
client.send(b"Omega")
client.close() 

print ("Accepted connection from: %s:%d"%(addr[0],addr[1]))

# REFERENCE: Chapter 1 - Network Programming Basic
