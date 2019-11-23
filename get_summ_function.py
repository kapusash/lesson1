def get_summ(one, two, delimiter='&'):
    concat = str(str(one) + str(delimiter) + str(two))
    return concat
result = get_summ(0,'python','*')
print(result.upper())

