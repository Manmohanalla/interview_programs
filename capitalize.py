def capitalize(string):
    lst = string.split(' ')
    str = ''
    for i in lst:
        if i.isalpha():
            i = i.title()
        str+=i+' '
    return str

print capitalize('hello   world 3g')


