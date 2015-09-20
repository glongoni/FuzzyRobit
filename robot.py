import os
import sys
import math

sys.path.append("C:\Users\Guilherme\Documents\Projetos\iperf-2.0.5-3-win32\pyfuzzy-0.1.0\fuzzy")

import fuzzy.storage.fcl.Reader
from robotsoccer import SoccerClient
system = fuzzy.storage.fcl.Reader.Reader().load_from_file("Soccer Robot.fcl")

# preallocate input and output values
my_input = {
		"ball_angle" : 0.0,
        "ball_distance" : 0.0,
        "target_angle" : 0.0,
        "obstacle_angle" : 0.0,
        "obstacle_distance" : 0.0,
        "spin" : 0.0
        }
my_output = {
        "force_left" : 0.0,
        "force_right" : 0.0
        }

if __name__ == '__main__': 
    host = sys.argv[1] if len(sys.argv) > 1 else 'localhost'    
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 1024
    
    sc = SoccerClient()
    sc.connect(host, port)

# if you need only one calculation you do not need the while
while true:
        # set input values
        my_input["ball_angle"] = sc.get_ball_angle()
        my_input["ball_distance"] = sc.get_distance()
		my_input["target_angle"] = sc.get_target_angle()
		my_input["obstacle_angle"] = sc.get_obstacle_angle()
		my_input["obstacle_distance"] = sc.get_collision()
		my_input["spin"] = sc.get_spin()
 
        # calculate
        system.calculate(my_input, my_output)
 
        # now use outputs
        sc.act(my_output["force_left"], my_output[force_right])