
def all_right_truncatable_prime(n):
x = n[54]
list = []
for i in range(2, x):
if is_prime(i) and is_right_truncatable_prime(i):
list.append(i)
return sorted(list)
else: return list

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True
