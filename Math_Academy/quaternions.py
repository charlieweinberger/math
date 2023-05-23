def mult(quaternions):
    if len(set(quaternions)) == 1: print(-1)
    if quaternions == 'ij': print('k')
    if quaternions == 'ik': print('-j')
    if quaternions == 'ji': print('-k')
    if quaternions == 'jk': print('i')
    if quaternions == 'ki': print('j')
    if quaternions == 'kj': print('-i')

mult('ij')
mult('ji')