moons = {
"moon1" : {"x" : 5, "y" : 4, "z" : 4, "vel_x" : 0, "vel_y" : 0, "vel_z" : 0},
"moon2" : {"x" : -11, "y" : -11, "z" : -3, "vel_x" : 0, "vel_y" : 0, "vel_z" : 0},
"moon3" : {"x" : 0, "y" : 7, "z" : 0, "vel_x" : 0, "vel_y" : 0, "vel_z" : 0},
"moon4" : {"x" : -13, "y" : 2, "z" : 10, "vel_x" : 0, "vel_y" : 0, "vel_z" : 0}
}
def motion(moons):
	for _ in range(1000):
		for k, v in moons.items():
			for x, y in v.items():
				

motion(moons)