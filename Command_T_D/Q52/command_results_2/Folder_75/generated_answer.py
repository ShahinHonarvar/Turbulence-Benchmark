def palindrome_of_length_n(s):
    return set(
        ''.join(
            c
            for i in range(1, n+1)
            for c in s[i-1:i+2]
            if c.lower() in 'qwertyuiopasdfghjklzxcvbnm'
        )
        for n in range(1, len(s)+1)
    )
