import zmq
from random import choices
from string import ascii_uppercase as capitals

ctx = zmq.Context()
socket = ctx.socket(zmq.REQ)

my_name = ''.join(choices(capitals, k=4))
socket.connect('tcp://127.0.0.1:2345')
silence = 0
loops = 0
while True:
	loops += 1
	msg = input('send the msg?')
	socket.send_string(f'{my_name},  loop: {loops}')
	resp = socket.recv_string()
	print(resp)


