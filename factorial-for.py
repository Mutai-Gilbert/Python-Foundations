# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1
count = 1
# write your for loop here
for count in range(1,7):
    product *= count
    count +=1


# print the factorial of number
print(product)