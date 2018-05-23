import sys

friend = sys.stdin.readline()
friend = friend[:-1]

if friend == "gordo" or friend == "sam":
    greeting = "Suuup dude"
elif friend == "kyle" or friend == "sam":
    greeting = "Greetings mister {}, how are we doing today?".format(friend)
else:
    greeting = "I don't know you, I hate you"

print greeting

