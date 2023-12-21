
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the substring from index 155 to index 283
    substr = string[154:284]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i+103, min(i+121, len(substr))):
            if substr[i:j] == substr[i:j][::-1]:
                palindromes.add(substr[i:j])
    return palindromes
