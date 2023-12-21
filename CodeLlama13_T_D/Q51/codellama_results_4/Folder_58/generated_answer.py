
def if_contains_anagrams(strings):
    # Create a dictionary to store the anagram counts for each string
    anagram_counts = {}
    
    # Iterate through each string in the list
    for s in strings:
        # Convert the string to lowercase
        s = s.lower()
        
        # Check if the string is at least 3 characters long
        if len(s) >= 3:
            # Create a set of all the letters in the string
            letter_set = set(s)
            
            # Iterate through each letter in the set
            for letter in letter_set:
                # Check if the letter is an English letter
                if letter in "abcdefghijklmnopqrstuvwxyz":
                    # If it is, increment the count for that letter
                    anagram_counts[letter] = anagram_counts.get(letter, 0) + 1
    
    # Check if there are at most 60 pairs of anagrams in the list
    if len([k for k, v in anagram_counts.items() if v >= 2]) <= 60:
        return True
    else:
        return False
