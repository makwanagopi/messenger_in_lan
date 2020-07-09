from socket import *
import threading
import sys
from playsound import playsound

FLAG = False

def recv_from_cilent(conn):
	global FLAG
	try:
		while True:
			if FLAG == True:
				break
			message = conn.recv(1024).decode()

			if message == 'q':
				conn.send('q'.encode())
				print('closing connection')
				conn.close()
				FLAG = True
				break
			print('Cilent :' + message)
		playsound('alert-signal.wav')
	except:
		conn.close()

def send_to_cilent(conn):
	global FLAG
	try:
		while True:
			if FLAG == True:
				break
			send_msg = input('')
			if send_msg == 'q':
				conn.send('q'.encode())
				print('closing connection')
				conn.close()
				FLAG = True
				break
			conn.send(send_msg.encode())
	except:

		conn.close()
def main():
	threads = []
	global FLAG

	HOST = '192.168.1.9'
	serverport = 6789
	serverSocket = socket(AF_INET,SOCK_STREAM)

	serverSocket.bind((HOST,serverport))
	serverSocket.listen(1)

	print('the chat server is ready to connect the cilent')

	connectionSocket,addr = serverSocket.accept()

	print('Server is connected with a cilent chat\n')

	t_rcv = threading.Thread(target=recv_from_cilent,args =(connectionSocket,))
	t_send = threading.Thread(target=send_to_cilent,args =(connectionSocket,))


	threads.append(t_rcv)
	threads.append(t_send)

	t_rcv.start()
	t_send.start()

	t_rcv.join()
	t_send.join()

	print('EXITING ')
	serverSocket.close()

	sys.exit()


if __name__ == '__main__':
	main()





