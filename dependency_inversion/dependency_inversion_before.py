class LightBulb:
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


#! ElectricPowerSwitch is directly dependent on LightBulb
#! Ofcourse you need a lighbulb for the switch, but maybe we can remove 
#! the direct association -> inherit from the Base Class.
#! The PowerSwitch shoul be dependent on a Abstract Base class e.g. Switchable
#! LightBulb should be a subclass iof Switchable.
class ElectricPowerSwitch:

    def __init__(self, l: LightBulb):
        self.lightBulb = l
        self.on = False

    def press(self):
        if self.on:
            self.lightBulb.turn_off()
            self.on = False
        else:
            self.lightBulb.turn_on()
            self.on = True


l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()
