#!/usr/bin/python3

# Python to parse my LoTW DXCC accepted QSL's (Downloaded from LoTW site) so I can quickly see if I have work 
# an entity or not. So far I do not look at band or mode just if I have worked an entity or not period.
# I need to add if I need a band or mode for the entity as well.  The output needs to show that I 
# have the entity but need different bands or modes.
#
# I am only really intrested in 80m 40m 20m 15m 10m.  160m 30m 17m 12m I will take if I don't have the entity!
# Mode wise for now only Phone and CW.  Digital and Sat I may try later...  I want 5 Band DXCC for Phone and CW! 
#
# NOTE:  This is also only for accepted LoTW credits.  If I have not applied for the new credits
# i.e. new DXCC contacts they will not show in this adi file!  I should keep another file of 
# credits to be applied for as I work them and add them to this program.
#

DXCCTag = "<COUNTRY:"
DXCCDict = {}
DXCCKey = ""
Count = 0;

try:
	f = open("DXCC_QSLs_20171109_184150.adi", encoding = 'utf-8')
	for line in f:
		if line[0:8] == DXCCTag[0:8]:
			index = line.index('>')
			DXCCKey = line[index+1: ].rstrip()
			if DXCCKey not in DXCCDict:
				DXCCDict[DXCCKey] = DXCCKey		# Value needs to contain MODE and BAND confirmed.
				Count += 1;

	print ("No DXCC's imported: ", Count)
	for K in sorted(DXCCDict):					# Need to add the bands and modes worked...
		print (K)
finally:
	f.close()

# APP_LoTW_CREDIT_GRANTED - Award Enumeration
#DXCC-2			 2 Meters
#DXCC-6			 6 Meters
#DXCC-10		10 Meters
#DXCC-12		12 Meters
#DXCC-15		15 Meters
#DXCC-17		17 Meters
#DXCC-20		20 Meters
#DXCC-30		30 Meters
#DXCC-40		40 Meters
#DXCC-80		80 Meters
#DXCC-160		160 Meters
#DXCC-5B		5-Band
#DXCC-5B-6		5-Band (6 Meter Endorsement)
#DXCC-5B-12		5-Band (12 Meter Endorsement)
#DXCC-5B-17		5-Band (17 Meter Endorsement)
#DXCC-5B-30		5-Band (30 Meter Endorsement)
#DXCC-5B-160	5-Band (160 Meter Endorsement)
#DXCC-CHAL		Challenge
#DXCC-CW		CW
#DXCC-CW-HR		CW (Honor Roll)
#DXCC-M			Mixed
#DXCC-M-HR		Mixed (Honor Roll)
#DXCC-PH		Phone
#DXCC-PH-HR		Phone (Honor Roll)
#DXCC-RTTY		Digital
#DXCC-RTTY-HR	Digital (Honor Roll)
#DXCC-SAT		Satellite
