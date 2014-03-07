__author__ = 'archmagece'


def num2formatted_str(number, length):
    number_str = str(number)
    if length < len(number_str):
        length = len(number_str)
    number_tmp = str()
    for num in range(length):
        number_tmp += "0"
    number_tmp += number_str
    return number_tmp[len(number_tmp)-length:]
