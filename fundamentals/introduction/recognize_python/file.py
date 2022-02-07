num1 = 42 #variable num1 is an int
num2 = 2.3 #variable num2 is an float
boolean = True #boolean datatype
string = 'Hello World' #string datatype
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']#list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#dictionary
fruit = ('blueberry', 'strawberry', 'banana') #this is a truple
print(type(fruit))#print the type of data
print(pizza_toppings[1])#print 2nd value from list
pizza_toppings.append('Mushrooms')#you're going to add mushroom value to list
print(person['name'])#print the value from key "name"
person['name'] = 'George'#change value from john to George
person['eye_color'] = 'blue'#add a new value to person dictionary
print(fruit[2])#print banana

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
"""                              for loop
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
"""
def print_hello_ten_times(): #function
    for num in range(10): #run 10 times
        print('Hello') #print hello 10 times

print_hello_ten_times() #calling the function

def print_hello_x_times(x): #function
    for num in range(x): #running it 4 times
        print('Hello') #print hello 4 times

print_hello_x_times(4) #calling the function with argument 0f 4

def print_hello_x_or_ten_times(x = 10): #fucntion with defaul "x = 10"
    for num in range(x): #run for times of value x
        print('Hello') #print hello x ammount of times

print_hello_x_or_ten_times() #calling fucntion
print_hello_x_or_ten_times(4) #calling function


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