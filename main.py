# main.py
from checker import evaluate_password, is_strong

def display_results(checks):
    print("\nPassword Strength Check:")
    for key, passed in checks.items():
        status = "✅" if passed else "❌"
        print(f"{key.capitalize():<10}: {status}")
    
    if is_strong(checks):
        print("\n✅ Your password is strong!")
    else:
        print("\n❌ Your password is weak. Try improving it based on the failed checks.")

def main():
    password = input("Enter a password to check: ")
    checks = evaluate_password(password)
    display_results(checks)

if __name__ == "__main__":
    main()
