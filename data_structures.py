#lab 04

# example 1a

groceries = ['bananas','strawberries','apples','bread']
groceries.append('champagne')
print groceries

# example1b

groceries = ['bananas','strawberries','apples','bread']
groceries.append('champagne') # add champagne to the list of groceries
groceries.remove('bread')  # remove bread from the list of groceries
print groceries

# example 1c

groceries = ['bananas','strawberries','apples','bread']
groceries.append('champagne') # add champagne to the list of groceries
groceries.remove('bread')  # remove bread from the list of groceries
groceries.sort()
print groceries

# example 2a

print 'Dictionary would be used as the data type' 
dict = {'Apples':'7.3','Bananas':'5.5','Bread':'1.0','Carrot':'10.0','Champagne':'20.90','Strawberries':'32.6'}
print  'Apple is', dict['Apples']
dict['Strawberries'] = 63.43
print 'The price of Strawberries in winter now is', dict['Strawberries'] # updated strawberries price

dict['chicken'] = 6.5
print dict # prints all entries in the dictionary
print 'Hehe customers we have chicken now in stock at', dict['chicken']

#example3
 

in_stock = ('Apples','Bananas','Bread','Carrot','Champagne','Strawberries') 

always_in_stock = ('Apples','Bananas','Bread','Carrot','Champagne','Strawberries')
print 'Come to shoprite! We always sell:\n', always_in_stock[0:6]

for i in always_in_stock:
    print i


#example4
    



