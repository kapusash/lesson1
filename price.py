def format_price(price):
    price = int(price)
    result_string = (f'Цена: {price} руб.')
    return result_string
display_price = format_price(56.24)
print(display_price)