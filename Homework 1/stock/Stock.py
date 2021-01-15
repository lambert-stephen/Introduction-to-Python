#Stephen Lambert
#python program that calculates the commison someone pays a broker for a stock
#caculates the return after investments
#varibles defined below
Number_shares = 2000
Purchase_price = 40.00
Selling_price = 42.75
Commission_rate =0.03
#calculations
total_before_commission = (Number_shares * Purchase_price)
broker_commission = (total_before_commission * Commission_rate)/100
total_of_purchase = (broker_commission + total_before_commission)
#prints all neccessary output
print("Amount of money Joe paid for stock: $",format(total_before_commission,'.2f'))
print("Amount of commission Joe paid his broker when buying stock: $",format(broker_commission,',.2f'))
#calculations
sold_shares = (Number_shares * Selling_price)
Commission_after_sale = (sold_shares * Commission_rate)/100
#prints all neccessary output
print("Amount of money Joe sold the stock for: $",format(sold_shares,',.2f'))
print("Amount of commission Joe paid his broker when he sold the stock: $",format(Commission_after_sale,',.2f'))
#calculations
Money_left_over = (sold_shares - Commission_after_sale)
print("Amount of money Joe had left when he sold the stock and paid his broker: $",format(Money_left_over,',.2f'))
#prints whether the investor made a profit or not
if Money_left_over > 0:
    print("Joe made a profit!")
else:
    print("Joe lost Money")
