
def palindromes_of_specific_lengths(string):
    result = set()
    substring = string[41:90].lower()
    
    for i in range(len(substring)):
        for length in range(23, 39):
            if i + length <= len(substring):
                substr = substring[i:i+length]
                if substr == substr[::-1] and substr.isalpha():
                    result.add(substr)
    
    return result
