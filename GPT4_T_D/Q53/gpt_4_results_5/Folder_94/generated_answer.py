
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub(r'\W+', '', s).lower()
    result_set = set()

    for i in range(len(s)):
        for j in range(i+41, len(s)+1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result_set.add(substring)

    return result_set
