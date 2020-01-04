from typing import NamedTuple

class Moon(NamedTuple):
	x: int
	y: int
	z: int
class Vel(NamedTuple):
	x: int
	y: int
	z: int
moons = {"Io":Moon(5, 4, 4),"Europa":Moon(-11, -11, -3),"Ganymede":Moon(0, 7, 0),"Callisto":Moon(-13, 2, 10)}
#Test
#moons = {"Io":Moon(-8, -10, 0),"Europa":Moon(5, 5, 10),"Ganymede":Moon(2, -7, 3),"Callisto":Moon(9, -8, -3)}
vel = {"Io":Vel(0,0,0), "Europa":Vel(0,0,0), "Ganymede":Vel(0,0,0), "Callisto":Vel(0,0,0)}

def moon_velocity(moons):
	total_energy = 0
	def velocity(moon, compare):
		if moon > compare:
			return -1
		elif moon < compare:
			return +1
		elif moon == compare:
			return 0
	for _ in range(1000):
		tmp_moons = {**moons}
		for moon_name, moon_value in tmp_moons.items():
			for compare_name, compare_value in tmp_moons.items():
				if moon_name == compare_name:
					continue
				else:
					tmp_vel_x = vel.get(moon_name).x + velocity(moon_value.x, compare_value.x)
					tmp_vel_y = vel.get(moon_name).y + velocity(moon_value.y, compare_value.y)
					tmp_vel_z = vel.get(moon_name).z + velocity(moon_value.z, compare_value.z)
					vel[moon_name] = Vel(tmp_vel_x,tmp_vel_y,tmp_vel_z)
			moons[moon_name] = Moon((moon_value.x + vel.get(moon_name).x),(moon_value.y + vel.get(moon_name).y),(moon_value.z + vel.get(moon_name).z))
	for moon_name in moons:
		pot = abs(moons.get(moon_name).x) + abs(moons.get(moon_name).y) + abs(moons.get(moon_name).z)
		kin = abs(vel.get(moon_name).x) + abs(vel.get(moon_name).y) + abs(vel.get(moon_name).z)
		total_energy += pot * kin
	return total_energy

print(moon_velocity(moons))