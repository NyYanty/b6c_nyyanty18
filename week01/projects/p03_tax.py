is_running = True
while is_running :
    amount = input('Please enter your amount:')
    if not amount.isdigit()or int(amount) <= 0:
        print("Number is incorrect, try again.")
    else:
        check_rate = True
        while check_rate:
            rate = input('Please enter tax rate:')
            if not rate.isdigit() or int(rate) < 1 or int(rate) >99:
                print('Rate is incorrect, try again.')
            else:
                amount = int(amount)
                rate = int(rate)
                tax = amount*rate/100
                net=amount-tax
                '{:.2f}'.format(net)
                print(f"===== ===== ===== ===== =====\nAMOUNT:{amount}$\nRATE: {rate}%")
                print(f"===== ===== ===== ===== =====\nTAX: {tax}$\nNET: {net}$\n===== ===== ===== ===== =====")

               check_rate = False
               is_running = False
