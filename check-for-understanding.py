num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0 # starting the count from zero
list_sum = 0 # sum the odd numbers
i = 0 # the num_list i
len_num_list = len(num_list) #length of the list

while (count_odd < 5) and (i < len_num_list): # counting odd numbers so long as the comdition is met
    if num_list[i] % 2 != 0: #checking the ith array if its an odd number
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))
