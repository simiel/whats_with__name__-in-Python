print(__name__)
# the above game me "__main__" as what is stored in __name__

print(type(__name__))
# print(help(__name__))
# print(dir(__name__))
# It is a string object

print("The code from simiel2 is run once it is imported once, but not in subsequent imports")
from simiel2 import simiel
simiel()
print(__name__)
__name__ = '`SIMIEL`'
print(__name__)
from simiel2 import simiel
import simiel2

from simiel2 import *


# trying out if statement from simiel3
import simiel3

print("The funtion 'Nii' from simiel3 doesn't run till it's called here")
simiel3.Nii()