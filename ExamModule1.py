# # Number 1

def Hashtag (string):
    z = "#"
    for word in string.split():
        z += word.capitalize()

    if len (z) > 140 or z == '#':
        print (False)
    else:
        print (z)

Hashtag ("Hello there how are you doing")
Hashtag ("Hello World")
Hashtag (" ")
Hashtag ("fox brown quick speed how click clean bear where golf hotel cup soccer baseball badminton house user bird animal office regex opajopjopajodopjjiopaidajijdoajopdjoajdoacinianiainianpinioakopacomaomopamopmopmcaopmopmcopmowjejopjopjocajojopjopscjopjerjwuiewjijwnsxjacnudnsao")



# # Number 2

def create_phone_number (number):
    try:
        print('({}{}{}) {}{}{}-{}{}{}{}'.format(number[0],number[1],number[2],number[3],number[4],number[5],number[6],number[7],number[8],number[9]))
    except:
        print(False)

create_phone_number([1,2,3,4,5,6,7,8,9,0])
create_phone_number([1,2,3,4,5,6,7,8,9])
create_phone_number([0,8,2,3,4,8,9,1,8,7])
create_phone_number([0,8,4,5,7,6,8,3,1])



# # Number 3

def fungsi_sort(angka):
    for i in range(len(angka)):
        for j in range (i+1, len(angka)):
            if angka [i] % 2 == 0 and angka [i] % 2 == 0:
                if angka [i] < angka [j]:
                    angka[i], angka[j] = angka[j], angka[i]
            elif angka [i] % 2 != 0 and angka [j] % 2 != 0:
                if angka[i] > angka [j]:
                    angka[i], angka[j]= angka[j], angka[i]

    return angka
print (fungsi_sort([5,3,2,8,1,4]))



# # Number 4

kolom = int(input('Masukkan Hollow Triangle: '))
for row in range (1, kolom+1):
    for col in range (1,2*kolom):
        if row == kolom or row+col == kolom+1 or col-row == kolom-1:
            print ('#', end='')
        else:
            print(end= '_')
    print()








