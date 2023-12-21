
def palindromes_of_specific_lengths(string):
    substring = string[26:91].lower()
    palindromes = set()
    for length in range(27, 59):
        for i in range(len(substring) - length + 1):
            current_substring = substring[i:i+length]
            if current_substring == current_substring[::-1] and current_substring.isalpha():
                palindromes.add(current_substring)
    return palindromes
