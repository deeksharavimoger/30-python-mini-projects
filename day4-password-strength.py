import string

print("🔐 Password Strength Checker")

password = input("Enter your password: ")

length_ok = len(password) >=8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(char in string.punctuation for char in password)

score = sum([length_ok, has_upper, has_lower, has_digit, has_symbol])

if score == 5:
    print("Strong password💪🔥")

elif 3 <= score <5:
    print("Medium password ⚠️")

else:
    print("Weak password ❌")