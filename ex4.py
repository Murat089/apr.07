info = input('Введите текст: ') 
txt = f'''{info}'''
s = txt[0:len(txt)//2]
d = txt[len(txt)//2: len(txt)]
print(s.upper(), d.lower())
