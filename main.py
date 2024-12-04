string = input("Введите cтроку ") #Ввод строки
glas='уеыаоэяиюУЕЫАОЭЯИЮ' #строка гласных
glas_count=0 #инициализация переменных
for i in string: #перебор строки
    if i in glas:
        glas_count+=1
          
print(f"количество гласных {glas_count}")
        
