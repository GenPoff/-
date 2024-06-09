immutable_var='Здесь',25,'Капибар',False
print(immutable_var)
#immutable_var[1]=0
#print(immutable_var)    # выдает ошибку, ибо кортеж не поддерживает изменения элементов
immutable_var=['Здесь',25],'Капибар',False
print(immutable_var)
immutable_var[0][1]=0
print(immutable_var)        #а тут изменилось, потому что в кортеж первым эелементом ставится список, который можно менять

mutable_list=['тут', 8, 'Пушишек', True]
print(mutable_list)
mutable_list[1:3]=29, 'Барашков'
print(mutable_list)