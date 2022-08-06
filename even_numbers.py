#Finding the sum and displaying the even numbers less than a number

#Taking a number from the user
num1 = int(input('Enter your number: '))
i = 1
sum = 0

#Setting an empty list to contain the even numbers
num = []

while i < num1:
    if i%2 ==0:
        sum = sum +i
#This command add i each time its satifies the condition
        num.append(i)
    i += 1

print(num)
print("The sum of even numbers less than", num1, "is", sum)