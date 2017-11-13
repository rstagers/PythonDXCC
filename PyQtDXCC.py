#!/usr/bin/python3

# pyuic4 -x DXCCPrefixLookup.ui -o DXCCPrefixLookup.py
# Another way is to use the pyuic4 created source file
# this article shows how to connect up events so they 
# are seperate from teh generated file.  That way you don't
# lose work if you redesigne the UI and regen the file.
# https://nikolak.com/pyqt-qt-designer-getting-started/

import sys
import time
import plistlib
from PyQt4 import Qt, QtCore, QtGui, uic

DXCCDict = {}
 
qtCreatorFile = "DXCCPrefixLookup.ui" # Enter ui file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)

		#Connect events here!
		self.lineEditPrefix.returnPressed.connect(self.on_lineEditReturn)

		# all checkboxes are READ ONLY don't allow the user to check them!
		self.checkBox2m.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBox2m.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBox2m.setFocusPolicy(QtCore.Qt.NoFocus)
		
		self.checkBox6m.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBox6m.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBox6m.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBox10m.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBox10m.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBox10m.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBox12m.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBox12m.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBox12m.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBox15m.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBox15m.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBox15m.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBox17m.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBox17m.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBox17m.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBox20m.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBox20m.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBox20m.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBox30m.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBox30m.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBox30m.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBox40m.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBox40m.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBox40m.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBox80m.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBox80m.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBox80m.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBox160m.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBox160m.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBox160m.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBox5Band.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBox5Band.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBox5Band.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBox5B6mE.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBox5B6mE.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBox5B6mE.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBox5B12mE.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBox5B12mE.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBox5B12mE.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBox5B17mE.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBox5B17mE.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBox5B17mE.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBox5B30mE.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBox5B30mE.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBox5B30mE.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBox5B160mE.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBox5B160mE.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBox5B160mE.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBoxMixedHR.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBoxMixedHR.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBoxMixedHR.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBoxMixed.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBoxMixed.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBoxMixed.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBoxPhone.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBoxPhone.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBoxPhone.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBoxSatellite.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBoxSatellite.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBoxSatellite.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBoxDigitalHR.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBoxDigitalHR.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBoxDigitalHR.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBoxCW.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBoxCW.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBoxCW.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBoxCWHR.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBoxCWHR.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBoxCWHR.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBoxPhoneHR.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBoxPhoneHR.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBoxPhoneHR.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBoxChallenge.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBoxChallenge.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBoxChallenge.setFocusPolicy(QtCore.Qt.NoFocus)

		self.checkBoxDigital.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
		self.checkBoxDigital.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)
		self.checkBoxDigital.setFocusPolicy(QtCore.Qt.NoFocus)

		# Start with Awrards section hidden
		self.hideAwardsSection()
		
		# While loading hide all other controls and labels
#		self.labelNumberVerifiedText.hide()
#		self.labelNumberVerifiedCount.hide()
#		self.labelPrefix.hide()
#		self.labelVerified.hide()
#		self.lineEditPrefix.hide()
#		self.labelDXCCPrefixEnter.hide()
		# Use the Country Lable to tell user we are loading country data, it takes a bit.
