num1 = 42 #variable num1 is 42
num2 = 2.3 #variable num2 is 2.3
boolean = True #boolean datatype
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']#array
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#object
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))#print fruit
print(pizza_toppings[1])#print 2nd value from array
pizza_toppings.append('Mushrooms')#idk what append does
print(person['name'])#print name from object person
person['name'] = 'George'#change value from john to George
person['eye_color'] = 'blue'#add a new value to person obect
print(fruit[2])#print banana i think

"""                            conditional
if num1 > 45:                   if statement
    print("It's greater")       
else:                           if elsestatement
    print("It's lower")
"""
"""                               another conditional with more if else statements                     
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
"""
"""                           for loops with a while loop
for x in range(5):            start
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):       stop
    print(x)
x = 0
while(x < 5):                 while loop
    print(x)
    x += 1
"""
pizza_toppings.pop() #removing last value from array
pizza_toppings.pop(1) #removing value that has index of 1

print(person)            #object
person.pop('eye_color')  #removing eye color
print(person)            #print person with new values
"""                              for loop?
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
"""
def print_hello_ten_times(): 
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)