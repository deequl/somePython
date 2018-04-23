
#_Python Debugger


first = "First"
second = "Second"
import pdb; pdb.set_trace()
#      ^^^
result = first + second
third = "Third"
result += third
print(result)

# Common PDB Commands:
# (Pdb) l    -> (list) Show the map
# (Pdb) n    -> (next line) execute next instruction
# (Pdb) p    -> (print) print the value of 
# (Pdb) c    -> (continue) finishes debugging

#(Pdb) p first
#· 'First'      -> variable first has "First"