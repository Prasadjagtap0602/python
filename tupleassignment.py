# Write a Python program to create a tuple.
t1=(1,2,3,4,5)
print(t1)


#Write a Python program to create a tuple with different data types
t2=(1,5,8.9,"prasad",[10,20,30])
print(t2[0])
print(type(t2))


#Write a Python program to unpack a tuple in several variables.
t3=(10,20,30)
t4,t5,t6=t3
print("t4:",t4)
print("t5:",t5)
print("t6:",t6)


#Write a Python program to add an item in a tuple.
t7=[10,20,30]
t7.append(40)
print(t7)


#Write a Python program to convert a tuple to a string.
t7=str(t7)
print(type(t7))


#Write a Python program to reverse a tuple
t8=(100,200,300,400)
rev=t8[::-1]
print(rev)

#Write a Python program to convert a list to a tuple.
l2=(10,20,30,40)
t9=tuple(l2)
print(t9)
print(type(t9))


#Write a Python program to remove an item from a tuple.
t10=(1,2,3,4,5,6)
t10=list(t10)
print(t10.remove(2))
print(t10)

#Write a Python program to slice a tuple.
t11=(1,2,3,4,5,6)
t12=t11[1:3]
print(t12)






