#		self.labelCountry.setText("Loading DXCC list and ARRL Verified data")


		#some howto do for later!
		self.labelNumberVerifiedCount.setText("200")
		self.labelNumberVerifiedCount.setStyleSheet("color: red")
		self.checkBox160m.setChecked(True)

	# Here is where I do the lookup and display the information!
	def on_lineEditReturn(self):
		inputPrefix = self.lineEditPrefix.text()
		self.lineEditPrefix.setText("")
		if inputPrefix:

			self.labelPrefix.setStyleSheet("color: darkred");
			self.labelPrefix.setText(inputPrefix.upper())
			if inputPrefix.upper() in pl:
				self.labelCountry.setStyleSheet("color: blue; font-style: italic");
				self.labelCountry.setText(pl[inputPrefix.upper()]['Country'])
				# Now check if we are Verified or not
				# If we are, display Verified and set awards checkboxes 
				# and display the awards verified by ARRL
				DXCCId = str (pl[inputPrefix.upper()]['ADIF'])			# Must explicity state this is a string or it will thinkk it is an int! Wow just Wow
				if DXCCDict.get(DXCCId) == None:
					self.labelVerified.setStyleSheet("color: red; font-weight: bold")
					self.labelVerified.setText("NEEDED!")
					self.hideAwardsSection()
				else:
					self.labelVerified.setStyleSheet("color: limegreen; font-weight: bold")
					self.labelVerified.setText("VERIFIED!")
					CurrentRecord = DXCCDict.get(DXCCId)
					self.setAwards(CurrentRecord)
					
  
			else:
				self.hideAwardsSection()
				self.labelCountry.setStyleSheet("color: red; font-weight: bold")
				self.labelCountry.setText("Invalid Prefix")
				self.labelVerified.setText("")	

	def clearAllAwards(self):
		self.checkBox2m.setChecked(False)
		self.checkBox6m.setChecked(False)
		self.checkBox10m.setChecked(False)
		self.checkBox12m.setChecked(False)
		self.checkBox15m.setChecked(False)
		self.checkBox17m.setChecked(False)
		self.checkBox20m.setChecked(False)
		self.checkBox30m.setChecked(False)
		self.checkBox40m.setChecked(False)
		self.checkBox80m.setChecked(False)
		self.checkBox160m.setChecked(False)
		self.checkBox5Band.setChecked(False)
		self.checkBox5B6mE.setChecked(False)
		self.checkBox5B12mE.setChecked(False)
		self.checkBox5B17mE.setChecked(False)
		self.checkBox5B30mE.setChecked(False)
		self.checkBox5B160mE.setChecked(False)
		self.checkBoxMixedHR.setChecked(False)
		self.checkBoxMixed.setChecked(False)
		self.checkBoxPhone.setChecked(False)
		self.checkBoxSatellite.setChecked(False)
		self.checkBoxDigitalHR.setChecked(False)
		self.checkBoxCW.setChecked(False)
		self.checkBoxCWHR.setChecked(False)
		self.checkBoxPhoneHR.setChecked(False)
		self.checkBoxChallenge.setChecked(False)
		self.checkBoxDigital.setChecked(False)

	def setAwards(self, ARRLAwards):
		self.clearAllAwards()
		Credits = ARRLAwards.getCredits()
		if "DXCC-2" in Credits:
			self.checkBox2m.setChecked(True)
		if "DXCC-6" in Credits:
			self.checkBox6m.setChecked(True)
		if "DXCC-10" in Credits:
			self.checkBox10m.setChecked(True)
		if "DXCC-12" in Credits:
			self.checkBox12m.setChecked(True)
		if "DXCC-15" in Credits:
			self.checkBox15m.setChecked(True)
		if "DXCC-17" in Credits:
			self.checkBox17m.setChecked(True)
		if "DXCC-20" in Credits:
			self.checkBox20m.setChecked(True)
		if "DXCC-30" in Credits:
			self.checkBox30m.setChecked(True)
		if "DXCC-40" in Credits:
			self.checkBox40m.setChecked(True)
		if "DXCC-80" in Credits:
			self.checkBox80m.setChecked(True)
		if "DXCC-160" in Credits:
			self.checkBox160m.setChecked(True)
		if "DXCC-5B" in Credits:
			self.checkBox5Band.setChecked(True)
		if "DXCC-5B-6" in Credits:
			self.checkBox5B6mE.setChecked(True)
		if "DXCC-5B-12" in Credits:
			self.checkBox5B12mE.setChecked(True)
		if "DXCC-5B-17" in Credits:
			self.checkBox5B17mE.setChecked(True)
		if "DXCC-5B-30" in Credits:
			self.checkBox5B30mE.setChecked(True)
		if "DXCC-5B-160" in Credits:
			self.checkBox5B160mE.setChecked(True)
		if "DXCC-M" in Credits:
			self.checkBoxMixed.setChecked(True)
		if "DXCC-M-HR" in Credits:
			self.checkBoxMixedHR.setChecked(True)
		if "DXCC-PH" in Credits:
			self.checkBoxPhone.setChecked(True)
		if "DXCC-PH-HR" in Credits:
			self.checkBoxPhoneHR.setChecked(True)
		if "DXCC-CW" in Credits:
			self.checkBoxCW.setChecked(True)
		if "DXCC-CW-HR" in Credits:
			self.checkBoxCWHR.setChecked(True)
		if "DXCC-RTTY" in Credits:
			self.checkBoxDigital.setChecked(True)
		if "DXCC-RTTY-HR" in Credits:
			self.checkBoxDigitalHR.setChecked(True)
		if "DXCC-SAT" in Credits:
			self.checkBoxSatellite.setChecked(True)
		if "DXCC-CHAL" in Credits:
			self.checkBoxChallenge.setChecked(True)

		self.showAwardsSection()
	
	def showUIElements(self):
		self.labelNumberVerifiedText.show()
		self.labelNumberVerifiedCount.show()
		self.labelPrefix.show()
		self.labelVerified.show()
		self.lineEditPrefix.show()
		self.labelDXCCPrefixEnter.show()


	def hideAwardsSection(self):
		self.labelVerifiedAwards.hide()
		self.labelBandAwards.hide()
		self.checkBox2m.hide()
		self.checkBox6m.hide()
		self.checkBox10m.hide()
		self.checkBox12m.hide()
		self.checkBox15m.hide()
		self.checkBox17m.hide()
		self.checkBox20m.hide()
		self.checkBox30m.hide()
		self.checkBox40m.hide()
		self.checkBox80m.hide()
		self.checkBox160m.hide()
		self.label5Band.hide()
		self.checkBox5Band.hide()
		self.checkBox5B6mE.hide()
		self.checkBox5B12mE.hide()
		self.checkBox5B17mE.hide()
		self.checkBox5B30mE.hide()
		self.checkBox5B160mE.hide()
		self.labelModeAwards.hide()
		self.checkBoxMixedHR.hide()
		self.checkBoxMixed.hide()
		self.checkBoxPhone.hide()
		self.checkBoxSatellite.hide()
		self.checkBoxDigitalHR.hide()
		self.checkBoxCW.hide()
		self.checkBoxCWHR.hide()
		self.checkBoxPhoneHR.hide()
		self.checkBoxChallenge.hide()
		self.checkBoxDigital.hide()

	def showAwardsSection(self):
		self.labelVerifiedAwards.show()
		self.labelBandAwards.show()
		self.checkBox2m.show()
		self.checkBox6m.show()
		self.checkBox10m.show()
		self.checkBox12m.show()
		self.checkBox15m.show()
		self.checkBox17m.show()
		self.checkBox20m.show()
		self.checkBox30m.show()
		self.checkBox40m.show()
		self.checkBox80m.show()
		self.checkBox160m.show()
		self.label5Band.show()
		self.checkBox5Band.show()
		self.checkBox5B6mE.show()
		self.checkBox5B12mE.show()
		self.checkBox5B17mE.show()
		self.checkBox5B30mE.show()
		self.checkBox5B160mE.show()
		self.labelModeAwards.show()
		self.checkBoxMixedHR.show()
		self.checkBoxMixed.show()
		self.checkBoxPhone.show()
		self.checkBoxSatellite.show()
		self.checkBoxDigitalHR.show()
		self.checkBoxCW.show()
		self.checkBoxCWHR.show()
		self.checkBoxPhoneHR.show()
		self.checkBoxChallenge.show()
		self.checkBoxDigital.show()


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



