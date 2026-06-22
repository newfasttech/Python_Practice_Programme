#list[]
#create list and add list Item 

#studname = ["Anjali","Himansi","Hemangi","kishan","Aashish","Hiren"]
#print(studname)

# print(studname[0:3])

#studname.append(10)
#print(studname)

#demo = []

# append= add one value

#demo.append("one")
#print(demo)
#demo.append('two')
#print(demo)

# extend= add multiple value in list

#studname.extend(["three","four","five"])
#print(studname)

 # insert= add value at specific position

#demo.insert(1,60)
#print(demo)

#demo.insert(0,"anjali")
#print(demo)

 # clear= remove all value of list

#demo.clear()
#print(demo)


# next.topiccccccc  Remove and delete clear list

# studentname=["pooja","jashoda","nandani","priya","khushbu","krishnaaa","anjalii","jahal","sneha"]
# # print(studentname)

 # remove

# print(studentname.remove('krishnaaa'))
# # print(len(studentname))

# pop

# print(studentname.pop(3))
# # print(studentname)
# print(studentname.pop())
# # print(studentname)

 # delete
# del studentname[2]
# print(studentname)

# one by one

# for j in studentname:
#     print(f'Student name => {j}')

# alphabetical order

# studentname.sort()
# print(studentname)

# reverse alphabetical order

# studentname.reverse()
# print(studentname)


# change list item

# studentname=["pooja","jashoda","nandani","priya","khushbu","krishnaaa","priya","anjalii","jahal","sneha"]
# # print(studentname)
# # studentname[0] = "aarati"
# # print(studentname)


#..................................... copy list 
# mylist = studentname.copy()
# print(mylist)

# #......................................count method(to know repeatation of word)
# j = studentname.count("priya")
# print(j)

# # ........................................... join list...
# alph  = ["A","B","C"]
# num = [1,2,3,4]

# # alphanum = alph + num

# # print(alphanum)


# print(alph)

# for k in num :
#     alph.append(k)

# print(alph)




#information..........................
# List Methods
# Python has a set of built-in methods that you can use on lists.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# practiceeeee........
# list=["pooja","jashoda","nandani","krishna","khushbu","rajpriya","krishna","anjali","sneha","jahal","payal","priyanshi","nency"]
# print(list)
# list[0]="mansi"
# print(list)
# mylist=list.copy()
# print(mylist)
# A = list.count("krishna")
# print(A)
# B=("a","b","c")
# C=("1","2","3")
# D=C+B
# # print(D)
# # list.append("payal")
# # print(list)
# # list.extend(["nencyyy","priyanshiii"])
# # print(list)
# # list.insert(6,"anjali")
# # print(list)
# # list.remove("sneha")
# # print(list)
# # list.pop(3)
# # print(list)
# # # del list
# # list.pop(3)
# # print(list)
# # list=["anjali","krishna","jahal","dhruvi"]
# # print(list)
# # list.append("khushbu")
# # print(list)
# # list.extend(["priyanshi","nandani"])
# # print(list)
# # list.insert(2,"anjali")
# # print(list)
# # list.remove("priyanshi")
# # list.pop(4)
# # print(list)


name=["nandani","pooja","jashoda","khushbu","priya","krishna","anjali","jahal"]
print(name)
print(type(name))
print(len(name))
name.append("sneha")
print(name)
name.extend(["priyanshi","nency"])
print(name)
name.insert(1,"payal")
print(name)
name.remove("sneha")
print(name)
name.pop(7)
print(name)
name.reverse()
print(name)
if "anjali" in name:
    print("yes..it is..")
else:
    print("no..it's not..")
for x in name:
    print(x)
for x in name:
    print(f"name => {x}")
