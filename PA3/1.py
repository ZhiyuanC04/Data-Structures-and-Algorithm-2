def func4(edi, esi, edx):
    eax = edx - esi
    eax += eax >> 31
    ebx = (eax >> 1) + esi
    if ebx > edi:
        return func4(edi, esi, ebx - 1) + ebx
    elif ebx < edi:
        return func4(edi, ebx + 1, edx) + ebx
    else:
        return ebx

# Find the first input value that satisfies the conditions
for i in range(14):
    if func4(i, 0, 14) == 18:
        print("First input value:", i)
        break
