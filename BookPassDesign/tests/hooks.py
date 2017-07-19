from lettuce import before, after, world
from BookPassDesign.classes import Reader

@before.each_scenario
def testing_reader():
    world.reader = world.a_reader()