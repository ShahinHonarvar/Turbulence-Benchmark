
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i + 21, len(s) + 1):
            if all(char.isalpha() for char in s[i:j]):
                sub = s[i:j]
                if sub == sub[::-1]:
                    palindrome_set.add(sub)
    return palindrome_set
