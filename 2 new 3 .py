import time
K = int(input())
start_time = time.time()  # ставим таймер на начальное значение ставим его до input что бы не было задержек
file = list(open('text_2.txt', 'r').read())  # чтение файла
file_out = []

# различные переменные счётчики
K_s = 0
para = 1
para_s = 1
all_s = 0
K_s_p = 0
K_break = 0
lust_number = 0
for i in range(len(file)): # проходим по всему списку


    if file[i].isdigit() :  # проверка на цыфру так как работаем только с цифрами
        all_s += 1

        if int(file[i]) == 0 and K_break == 0:  # Проверка на K нулей
            try:
                for j in range(K): # считаем нули что бы они совпадали с количеством K
                    if int(file[i+j]) == 0:
                        K_s += 1

                if K_s == K:  # нашли наше количество, выставляем все счётчики что бы они пропускали верное кол во пар, и не брали текущие нули
                    print('K нулей нашлось')
                    K_s = 0
                    para_s = 2 * K - 1
                    #para = K + 3
                    para = K * 2 + K - 1

                    K_s_p = K

                    K_break = 1


                else:  # сбрасываем счётчик
                    K_s = 0

            except:
                pass
        if para == 0:  # проверяем что это нужная пара
                para = para_s
                file_out.append(file[i])
                for g in range(all_s): # обрабатываем пару занося нужные нули
                    file_out.append('0')
                #file_out.append(file[i-1])
                file_out.append(lust_number)
        else:  # если это не та пара то просто выводим её не обрабатывая
            if K_break == 1:
                K_break = 2
                if K == 1:
                    file_out.append(file[i])
            else:
                if para != 1 and K_s_p <= 0 :

                    file_out.append(file[i])
            para -= 1
            K_s_p -= 1

        lust_number = file[i]
    else:
        #para = para_s
        file_out.append(file[i])  # поскольку это не цыфра просто выводим


print(''.join(file_out))  # ввыводим всё обработанное и время выполнения
print('время выполнения', time.time() - start_time)
