
def all_left_right_truncatable_prime(num_list):
    res = []
    for num in num_list:
        s = str(num)
        while s:
            s = s[0] + s[1:]
            if all(map(str.isdigit, s)) and (s in '2357') and (int(s) <= num):
                res.append(int(s))
                break
    return res
