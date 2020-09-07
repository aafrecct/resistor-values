![Resistor Values Logo](./ResistorValues.svg)

A small terminal tool to get the values of resistors given their color codes.
It was too much to ask of me to learn them and this is a fast way to get them.

It might draw a resistor with the given colors in the future.

# Sintax
```
resistor -[Options] colors-abreviated
```
or
```
resistor -[Options] color0 color1 color2 color3 [color4] [color5]
```

# Options
-h: Prints a help message and exits.
-u: Specifies the unit in which to display the result.
    o[H]ms, [K]iloohms, [M]egaohms | Default: K
-c: Returns the value in scientific notation.
    Will ignore -u option if given, output is always in ohms.
-s: Returns the value without simbols.
-p: Returns the tolerance value in ohms instead of percentage.


# Colors
Color | Abreviation
----- | -----------
Black | b
Brown | n
Red | r
Orange | o
Yellow | y
Green | g
Blue | l
Purple / Violet | p
Gray | t
White | w
Gold | d
Silver | s

