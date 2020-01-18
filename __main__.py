#!/usr/bin/env python

from sys import argv
from termcolor import colored
from resistor import Resistor

help = """
Returns the value of a resistor given the color of its stripes.

Usage:
    resistor -[Options] colors
    or
    resistor -[Options] color0 color1 color2 color3 [color4] [color5]

Options:
    -h: Prints a help message and exits.
    -u: Specifies the unit in which to display the result.
        o[H]ms, [K]iloohms, [M]egaohms | Default: K
    -c: Returns the value in scientific notation.
        Will ignore -u option if given, output is always in ohms.
    -s: Returns the value without simbols.
    -p: Returns the tolerance value in ohms instead of percentage.

Value abreviations:
    Black:     b
    Brown:     n
    Red:       r
    Orange:    o
    Yellow:    y
    Green:     g
    Blue:      l
    Purple /
    Violet:    p
    Gray:      t
    White:     w
    Gold:      d
    Silver:    s
"""

# Declaration of variables.
translations = {
  "black": "b",
  "brown": "n",
  "red": "r",
  "orange": "o",
  "yellow": "y",
  "green": "g",
  "blue": "l",
  "purple": "p",
  "violet": "p",
  "gray": "t",
  "grey": "t",
  "white": "w",
  "gold": "d",
  "silver": "s"
}
units = ['megaohm', 'kiloohm', 'ohm']
units_sym = ['MΩ', 'KΩ', 'Ω']
error_messages = (
    'Do not use this command with sudo.',
    'Number of positional arguments is too low.',
    'The maximum number of colors is 6. You provided {0}.',
    '{0} is not an option.',
    '{0} is not a recongnized color.')
options = ('h', 'u', 'c', 's', 'p')


# Get the arguments given, excluding the command.
# Returns a dictionary with 3 keys: exec, options and colors.
def get_arguments():
    arguments = [i.lower() for i in argv]    # All the arguments

    # Creates a dictionary with boolean values for the posible
    options_list = [i.lower() for i in ''.join([j[1:] for j in argv if j[0] == '-'])]
    given_options = {option: option in options_list for option in options}
    if given_options['u']:
        u = [i for i in ['h', 'k', 'm', 'H', 'K', 'M'] if i in arguments][0]
        given_options['u'] = u
        arguments.remove(u)
    else:
        given_options['u'] = 'k'

    # Creates a tuple that can be given as an agument to the Resistor class.
    colors = [j.lower() for j in arguments if j[0] not in ['_', '-', '?', '(', '@']]
    if len(colors) > 1:
        colors = [translations[i] for i in colors]
    else:
        colors = [i for i in colors]

    # Arguments that set the execute flag to False.
    if 'sudo' in arguments:
        print(error_messages[0])
        execute = False
    elif given_options['h']:
        print(help)
        execute = False
    else:
        execute = True

    return {'execute': execute, 'options': given_options, 'colors': colors}

def main():
    output = ""
    arguments = get_arguments()
    resistor = Resistor(arguments['colors']).full_form()

    # Value of the resistor.
    if arguments['options']['c']: # Cientific notation
        output += colored(resistor[0][3], 'cyan', attrs=['bold'])
    elif arguments['options']['u'] == 'h': # In ohms
        output += colored(resistor[0][0], 'cyan', attrs=['bold'])
    elif arguments['options']['u'] == 'k': # In kiloohms
        output += colored(resistor[0][1], 'cyan', attrs=['bold'])
    elif arguments['options']['u'] == 'm': # In megaohms
        output += colored(resistor[0][2], 'cyan', attrs=['bold'])

    # Tolerance of the resistor.
    output += "    "
    if arguments['options']['p']:
        output += colored(resistor[1][1], 'blue')
    else:
        output += colored(resistor[1][0], 'blue')

    # TCR if given.
    output += "    "
    output += colored(resistor[2], 'magenta', attrs=['dark'])  if resistor[2] != None else ""

    if arguments['options']['s']:
        for u in units:
            output = output.replace(u, colored(u, 'white'))
        output = output.replace('%', colored('%', 'white'))

    else:
        for u in units:
            output = output.replace(u, colored(units_sym[units.index(u)], 'white'))
        output = output.replace('%', colored('%', 'white'))
        output = output.replace('+-', '±')

    print(output)

if __name__ == '__main__':
    if get_arguments()['execute']:
        main()
