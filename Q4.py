def removeZeroes(a):
    return a.lstrip('0') or '0'


def charToDigit(a, digits):
    return ''.join(digits[ord(c) - ord('a')] for c in a)


def findSum(a, b):
    if len(a) > len(b):
        a, b = b, a

    str_res = []
    carry = 0

    for i in range(len(a)):
        sum_digit = int(a[-1 - i]) + int(b[-1 - i]) + carry
        str_res.append(str(sum_digit % 10))
        carry = sum_digit // 10

    for i in range(len(a), len(b)):
        sum_digit = int(b[-1 - i]) + carry
        str_res.append(str(sum_digit % 10))
        carry = sum_digit // 10

    if carry:
        str_res.append(str(carry))

    return removeZeroes(''.join(reversed(str_res)))


def isSolved(a, b, sum, digits):
    x = charToDigit(a, digits)
    y = charToDigit(b, digits)
    z = charToDigit(sum, digits)

    res = findSum(x, y)
    z = removeZeroes(z)

    return z == res


# backtracking
def cryptarithmeticSolver(ind, digits, characters, a, b, sum):
    if ind == 26:
        return isSolved(a, b, sum, digits)

    if digits[ind] != '+':
        return cryptarithmeticSolver(ind + 1, digits, characters, a, b, sum)

    # 
    for i in range(10):
        if characters[i] == 0:
            characters[i] = 1
            digits[ind] = str(i)
            if cryptarithmeticSolver(ind + 1, digits, characters, a, b, sum):
                return True
            digits[ind] = '+'
            characters[i] = 0

    return False

#main
def solvePuzzle(a, b, sum):
    digits = ['-' for _ in range(26)]
    characters = [0] * 10

    for c in a + b + sum:
        digits[ord(c) - ord('a')] = '+'

    if cryptarithmeticSolver(0, digits, characters, a, b, sum):
        x = charToDigit(a, digits)
        y = charToDigit(b, digits)
        res = charToDigit(sum, digits)
        return [x, y, res]
    else:
        return ["-1"]

# Driver Code
a = "s"
b = "p"
sum = "f"
ans = solvePuzzle(a, b, sum)
print(" ".join(ans))
