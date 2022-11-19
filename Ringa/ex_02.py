### Retornar True se for possivel tirar a foto
### Condição em que serão 2 iguais de alunos, diferenciados apelas pela cor da camisa
### Separados por 2 fileiras iguais, os alunos da frente não poderiam ser maiores que os de tras
### E para cada fileira, a cor das camisas devem ser iguais
### Exemplo: [162, 181, 151, 160, 170], [150, 179, 149, 152, 154]
 

def func(black, orange):
    photo_status = False
    index = 0

    for n in black:
        if n < orange[index]:
            photo_status = False
            index = 0
            break
        else:
            index += 1
            photo_status = True

    if photo_status:
        return photo_status

    index = 0

    for i in orange:
        if i < black[index]:
            photo_status = False
            index = 0
            break
        else:
            index += 1
            photo_status = True

    if photo_status:
        return photo_status


if __name__ == '__main__':
    func([162, 181, 151, 160, 170], [150, 179, 149, 152, 154])
    print(func([162, 181, 151, 160, 170], [150, 179, 149, 152, 154]))