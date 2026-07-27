import re

def check_rule(rule):
    for i, value in enumerate(rule):
        if value is False:
            print("\nBetter password need atleast: ")
            break
    else:
        print("Valid!")

    if rule[0] is False:
        print("8 characters")
    if rule[1] is False:
        print("one uppercase")
    if rule[2] is False:
        print("one lowercase")
    if rule[3] is False:
        print("one digit")
    if rule[4] is False:
        print("one special character")

    print()

def check_length(password):
    if len(password) >= 8:
        return True
    else:
        return False


def check_uppercase(password):
    return bool(re.search(r"[A-Z]", password))


def check_lowercase(password):
    return bool(re.search(r"[a-z]", password))

def check_digit(password):
    return bool(re.search(r"[0-9]", password))
    
def check_special_char(password):
    return bool(re.search(r"[!@#$%^&*]", password))
    

while True:
    password = input("Enter password: ")
    if not password:
        print("Password cannot be empty.\n")
        continue
    
    with open("common_passwords.txt", 'r', encoding="utf-8") as f:
        common_password = f.read().splitlines()
        if password in common_password:
            print("Password was found in common list. Try another one.\n")
            continue
    
    break

rule = [
    check_length(password),
    check_uppercase(password),
    check_lowercase(password),
    check_digit(password),
    check_special_char(password)
]

score = 0
for value in rule:
    if value is True:
        score += 1

print(f"\nScore: {score}/5")
if score <= 2:
    print("Weak Password!\n")
elif score <= 4:
    print("Medium Password!\n")
else:
    print("Strong Password!\n")
    
check_rule(rule)