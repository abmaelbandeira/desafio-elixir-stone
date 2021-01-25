from shopping_list.shopping_list import shopping_list_func


if __name__ == '__main__':
    shopping_list = []
    email_list = []
    print('=====Shopping list====')
    while True:
        product = input("Product: ")
        if product == "end":
            break
        amount = int(input("Amount: "))
        price = int(input("Price: "))
        shopping_list.append([product, amount, price])

    print("====Emails list====")
    while True:
        email = input("Email: ")
        if email == "end":
            break
        email_list.append(email)
    print(shopping_list_func(shopping_list, email_list))
