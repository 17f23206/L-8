print("What is your name?")
name = input().lower()
if name == "anakin":
  print("How do you do Anakin!")
else:
  print(f"Nice name, {name}")
print(f"So {name}, is it hot or cold where you are today?")
weather = input().upper()
if weather == "COLD":
  print("You must be freezing!")
elif weather == "HOT":
  print("Drink plenty of water")
else:
  print("I can't advise you on that type of weather.")
print("Do you like the colour blue?")
likes_blue = input().lower()
if likes_blue == "Yes":
  print("I like blue too")
print("Have a good day! Bye!")
print("wait, what is your favourite dog?")
dog = input().lower()
if dog == "retriever":
  print("that is my favourite dog too!")