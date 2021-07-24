
charater_name = "John"
charater_age = "35"
print("there once was a man named " + charater_name + ",")
print("he was 35 years old.")
charater_name="mike"
print("he really liked the name " + charater_name)
print("but didnt like being 25")

print("Giraffe\nAcademy")
print("Giraffe\"Academy")
print("Giraffe\Academy")

print("working with strings")
phrase="Giraffe Academy"
print(phrase)
print (phrase + " is cool")
print (phrase.lower())
print (phrase.upper())
print (phrase.lower())
print (phrase.isupper())
print (phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase[3])
print(phrase.index("a"))
print(phrase.index("Academ"))
print(phrase.replace("Giraffe", "Elephant"))

print("working with numbers")
print(3 + 4.5)
print(3 * 4 + 5)
print(3 * (4 + 5))
print(10 % 3)

my_num=5
print(my_num)
print(str(my_num))
print(str(my_num) + " my favourite number")
my_num= -5
print(abs(my_num))
print(pow(4,2))
print(max(4,2))
print(min(4,2))
print(round(4,2))

from math import *
my_num = -5
print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))

print("Getting imput from users")
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)

print("Building a Basic Calculator")
num1= input("Enter a number: ")
num2= input("Enter another number: ")
result = float(num1) + float(num2)
print(result)

print("Mad libs Game")
colour= input("Enter a colour")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + colour)
print(plural_noun + " are blue")
print("I love " + celebrity)

print("Lists")
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby" ]
friends[1]= "Mike"
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])

lucky_numbers = [4,8,15,16,23,42]
friends = ["Kevin","Karen", "Jim", "Oscar","Toby"]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
friends.pop()
friends.reverse()
friends2 = friends.copy()
print(friends)
print(friends.index("Kevin"))
print(friends.count("Toby"))

print("Tuple")
coordinates = (4,5)
print(coordinates[1])

print("Functions")
def say_hi(name,age):
    print("Hello " + name + ", you are "+ age)


say_hi("Mike ", "35")
say_hi("steve ", "70")

print ("Return Statement in python functions")
def cube(num):
    return num*num*num
result = cube(4)
print(result)
print (cube(3))

print ("if statements")
is_male =True
if is_male:
    print("you are a male")
else:
    print ("you are not a male")

is_male =True
is_tall =True
if is_male or is_tall:
    print("you are a male or tall or both")
else:
    print ("you neither male nor tall")

is_male =True
is_tall =True
if is_male and is_tall:
    print("you are a tall male")
else:
    print ("you are neither not male or not tall or both")

is_male =False
is_tall =True
if is_male and is_tall:
    print("you are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but are tall")
else:
    print ("you are not a male or not tall")

print("if statements and comparions")
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,40,5))

print("Building a Better Calculator")

num1 = float(input("Enter first number: "))
op = (input("Enter operator: "))
num1 = float(input("Enter second number: "))

if op == "+":
    print("num1 + num2")
elif op == "_":
    print("num1 - num2")
elif op == "/":
    print("num1 / num2")
elif op == "*":
    print ("num1 * num2")
else:
    print ("invalid operator")
#something is not right above, shouldnt need to put" on it and still not printing out the right out number it says error

print ("dictionaries")

print("whlie loop")
i = 1
while i <= 10:
    print(i)
    i += 1

print("done with loop")

print ("Building a Guessing Game")
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")

print("For Loop")
for letter in "Giraffe Academy":
    print(letter)
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)
#(for "" can be named anything but if you want to access it you have to print that word)
for index in range(10):
    print(index)
#what ever value in the last postion e.g 10 wouldnt be included when its printed out e.g 0-9
friends = ["Jim", "Karen", "Kevin"]
for index in range(len(friends)):
    print(friends[index])

print ("Exponent Function")
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(3,4))

print("2D lists")
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[2][1])
# it will print out row 2 and the second number will be 8 since it always starts with 0,1,2
print("2D lists and Nested Loops together")
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for row in number_grid:
    print(row)
for row in number_grid:
    for col in row:
        print(col)


print("Build a Translator")
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou" :
            translation = translation + "g"
        else:
            translation = translation + letter
    return  translation

print(translate(input("Enter a Phrase: ")))

print("Try Except")
# try except block allows programs to try out a piece of code

try:
    number = int(input("Enter a number: "))
    print(number)
except:
    # you can after the except inorder to catch a specific error e.g except valueerror
    print("invalid input")







