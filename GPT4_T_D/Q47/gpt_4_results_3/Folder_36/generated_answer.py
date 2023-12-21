
def palindromes_of_specific_lengths(my_str):
    def is_palindrome(s):
        return s == s[::-1] and s.isalpha()
      
    substring = my_str[124:284].lower()
    palindromes = set()

    for length in range(115, 135):
        for i in range(len(substring) - length + 1):
            substring_potential_p = substring[i:i+length]
            if is_palindrome(substring_potential_p):
                palindromes.add(substring_potential_p)
                
    return palindromes
