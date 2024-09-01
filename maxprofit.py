def maxprofitonstocks(prices):
    if not prices:
        return 0

    min_price = float("inf")
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit


def main():
    prices = [11, 15, 21, 14, 13]
    res = maxprofitonstocks(prices)
    print(res)


main()
