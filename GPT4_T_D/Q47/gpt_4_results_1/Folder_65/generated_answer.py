
def palindromes_of_specific_lengths(s):
    import re
    s = s[15:96].lower()
    letters_only = re.sub(r'[^a-z]', '', s)
    palindrome_set = set()
    
    for i in range(len(letters_only)):
        for j in range(20,67):
            if i + j > len(letters_only):
                break
            sub_string = letters_only[i:i+j]
            if sub_string == sub_string[::-1]:
                palindrome_set.add(sub_string)

    return palindrome_set