def parseArrlData(filename):
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

	DXCCKey = ""
	Count = 0;

	try:
		f = open("DXCC_QSLs_20171109_184150.adi", encoding = 'utf-8')
		for line in f:
		# look for the <eoh> signals the start of records!
			if not Start and line[0:len(eohTag)] == eohTag[0:len(eohTag)]:
				Start = True;	# Don't really need this unless I wnat to 
				continue
#				elif not Start:		# Here if we want to process the header.			
#					print(line)		# might want to get the date in the file!

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
					NewRecord.setDeleted(True)		

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
		return Count


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)

	# Create and display the splash screen
#	splash_pix = QtGui.QPixmap('splash_loading.png')
#	splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
#	splash.setMask(splash_pix.mask())
#	splash.show()
#	app.processEvents()

	# Read in the DXCC list...  there is a problem with this and the ARRL verification
	# data.  The strings don't match 100%.  i.e. ARRL says UNITED STATES while DXCC list
	# says UNITED STATES OF AMERICA!  I have to use the ADIF number i.e. for US 291 to
	# do the matching, I think!  
	pl = plistlib.readPlist('cty_plist/cty.plist')

	# Parse the ARRL_DXCC_VERIFIED.ADI and creat our dictionary.
	ARRLcnt = parseArrlData("DXCC_QSLs_20171109_184150.adi")

	window = MyApp()
	window.show()
	window.setFixedSize(window.size())
	# blank out the Country Label
	window.labelNumberVerifiedCount.setText(str(ARRLcnt))
	window.labelCountry.setText("")
	window.labelPrefix.setText("")
	window.labelVerified.setText("")	

#	splash.finish(window)

	sys.exit(app.exec_())
