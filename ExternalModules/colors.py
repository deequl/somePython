#python -m pip install NAME_OF_PACKAGE

#python -m pip install termcolor
import sys
import termcolor  #help(termcolor)
text=termcolor.colored("Hi there", color="red")
print(text)

#=============================================

from termcolor import colored
text=colored("Hi there", color="cyan")
print(text)