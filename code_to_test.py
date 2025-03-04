# # use For while loop to Greet people in revrese order of list items
# # name_list = ["Ram","Shyam","Ghanshyam"]
# # counts=len(name_list)
# # print(counts)
# # i=counts
# # while (i<=len(name_list)):
# #     i=i-1
# #     if i==-1:
# #         break
# #     print("Hello ",name_list[i]
#
# s='Banglore'
# # for i in s:
# #     print(i)
# # print(len(s))
# # for idx in range(len(s)):
# #     print("idx",s[idx])
#
#
# #How to reverse the word in different ways
# s1 ="etl qa labs"
# l=s1.split(' ')
# # print(l)
# # count=len(l)
# # print(count)
#
# # s1 ="etl qa labs"
# # expetcted output : labs qa etl
# # l = s1.split()
# # # ['etl', 'qa', 'labs']
# # ans =""
# # length = len(l) -1 # 3-1 = 2
# # while length >=0:
# #     ans = ans + l[length]+" " # 1st iteration ans = ""+l[2] = labs
# # # 2nd iteration ans = labs + l[1] = labs qa
# # # 3rd iteration = labs qa + l[0] = labs qa etl
# #     length = length -1
# # print(ans)
# ans=''
# for i in  reversed(l):
#     ans=ans+i+' '
#
# print(ans)
#
#
#
# # s1 ="etl qa labs"
# # l = s1.split()
# # print(l)
# # #['etl', 'qa', 'labs']
# # revlist = l[::-1]
# # print(revlist)
# # print(revlist," ",type(revlist))
# # ans = " ".join(revlist)
# # print(ans,type(ans))
#
# # name="Krishna sadashiv kalal"
# # a=name.split(' ')
# # print(a)
# # revlist = a[::-1]
# # ans=" ".join(revlist)
# # print(ans)
#
#
# # ASCII
# # s1 = "abc" # 65 + 25 = 90
# # sum = 0
# # for ch in s1:
# #     sum = sum +ord(ch)
# #     print(sum)
#
# # s1 = "ETLQALABS"
# # # output => QALAB
# # startindex = s1.find('Q')
# # endtindex = s1.find('B')
# # ans = s1[startindex:endtindex+1:1]
# # print(ans)
#
# s2="SLKSOFTPVT"
# #Output=SLKSOFT
# Start_index=s2.find('S')
# Endindex=s2.find('T')
# ans=s2[Start_index:Endindex+1:1]
# print(ans)
#
#
# channel_name = "ETL QA Labs"
# # length of the string ( total number of characters in the string )
# n = len(channel_name)
# #print(n)
# startIndex = 0
# endIndex = n -1
# # way 1
# for idx in range(startIndex,endIndex+1,1):
# #print(channel_name[idx], end = ",")
#     pass


j=0
x=int(input("Enter the number\n"))
for i in range(2,x+1):
    if x%i==0:
        j=j+1

if j==1:
    print("Number is  prime")

else:
    print("Num is not prime ")



