price = 100 # global

def increment():
    price = 200 # local
    price = price * 7
    print(price)
    return price

print(price)    
increment()
    
    


