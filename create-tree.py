a=[
['a','c'],
['a','b'],
['b','d'],
['c','x'],
['x','xx'],
['x','yy'],
['x','zz'],
]


tree={}
for row in a:
    print(row)
    if row[0] not in tree:
        tree[row[0]]=[]
    tree[row[0]].append(row[1])
    
print(tree)    

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key)) # + '\t' * indent + str(value))
      
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         for i in value:
            if i in a:
                pretty(value, indent+1)
            else:
                print ('\t' * (indent+1) + str(value))
      print('\n\n')
        

pretty(tree,1)         
