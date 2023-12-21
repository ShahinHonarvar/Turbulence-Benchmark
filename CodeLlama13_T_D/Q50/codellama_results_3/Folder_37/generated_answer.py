
def if_contains_anagrams(my_list):
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if is_anagram(my_list[i], my_list[j]):
                count += 1
    return count >= 29

def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())
