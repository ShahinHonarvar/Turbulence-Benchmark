
def all_left_right_truncatable_prime(n):
    for p in range(3, n[46], 2):
        s = str(p)
        for i in range(len(s)):
            if s[i] == '0':
                break
            elif s[i] == '5':
                if i == len(s) - 1 or s[i + 1] == '0' or s[i + 1] == '5':
                    break
            elif s[i] == '7':
                if i == len(s) - 1 or s[i + 1] == '0' or s[i + 1] == '7':
                    break
            elif s[i] == '3':
                if i == len(s) - 1 or s[i + 1] == '0' or s[i + 1] == '3':
                    break
            elif s[i] == '2':
                if i == len(s) - 1 or s[i + 1] == '0' or s[i + 1] == '2':
                    break
            elif s[i] == '1':
                if i == len(s) - 1:
                    break
        else:
            yield p
```
	