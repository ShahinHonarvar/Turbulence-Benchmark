
def if_contains_anagrams(my_list):
    # Get the number of anagrams in the list
    num_anagrams = len([i for i in my_list if is_anagram(i)])
    # Return True if there are at most 58 pairs of anagrams, False otherwise
    return num_anagrams <= 58

def is_anagram(str1):
    # Convert the string to lowercase for case-insensitive comparison
    str2 = str1.lower()
    # Check if the string is a palindrome (i.e., the same string read from both ends)
    if str2 == "".join(reversed(str2)):
        # Get the frequency of each letter in the string
        freq = [str2.count(chr(i)) for i in range(97, 123)]
        # Check if there are at most 58 pairs of letters with the same frequency
        return all([freq[i] <= 58 * (i + 1) for i in range(26)])
    else:
        # If the string is not a palindrome, then it cannot be an anagram
        return False
