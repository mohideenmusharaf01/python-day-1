# Question 1
n = int(input("Enter N: "))
number = int(input("Enter number: "))

print("Primes:", end=" ")
for i in range(2, n + 1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")

factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("\nFactorial:", factorial)

a, b = 0, 1
print("Fibonacci:", end=" ")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

temp = number
digit_sum = 0
reverse = 0

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    reverse = reverse * 10 + digit
    temp //= 10

print("\nDigit Sum:", digit_sum)
print("Reverse:", reverse)



# Question 2
n = int(input("\nEnter pattern size: "))

print("Right Triangle")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

print("\nPyramid")
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

print("\nNumber Triangle")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\nMultiplication Grid")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}", end="   ")
    print()



# Question 3
text = input("\nEnter a string: ")

reverse_loop = ""
for char in text:
    reverse_loop = char + reverse_loop

reverse_slice = text[::-1]

cleaned = ""
for char in text:
    if char != " ":
        cleaned += char.lower()

is_palindrome = cleaned == cleaned[::-1]

vowels = 0
consonants = 0
digits = 0

for char in text:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Loop Reverse:", reverse_loop)
print("Slice Reverse:", reverse_slice)
print("Palindrome:", "Yes" if is_palindrome else "No")
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)



# Question 4
customer = input("\nCustomer: ")
units = int(input("Units: "))

if units <= 100:
    amount = units * 3.50
elif units <= 200:
    amount = 100 * 3.50 + (units - 100) * 5.00
elif units <= 300:
    amount = 100 * 3.50 + 100 * 5.00 + (units - 200) * 7.00
else:
    amount = 100 * 3.50 + 100 * 5.00 + 100 * 7.00 + (units - 300) * 8.50

print(f"Customer : {customer}")
print(f"Units : {units}")
print(f"Amount : ₹{amount:.2f}")



# Question 5
amount = int(input("\nWithdrawal Amount: "))

if amount > 20000 or amount % 10 != 0:
    print("Transaction Rejected")
else:
    remaining = amount
    notes_500 = remaining // 500
    remaining %= 500

    notes_200 = remaining // 200
    remaining %= 200

    notes_100 = remaining // 100
    remaining %= 100

    notes_50 = remaining // 50
    remaining %= 50

    notes_10 = remaining // 10

    total_notes = notes_500 + notes_200 + notes_100 + notes_50 + notes_10

    print(f"₹500 notes : {notes_500}")
    print(f"₹200 notes : {notes_200}")
    print(f"₹100 notes : {notes_100}")
    print(f"₹50 notes : {notes_50}")
    print(f"₹10 notes : {notes_10}")
    print(f"Total Notes : {total_notes}")
    print(f"Amount : ₹{amount}")



# Question 6
entry = input("\nEntry Time: ")
exit_time = input("Exit Time: ")

entry_hour, entry_minute = map(int, entry.split(":"))
exit_hour, exit_minute = map(int, exit_time.split(":"))

entry_total = entry_hour * 60 + entry_minute
exit_total = exit_hour * 60 + exit_minute

if exit_total < entry_total:
    exit_total += 24 * 60

duration = exit_total - entry_total
hours = duration // 60
minutes = duration % 60

billable_hours = (duration + 59) // 60

if billable_hours <= 1:
    fee = 30
else:
    fee = 30 + (billable_hours - 1) * 20

print(f"Parking Duration : {hours} hours {minutes} minutes")
print(f"Billable Hours : {billable_hours}")
print(f"Parking Fee : ₹{fee}")



# Question 7
deliveries = int(input("\nNumber of Deliveries: "))

total_distance = 0
total_earnings = 0

for i in range(1, deliveries + 1):
    distance = float(input(f"Distance for delivery {i}: "))
    total_distance += distance

    if distance <= 5:
        earnings = 40
    else:
        earnings = 40 + (distance - 5) * 8

    total_earnings += earnings

average_distance = total_distance / deliveries

print(f"Total Distance : {total_distance:.2f} km")
print(f"Total Earnings : ₹{total_earnings:.2f}")
print(f"Average Distance : {average_distance:.2f} km")



# Question 8
x = int(input("\nEnter integer: "))

sign = -1 if x < 0 else 1
x = abs(x)
reverse = 0

while x > 0:
    digit = x % 10
    reverse = reverse * 10 + digit
    x //= 10

print(sign * reverse)



# Question 9
x = int(input("\nEnter integer: "))

if x < 0:
    print(False)
else:
    original = x
    reverse = 0

    while x > 0:
        digit = x % 10
        reverse = reverse * 10 + digit
        x //= 10

    print(original == reverse)



# Question 10
n = int(input("\nEnter N: "))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
