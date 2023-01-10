import random
import string
for a in range(0,10):
    source = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(source) for i in range(11)))
    print("GIEOQUE_"+result_str.upper())
