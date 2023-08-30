#new task 1
#Write a Python program to remove all the duplicate characters from a string and return the modified string.

duplicated_string = "idgold@gggmail.com conttent: Marry has a lambb and lives in Asgardd, she is an Arsgadiann. A sibbling to Thor, son of odin while their step-brotherr is lokki."

#Algorithm
#step 1- Rewrite  the string
#step 2- Glance


def remove_duplicate(duplicated_string):
  modified = []
  for char in duplicated_string:
    if char not in modified:
      modified.append(char)
      result = "".join(modified)
  return result


#modify = remove_duplicate(duplicated_string)
#print(modify)

string = "mango tomatoes Trees keep rookie seek "


def count_dup(string):
  previouz_char = ""
  count = 1
  for char in string:
    if previouz_char == char:
      #duplicate found
      count = count + 1
    else:
      #unique char found
      count = 1
      previouz_char = char

    print(count, char)


#abc = count_dup(string)
#print(abc)

#Task 1
#Write a function that takes a string as input and returns the length of the longest
#consecutive sequence of the same character.
#Algorithm
#write a function that takes in a string
# write a for-loop to run through the string
# write an if statement to check for longest character
# use a length method(len) to count
#return the final result
listed_cars = "benz toyota subaru cheerokee corolla"


def length_of_string(listed_cars):
  counter = 1
  previous_car = ""
  for motor in listed_cars:
    if previous_car == motor:

      counter = counter + 1
    else:
      counter = 1
    print(counter, motor)
    previous_car = motor
  return previous_car


#vehicle = length_of_string(listed_cars)
#print(vehicle, '\n')

#Task 2
#Write a function to count the number of vowels in a string.

vowels = ['a', 'e', 'i', 'o', 'u']
sentence = "wetin man go do, i enter supermarket go buy groceries, my money no come reach the amount to get it from the store."

#Algorithm
#1.write a function that takes in a string
#2.introduce a counter
#3.Glance through the string with a for-loop
#4.introduce an if statement to check vowels in string
#5.Return final result


def vowel_count(sentence):
  counter = 0
  data = vowels
  for vowel_letters in sentence:
    if vowel_letters in data:
      counter += 1
      result = counter
  return result


#counting = vowel_count(sentence)
#print("The number of vowels in the sentence is:", counting)

string = "idgold@gggmail.com conttent: Marry has a lambb and lives in Asgardd, she is an Arsgadiann. A sibbling to Thor, son of odin while their step-brotherr is lokki"


def remove_dup(string):
  previouz_char = ""
  new_string = ""
  for char in string:
    if previouz_char == char:
      #duplicate found
      pass
    else:
      #unique char found
      new_string = new_string + char

    previouz_char = char
  return new_string


#abc = remove_dup(string)
#print(abc)
