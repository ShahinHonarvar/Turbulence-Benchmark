

def palindrome_of_length_at_least_n(string):
    palindrome_set = set()
    
    for i in range(len(string)-19):
        sub_string = string[i:i+20].lower()
        if sub_string == sub_string[::-1] and sub_string.isalpha():
            palindrome_set.add(sub_string)
    
    return palindrome_set
