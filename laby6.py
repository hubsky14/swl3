import socket
	import time 
	import operator
	

	operates = { '+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
	

	

	def computeRPN(wyr):
	    stack = []
	    for sign in wyr:
	        if set(sign).issubset(set("0123456789.")):
	            stack.append(float(sign))
	        elif sign in operates:
	            a = stack.pop()
	            b = stack.pop()
	            op = operates[sign]
	            stack.append(op(b,a))
	    return stack
	

	

	HOST = '127.0.0.1'
	PORT = 9990
	

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(5)
	

	while True:
	    klient, adres = s.accept()
	    while True:
	        klient.send(bytes("Wpisz wyrazenie w RPN: ", "utf-8"))
	        dane = klient.recv(100)
	        wyrazenie =''
	        while dane != b'\r\n':
	            dekodowane = dane.decode()
	            wyrazenie += dekodowane
	            temp = klient.recv(100)
	            dane = temp
	        wynik = obliczzRPN(wyrazenie.split())
	        print(wynik)
	        klient.send(bytes(str(wynik) + '\n\r', "utf-8"))

