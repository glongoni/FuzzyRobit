import os
import sys
import math
import time

sys.path.insert(0, "C:\Users\Guilherme\Documents\Projetos\robotsoccer-python")
sys.path.insert(0, "C:\Users\Guilherme\Documents\Projetos\pyfuzzy-0.1.0")

import fuzzy.storage.fcl.Reader
from robotsoccer import SoccerClient
system = fuzzy.storage.fcl.Reader.Reader().load_from_file("RobotSoccer.fcl")

# preallocate input and output values
my_input = {
		"ball_angle" : 0.0,
        "target_angle" : 0.0
        }
my_output = {
        "r_right" : 0.0,
		"r_left" : 0.0
        }

if __name__ == '__main__': 
    host = sys.argv[1] if len(sys.argv) > 1 else 'localhost'    
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 1024
    
    sc = SoccerClient()
    sc.connect(host, port)

# if you need only one calculation you do not need the while
while True:
		# set input values
		my_input["ball_angle"] = math.degrees(sc.get_ball_angle())
		my_input["target_angle"] = math.degrees(sc.get_target_angle())
		my_input["robot_spin"] = sc.get_spin()
		my_input["ball_distance"] = sc.get_ball_distance()
		
		# calculate
		system.calculate(my_input, my_output)
		
		# now use outputs
		#angle = my_output["angle"]
		#angle = 0.0
		
		#force_left = math.cos(math.radians(angle)) + my_input["robot_spin"]
		#force_right = math.sin(math.radians(angle)) + my_input["robot_spin"]
		#print "---------------------------------------------------------------------------------"
		#print "Ball_angle: ", my_input["ball_angle"], "target_angle ", my_input["target_angle"], "spin: " , my_input["robot_spin"]
		
		#print "angle: ", angle, "left: ", force_left, "right: ", force_right
		
		force_left = my_output["r_left"]
		force_right = my_output["r_right"]
		
		sc.act(force_left, force_right)
		
		time.sleep(0.4)