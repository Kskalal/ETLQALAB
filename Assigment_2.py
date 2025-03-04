from collections import Counter
# use For loop to print to greet the people in the list
'''
name_list = ["Ram","Shyam","Ghanshyam"]
for i in name_list:
    print("Hello ",i)



# use while loop to print to greet the people in the list
name_list = ["Ram","Shyam","Ghanshyam"]
i=0
while (i<len(name_list)):
    print("Hello ",name_list[i])
    i=i+1



# use For loop Greet people in revrese order of list items
name_list = ["Ram","Shyam","Ghanshyam"]
for i in  reversed(name_list):
    print("Hello ",i)


# use add few items to list
name_list = ["Ram","Shyam","Ghanshyam"]
print("Before adding item ",id(name_list))
name_list.append("Krishna")
name_list.append("Sagar")
name_list.append("Manju")
print("After adding item ",id(name_list))
print(name_list)

#Remove some items and see the ordering of the item
name_list=['Ram', 'Shyam', 'Ghanshyam', 'Krishna', 'Sagar', 'Manju']
name_list.remove("Ram")
print(name_list)


name_list = {"Ram","Shyam","Ghanshyam"}
# print the elements form set
print(name_list)


#Trying to access specific item from the set
name_list = {"Ram","Shyam","Ghanshyam"}
print(name_list[0])

'''

# List=[1,2,3,4,5,7]
# # def max_list(List):
# #     max=List[0]
# #     for i in List:
# #         if i>max:
# #             max=i
# #     return i
# #
# # print(max_list(List))

# name='Nagaraj'
# list_name=list(name)
# print(list_name)
#
#
#
# print(dict(Counter(list_name)))

Name='Vrishank'
start_index=Name.find('s')
End_index=Name.find('k')
c=Name[start_index:End_index:1]
print(c)
