
import itertools

def all_left_right_truncatable_prime(num_list):
    for p in itertools.permutations(list(range(1, int(num_list[0])+1)), 2):
        if p[0] != p[1]:
            yield int(str(p[0]) + str(p[1])[1:])
            break
```
	