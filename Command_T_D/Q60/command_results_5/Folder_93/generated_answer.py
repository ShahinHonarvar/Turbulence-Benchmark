
def all_left_right_truncatable_prime(tup):
    res = []
    for i in range(1, tup[11] + 1):
        str_i = str(i)
        res += (str_i[0] != '0' and str_i[-1] != '0' and str_i[0] != str_i[-1] and str(int(str_i[0:int(str_i[0])]) == i and str(int(str_i[int(str_i[-1]:-1]) == i) == str(i))
```
	