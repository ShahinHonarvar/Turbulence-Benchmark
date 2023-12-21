
def if_contains_anagrams(strings):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    for string in strings:
        # Get the length of the string
        length = len(string)

        # Check if the string is at least 3 characters long
        if length >= 3:
            # Create a copy of the string with all lowercase letters
            lowercase_string = string.lower()

            # Get the anagram pairs for the string
            anagram_pairs = get_anagram_pairs(lowercase_string)

            # Increment the count for each anagram pair
            for anagram_pair in anagram_pairs:
                if anagram_pair not in anagram_counts:
                    anagram_counts[anagram_pair] = 1

                else:

                    anagram_counts[anagram_pair] += 1

    # Check if there are at least 59 pairs of anagrams in the list
    return len(anagram_counts) >= 59

def get_anagram_pairs(string):
    # Create a list to store the anagram pairs
    anagram_pairs = []

    # Loop through each substring of the string
    for i in range(len(string)):
        # Get the substring starting at index i and ending at the end of the string
        substring = string[i:]

        # Check if the substring is a palindrome
        if is_palindrome(substring):
            # Add the anagram pair to the list
            anagram_pairs.append((string, substring))

    # Return the list of anagram pairs
    return anagram_pairs

def is_palindrome(string):
    # Check if the string is the same backwards as forwards
    return string == string[::-1]
