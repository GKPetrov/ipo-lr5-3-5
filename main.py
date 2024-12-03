a =str(input("Введите cтроку "))
gl=('у','е','ы','а','о','э','я','и','ю','У','Е','Ы','А','О','Э','Я','И','Ю')
gl_count=0
for i in range(len(a)):
    for b in range(len(gl)):
        if(gl[b]==a[i]):
            gl_count+=1

print(f"количество гласных {gl_count}")
