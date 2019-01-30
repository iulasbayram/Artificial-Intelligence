# Student Name: Ismail Ulaş Bayram
# Student ID: 220201040

from random import randint

sample_num = 100000 # iteration number

max = 100 # upper boundary for random variable
min = 1 # lower boundary for random variable

# All counter are initialized
counterOfPlus_D = 0
counterOfPlus_D_Minus_A = 0
counterOfPlus_E_Minus_B = 0
counterOfMinus_B = 0
counterOfPlus_A_Plus_D_Minus_E = 0
counterOfPlus_D_Minus_E = 0
counterOfPlus_B_Minus_E_Plus_A = 0
counterOfPlus_A = 0

counter = 0 # counter for while loop

# Booleans of all nodes with respect to random variables of them
bool_A, bool_B, bool_C, bool_D, bool_E = None, None, None, None, None

# Truth tables of all nodes except node A
truth_table_of_B = [[False,0.2],[True,0.8]]
truth_table_of_C = [[False,0.05],[True,0.2]]
truth_table_of_D = [[False,False,0.05],[False,True,0.8],[True,False,0.8],[True,True,0.8]]
truth_table_of_E = [[False,0.6],[True,0.8]]

# This method is written to get exact expression from truth table of node by giving
# two parameters which are truth table of one of them and booleans of its parents
# E.g. truth_table_of_node -> [[False,False,0.05],[False,True,0.8],[True,False,0.8],[True,True,0.8]] and
# parent_bools -> [False,True]. Return value must be [False,True,0.8]
def getExpressionOfNode(truth_table_of_node,parent_bools):
    match = None
    for expression in truth_table_of_node:
        counter = 0
        for i in range(len(parent_bools)):
            if(parent_bools[i] == expression[i]):
                counter += 1
            if(counter == len(parent_bools)):
                match = expression

    return match


while(counter < sample_num):

    # Random variables are generated as below
    rand_A = randint(min, max) / max
    rand_B = randint(min, max) / max
    rand_C = randint(min, max) / max
    rand_D = randint(min, max) / max
    rand_E = randint(min, max) / max

    if(rand_A <= 0.2):
        bool_A = True
    else:
        bool_A = False

    expression_B = getExpressionOfNode(truth_table_of_B,[bool_A]) # After specifying boolean of A, we can get exact value of node B by looking truth table of it

    if(rand_B <= expression_B[len(expression_B)-1]):
        bool_B = True
    else:
        bool_B = False

    expression_C = getExpressionOfNode(truth_table_of_C,[bool_A]) # After specifying boolean of A, we can get exact value of node C by looking truth table of it

    if(rand_C <= expression_C[len(expression_C)-1]):
        bool_C = True
    else:
        bool_C = False


    expression_D = getExpressionOfNode(truth_table_of_D,[bool_B,bool_C]) # After specifying booleans of B and C, we can get exact value of node D by looking truth table of it

    if(rand_D <= expression_D[len(expression_D)-1]):
        bool_D = True
    else:
        bool_D = False

    expression_E = getExpressionOfNode(truth_table_of_E,[bool_C]) # After specifying boolean of C, we can get exact value of node E by looking truth table of it

    if(rand_E <= expression_E[len(expression_E)-1]):
        bool_E = True
    else:
        bool_E = False


    #-------------------------------------------------------------
    # P(+D) -> means that bool_D = True
    #-------------------------------------------------------------
    if(bool_D == True):
        counterOfPlus_D += 1

    #-------------------------------------------------------------
    # P(+D,-A) -> means that bool_D = True and bool_A = False
    #-------------------------------------------------------------
    if(bool_D == True and bool_A == False):
        counterOfPlus_D_Minus_A += 1


    #-------------------------------------------------------------
    # P(+E|-B) = P(+E,-B) / P(-B)
    # P(+E,-B) -> means that bool_E = True and bool_B = False
    # P(-B) -> means that bool_B = False
    #-------------------------------------------------------------
    if(bool_E == True and bool_B == False):
        counterOfPlus_E_Minus_B += 1

    if(bool_B == False):
        counterOfMinus_B += 1

    #-------------------------------------------------------------
    # P(+A|+D,-E) = P(+A,+D,-E) / P(+D,-E)
    # P(+A,+D,-E) -> means that bool_A = True , bool_D = True and bool_E = False
    # P(+D,-E) -> means that bool_D = True and bool_E = False
    #-------------------------------------------------------------
    if(bool_A == True and bool_D == True and bool_E == False):
        counterOfPlus_A_Plus_D_Minus_E += 1

    if(bool_D == True and bool_E == False):
        counterOfPlus_D_Minus_E += 1

    #-------------------------------------------------------------
    # P(+B,-E|+A) = P(+B,-E,+A) / P(+A)
    # P(+B,-E,+A) -> means that bool_B = True , bool_E = False and bool_A = True
    # P(+A) -> means that bool_A = True
    #-------------------------------------------------------------
    if(bool_B == True and bool_E == False and bool_A == True):
        counterOfPlus_B_Minus_E_Plus_A += 1

    if(bool_A == True):
        counterOfPlus_A += 1

    counter += 1


print("Probability of P(+D) -> ", counterOfPlus_D / sample_num)
print("Probability of P(+D,-A) -> ", counterOfPlus_D_Minus_A / sample_num)
print("Probability of P(+E|-B) = P(+E,-B) / P(-B) -> ", counterOfPlus_E_Minus_B / counterOfMinus_B)
print("Probability of P(+A|+D,-E) = P(+A,+D,-E) / P(+D,-E) -> ", counterOfPlus_A_Plus_D_Minus_E / counterOfPlus_D_Minus_E)
print("Probability of P(+B,-E|+A) = P(+B,-E,+A) / P(+A) -> ", counterOfPlus_B_Minus_E_Plus_A / counterOfPlus_A)