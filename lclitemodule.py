#!/usr/bin/python3

class lcmodule:

	def address(self):
		if self.idnum == range (1,2,3,4,5,6,7,8):
			self.idnum = "invalid range"

	def logicalbuttonpressed(self):
		if self.logicalbuttonpressed == "On" : {
			print(" the app button has been pressed", mylcmodule.logicalbuttonpressed)
			}
				self.logicalbuttonpressed = "Off"
				
	def physicalchanneloutput(self):
		if self.physicalchanneloutput == range(1,2,3,4): {
			print("Physical channel output is", mylcmodule.physicalchanneloutput)
			}
				self.physicalchanneloutput = "Off"

	def physicalchanneloutputstate(self) :
		if self.physicalchanneloutputstate == "On"
			self.physicalchanneloutputstate = "Off"
				
	def logicalchannelinput(self) : {
		if self.logicalchannelinput == range(1,2,3,4,5,6,7,8) :{
			print(" logical channel input is valid", mylcmodule.logicalchannelinput)
			}
				self.logicalchannelinput = "Invalid channel assignment"
				
mylcmodule = lcmodule()
mylcmodule.idnum = 1
mylcmodule.logicalbuttonpressed = "On"
mylcmodule.logicalchannelinput = range (1,2,3,4,5,6,7,8)
mylcmodule.physicalchanneloutput = range (1,2,3,4)

print("my lc module address is", mylcmodule.idnum)
print("a logical channel is ", mylcmodule.logicalbuttonpressed)
print("my logical channel input is ", mylcmodule.logicalchannelinput)
print("my physical channel output address is", mylcmodule.pyhsicalchanneloutput)
print("my physical channel output is",mylcmodule.physicalchanneloutputstate)
print("Let's change the state of the output")
print
mylcmodule.physicalchanneloutputstate()
mylcmodule.logicalbuttonpressed()
mylcmodule.address()
print("my physical output channel is", mylcmodule.physcalchanneloutputstate)
print("my lc module address is", mylcmodule.idnum)
print("a logical channel is ", mylcmodule.logicalbuttonpressed)
