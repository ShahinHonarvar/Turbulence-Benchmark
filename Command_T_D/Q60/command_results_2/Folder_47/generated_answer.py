
import itertools

def all_left_right_truncatable_prime(x):
    for n in itertools.permutations(str(x)):
        if n[0]!='0' and str(x)[-1]!='0' and all(str(x)[i]!=str(x)[i-1] and str(x)[i]!=str(x)[i+1] for i in range(1,len(str(x)))):
            yield int(str(x)[0])
    return []
