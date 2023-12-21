
def palindromes_of_specific_lengths(string):
    # Get the substring from index 35 to 88, both inclusive
    substr = string[34:89]
    
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each length between 24 and 33 (both inclusive)
    for length in range(24, 34):
        # Get all possible combinations of a palindrome with the given length
        combos = [''.join(x) for x in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=length)]
        
        # Iterate over each combination and check if it is a palindrome
        for combo in combos:
            if combo == combo[::-1] and len(combo) == length:
                # Add the palindrome to the set
                palindromes.add(combo)
    
    return palindromes
