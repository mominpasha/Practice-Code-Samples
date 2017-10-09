#style 1 in importing a module
import math

dir(math)

math.sqrt(100)

math.e

math.log10(100)

math.pi

del math

#style 2 in importing a module
from math import *

locals()

pi

#style 3 in importing a module
from math import pi as PI

locals()

PI