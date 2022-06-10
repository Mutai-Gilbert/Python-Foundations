#example zipping the list 
letters = ['a', 'b', 'c']
nums = [1, 2, 3]
for letter,num in zip(letters,nums):
    print("{}: {}".format(letter,num))

    #unzipping the list
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)    

#enumarate example
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i,letter)