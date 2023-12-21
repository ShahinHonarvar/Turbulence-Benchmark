
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return gcd(gcd(lst[944], lst[814]), lst[865])
