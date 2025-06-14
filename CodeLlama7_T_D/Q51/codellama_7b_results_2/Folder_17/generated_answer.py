
def if_contains_anagrams(my_list):
    # Define a function to check if two strings are anagrams
    def is_anagram(str1, str2):
        # Convert both strings to lowercase
        str1 = str1.lower()
        str2 = str2.lower()
        # Sort the characters of each string
        sorted_str1 = ''.join(sorted(str1))
        sorted_str2 = ''.join(sorted(str2))
        # Return True if the strings are anagrams, False otherwise
        return sorted_str1 == sorted_str2
    # Define a function to count the number of anagrams in a list of strings
    def count_anagrams(my_list):
        count = 0
        for i in range(len(my_list) - 1):
            for j in range(i + 1, len(my_list)):
                if is_anagram(my_list[i], my_list[j])):
                    count += 1
        return count
    # Return True if there are at most 22 pairs of anagrams in the list, False otherwise
    return count_anagrams(my_list) <= 22
