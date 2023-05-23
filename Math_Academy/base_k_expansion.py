import random

def compute_ab():
    b = random.randint(1, 100)
    a = random.randint(1, b)
    return str(a) + '/' + str(b)

def compute_repeating_xy(xy=random.randint(11, 99)):
    new_xy = '0.'
    for _ in range(20):
        new_xy += str(xy)
    return float(new_xy)

class BaseKExpansion():
    
    def __init__(self, fraction, decimal):
        
        self.fraction = fraction
        self.decimal = decimal

        self.a = int(self.fraction.split('/')[0])
        self.b = int(self.fraction.split('/')[1])
        self.x = int(str(self.decimal)[2])
        self.y = int(str(self.decimal)[3])

    def max_n(self, fraction, k_to_the_i):
        n = 0
        while fraction > n / k_to_the_i:
            n += 1
        return n - 1

    def find_k(self):
        
        for k in range(1, 100):

            print("\nk:", k)

            if self.x / k > self.a / self.b:
                continue

            print("")

            c = self.a - self.x * self.b / k
            n = self.max_n(c / self.b, k ** 2)
            
            if n == self.y:
                return k
            else:
                continue
        
        return 'no options worked'

ab = '19/28'
xy = 0.36 # could also be compute_repeating_xy(36)

print("\na/b:", ab)
print("xy:", xy)

base_k_expansion = BaseKExpansion(ab, xy)
k = base_k_expansion.find_k()
print("\ncorrect k:", k)