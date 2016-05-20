#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @project: VulScanner
# @author: TheLost

import threading
import socket

PORT_LIST = [
	80,
	2375,
	8080,
	9090
	]

class PortScanner(threading.Thread):

	def __init__(self, ip, port):    
		threading.Thread.__init__(self)
		self.ip = ip
		self.port = port

	def run(self):
		#port = '2375'
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex((self.ip, int(self.port)))
			#print result
			if result == 0:
				print '\r' + self.ip + ': %d  ---------------------------------------> open' % (self.port)
				sock.close()

			else:
				sock.close()
			

		except:
			print self.ip + '--------Error...'

def get_ip_list(host, start = 1, end = 255):
	iplist = []
	ip_pre = ""
	for pre in host.split('.')[0:3]:
		ip_pre = ip_pre + pre + '.'
	for i in range(start, end):
		iplist.append(ip_pre + str(i))
	return iplist

def ip_c_port_scan(host):
	#host = '121.18.230.160'
	ip_list = get_ip_list(host)
	threads = []
	print "IP Port Scan Start !"
	for ip in ip_list:
		
		for port in PORT_LIST:
			t2 = PortScanner(ip, port) 
			threads.append(t2)
	for t in threads:
		t.start()
	for t in threads:
		t.join()

	print "\rIP Port Scan Over !"


if __name__ == '__main__':
	ip_c_port_scan("121.18.230.160")
