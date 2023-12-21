import re
def find_divisors_in_range(n):
    if n < 48 or n > 92:
        return []
    else:
        str_n = str(n)
        match = re.findall(r'(\d+)', str_n)
        if match:
            if int(match[0]) <= int(str(n)) // 2:
                return [int(i) for i in str_n.split('/')]
        else:
            return []
