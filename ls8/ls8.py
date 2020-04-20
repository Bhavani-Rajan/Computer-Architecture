#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()
# print("before loading")
cpu.load()
# print(cpu.ram)
cpu.run()