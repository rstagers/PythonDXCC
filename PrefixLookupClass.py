#!/usr/bin/python3

import os
import sys
import telnetlib
import plistlib

os.system('clear')
# Read in the DXCC list...  there is a problem with this and the ARRL verification
# data.  The strings don't match 100%.  i.e. ARRL says UNITED STATES while DXCC list
# says UNITED STATES OF AMERICA!  I have to use the ADIF number i.e. for US 291 to
# do the matching, I think!  
pl = plistlib.readPlist('cty_plist/cty.plist')


class LoTWVerified:
	def __init__(self):
		self.Country = "No Country"
		self.Mode = "No Mode"
		self.Band = "No Band"
		self.DXCCId = "No Id"
		self.Deleted = False
		self.Credits = {}

	def setCountry(self, Cnty):
		self.Country = Cnty

	def getCountry(self):
		return self.Country

	def setMode(self, Mod):
		self.Mode = Mod

	def getMode(self):
		return self.Mode

	def setBand(self, Bnd):
		self.Band = Bnd

	def getBand(self):
		return self.Band

	def setDXCCId(self, dxcc):
		self.DXCCId = dxcc

	def getDXCCId(self):
		return self.DXCCId

	def setDeleted(self, delDXCC):
		self.Deleted = delDXCC

	def getDeleted(self):
		return self.Deleted

	# This is a dictionary, I get a string from the adi file
	def setCredits(self, ARRLCred):
		# need to break up the string, check if the award exists as a key
		# if not add the key.. otherwise move on to the next award in the string!
		credits_split = ARRLCred.split(',')
		for s in credits_split:
			if s not in self.Credits:
				self.Credits[s] = s				

	def getCredits(self):
		return self.Credits

	def mergeCredits(self, newCredits):
		self.Credits = {**self.Credits, **newCredits}

eohTag = "<eoh>"
eorTag = "<eor>"

newRecordFlag = True
CountryTag = "<COUNTRY:"
ModeTag = "<APP_LoTW_MODEGROUP:"
BandTag = "<BAND:"
DXCCTag = "<DXCC:"
DeletedTag = "<APP_LOTW_DELETED_ENTITY:"
CreditTag = "<APP_LoTW_CREDIT_GRANTED:"

Start = False;

DXCCDict = {}
DXCCKey = ""
Count = 0;


try:
	f = open("DXCC_QSLs_20171109_184150.adi", encoding = 'utf-8')
	for line in f:
# look for the <eoh> signals the start of records!
		if not Start and line[0:len(eohTag)] == eohTag[0:len(eohTag)]:
			Start = True;	# Don't really need this unless I wnat to 
			continue
#		elif not Start:		# Here if we want to process the header.			
#			print(line)

# When we get here we have read the first line past the <eoh> tag..  so we are starting a new record.
# parse out the information I need for this DXCC verification and store it in the dictionary.  If the 
# ADIF Number already exists then update the record with the new verification, could be a new mode, band
# i.e. it is a verification of a new award type granted for this record.  Accumulate all the awards into
# the ADIFKey used for the dictionary entry.

