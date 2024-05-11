print("Welcome, user!")

print("\nThis is the Statistical Independence Determiner, a program that is designed to, as its name suggests, determine if a pair of discrete random variables is whether or not statistically independent. ")

print("\nIdentifying if the given is statistically independent can be done by using the formula f(x,y) = g(x)h(x).")

print("\nWherein:")

print("\nf(x,y) represents the value of variables X and Y")

print("\ng(x)h(y) represents the product of the Marginal Distributions of X and Y.")

print("\nIt is important to note that in order to achieve statistical independence, the equivalence of f(x,y) = g(x)h(y) must be observed for ALL values of X and Y. ")

print("\nLet's begin!")

print("Example of a Joint Probability Distribution Table")

from tabulate import tabulate

mydata = [
	["0", "0", "1/30", "2/30", "3/30", "6/30"],
	["1", "1/30", "2/30", "3/30", "4/30", "10/30"],
	["2", "2/30", "3/30", "4/30", "5/30", "14/30"],
	["g(x)", "3/30", "6/30", "9/30", "12/30", "30/30 or 1"]
]

head = ["", "0", "1", "2", "3", "h(y)"]

print(tabulate(mydata, headers=head, tablefmt="grid"))

print("\nf(x,y) = (x+y)/30")

print("\nNOTE: Your input should be in the form of a fraction/ decimal NOT coordinates and derived from a Joint Probability Distribution Table.")
i = 1

while True:
    
    from fractions import Fraction
        
    f = Fraction(input("\nEnter value of f(x,y): "))
    g = Fraction(input("Enter value of g(x): "))
    h = Fraction(input("Enter value of h(y): "))
    gh = g*h
    
    if f == gh:
    
        print("f(x,y) = g(x)h(y) --->", f, "=", gh)
        print("\nResult: Statistically Independent.")
    
    elif f != gh:
        print("f(x,y) = g(x)h(y) --->", f, "≠", gh)
        print("\nResult: NOT Statistically Independent.")
    
    i = eval(input("\nWould you like to submit another entry? \nEnter 1 for yes and 0 for no: "))
    
    if i == 0:
        
        print("\nThank you for using our program! \nThe End.")
             
        break
    
    elif i != 1 or 0:
        
        print("\nInvalid input. Try again.")
        
        break
