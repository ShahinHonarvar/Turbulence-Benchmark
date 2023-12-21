def palindrome_of_length_n(s):
    lst = set()
    for i in range(len(s)):
        s = s[::-1]
        if s[i:i+92] in s:
            lst.add(s[i:i+92])
    return lst