# The DXCCKey will be the ADIF for this record.  The other data will be stored in another dict?
  		
		if newRecordFlag:
			NewRecord = LoTWVerified()
			newRecordFlag = False

		# Not really needed
		if line[0:len(CountryTag)] == CountryTag[0:len(CountryTag)]:
			index = line.index('>')
			# Strip off the return and make sure it is Uppercase!
			NewRecord.setCountry(line[index+1: ].rstrip().upper())	
		
		# Not really needed
		if line[0:len(ModeTag)] == ModeTag[0:len(ModeTag)]:
			index = line.index('>')
			# Strip off the return and make sure it is Uppercase!
			NewRecord.setMode(line[index+1: ].rstrip().upper())		

		# Not really needed
		if line[0:len(BandTag)] == BandTag[0:len(BandTag)]:
			index = line.index('>')
			# Strip off the return and make sure it is Uppercase!
			NewRecord.setBand(line[index+1: ].rstrip().upper())		

		if line[0:len(DXCCTag)] == DXCCTag[0:len(DXCCTag)]:
			index = line.index('>')
			# Strip off the return and make sure it is Uppercase!
			NewRecord.setDXCCId(line[index+1: ].rstrip().upper())		

		if line[0:len(CreditTag)] == CreditTag[0:len(CreditTag)]:
			index = line.index('>')
			# Strip off the return and make sure it is Uppercase!
			NewRecord.setCredits(line[index+1: ].rstrip().upper())		

		if line[0:len(DeletedTag)] == DeletedTag[0:len(DeletedTag)]:
			index = line.index('>')
			if line[index+1: ].rstrip().upper() == 'NO':
				NewRecord.setDeleted(False)		
			else:
				NewRecord.setDeleted(False)		

		# Have we reached the end of this record... if so set the flag to create
		# a new Record and stor or update teh current record we decoded. 				
		if line[0:len(eorTag)] == eorTag[0:len(eorTag)]:
			newRecordFlag = True
			if NewRecord.getDXCCId() not in DXCCDict:
				DXCCDict[NewRecord.getDXCCId()] = NewRecord		
				Count += 1;
			else:
				Credits = DXCCDict[NewRecord.getDXCCId()]
				# I used this to see if the awards were duplicated... they are! so... read below!
				#print("Stored Credits", Credits.getCredits())				
				#print("New Credits", NewRecord.getCredits())
				#key = input("PAK...")
				# Need to put only new credits into stored record.  
				# Have to see if a sting is already in the awards 
				# and if it is don't put it in again!  Only add a 
				# string if it is not already in the awards string!

				# I use a dictionary here. class meber function breaks 
				# up the strings in the new awards string and sees if 
				# the key is in the dictionary. If it is don't add it 
				# again, duh!  Otherwise add a new awards as a new key...  
				# Could be overkill but it works and is simple.

				#print("Current..", Credits.getCredits(), "\n") 
				Credits.mergeCredits(NewRecord.getCredits())
				#print("New..", NewRecord.getCredits(), "\n")								
				#print("Merged..", DXCCDict[NewRecord.getDXCCId()].getCredits(), "\n")
				#key = input("PAK...")
				 



#	for K in sorted(DXCCDict):					# Need to add the bands and modes worked...
#		print (K)
finally:
	f.close()

#print(DXCCDict['291'].getCountry())
#print(DXCCDict.items())

#for i, value in DXCCDict.items():
#	if value.getMode() == "":
#		print(i, value.getCountry(), value.getBand())
#	else:
#		print(i, value.getCountry(), value.getMode(), value.getBand())


#fake = input ("Press any key to continue!")
print ('\033[1m\033[32mPrefix Lookup - Number of Verified DXCC\'s imported: \033[0m', Count, end = '')

while True:
	print("\033[3;0H", end='')
	print("\033[K", end='')
	argument = input("Enter Prefix: ")
	print("\033[5;0H", end='')
	print("\033[K", end='')
 
	if argument.upper() in pl:
		Country = pl[argument.upper()]['Country'].upper()
		DXCCId = str (pl[argument.upper()]['ADIF'])			# Must explicity state this is a string or it will thinkk it is an int! Wow just Wow
		print(argument.upper(), "\033[1m\033[33m", Country, "\033[0m", end='')
		if DXCCDict.get(DXCCId) == None: 
		#if DXCCId not in DXCCDict:
			print(" \033[1m\033[31mNEEDED!\033[0m")
	
			print("\033[7;0H", end='')
			print("\033[J", end='')
		else:
			print(" \033[1m\033[32mVERIFIED!\033[0m")
			CurrentRecord = DXCCDict.get(DXCCId)
			print("\033[7;0H", end='')
			print("\033[J", end='')
			print("Awarded: ", CurrentRecord.getCredits())			
			print("\n")
		#print(pl[argument.upper()])


	else:
		print("Prefix", argument.upper(), "not found!")


