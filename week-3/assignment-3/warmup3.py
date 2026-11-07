
# False because not True is False, and False and False is False.
print(not True and False)

# True because and is evaluated before or, leaving True or False.
print(True or False and False)

# False because 5 is greater than 3, so not True becomes False.
print(not (5 > 3))

# False because the first expression is True and the last is False.
print(10 == 10 and 4 != 4)

# True because not False is True, not True is False.
print(not False or not True)
