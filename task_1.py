import fnmatch

n = 3146
mask = '1*7[2-3]1?4'
sp1 = []

for num in range(1, 10**9 + 1):
    num_str = str(num)
    if fnmatch.fnmatch(num_str, mask):
        if num % n == 0:
            sp1.append(num // n)

print(sp1)