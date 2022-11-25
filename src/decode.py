# Please note:
# If you are using the VSCode extension it will open the serial port, not allowing this program to read it.
# I recommend copying this file somewhere else and running it from VSCode, or running it from the terminal.

from serial.tools import list_ports
import serial
import json
import redis
import datetime

port = list(list_ports.comports())
for index, p in enumerate(port):
    print(str(index) + ": " + str(p.device))
    
selectedPort = int(input("Pick a port: "))

ser = serial.Serial(str(port[selectedPort].device), 115200, timeout=None)
redis_obj = redis.Redis(host="127.0.0.1", port=6379) # Change settings for Redis here. This will connect to a local database without a username or password.

while True:
    data_raw = ser.readline()
    try:
        data_json = json.loads(data_raw) # We need to verify we have actual JSON. The brain likes to send other values at startup.
    except:
        next
    else:
        print(data_json)
        ser.flushInput()
        
        date = datetime.datetime.now()
        timestamp = int(date.timestamp() * 1000)
        pipe = redis_obj.pipeline()
        
        for key, value in data_json.items():
            pipe.execute_command(
                "ts.add", key, timestamp, value
            )
        pipe.execute()
        
        