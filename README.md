# cellular-rocktomata

“Life sucks, but in a beautiful kind of way.”

Axl Rose

Implementing Wolfram-style cellular automata in (mostly) idiomatic rockstar. Avoiding obviously 'program-y' conventions like parentheses, brackets, comments, and numerical digits in favor of poetic vocabulary more in line with the style of a Bon Jovi power ballad. 

A python 3 transpilation (rocktomata.py, generated via https://github.com/yanorestes/rockstar-py) is included for convenience. To run with default settings (rule 30 for 24 generations):
```
python3 rocktomata.py
```
To update settings edit the values for Scottie (the rule) and Life (# generations), or from a python console:
```
import rocktomata

rocktomata.rock_remembrance(rule,generations)
```
NOTE: The simulation doesn't extend past a fixed width determined by the number of generations, so for some settings artifacts from the edge can creep in. That's rock'n'roll for you. 
This implementation makes use of arbitrarily sized ints and '+' for string concatenation, so translating to other languages may not work.

Overview of cellular automata here: http://mathworld.wolfram.com/ElementaryCellularAutomaton.html
