print("Hello, World!")

#/variables

x=5  #int
y=3.14 #float
z="ABC" #string
print(x)
print(y)
print(z)

"""
Addition
"""
a=10
b=20
c=a+b
print(c)

# types of numbers
d=10  #int
e=5.3  #float
f=1j  #complex

print(type(d))
print(type(e))
print(type(f))

g=-1  #int
h=3e5  #float
i=4+6j #complex

print(type(g))
print(type(h))
print(type(i))

k="LMN"
print(type(k))

#plus operator
print("Hello "+k) #Hello LMN
print ("Hello "+"XYZ")

print(d+g)
#print(d+k) #error
l="20"
#print(g+l) #error

"""Type casting: Forceful conversion of one data type into another"""
g=-1
l="20"
m=int(l) #convert into int
print(m)
n=g+m
print(n)

e=5.3
o=int(e) #convert float into int
print(o)

p=float(o)
print(p)
q=str(e)
r=l+q
print(r)

print("A="+str(g))

#print("Enter the name")
#n=input()
#print("Hello "+n)

#shortcut way to take input
#name =input("Enter the name")
#print("Hello "+name)

s=input("Enter the first number") #input is always in string format
t=input("Enter the second number")

u=s+t  #x=10,y=20,z=1020
print(u)
v=int(s)+int(t)  ##x=10,y=20,z=30
print(v)



