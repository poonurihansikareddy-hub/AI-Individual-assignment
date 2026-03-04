import random

def math_captcha():
    a = random.randint(1,20)
    b = random.randint(1,20)

    print("\nMath CAPTCHA")
    print("Solve:", a, "+", b)

    user = int(input("Your answer: "))

    if user == a + b:
        print("PASS - Human verified")
    else:
        print("FAIL - Bot detected")


def logic_captcha():

    questions = {
        "What comes after Tuesday?": "Wednesday",
        "How many days are in a week?": "7",
        "What color is the sky on a clear day?": "blue"
    }

    q = random.choice(list(questions.keys()))
    answer = questions[q]

    print("\nLogic CAPTCHA")
    print(q)

    user = input("Your answer: ").strip()

    if user.lower() == answer.lower():
        print("PASS - Human verified")
    else:
        print("FAIL - Bot detected")


def text_captcha():

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    captcha = ""

    for i in range(5):
        captcha += random.choice(letters)

    print("\nText CAPTCHA")
    print("Type this text:", captcha)

    user = input("Enter text: ")

    if user == captcha:
        print("PASS - Human verified")
    else:
        print("FAIL - Bot detected")


def run_captcha():

    print("\nCAPTCHA SYSTEM")

    choice = random.choice(["math", "logic", "text"])

    if choice == "math":
        math_captcha()

    elif choice == "logic":
        logic_captcha()

    else:
        text_captcha()


if __name__ == "__main__":
    run_captcha()