#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @project: VulScanner
# @author: TheLost

import re

"""Filt IP from file"""
def ip_filter(file_name):

	ipPattern = r"([1]?\d\d?|2[0-4]\d|25[0-5])\.([1]?\d\d?|2[0-4]\d|25[0-5])\.([1]?\d\d?|2[0-4]\d|25[0-5])\.([1]?\d\d?|2[0-4]\d|25[0-5])"
	file_object = open(file_name)

	try:
		"""Read file"""
		message = file_object.read( )
	finally:
		file_object.close( )

	pattern = re.compile(ipPattern) 
	match = pattern.findall(message)

	ip_list = []

	if match:
		for m in match:
			ip = m[0] + '.' + m[1] + '.' + m[2] + '.' + m[3]
			ip_list.append(ip)

		"""Remove Same IP"""
		ip_list= list(set(ip_list))
		for ip in ip_list:
			print ip
		with open(file_name + '_ip', 'wt') as handle:
	    		handle.write( '\n'.join(ip_list))
	else:
		print "Not Match"


if __name__ == '__main__':
	ip_filter("tuniu.com.txt")