import math

def entropy(num_class_0, num_class_1):

    if num_class_0 == 0 or num_class_1 == 0:
        return 0
    
    p0 = num_class_0 / (num_class_0 + num_class_1)
    p1 = num_class_1 / (num_class_0 + num_class_1)
    
    return - p0 * math.log(p0) - p1 * math.log(p1)

print(entropy(4, 2))