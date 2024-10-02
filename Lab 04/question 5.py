names = input('Enter a name: ')
while 'END' not in names:
    names += ", " + input('Enter a name: ')
names = names.replace(', END', '')
print(names)

# other method without string methods

name = input('Enter a name: ')
names = ''
while name != 'END':
    if names == '':
        names += name
    else:
        names += ', ' + name
    name = input('Enter a name: ')
print(names)