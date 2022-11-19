### Retornar em um array o par de numeros que somados iriam chegar ao numero alvo.
#### Caso não encontre nenhum retornar um array vazio.


def func(array, target_sum):
    sum = 0
    for n in array:
        for i in array:
            if n != i:
                sum = n+i
            if sum == target_sum:
                return [n, i]
            break
    return []


if __name__ == '__main__':
    func([2, 8, 5, 7], 10)
    func([2, 2, 5, 7], 10)
    print(func([2, 8, 5, 7], 10))
    print(func([2, 2, 5, 7], 10))
