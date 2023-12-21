
def palindromes_of_specific_lengths(string):
    english_palindrome_set = set()
    substring = string[100:201]
    
    for i in range(len(substring)):
        for j in range(i+5, min(i+11, len(substring)+1)):
            sub_sub_string = substring[i:j]
            if sub_sub_string == sub_sub_string[::-1] and sub_sub_string.isalpha():
                english_palindrome_set.add(sub_sub_string.lower())
                
    return english_palindrome_set
