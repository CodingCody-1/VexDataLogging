# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       CodingCody                                                   #                                      #
# 	Description:  Logging data using Redis                                     #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
import json

# Brain should be defined by default
brain=Brain()

# Robot configuration code
motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_b = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)

wait(30, MSEC) # wait for initialization


loggingEvent = Event() # Make a event for the data logger. We need this to run the data logging in parrel with the rest of the program

# Make data logging function
def dataLogging():
    while True:
        # For values note that item 0 is the tag name in Redis.
        # If you want to add or remove them you only need the change the list below.
        values = {
            "ts:motor:a:rpm": motor_a.velocity(RPM),
            "ts:motor:b:rpm": motor_b.velocity(RPM),
            
            "ts:motor:a:amps": motor_a.current(),
            "ts:motor:b:amps": motor_b.current(),
        }
        
        json_object = json.dumps(values)
        print(json_object)
        wait(10,MSEC) # You can change the time between sends here.


def whenStarted():
    global loggingEvent
    loggingEvent.broadcast()
    
# Add events handlers
loggingEvent(dataLogging)

wait(15, MSEC) # Wait for event handlers to apply. (This is very important. It will not work without this!)
whenStarted()