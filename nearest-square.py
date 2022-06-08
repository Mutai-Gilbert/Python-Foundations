limit = 40 # here we are setting the limit number

num = 0 # initializing the count
while (num+1)**2 < limit: # the num is added 1 because we cannot square zero, now it's square should be less than the limit
    num += 1 # increment as we go back to the loop
nearest_square = num**2 # we now perfom the  square

print(nearest_square)