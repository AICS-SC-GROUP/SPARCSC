import sys
sys.path.append('/home/lwang/code/amuse-git/src')
import numpy
import amuse
#import matplotlib.pyplot as plt

from amuse.units import nbody_system
from amuse.units import units
from amuse.community.petar.interface import petar
from amuse.ic.plummer import new_plummer_model

print "Initial"

gravity = petar(number_of_workers=2, redirection='none')

print "Add 50 particle"
number_of_stars=50
particles = new_plummer_model(number_of_stars)
particles[0].mass = 1.0|nbody_system.mass
particles[1].mass = 0.1|nbody_system.mass
#print particles

gravity.particles.add_particles(particles)

for index in [1,2,3]:
    print "Get particle ",index," from code, should get:"
    print particles[index-1]
    print "result from API petar.particles[",index-1,"] :"
    print  gravity.particles[index-1]
    print "Using API peter.get_mass(",index,"), should return the same mass :"
    print  gravity.get_mass(index)
    print "Get potential:"
    print  gravity.get_potential(index)
    print ""

print "Del particle 2 from code"
gravity.delete_particle(2)

print "Get particle 3 from code again,:"
print "result from API petar.particles[",2,"] :"
print  gravity.particles[2]
print "Using API peter.get_mass(",3,"), should return the same mass :"
print  gravity.get_mass(3)

print "evaluate potential at deleted particle position"
print gravity.get_potential_at_point(0.0|nbody_system.length, *particles[1].position)

print "evolve to time = 1.0"
gravity.evolve_model(1.0|nbody_system.time)

#gravity.particles[1].mass = 1.0|nbody_system.mass
#gravity.evolve_model(3.0|nbody_system.time)


gravity.stop()

