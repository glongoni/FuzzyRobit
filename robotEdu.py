import os
import sys
import math
import time

sys.path.insert(0, "..\robotsoccer-python")
sys.path.insert(0, "..\pyfuzzy-0.1.0")

import fuzzy.storage.fcl.Reader
from robotsoccer import SoccerClient
system_direction = fuzzy.storage.fcl.Reader.Reader().load_from_file("direction.fcl")
#system = fuzzy.storage.fcl.Reader.Reader().load_from_file("RobotSoccer.fcl")

# preallocate input and output values
my_input = {
		"ball_angle" : 0.0,
        "target_angle" : 0.0,
		"robot_spin" : 0.0,
		"ball_distance" : 0.0,
		"obstacle_distance" : 0.0,
		"target_distance" : 0.0,
		"obstacle_angle" : 0.0
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
		my_input["robot_spin"] = math.degrees(sc.get_spin())
		my_input["ball_distance"] = sc.get_ball_distance()
		my_input["obstacle_distance"] = sc.get_obstacle_distance()
		my_input["target_distance"] = sc.get_target_distance()
		my_input["obstacle_angle"] = math.degrees(sc.get_obstacle_angle())
		# calculate
		system_direction.calculate(my_input, my_output)
		
		# now use outputs
		#angle = my_output["angle"]
		#angle = 0.0
		
		print "---------------------------------------------------------------------------------"
		print "Ball_angle: ", my_input["ball_angle"], "target_angle ", my_input["target_angle"], "spin: " , my_input["robot_spin"]
		print "Ball_distance", my_input["ball_distance"], "obstacle_distance", my_input["obstacle_distance"], my_input["obstacle_angle"]
		print "---------------------------------------------------------------------------------"
		
		#print "angle: ", angle, "left: ", force_left, "right: ", force_right
		
		force_left = my_output["r_left"]
		force_right = my_output["r_right"]
		
		print force_left, force_right
		
		sc.act(force_left, force_right)
		#sc.act(-1, -1)
		
		#time.sleep(0.05)