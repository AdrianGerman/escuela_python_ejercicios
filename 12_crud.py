# CRUD Create, Read, Update & Delete

numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[1])

numbers[-1] = 10
print(numbers)

numbers.append(700)
print(numbers)

numbers.insert(0, 'hola')
print(numbers)

numbers.insert(3, 'change')
print(numbers)

task = ['todo 1', 'todo 2', 'todo 3', 'todo 4']
new_list = numbers + task
print(new_list)

index = (new_list.index('todo 2'))
new_list[index] = 'todo changed'
print(new_list)

# delete
new_list.remove('todo 1')
print(new_list)

# con pop eliminas el ultimo elemento de la lista
new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

# intercambia todas las pocisiones de la lista
new_list.reverse()
print(new_list)


#ordenar elementos de una lista
print('\n')
numbers_a = [1, 4, 7, 9, 3]
numbers_a.sort()
print(numbers_a)

string = ['re', 'ag', 'ed', 'zl', "af"]
string.sort()
print(string)