with open('./data/data2017.txt') as f:
    lines = f.readlines()
    for ln in lines:
        ln = ln.replace(',', '').replace(':', '').replace('int64', '') \
            .replace('Name', '').replace('dtype', '').replace('/', ' ') \
            .replace('object', '').replace('float64', ' ') \
            .replace('NaN', '').replace('NaN', ' ') \
            .replace('.', ' ')
        text = ln.split()

        if text[0].isnumeric():
            text.pop(0)
        if text[0].isnumeric():
            text.pop(0)
        if text[0].isnumeric():
            text.pop(0)

        if not text[1].isnumeric():
            text[0] = f'{text[0]} {text[1]}'
            text.pop(1)

        if not text[2].isnumeric():
            text.insert(2, '0')
            text.insert(3, '0')

        if not text[1].isnumeric():
            text[0] = f'{text[0]} {text[1]}'
            text.pop(1)

        if len(text) > 6 and not text[5].isnumeric():
            text[4] = f'{text[4]} {text[5]}'
            text.pop(5)

        if len(text) > 6 and not text[5].isnumeric():
            text[4] = f'{text[4]} {text[5]}'
            text.pop(5)

        if len(text) > 7 and not text[6].isnumeric():
            text.insert(6, '0')
            text.insert(7, '0')

        if len(text) > 9 and not text[9].isnumeric():
            text[8] = f'{text[8]} {text[9]}'
            text.pop(9)

        if len(text) > 9 and not text[9].isnumeric():
            text[8] = f'{text[8]} {text[9]}'
            text.pop(9)

        if len(text) > 9 and not text[9].isnumeric():
            text[8] = f'{text[8]} {text[9]}'
            text.pop(9)

        if len(text) > 7 and not text[7].isnumeric():
            text.insert(7, '0')
            text.insert(9, '0')

        if len(text) == 10:
            text.insert(9, '0')

        if len(text) == 10:
            text.insert(9, '0')

        if len(text) == 11 and text[9].isnumeric() and int(text[9].strip())>100:
            text.insert(9, '0')

        if len(text) == 7:
            text.insert(1, '0')
            text.insert(3, '0')
            text.insert(6, '0')
            text.insert(7, '0')
            text.insert(9, '0')

        notwanted = ['-------------------------------', 'CONSTITUENCY_NAME', 'GRAND TOTAL', 'CAW']
        if not set(text) & set(notwanted):
            text.insert(0, f'{len(text)}')
            s = ','.join(text)
            print(f' {s}')
