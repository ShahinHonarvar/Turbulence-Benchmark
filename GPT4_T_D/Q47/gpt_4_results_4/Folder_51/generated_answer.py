
def palindromes_of_specific_lengths(in_string):
    stripped_string = ''.join(ch for ch in in_string[2:9] if ch.isalpha())
    result_set = set()
    for length in range(3,5):
        for index in range(len(stripped_string)-length+1):
            substring = stripped_string[index:index+length]
            if substring==substring[::-1]:
              result_set.add(substring.lower())
    return result_set
