# define global variable
my_var = 10

def make_vars():
    my_stuff = 20
    # print local variable
    print(my_stuff)
    # print global variable
    print(my_var)

class Our_vars:
    def __init__(self, var1, var2):
        # assign class variable from new obj arg
        self.var1 = var1
        # assign class variable from new obj arg
        self.var2 = var2
        # assign class variable from global variable
        self.var3 = my_var
    class_var = "class var"

# assign new object with values for var1 and var2
the_vars = Our_vars(42, 24)

# next 3 lines print obj variable
print(the_vars.var1)
print(the_vars.var2)
print(the_vars.var3)

# prints global(also local in this case) variable
print(my_var)

# call function that prints global and local variables
make_vars()

# prints locally assigned variable from class
print(the_vars.class_var)

# this variable is not defined in this scope, only in the function scope - Error
# print(my_stuff)
