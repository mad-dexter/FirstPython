

def my_function(str1="Unknown", str2 = "Unknown"):
    print("My name is = "+str1+" and my age is = "+str2)

# my_function("ABhishek")
# my_function()
# my_function("Abhishek","29")
# my_function(str2="22")
# my_function(str1="LA LA LA",str2="99")
#
# list1 = ["ABC","XYZ","BCD","AAA"]
# print(list1)
# print(sorted(list1))
# print(list1[2:])
#
# dict1 = {}
# dict1[1] = "Abhishek"
# dict1[2] = "Bhagyashree"
#
# print(dict1)
#
# # Python tuple
# tup = ('AB',22,33,"zz")
# print(tup)

# def print_peoples(*peoples):
#     print(peoples)
#     for p in peoples:
#         print("The person name is = ",p)
#
#
# print_peoples("Abhishek","Bhagyashree","Divya","Shilpa")

# def addition(*numbers):
#     return(sum(numbers))
#
# print(addition(2,3,4,5))
#
# check = "Bhagyashree1"
#
# if check == "Abhishek":
#     print("My name is Abhishek Bacchan")
# elif check == "Bhagyashree":
#     print("It's Bhagyashree")
# else:
#     print("Default Value")
#
#
# # Loop practice
# list1 = [1,2,3,9,4,5]
# flag = True
# counter = 1
#
# for p in list1:
#     print("The current item is ",p)
#
#
# while flag:
#     print(counter)
#     if counter == 100:
#         flag = False
#     counter += 1


def loopFunction(*arr1):
    for a in arr1:
        print("The current object is = "+str(a))


loopFunction("ABC","XYZ",1,2)