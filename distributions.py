import math

def distribution(starting_point, num_range, round_to, f, boolean=(lambda x: True)):
    
    start, end = num_range
    inv = end == 'infinity'

    end = start - 1 if inv else end
    start = starting_point if (inv or start == 'min') else start

    total = 0
    for x in range(start, end + 1):
        if boolean(x):
            total += f(x)
    
    total = 1 - total if inv else total
    return round(total, round_to)

def poisson(l, num_range, round_to):
    return distribution(0, num_range, round_to, lambda x: (l ** x * math.e ** -l) / math.factorial(x))

def geometric(p, num_range, round_to):
    return distribution(1, num_range, round_to, lambda x: (1 - p) ** (x - 1) * p)

def binomial(n, p, num_range, round_to):
    return distribution(0, num_range, round_to, lambda x: choose(n, x) * (p ** x) * ((1 - p) ** (n - x)))

def hypergeometric(big_n, big_k, n, num_range, round_to):
    return distribution(0, num_range, round_to, lambda x: choose(big_k, x) * choose(big_n - big_k, n - x) / choose(big_n, n), lambda x: max(0, n + big_k - big_n) <= x <= min(n, big_k))

def exponential(l, num_range, round_to):
    start, end = num_range
    end = 1000000000000 if end == 'infinity' else end
    total = - math.e ** (-l * start) + math.e ** (-l * end)
    return abs(round(total, round_to))

def choose(a, b):
    return math.factorial(a) / (math.factorial(b) * math.factorial(a - b))

def ftd(string):
    a, b = string.split('/')
    return float(a) / float(b)

hypergeometric = hypergeometric(29, 12, 15, [10, 'infinity'], 4)
print(hypergeometric)