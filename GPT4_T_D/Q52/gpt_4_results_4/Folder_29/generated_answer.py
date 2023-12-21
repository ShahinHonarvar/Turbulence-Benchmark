
def palindrome_of_length_n(s):
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i+19, len(s)+1):
            sub_string = s[i:j]
            if sub_string == sub_string[::-1] and sub_string.isalpha():
                palindrome_set.add(sub_string)
    return palindrome_set
