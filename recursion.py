def sumOfDigits(num):
    num = str(num)
    if len(num) == 1:
        return num
    else:
        return int(num[0]) + int(sumOfDigits(num[1:]))


def sumOfNaturals(n):
    if n == 0:
        return n
    else:
        return n - 1 + sumOfNaturals(n - 1)


# print(sumOfNaturals(20))
# s = sumOfDigits(484903)
# print(s)

def hcf(n1, n2):
    if n1 < n2:
        small = n1
    elif n2 < n1:
        small = n2
    else:
        return n1
    while small > 0:
        if n1 % small == 0 and n2 % small == 0:
            return small
        small -= 1


def hcf_recursion(n1, n2, small):
    if n1 % small == 0 and n2 % small == 0:
        return small
    else:
        return hcf_recursion(n1, n2, small - 1)


def lcm(n1, n2, small):
    h = hcf_recursion(n1, n2, small)
    return (n1 * n2) // h


n1 = 15
n2 = 100
small = 0
small = (n1 if n1 < n2 else n2)
h = hcf_recursion(n1, n2, small)
l = lcm(n1, n2, small)
print(h)
print(l)
