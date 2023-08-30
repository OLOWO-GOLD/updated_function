#Task 1
#Write a function that takes a string as input and returns the length of the longest consecutive sequence of the same character.

#Algorithm
#step 1: Glance through the string
#step 2: check for identical characters together
#step 3: count
#step 4: reset counter
#step 5: check for highest count
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
    result = previous_car
  return result

vehicle = length_of_string(listed_cars)
print(vehicle)


#Task 2
#Write a function to count the number of vowels in a string.

vowels = ['a','e','i','o','u']
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
            counter+=1
            result = counter
    return result
vehicle = vowel_count(sentence)
print(vehicle)


      