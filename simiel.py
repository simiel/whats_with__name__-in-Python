print(__name__)
# the above game me "__main__" as what is stored in __name__

print(type(__name__))
# print(help(__name__))
# print(dir(__name__))
# It is a string object

from simiel2 import simiel
simiel()
print(__name__)
__name__ = '`SIMIEL`'
print(__name__)