"""
Test any new function at here
"""
import re

mul_command = '-t#s///'
new = re.sub('[#/]', '', mul_command)
print(new)
