# QUESTION1. Type Casting & Numeric Operations

try:
    integer_value = int(input("Integer: "))
    decimal_value = float(input("Decimal: "))
    print(f"Integer Value : {integer_value}")
    print(f"Integer Type : {type(integer_value).__name__}")
    print(f"Float Value : {decimal_value}")
    print(f"Float Type : {type(decimal_value).__name__}")
    print(f"Rounded Value : {round(decimal_value)}")
    divisor = int(decimal_value)
    print(f"{integer_value} / {divisor} = {integer_value / divisor:.4f}")
    print(f"{integer_value} // {divisor} = {integer_value // divisor}")
    print(f"{integer_value} % {divisor} = {integer_value % divisor}")
    print(f"{integer_value} ** 2 = {integer_value ** 2}")
    print(f"String Value : {str(integer_value)}")
except (ValueError, ZeroDivisionError):
    print("Invalid numeric input")

# QUESTION2. Caesar Cipher

message = input("Message: ")
shift = int(input("Shift: "))

def caesar(text, amount):
    result = ""
    for char in text:
        if "A" <= char <= "Z":
            result += chr((ord(char) - 65 + amount) % 26 + 65)
        elif "a" <= char <= "z":
            result += chr((ord(char) - 97 + amount) % 26 + 97)
        else:
            result += char
    return result

encrypted = caesar(message, shift)
print("Encrypted:", encrypted)
print("Decrypted:", caesar(encrypted, -shift))

# QUESTION 3. Number Analyzer

start = int(input("Start: "))
end = int(input("End: "))
print("Number Prime Perfect Armstrong Palindrome Digit Sum Digits Binary")

for number in range(start, end + 1):
    prime = number >= 2
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break

    divisor_sum = sum(i for i in range(1, number) if number % i == 0)
    perfect = number > 1 and divisor_sum == number

    digits = 1 if number == 0 else len(str(number))
    temp = number
    digit_sum = 0
    reverse = 0
    armstrong_sum = 0
    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        reverse = reverse * 10 + digit
        armstrong_sum += digit ** digits
        temp //= 10

    palindrome = number == reverse
    armstrong = number == armstrong_sum

    if number == 0:
        binary = "0"
    else:
        temp = number
        binary = ""
        while temp:
            binary = str(temp % 2) + binary
            temp //= 2

    print(number, "Yes" if prime else "No", "Yes" if perfect else "No",
          "Yes" if armstrong else "No", "Yes" if palindrome else "No",
          digit_sum, digits, binary)

# 4. Number System Converter + GCD/LCM

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

def convert_base(number, base):
    digits = "0123456789ABCDEF"
    if number == 0:
        return "0"
    result = ""
    while number:
        result = digits[number % base] + result
        number //= base
    return result

a, b = number1, number2
while b:
    a, b = b, a % b

gcd = a
lcm = abs(number1 * number2) // gcd if gcd else 0

print("Binary :", convert_base(number1, 2))
print("Octal :", convert_base(number1, 8))
print("Hexadecimal :", convert_base(number1, 16))
print("GCD :", gcd)
print("LCM :", lcm)

#QUESTION 5. Two-Divisor FizzBuzz

n = int(input("N: "))
divisor1 = int(input("Divisor 1: "))
word1 = input("Word 1: ")
divisor2 = int(input("Divisor 2: "))
word2 = input("Word 2: ")

for i in range(1, n + 1):
    if i % divisor1 == 0 and i % divisor2 == 0:
        print(word1 + word2)
    elif i % divisor1 == 0:
        print(word1)
    elif i % divisor2 == 0:
        print(word2)
    else:
        print(i)

# QUESTION 6. Student Mark Conversion & Result Analyzer

students = int(input("Students: "))
print("Student Total Average Grade")

for _ in range(students):
    data = input().split(":")
    name = data[0].strip()
    try:
        marks = [float(x) for x in data[1].split()]
        if any(mark < 0 or mark > 100 for mark in marks):
            print(name, "Invalid marks")
            continue

        total = sum(marks)
        average = total / len(marks)

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        print(f"{name} {total:.0f} {average:.2f} {grade}")
    except (ValueError, IndexError):
        print(name, "Invalid marks")

# QUESTION7. Digital Payment Transaction Analyzer

transactions = int(input("Transactions: "))
successful = []
rejected = 0

for _ in range(transactions):
    try:
        amount = float(input())
        if amount < 0:
            rejected += 1
        else:
            successful.append(amount)
    except ValueError:
        rejected += 1

print(f"Successful Transactions : {len(successful)}")
if successful:
    total = sum(successful)
    print(f"Total Amount : ₹{total:.2f}")
    print(f"Highest Transaction : ₹{max(successful):.2f}")
    print(f"Lowest Transaction : ₹{min(successful):.2f}")
    print(f"Average Transaction : ₹{total / len(successful):.2f}")
else:
    print("Total Amount : ₹0.00")
    print("Highest Transaction : ₹0.00")
    print("Lowest Transaction : ₹0.00")
    print("Average Transaction : ₹0.00")
print(f"Rejected Transactions : {rejected}")

# QUESTION 8. LeetCode #8 - String to Integer (atoi)

s = input("Input: ")
i = 0

while i < len(s) and s[i] == " ":
    i += 1

sign = 1
if i < len(s) and s[i] in "+-":
    if s[i] == "-":
        sign = -1
    i += 1

number = 0
while i < len(s) and "0" <= s[i] <= "9":
    number = number * 10 + ord(s[i]) - ord("0")
    i += 1

print(sign * number)

# QUESTION 9. LeetCode #67 - Add Binary

a = input("a = ")
b = input("b = ")

i = len(a) - 1
j = len(b) - 1
carry = 0
result = ""

while i >= 0 or j >= 0 or carry:
    total = carry
    if i >= 0:
        total += ord(a[i]) - ord("0")
        i -= 1
    if j >= 0:
        total += ord(b[j]) - ord("0")
        j -= 1

    result = str(total % 2) + result
    carry = total // 2

print(result)

# QUESTION 10. LeetCode #202 - Happy Number

number = int(input("Enter number: "))
seen = set()

while number != 1 and number not in seen:
    seen.add(number)
    total = 0
    while number:
        digit = number % 10
        total += digit * digit
        number //= 10
    number = total

print(number == 1)
