#Определение количества различных подстрок с
#использованием хеш-функции. Пусть на вход функции дана строка.
#Требуется вернуть количество различных подстрок в этой строке.
#Примечание: в сумму не включаем пустую строку и строку целиком.
import hashlib
s = str(input("Введите строку : "))

print ('Длина строки', len(s))
def num_comb(s):
    set_comb = set()
    for i in range (len(s)):
        for j in range(len(s)+1):
            hash1 = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
            if hash1 == hashlib.sha1(s.encode('utf-8')).hexdigest() or hash1 == hashlib.sha1(s[0:0].encode('utf-8')).hexdigest():
                count = 1
            else:

               set_comb.add(hash1)
              # print(s[i:j], i, j)
               #print(set_comb)
    return(f'Количество уникальных подстрок:' ,len(set_comb))    
print (num_comb(s))   

