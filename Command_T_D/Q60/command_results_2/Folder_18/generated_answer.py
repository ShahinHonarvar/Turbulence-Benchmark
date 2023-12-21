
import string
import itertools

def all_left_right_truncatable_prime(test_input):
    for p in range(2,int(test_input[0])+1):
        if all(i!=0 for i in str(p)):
            yield p
    for p in itertools.permutations(range(2,int(test_input[0])+1)):
        if all(i!=0 for i in str(p)):
            yield p
```
	