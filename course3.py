import random
import sys

secret_number = random.randint(1, 100)

print "You have 3 tries to guess my secret number."
print "If you fail, I will hold you in contempt, likely forever."


def process_user_guess(asked_count):
    print "Provide your {} value:".format(asked_count)

    value = sys.stdin.readline()
    value = value.strip()
    number = int(value)

    if number == secret_number:
        print "whoopie"
        return True

    elif number > secret_number:
        print "You guessed too high amigo"
    else:
        print "You guessed lower pendejo!"
    return False


guessed = process_user_guess("first")
if not guessed:
    guessed = process_user_guess("second")
if not guessed:
    guessed = process_user_guess("third")

print "The number was {}".format(secret_number)
