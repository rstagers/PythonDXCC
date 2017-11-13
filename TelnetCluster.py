#!/usr/bin/python3
# Startuing a Python Telnet DXCC Cluster program to help monitor for DX on my Linux Box
# without having to install someone elses crap!  Eventully I want this thing to tell me 
# if a DX station is needed by me or not!  I would also likt it to be interactive so I 
# can send commands to the cluster for filtering and such.
#
import telnetlib
import plistlib

#import xml.etree.cElementTree as ET

#HOST = "dxcc.ve7cc.net"
#tn = telnetlib.Telnet(HOST, 23)

#tn.interact()
#tn.read_until(b"login: ")
#print ("login:")
#tn.write(b'k9vd\n')
#print ("mycall")
#print(tn.read_very_eager().decode('ascii'))


def connction():
	global tn
	while True:
		try:
			tn = telnetlib.Telnet('dxcc.ve7cc.net', '23')
			break
		except socket.timeout:
			print ("Cluster Connect Failed")


def cluster_feed():
	tn.read_until(b"login:")
	tn.write(b"k9vd\n") # send the callsign
	print ("Connected to DXCluster\n")
#	tn.write(b"sh/filter dxbm\n")			# Show band mode filter
	tn.write(b"set/filter dxbm/off\n")		# reset band mode filter to all
#	tn.write(b"SET/FILTER DXCTY\n")	
	tn.write(b"set/filter dxbm/pass 160-cw,80-cw,40-cw,30-cw,20-cw,17-cw,15-cw,12-cw,10-cw\n")
#	tn.write(b"set/filter hf/cw\n")			# Supposed to work but I get Invalid

	tn.write(b"set/filter dxcty/reject k,xe,ve\n")  # reject spots of US Canada and Mexico
	tn.write(b"SET/FILTER K,XE,VE/PASS\n")				# US, Mexico and Canada spot sources only

#	tn.write(b"SH/FILTER DXCTY\n")

	while True:
		line = tn.read_until("\n".encode('latin-1'))
# This is where I need to break apart the spot and get the prefix of the spotted DX
# I will add this to the output so that I know the country that the call is.
# also I need to chedk my confirmed verified lists to see if I have this entity 
# at all or for this band and mode.  Indicate NEEDED if I do not have a confirmation 
# or ARRL verification.  
# Spots are prefixed with DX
# WCY is solor data
# WWV is WWV data..  basically I am only intrested in DX de lines! 
# OK I am looking at my VE7CC output and I believe that the foramt
# is a follows:
#
# DX de CALL: <spaces to freq><frequency>(first non number ends) 
# <spaces to comment><comment 0x20 0x20><spaces to prefix><prefix 0x20>
# <time 0x20> <state 0x0a>
# it appease that spaces are doubled 

# Defined regular expressions for obtaining callsign, frequency etc from a 
# spot

#callsign_pattern = "([a-z|0-9|/]+)"
'''
https://regex101.com/
^DX de [A-Z|0-9|\/]+:\s+[0-9|.]+\s+[A-Z|0-9|\/]+\s+(.*)\s+(\d{4}Z)                        
'''
#frequency_pattern = "([0-9|.]+)"
'''
this will match digits 0-9.
'''
#pattern = re.compile("^DX de "+callsign_pattern+":\s+"+frequency_pattern+"\s+"+callsign_pattern+"\s+(.*)\s+(\d{4}Z)", re.IGNORECASE)
'''
Match from start of string "DX de "  


'''


		print(line.rstrip().decode('latin-1'))

# this will read thee plist xml for the DXCC information! DAMN!
pl = plistlib.readPlist('cty_plist/cty.plist')
print(pl['CL']) # pass the prefix and you get back the information for that prefix!


connction()
cluster_feed()

