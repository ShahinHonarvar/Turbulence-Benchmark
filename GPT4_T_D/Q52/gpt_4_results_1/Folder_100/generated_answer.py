
def palindrome_of_length_n(string):
    string = string.lower()
    s_set = set()
    for i in range(len(string)):
        if i+91 > len(string):
            break
        substr = string[i:i+91]
        if substr == substr[::-1]:
            if substr.isalpha():
                s_set.add(substr)
    return s_set
