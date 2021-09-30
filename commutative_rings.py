ints = '0123456789'

def is_commutative(ring):

    if len(ring) == 1: return True
    if ring == 'Z' and all(elem in ints for elem in ring[1:]): return True
    if ring[0] == 'M': return False

    if ring == 'N[x]': return False
    if ring[1:] in ['-[x]', '+[x]']: return False
    if ring[0] == 'Z' and ring[1] in ints and ring[2:] == '[x]': return True

    return 'unknown'

ring = 
print(is_commutative(ring))