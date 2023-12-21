
import re

def all_left_right_truncatable_prime(x_int):
    x = str(x_int)
    s = str(2)
    while s < x:
        s += str(x // 10**2 + 1)
        if re.match(r'[0-9][0-9]*', s):
            yield int(s)
        s = str(x // 10**2 + 1)
```
	