from prettytable import PrettyTable

pt = PrettyTable()
# want to add Pokemon Name, Type, then Pikachu Electric, Squirtle, Water, Charmander, Fire
pt.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
pt.add_column('Type', ['Electric', 'Water', 'Fire'])
pt.add_column('Number', ['#0025', '#0007', '#0004'])

nt = pt

print(pt)

nt.align = 'l'
print(nt)