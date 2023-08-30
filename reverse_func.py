#Task one
#Write a function to reverse a string.
#do not use strin methods
#create your own algorithm
#for example
#Olowogold =  dlogowolo
#Tosin =nisoT
#Idris = sirdi
#ojure = erujo
#use  the examples to test your code
def reverse(string):
  reversed_string = ""
  for k in string:
   reversed_string = k+reversed_string
  result = 'reversed string is:',reversed_string.lower()
  return result
   
#strin = reverse('string')
#print(strin)


#algorithm
#input  string: string
#break input string into each character: s  t  r  i  n  g
#reassemble string from the end: g  n  i   r  t  s

#Code Tester
def test_reversed_words():
  #input values
  string = 'tosin idris banana Rotator ojure Olowogold Deified'
  reverse_checker = reverse(string)
  print(reverse_checker)  

test_reversed_words()


#Task  two
#write a function to check if a string is a palindrome.
#your funcion should return. is_palindrome
#assume  All  letters are in the  same  case
#for example
#anna = is_palindrome
#Madam=is_palindrome
#banana= not_palindrome
#Rotator=is_palindrome
#Olowogold= not_palindrome
#Deified=is_palindrome

def find_palindrome(value):
  
  """This function  checks if a string palindrome:
    Usage: This function tasks a string  argument (value) """

  #prompt user for data 
  input_value = '' #input('Enter value: ')

  #update initial value if input data is empty
  if input_value:
    value = input_value
  
  print(f"{value}")
  
  reverse = value[::-1] 
  
  if value == reverse:
    results = "is_palindrome"
  else:
    results = "not_palindrome"
  return results
    
  #return results

#final_results = find_palindrome('value')
#print(final_results)


def test_palindrome():
  #input values
  value = ['tosin','idris','banana','Rotator',
           'Olowogold','Deified']  
  input_csv ='' #input('Enter CSV: ')

  #update value if input_csv is empty
  if input_csv:
    value = input_csv.split(',')
  print(f'{value}')
  
  for var in value:
    palindrome_checker = find_palindrome(var.lower())
    print(palindrome_checker)

#test_palindrome()



def calc_BMI(initial_name, initial_weight, initial_height):

  #input section: prompt the user for data
  input_name = input('Enter name: ')
  input_weight = input('Enter weight: ')
  input_height = input('Enter height: ')
  
  #print section
  #print(f"{initial_name},{initial_weight},{initial_height}")
  #print('input data:', input_name, input_weight, input_height)


  #update condition:  check if string is non-empty
  if input_name:
    initial_name=input_name
    
  if input_weight:
    initial_weight=int(input_weight)
    
  if input_height:
    initial_height=float(input_height)

  #final print
  #print(f"{initial_name},{initial_weight},{initial_height}")
  BMI=initial_weight/initial_height
  
  return f"{BMI} is the BMI for {initial_name}"
  
#initial_name
#bmi = calc_BMI("Olowogold",85,1.65)
#print(bmi)




input_name=''#input('Enter name')
input_weight =''#input('Enter weight')
input_height =''#input('Enter height')

if input_name:
  initial_name=input_name

if input_weight:
  initial_weight=input_weight

if input_height:
  initial_height=input_height
  



s= 'ioun  iyu uii'
k = s.split(" ")
#print(k)
#for  char  in s:
#  print(char)
#for item in k:
#  print(item)

#to check for something in algorithm: use if statement
