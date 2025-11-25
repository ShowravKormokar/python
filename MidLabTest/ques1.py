TreeT = {
    'A': [('B', 3), ('C', 5), ('D', 2)],
    'B': [('E', 4), ('F', 6)],
    'C': [('G', 1), ('H', 7)],
    'D': [('I', 3), ('J', 8)],
    'E': [('K', 2), ('L', 5)],
    'F': [('M', 1)],
    'G': [('N', 4)],
    'H': [('O', 3), ('P', 6)],
    'I': [('Q', 2)],
    'J': [('R', 3)],
    'K':[],'L':[],'M':[],'N':[],'O':[],'P':[],'Q':[],'R':[]
}

print("TreeT Representation:")
for node, edges in TreeT.items():
    print(f"{node}: {edges}")

