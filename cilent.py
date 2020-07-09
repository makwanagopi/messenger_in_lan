from socket import *
import threading
import sys
from playsound import playsound

FLAG = False

name = input('Enter Your name:')

def send_to_server(closck):
	global FLAG
	while True:
		if FLAG == True:
			break
		send_msg =name + ": "+ input('')
		closck.sendall(send_msg.encode())

def recv_from_server(closck):
	global FLAG 
	while True:
		data = closck.recv(1024).decode()
		if data == 'q':
			print('Closing connection')
			FLAG = True
			break

		print(name + data)
	playsound('alert-signal.wav')

def main():
	threads = []
	HOST = '192.168.1.9'
	PORT = 6789


	clienctSocket = socket(AF_INET,SOCK_STREAM)

	clienctSocket.connect((HOST,PORT))
	print(name + ',You are connected to a chat server\n')


	t_send = threading.Thread(target=send_to_server,args=(clienctSocket,))
	t_rcv = threading.Thread(target=recv_from_server,args=(clienctSocket,))


	threads.append(t_send)
	threads.append(t_rcv)

	
	t_send.start()
	t_rcv.start()

	t_send.join()
	t_rcv.join()


	print('EXITING ')

	sys.exit()

if __name__ == '__main__':
	main()
