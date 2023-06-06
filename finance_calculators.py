import math     #A class library to help use the power method pow()

print("investment\t- to calculate the amount of interest you'll earn on your investment")
print("bond    \t- to calculate the amount you'll have to pay on a home loan")

decision = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
decision = decision.lower()

# Calculations for the investment option
if (decision == "investment"):
        amount_to_invest = float(input("Enter the amount you want to invest: "))
        percentage = float(input("Enter the rate in terms of percentage the investment will yield per year: "))
        number_of_years = int(input("How long will you plan to invest?: "))
        interest = input("Do you want 'simple' or 'compound' interest?: ")
        interest = interest.lower()

        if (interest == "simple"):
                earning = amount_to_invest*(1 + percentage/100*number_of_years)
                print(earning)

        elif (interest == "compound"):
                earning = amount_to_invest* math.pow((1 + percentage/100),number_of_years)
                print(earning)

        else:
                print("You did not enter the right choice of interest.")    #Executed when spelling of simple or compound is wrong

# Calculation for the bond option
elif (decision == "bond"):
        house_value = float(input("What is the present value of the house?: "))
        rate = float(input("Please enter the rate: "))
        months = int(input("How many months will it take you to repay the bond?: "))

        repayment = (rate/1200*house_value)/(1-(1+rate/1200)**(-months))

        print(repayment)

else:
        print("Your input is neither 'investment' nor 'bond'")      #Executed when spelling of investment or bond is wrong
