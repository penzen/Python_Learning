import Team_Project

"""
Maturin develop which will build the rust code into a python library and
install it into the enviroment
"""
def prt():
    print("Hello world")


result = Team_Project.count_words("This is how you do it")
print(result)

ts = Team_Project.test()
fd = Team_Project.cal()

# The build only works with maturin dev -r, when adding new things, it compiles the c