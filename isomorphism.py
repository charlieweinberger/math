# only works for Z

def kernel(mod, f, e):
    return set([(x % mod) for x in range(-1000, 1000) if f(x) == e])

def image(mod, f):
    ans = []
    if f.__code__.co_argcount > 1:
        return 'must be one parameter'
    for x in range(-mod, mod):
        if f(x) in ans:
            return sorted(ans)
        ans.append(f(x))