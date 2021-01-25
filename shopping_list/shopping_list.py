def shopping_list_func(shopping_list, email_list):
    """
    function that receives a shopping list and an email,
    calculates the total of the list, and returns a dictionary
    with the amount that must be paid by each person

    :param shopping_list: Shopping list
    :param email_list: Email list
    :return:
    """

    total = 0
    amount_people = len(email_list)
    amount_paid_per_person = {}

    for item in shopping_list:
        total = total + (item[1] * item[2])

    try:
        total_per_person = total // amount_people
    except:
        return "Ops, the email list is empty "

    remainder = total % amount_people

    for email in email_list:
        if remainder > 0:
            amount_paid_per_person[email] = total_per_person + 1
            remainder = remainder - 1
        else:
            amount_paid_per_person[email] = total_per_person
    return(amount_paid_per_person)
