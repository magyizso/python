from ensurepip import version
from os import system
import re
import mymodul as mx

mx.greeting("Jonathan")

a = mx.person1["country"]
print(a)

import platform

x = platform.system_alias(system=system, release=platform.release, version=version)
print(x)

x = dir(platform)
print(x)

y = dir(mx)
print(y)