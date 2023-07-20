# Proper function:

def triple(value: int) -> int:
   "Return three times the parameter value."
   return 3 * value

assert triple(0) == 0
assert triple(5) == 15


"""

Notes:

- Include types in the function definition (line 3)
- Add a docstring comment right below the function definition (line 4)
- Write tests outside of the function, to confirm it works (lines 7 and 8)

"""