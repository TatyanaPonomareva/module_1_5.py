immutable_var=7,8,100,"Urban",False
tuple=immutable_var
print(tuple)
print(tuple[1])
print(tuple[2])
tuple[0]=8
print(tuple)
mutable_list=(["Слон","Кот"],200)
tuple_2=mutable_list
print(tuple_2)
tuple_2[0][1]="Пес"
print(tuple_2)