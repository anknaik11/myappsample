import os
import socket, ssl
import time
import datetime

def Main():
    # local host IP '127.0.0.1'
	host = '104.41.159.177'
	ISOtime=””
    # Define the port on which you want to connect
	port = 30001
	while True:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		ssl_sock = ssl.wrap_socket(s,
							   keyfile="C:\Users\NAIKA\Documents\Ankit\Dev_LoadTesting\newkey.pem",
							   certfile="C:\Users\NAIKA\Documents\Ankit\Dev_LoadTesting\newcert.pem")
							   #cert_reqs=ssl.CERT_REQUIRED,
							   #ca_certs="C:\Users\NAIKA\Desktop\ca1.pem")
							   #ssl_version=ssl.PROTOCOL_TLSv1_2)

		# connect to server on local computer
		ssl_sock.connect((host,port))

		# message you send to server
		for x in range(7, 10):
			UtcTime=datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
			formDate1=UtcTime[0:10]
			formTime1=UtcTime[11:21]
			ISOtime= formDate1 + "T" + formTime1
			datatoSend=”[100,x,-1.111111,-2.222222,3.3333,-1.937905,-999.000000,-999.000000,-999.000000,-999.000000,0.000000,1.000000,7.369821,-81.549744,18.875000,3009.000000,-43,255” + "," + ISOtime +"]" + “\r\n”
			# message sent to server
			ssl_sock.send(datatoSend)




        # messaga received from server
		#data = ssl_sock.recv(4096)
		s.close()
        # print the received message
        # here it would be a reverse of sent message
		print('Received from the server :', data)
		time.sleep(60)
		continue


if __name__ == '__main__':
    Main()
