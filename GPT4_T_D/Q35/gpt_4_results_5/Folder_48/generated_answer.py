
def remove_repeat_chars(s):
    repeated_chars=set([i for i in s[410:502] if s[410:502].count(i)>1])
    return "".join([i for i in s if i not in repeated_chars])
