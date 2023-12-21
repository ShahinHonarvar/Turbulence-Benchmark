
def palindromes_between_indices(string):
    english_letters = [char.lower() for char in string if char.isalpha()]
    palindrome_set = set()
    
    for i in range(len(english_letters) - 2):
        if english_letters[i:i+3] == english_letters[i:i+3][::-1]:
            palindrome_set.add(''.join(english_letters[i:i+3]))
    
    return palindrome_set
