cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

for keys in cast:
    print(keys)       
for key,value in cast.items():
    print("Actor: {}   Role: {}".format(key,value))    