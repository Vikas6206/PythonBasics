def greet_user(f_name,l_name):
    print(f'hi {f_name} {l_name}!')
    print('Welocome aboard')


#Always define the function first and then call them

print("Start")
#Positional argument
greet_user("Vikas","Kumar")
#Keyword argument example [functiona which taes multiple readable values
greet_user(l_name="Kumar",f_name="Vikas")
print("Finish")



#Function that return values

def square(number):
    return number*number;

input=int(input("Entrt number:"))
result=square(input)
print(result)

