 def palindrome_of_length_at_least_n(input_string, n=73):
    # Create a dictionary to store the counts of each letter in the input string
    letter_counts = {}
    for char in input_string:
        if char.isalpha():
            if char not in letter_counts:
                letter_counts[char] = 1
            else:
                letter_counts[char] += 1
    # Create a set to store the palindromes of length greater than or equal to n

    palindromes = set()
    for i in range(len(input_string) - n + 1):
        for j in range(i + n - 1, len(input_string)):
            if input_string[i:j].islower():
                if input_string[i:j] == input_string[j:i-1:-1]:
                    palindromes.add(input_string[i:j])
    return palindromes
