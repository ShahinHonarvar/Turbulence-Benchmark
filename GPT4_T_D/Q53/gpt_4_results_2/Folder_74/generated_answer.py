
def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindrome_set = set()
    for length in range(57, len(s)+1):
        for idx in range(len(s)-length+1):
            substring = s[idx:idx+length]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
