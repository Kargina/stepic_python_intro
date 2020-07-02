def gen_ticket_number(count, series, length=6):
    """
    генератор номеров билетов, входные параметры: count - количество билетов,
    series - номер серии, необязательный аргумент length - количество цифр
    в номере, по умолчанию равен 6, выход - строка вида: <номер билета> <серия билета>
    """
    counter = 0
    for b_ser in gen_series(series):
        for b_num in gen_number(length): 
            if counter == count:
                break
            ticket = f'{b_num} {b_ser}'
            yield ticket
            counter += 1


def gen_series(series):
    """
    генератор серий лотерейных билетов начиная с series по "ZZ" включительно, входные 
    параметры: series -  - номер серии, выход - строка, состоящая из двух заглавных 
    букв латинского алфавита
    """

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    first_char = series[0].upper()
    first = alphabet.find(first_char)
    second_char = series[1].upper()
    second = alphabet.find(second_char)
    for i in alphabet[first:]:
        for j in alphabet[second:]:
            yield(f'{i}{j}')
        second = 0


def gen_number(length=6):
    """
    генератор номеров лотерейных билетов в одной серии, входные параметры: 
    необязательный аргумент length - количество цифр в номере, по умолчанию равен 6
    """

    max_num = (10 ** length - 1)
    for i in range(1, max_num+1):
        yield str(i).zfill(length)
