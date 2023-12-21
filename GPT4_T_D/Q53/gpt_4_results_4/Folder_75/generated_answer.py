
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = ''.join(ch for ch in s if ch.isalpha())
    pals = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if j - i + 1 >= 40:
                temp = s[i:j+1]
                if temp == temp[::-1]:
                    pals.add(temp)
    return pals
