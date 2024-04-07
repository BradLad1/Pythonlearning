#enums are  readeable names bound to a constant value
from enum import Enum

class State(Enum):
    INACTIVE =0
    ACTIVE = 1

print(State.ACTIVE)#We can print out the state
print(State.INACTIVE.value)# we can print the value
print(State['ACTIVE'])
#THIS IS A WAY TO CREATE CONSTANTS IN PYTHON