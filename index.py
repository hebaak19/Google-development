while True:
    try:
        bill_amount=float(input("Enter the bill amount: "))
        if bill_amount<0:
            print("please enter a positive number ")
            continue
        tip_rate=float(input("Enter the tip rate: ") )
        if tip_rate<0:
            print("please enter a positive number ")
            continue
        break
    except ValueError:
        print("please enter a valid number ")
def calculate_bill(bill,rate):
    bill_rate=round((rate/100)*bill,2)
    total_bill=round((bill_rate+bill),2)
    print(f'{bill_rate} Tip ')
    return total_bill
    

print(f'{calculate_bill(bill_amount,tip_rate)} the total bill')
    
