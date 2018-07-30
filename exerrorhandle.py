# Error handling
var1  = 3
var2  = 4
fruits = {"can": "container", "sun": "sun-shine"}
try:
    var3 = var1 /var2
    print(fruits['XXX'])
except (ZeroDivisionError) as error:
    print("Trap ZeroDivisionError error")
except (KeyError) as error:
    print("Trap KeyError error")
except:
    print("Trap error")
