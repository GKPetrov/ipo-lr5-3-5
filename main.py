a = input("Введите cтроку ")
gl = 'уеыаоэяиюУЕЫАОЭЯИЮ'     #строка гласных
gl_count = 0  #инициализация переменных
for i in range(len(a)):    #перебор строки
    for b in range(len(gl)):
        if(gl[b]==a[i]):
            gl_count+=1

print(f"количество гласных {gl_count}")#вывод
