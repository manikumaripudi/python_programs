'''def do_twice(func):
    func()
    func()
def say_hello():
    print("hello")
do_twice(say_hello)      '''

'''
#assigning a function to a variable.
def Fun(a):
    print(a)
b=Fun
Fun(5)
b(10) '''
'''
#Nested functions:
def parent():
    print("this is parent function")
    def child1():
        print("this is child 1 function")
        def child2():
            print("this is child 2 function")
        child2()
    child1()
parent() ''' 
'''#closure
def outer():
  message="hello"
  def inner():
    print("Message:", message)

  return inner()

outer()'''

'''
def decorator(func):
  def wrapper():

    print("This is printed before the function is called")
    func()
    print("This is printed after the function is called")
  
  return wrapper

@decorator
def say_hello():
  print("Hello! The function is executing")


say_hello() '''

#split and upper

'''def fun(name):
    return "hello",name
print(fun("mani"))'''

'''
#class decorators
class Power(object):
	def __init__(self, arg):
		self._arg = arg

	def __call__(self, a, b):
		retval = self._arg(a, b)
		return retval ** 2


@Power
def multiply_together(a, b):
	return a * b


print(multiply_together)
print(multiply_together(2, 2))'''
'''
a=input("enter the string")
b=[]
l=len(a)
for x in range(0,l,1):
    if a[x] in 'aeiouAEIOU':
        if a[x] not in b:
         b.append(a[x])

print("the vowels in a given string are",b)'''
''''
#max of two no's
def max(a,b):
    if a>=b:
        return a
    else:
        return b
a=8
b=10
print(max(a,b))    '''
'''   
#interchanging of 1 and last elements in list
def SwapList(a):
    size=len(a)
    t=a[0]
    a[0]=a[size-1]
    a[size-1]=t
    return a 
a=['5','6','8','10','12']
print(SwapList(a))  '''

'''
# List of numbers
list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]
 
# Removing duplicates from the list
list2 = list(set(list1))
print(list2)
 
# Sorting the  list
list2.sort()
print(list2) '''

'''
str=["a","cat","ballon","mouse","at"]
for x in range(len(str)):
    str.sort( reverse=True)
    print(str[x])
print("the largest  string in a list is ",str[0]) '''
'''
#largest number in given two lists
def fun(a,b):
     a.extend(b)
     a.sort(reverse=True)
     return a[0]
a=[5,4,3,2,1]
b=[8,7,5,4,3,2]
c=fun(a,b)
print("the largest number is ",a[0]) '''
'''

# Find smallest number with key _values
dict={'a':3,'b':5,'c':3,'d':1}
print(str(dict))
temp=min(dict.values())
print(temp)
res=[i for i in dict if dict[i]==temp]#here i=key .
print(str(res))'''
#list of strings
str=['a','cat','ballon','mouse','at']
m=[]
for i in str:
    m.append(len(i))
    m.sort()
for i in str:
    if m[0]==len(i):
        print("the smallest number is ",i) 
    if(m[-1])==len(i):
        print("the largest number is ",i)  





    

    
        
   
