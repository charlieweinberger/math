import math

def set_part(tri_elem, mod, operation):
    ans = []
    
    var = 1
    while var not in ans:
        ans.append(var)

        if operation == '+':
            var = (var + tri_elem) % mod
        if operation == '*':
            var = (var * tri_elem) % mod

    return sorted(ans)

def group_part(mod):
    return [i for i in range(mod) if math.gcd(i, mod) == 1]

def list_mult(scalar, tri_elem, mod, operation):
    ans = []
    for n in set_part(tri_elem, mod, operation):
        if operation == '+':
            ans.append((scalar + n) % mod)
        if operation == '*':
            ans.append(scalar * n % mod)
    return sorted(ans)

def quotient_group(tri_elem, mod, operation):
    ans = []
    for elem in group_part(mod):
        sort = list_mult(elem, tri_elem, mod, operation)
        if sort not in ans:
            ans.append(sort)
    return ans

def get_order(tri_elem, mod, elem, operation):
    for i in range(1, 10):
        if   operation == '+' and (elem *  i) % mod == 0:
            return i
        elif operation == '*' and (elem ** i) % mod == 1:
            return i

# print(set_part(3, 12, '+'))
# print(quotient_group(9, 10, '*'))
# print(list_mult((4 * 5) % 11, 3, 11, '*')) # only works for '*'
print(get_order(4, 9, 8, '*')) # only works for '*'? test this