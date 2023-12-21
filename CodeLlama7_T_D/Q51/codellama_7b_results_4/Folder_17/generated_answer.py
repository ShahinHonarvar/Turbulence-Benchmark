
def if_contains_anagrams(words):
    # Create a set of all possible anagrams of the English letters
    anagram_set = set([])
    for i in range(26):
        for j in range(i+1, 27):
            anagram_set.add(''.join(sorted(chr(ord('a') + i) + chr(ord('a') + j))))
    # Initialize a counter for the number of anagrams found
    num_anagrams = 0

    # Iterate over each word in the list
    for word in words:
        # Convert the word to lowercase
        word = word.lower()

        # Check if the word is a palindrome
        if word == word[::-1]:
            continue

        # Split the word into its individual characters
        chars = [c for c in word]

        # Create a list of all possible anagrams of the word
        anagrams = []
        for i in range(len(chars)):
            for j in range(i+1, len(chars)+1):
                anagrams.append(''.join(sorted(chars[i:j]))))

        # Check if any of the anagrams are also palindromes
        for a in anagrams:
            if a == a[::-1]:
                num_anagrams += 1
                        
    # If there are at most 22 pairs of anagrams in the list, return True. Otherwise, return False.
    return num_anagrams <= 22
