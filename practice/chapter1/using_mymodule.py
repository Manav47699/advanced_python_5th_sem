#this is the file that will use the module. we can't do it in this file so do check "mymodule.py" and using_mymodule.py"
import mymodule

from mymodule import product

print (f"the sum is equal to {mymodule.addition(5, 4)}")

print (f"the product is equal to {product(2, 4)}")
