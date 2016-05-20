#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @project: VulScanner
# @author: TheLost

import sys, getopt
from scanner.ip_filter import *
from scanner.port_scanner import *


def usage():
	print "VulScanner"
	print ""
	print "A tool scan vulnerability"
	print "Usage:vul_scanner.py -u target_url"
	print "      vul_scanner.py -i target_ip"
	print ""

def ip_scan(ip):
	ip_c_port_scan(ip)

def vul_scan():

	try:
		opts, args = getopt.getopt(sys.argv[1:], "u:i:")
	except getopt.GetoptError as err:
		print str(err)
		usage()

	url = ""
	ip = ""

	for op, value in opts:
		if op == "-u":
			url = value
		elif op == "-i":
			ip = value
			ip_scan(ip)
		else:
			usage()


if __name__ == '__main__':
	vul_scan()
