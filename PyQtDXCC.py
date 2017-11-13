# pyuic4 -x DXCCPrefixLookup.ui -o DXCCPrefixLookup.py
# Another way is to use the pyuic4 created source file
# this article shows how to connect up events so they 
# are seperate from teh generated file.  That way you don't
# lose work if you redesigne the UI and regen the file.
# https://nikolak.com/pyqt-qt-designer-getting-started/

import sys
from PyQt4 import Qt, QtCore, QtGui, uic
 
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


		#some howto do for later!
		self.labelNumberVerifiedCount.setText("200")
		self.labelNumberVerifiedCount.setStyleSheet("color: red")
		self.checkBox160m.setChecked(True)

	# Here is where I do the lookup and display the information!
	def on_lineEditReturn(self):
		inputPrefix = self.lineEditPrefix.text()
		self.lineEditPrefix.setText("")
		if inputPrefix:
			self.labelPrefix.setText(inputPrefix.upper())


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



if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
	window.show()

#	window.hideAwardsSection()
#	window.showAwardsSection()

	sys.exit(app.exec_())
