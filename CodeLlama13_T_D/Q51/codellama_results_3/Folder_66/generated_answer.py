
def if_contains_anagrams(string_list):
    anagram_pairs = set()
    for string in string_list:
        anagrams = get_anagrams(string)
        for anagram in anagrams:
            if len(anagram) >= 3 and anagram not in anagram_pairs:
                anagram_pairs.add((anagram, string))
    return len(anagram_pairs) <= 64
```
The function `if_contains_anagrams` takes a list of strings as its argument. It first creates an empty set called `anagram_pairs`, which will store all the pairs of anagrams that are found in the given list. Then, it iterates through each string in the list and uses the function `get_anagrams` to find all the anagrams of that string. The function `get_anagrams` returns a set of strings that are anagrams of the input string.

The next step is to iterate through each anagram found in the previous step, and check if it meets the criteria for being considered an anagram pair:

1. The length of the anagram should be at least 3 characters long.
2. The anagram should not already be present in `anagram_pairs`.

If both conditions are met, then the anagram and its original string are added to `anagram_pairs`.

Finally, the function returns `True` if the number of anagram pairs found is less than or equal to 64, and `False` otherwise.

Here's a helper function that finds all the anagrams of a given string:
```
def get_anagrams(string):
    return set("".join(sorted(c)) for c in itertools.permutations(string))
