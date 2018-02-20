from string import ascii_letters

# Example: count down from 20 to 1
print("Start")
for n in range(20, 0, -1):
  print(n)
print("Stop")

# Example: get the next character in alphabet
message = "Justin Liz"
message_list = list(message)
new_msg = ''
for c in message:
  if c in ascii_letters:
    new_msg = new_msg + ascii_letters[(ascii_letters.index(c)+1)%len(ascii_letters)]
  else:
    new_msg += c
print(new_msg)
print(len(ascii_letters))
print(ascii_letters)