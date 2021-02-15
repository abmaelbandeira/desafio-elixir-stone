from shopping_list.shopping_list import shopping_list_func


if __name__ == '__main__':
    shopping_list = [['a', 1, 6], ['b', 1, 6], ['c', 1, 5]]
    email_list = ['a', 'b', 'c', 'd', 'e']
    print(shopping_list_func(shopping_list, email_list))
