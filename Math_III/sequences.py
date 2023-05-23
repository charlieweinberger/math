# terms = [4]
# num_terms = 10

# for i in range(len(terms), num_terms - len(terms) + 1):
#     terms.append(4 * ((terms[i-1]) ** (1/2)))

# print(terms)

# d = 6
# a = -13
# num_terms = 4

# terms = []

# for n in range(1, num_terms + 1):
#     terms.append(d*n + a)

# print(terms)

a_1 = 8
r = 4
num_terms = 4

terms = []

for n in range(1, num_terms + 1):
    terms.append(a_1 * (r ** (n - 1)))

print(terms)