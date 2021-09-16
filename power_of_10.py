# import math
# # def is_power(x, y):
    
# #     if x == 1:
# #         return True
    
# #     pow = 1 
# #     while (pow < y):
# #         pow = pow * x

# #     return (pow == y)

# def is_power(x, y):
#     res1 = math.log(y) // math.log(y)
#     res2 = math.log(y) / math.log(x)
    
#     return 1 if(res1 == res2) else 0
    
    


# print(is_power(10, 10))
# print(is_power(10, 1000))
# print(is_power(10, 10000))
# # print(is_power(2,30))
# # print(is_power(5,25))


# def is_power(x, y):
#     if y == 1:
#         return True        
#     pow = 1

#     while(pow < y):
#         pow = pow * x
    
#     return pow == y

# import math 

# def is_power(x, y):

#     res = math.log(y, x)


#     print(res)
#     return res.is_integer()



def is_power(x, y):
    if y == 1:
        return True
    pow = 1
    while(pow < y):
        pow = pow * x
    return pow == y


print(is_power(10, 1))
print(is_power(10, 1000))
print(is_power(10, 10090))
# print(is_power(10, 1050))



