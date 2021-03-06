import sys
sys.path.append('/home/lwang/code/amuse-git/src')
import numpy
import amuse
#import matplotlib.pyplot as plt

from amuse.units import nbody_system
from amuse.units import units
from amuse.community.petar.interface import petar
from amuse.ic.plummer import new_plummer_model

print("Initial")

gravity = petar(number_of_workers=2, redirection='none')

print("Add 50 particle")
number_of_stars=50
particles = new_plummer_model(number_of_stars)
particles[0].mass = 1.0|nbody_system.mass
particles[1].mass = 0.1|nbody_system.mass
#print particles

gravity.particles.add_particles(particles)

for index in [1,2,3]:
    print("Get particle ",index," from code, should get:")
    print(particles[index-1])
    print("result from API petar.particles[",index-1,"] :")
    print( gravity.particles[index-1])
    print("Using API peter.get_mass(",index,"), should return the same mass :")
    print( gravity.get_mass(index))
    print("Using API peter.get_position(",index,"), should return the same position :")
    print( gravity.get_position(index))
    print("Using API peter.get_velocity(",index,"), should return the same velocity :")
    print( gravity.get_velocity(index))
    print("Get acceleration:")
    print( gravity.get_acceleration(index))
    print("Get potential:")
    print( gravity.get_potential(index))
    print("")

print("set state of petar.particle[1](id=2) to particle[2](id=3)")
gravity.set_state(2,particles[2].mass,particles[2].position.x,particles[2].position.y,particles[2].position.z,particles[2].velocity.x,particles[2].velocity.y,particles[2].velocity.z,particles[2].radius)
print("get state of petar.particle[1](id=2), now should be original particle[2](id=3)")
print(gravity.particles[1])

print("set mass of petar.particle[1](id=2) to original particle[1](id=2)")
gravity.set_mass(2,particles[1].mass)
print("set position of petar.particle[1](id=2) to original particle[1](id=2)")
gravity.set_position(2,*particles[1].position)
print("set velocity of petar.particle[1](id=20 to original particle[1](id=2)")
gravity.set_velocity(2,*particles[1].velocity)
print("get state of petar.particle[1](id=2)")
print(gravity.particles[1])


print("Delete petar.particle[2](id=3) from code")
gravity.delete_particle(2)

print("Get petar.particle[2] from code again,:")
print("result from API petar.particles[2] :")
print( gravity.particles[2])
print("Using API peter.get_mass(3), should return the same mass :")
print( gravity.get_mass(3))

print("evaluate potential at deleted particle position")
print(gravity.get_potential_at_point(0.0|nbody_system.length, *particles[1].position))

print("evolve to time = 1.0")
gravity.evolve_model(1.0|nbody_system.time)

print("Test parameter change, update changeover and rbin")
gravity.parameters.r_out = 0.4|nbody_system.length
gravity.parameters.r_bin = 0|nbody_system.length
gravity.parameters.r_search_min = 0|nbody_system.length
gravity.parameters.dt_soft = 0|nbody_system.time
print(gravity.parameters)

print("evolve to time = 2.0")
gravity.evolve_model(2.0|nbody_system.time)

print(gravity.parameters)

#gravity.particles[1].mass = 1.0|nbody_system.mass
#gravity.evolve_model(3.0|nbody_system.time)


gravity.stop()

