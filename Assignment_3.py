#
from  collections import Counter
# Write a function to return the grade based on percentage
# X=float(input("Enter the value between 100\n"))
# def grade():
#     if X>=90:
#         print('A')
#     elif X>=80:
#         print('B')
#     elif X>=70:
#         print('C')
#     elif X>=60:
#         print('D')
#     else:
#         print("Fail")
# grade()

# Write a function that return a list of common elements from two different sets
# S1 = {1, 2, 3, 4, 5, 7}
# S2 = {1, 3, 5, 8, 7, 10}
# count=[]
# def dupliacte(S1,S2):
#     for i in S1:
#         for j in S2:
#             if j ==i:
#                 count.append(j)
#     return count
# print(dupliacte(S1,S2))

#Convert a String to a List of Characters
# strs="Krisha"
# char_list=list(strs)
# print(char_list)
# print(type(char_list))

#Given a list, write a function that provide the occurrence of element against each element in the list.
# List = [1,2,3,4,5,1,3]
# def count_occurrences(List):
#     return dict(Counter(List))
#
# occurances=count_occurrences(List)
# print(occurances)

#Write a python code to check if the given list contains duplicate elements and print yes or no as per input
List=[1,2,3,4,6,6]

def dup_val(List):
    if len(List)==len(set(List)):
        print("No")
    elif len(List)!=len(set(List)):
        print("yes")
dup_val(List)


# def duplicate_val(List):
    # for i in List:
    #     for j in range(start_index,end_index,1):
    #         i=i+1
    #         if i==j:
    #             print("yes")
    #             break
    #         else:
    #             print("No")




# duplicate_val(List)






# city = "ETL QA Labs"
# expected output: “sbaL AQ LTE”
# revist_list=city[::-1]
# ans=''
# l=city.split(' ')
# for i in reversed(l):
#     ans=ans+i+' '
# print(ans)


# Extract a substring form character "Q" and ends at "b"
# city = "ETLQALabs"
# #Expected O/P : QAlab
# Start_index=city.find('Q')
# End_index=city.find('b')
# C=city[Start_index:End_index+1:1]
# print(C)

# Write a python code to check if the given list contains duplicate elements and print yes or no as per input
# list1 =[1,2,3,4,3]
# list2 =[1,2,3,4]
# duplicate=list1[0]
# for i in list1:

##odd indexed elements
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
expected_output=list[1::2]
print(expected_output)

##even indexed elements
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
expected_output=list[0::2]
print(expected_output)
