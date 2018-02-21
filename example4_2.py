"""example4_2 counts down from 20 to 1, and get the next character in alphabet."""

from string import ascii_letters

# Example: count down from 20 to 1
print("Start")
for n in range(20, 0, -1):
    print("n=", n)
print("Stop")

# Example: get the next character in alphabet
message = 'JL'
new_msg = ''
for c in message:
    if c in ascii_letters:
        new_msg = new_msg + ascii_letters[(ascii_letters.index(c)+1)%len(ascii_letters)]
    else:
        new_msg += c
print(new_msg)
print(len(ascii_letters))
print(ascii_letters)

a, b = 0, 1
while b < 10:
    print("b=", b)
    a, b = b, a+b
print(a, b)

msg = "Justin Liz"
new_msg = ''
for c in msg:
    newChar = chr(ord(c)+1)
    print(newChar)
