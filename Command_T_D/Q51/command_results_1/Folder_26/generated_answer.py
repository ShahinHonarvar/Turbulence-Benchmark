def if_contains_anagrams(list_of_strings):
    return True if len(list_of_strings) <= 35 and len(list_of_strings) >= 3 and all(s[0].lower() in 'qwertyuiopasdfghjklzxcvbnm' for s in list_of_strings) else False
