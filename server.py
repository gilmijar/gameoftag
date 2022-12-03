import zmq
import time

ctx = zmq.Context()
socket = ctx.socket(zmq.ROUTER)

socket.bind('tcp://127.0.0.1:2345')
clients = {}
BLANK = b''
while True:
	for _ in (0,1):
		msg = socket.recv_multipart()
		clients[msg[0]] = msg[2].decode('utf-8')
	print(clients)
	for client, msg in clients.items():
		socket.send_multipart([client, BLANK, f'{msg} <--- reply'.encode()])
	time.sleep(0.005)
