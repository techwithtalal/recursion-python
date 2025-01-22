#
# https://youtube.com/@techwithtalal
#
# Tech With Talal
#

number = 5

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)

print(factorial(number)) # 120

# Output breakdown
# factorial(5) => 5 * factorial(4)
# factorial(4) => 4 * factorial(3)
# factorial(3) => 3 * factorial(2)
# factorial(2) => 2 * factorial(1)
# factorial(1) => 1 (base case)
# The result is 5 * 4 * 3 * 2 * 1 = 120