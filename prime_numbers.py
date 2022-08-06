#####  SUMMATION OF PRIME NUMBERS LESS THAN A GIVEN NUMBER  #####

print("Enter any number greater than 2")

# Take input from user
num1 = int(input("Enter your number : "))
sum = 0
prime_numbers = [2]

#Code stops if user input is less than 2
if num1 <= 2:
    print("Sum of all prime numbers less than", num1, ":", 0)

#iterate through to find prime numbers
for num in range(2, num1 - 1):
    i = 2
    for i in range(2, num):
        if (int(num % i) == 0):
            i = num
            break;

    #If the number is prime then add it.
    if i != num:
        sum += num
        prime_numbers.append(num)

print("This is the list of prime numbers to be added:"," ",prime_numbers)
print("Sum of all prime numbers less than", num1, ":", sum)