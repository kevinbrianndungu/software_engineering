def calculate_discount(price,discount_percent):
    discount = price * (discount_percent/100)
    final_price = price - discount

    if discount_percent >= 20:
        print(f"original price: {price}, Discount: {discount_percent} %")
        print(f"Discounted price: {price - discount}")
    else:
        print(f"final price (after discount): {final_price}")

    return final_price, price
    
price = float(input("whats the buying price:"))
discount_percent = float(input("state the percentage_discount:"))

final_price, original_price = calculate_discount(price, discount_percent)
