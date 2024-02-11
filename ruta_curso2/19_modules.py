import sys
print(sys.path)


import re
text = 'Mi numero de telefono es 311 394 2392, el codigo de país es 51, mi numero de la suerte es 7'
result  = re.findall('[0-9]+', text)
print(result)


import time
timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)


import collections
numbers = [1,3,5,6,4,23,6,7,8,9,12]
counter = collections.Counter(numbers)
print(counter)