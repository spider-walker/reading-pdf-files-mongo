txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08


def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)


final_prices = [get_price_with_tax(txn) for txn in range(10)]
print(list(final_prices))
