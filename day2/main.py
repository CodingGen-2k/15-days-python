#  operators

'''
a = 10
b = 3
print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.33
print(a // b) # Floor Division: 3
print(a % b)  # Modulus: 1
print(a ** b) # Exponentiation: 1000

a = 5
b = 7
print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True


x = 5
print(x > 3 and x < 10)  # True
print(x < 3 or x > 4)    # True
print(not(x > 3))        # False



x = 10
x += 5  # x = x + 5 → 15
x -= 3  # x = x - 3 → 12
x *= 2  # x = x * 2 → 24
x /= 6  # x = x / 6 → 4.0
x %= 2  # x = x % 2 → 0.0


a = [1, 2]
b = a
c = [1, 2]

print(a is b)      # True
print(a is c)      # False
print(a is not c)  # True


fruits = ['apple', 'banana']
print('apple' in fruits)      # True
print('mango' not in fruits)  # True'''


#  strings 

# a = "codingGen"
# b = 'codingGEn'
# c = '''codingGEn'''
# print(a[5])
# print(a[-4])
# print(a[6:])


# a = "  codingGen  "

# print(a.upper())
# print(a.lower())
# print(a.title())
# print(a.strip())
# print(a.replace("codingGen", "code"))
# print(a.find("Gen"))



name = input("name: ")
# mail = f"dear {name}, i hoope you are doing well!"
# mail = "dear {}, i hoope you are doing well!".format(name)
mail = "dear " + name + ", i hoope you are doing well!"
print(mail)
