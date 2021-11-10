# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.

greatest_product = 0
for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        product = x * y
        if str(product) == str(product)[::-1]:
            if product > greatest_product:
                greatest_product = product
print(greatest_product)


