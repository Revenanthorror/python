import re

def check_password(password):
    if len(password) < 12:
        return "Invalid"
    
    valid_chars_pattern = r'^[A-Za-z0-9!@#$%&*+]+$'
    if not re.match(valid_chars_pattern, password):
        return "Invalid"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in '!@#$%&*+' for c in password)
    
    if has_upper and has_lower and has_digit and has_special:
        return "Valid"
    else:
        return "Invalid"

def main():
    try:
        n = int(input("Введите количество паролей: "))
    except (ValueError, EOFError):
        return

    for _ in range(n):
        pwd = input().strip()
        print(check_password(pwd))

if __name__ == "__main__":
    main()