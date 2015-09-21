import os
import sys
import math

sys.path.insert(0, "C:\Users\Eduardo\Documents\cic-12\ia\robotsoccer-python-master")
sys.path.insert(0, "C:\Users\Eduardo\Downloads\pyfuzzy-0.1.0")

import fuzzy.storage.fcl.Reader
from robotsoccer import SoccerClient
system = fuzzy.storage.fcl.Reader.Reader().load_from_file("RobotSoccer.fcl")

# preallocate input and output values
my_input = {
		"ball_angle" : 0.0,
        "target_angle" : 0.0
        }
my_output = {
        "angle" : 0.0
        }

if __name__ == '__main__': 
    host = sys.argv[1] if len(sys.argv) > 1 else 'localhost'    
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 1024
    
    sc = SoccerClient()
    sc.connect(host, port)

# if you need only one calculation you do not need the while
while True:
        # set input values
        my_input["ball_angle"] = sc.get_ball_angle()
        my_input["target_angle"] = sc.get_target_angle()
 
        # calculate
        system.calculate(my_input, my_output)
 
        # now use outputs
        angle = my_output["angle"]
        force_left = math.cos(angle) - math.sin(angle)
        force_right = math.cos(angle) + math.sin(angle)
		
        print force_left, force_right
        
        sc.act(force_left, force_right)