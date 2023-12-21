def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(58):
        if s[i] in 'qwertyuiopasdfghjklzxcvbnm' and i >= (n-1):
            j = 0
            while i-j >= 0 and s[i-j] in 'qwertyuiopasdfghjklzxcvbnm':
                j += 1
            if j == i:
                res.add(s[i:j])
    return res
