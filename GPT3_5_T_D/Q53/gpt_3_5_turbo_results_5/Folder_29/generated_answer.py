
def palindrome_of_length_at_least_n(string):
    import re
    result = set()
    for i in range(len(string)-77):
        sub = string[i:i+78].lower()
        if sub == sub[::-1] and re.match(r'^[a-zA-Z]+$', sub):
            result.add(sub)
    return result
