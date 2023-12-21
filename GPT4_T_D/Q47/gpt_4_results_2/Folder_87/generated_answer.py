
def palindromes_of_specific_lengths(string):
    string = string[11:94].lower() 
    result_set = set()
    for length in range(34, 55):
        for i in range(len(string) - length + 1):
            substr = string[i:i+length]
            if substr == substr[::-1] and substr.isalpha():
                result_set.add(substr)
           
    return result_set
