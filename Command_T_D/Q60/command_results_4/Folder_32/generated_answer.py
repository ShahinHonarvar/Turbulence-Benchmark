
import sys
import itertools

def all_left_right_truncatable_prime(n):
    if not n:
        yield
    n = str(n[0])
    for i in range(len(n)):
        for p in range(10):
            for j in range(len(n)-i-1):
                if n[i] == str(p):
                    if n[i][:i] == '1' and n[-j-1] == '1':
                        yield int(n[:i]+n[i+1:j+2]+n[j+1:])
                    elif n[i][:i] == '1' and n[-j-1] == '2':
                        yield int(n[:i]+n[i+1:j+3])
                    elif n[i][:i] == '2' and n[-j-1] == '1':
                        yield int(n[:i]+n[i+1:j+3])
                    elif n[i][:i] == '2' and n[-j-1] == '2':
                        yield int(n[:i]+n[i+1:j+4])
```
	