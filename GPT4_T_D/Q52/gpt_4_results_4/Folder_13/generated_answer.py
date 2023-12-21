
def palindrome_of_length_n(s):
    s = s.lower()
    pals = set()
    for i in range(len(s)):
        for j in range(i + 206, len(s) + 1):
            temp = s[i:j]
            if temp == temp[::-1] and temp.isalpha():
                pals.add(temp)
    return pals
