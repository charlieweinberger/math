def n_cubed(n):
    return 0.25 * (n ** 2) * ((n + 1) ** 2)

def n_squared(n):
    return (1/6) * n * (n + 1) * (2*n + 1)

def n(n):
    return 0.5 * n * (n + 1)

val = 4 * n_cubed(14)
print(val)