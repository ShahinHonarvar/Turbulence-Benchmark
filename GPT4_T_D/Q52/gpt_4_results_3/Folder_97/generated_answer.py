
def palindrome_of_length_n(s):
    s = s.lower()
    result_set = set()

    for i in range(len(s) - 209):
        substring = s[i:i+210]
        if substring == substring[::-1] and substring.isalpha():
            result_set.add(substring)
            
    return result_set
