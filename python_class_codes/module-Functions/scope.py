# scope

# global | local

x = "global x"


def function():
    x = "local x"
    print("inside function ", x)


function()

print("outside function ", x)
