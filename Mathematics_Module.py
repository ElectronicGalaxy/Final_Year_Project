#
#
#   Author: David Rich-Seam
#
#   Last Updated: 30/03/2022
#
#   


import math
import cmath
import sympy as sym
from sympy import * 
import numpy as np
from sympy.solvers.solveset import solvify


class Mathematics_Class:

    def __init__(self):
        self.iResult = 0
        self.Realpart = 0                # Holds real part of the complex number
        self.ImagPart = 0                # Holds imaginary part of the complex number
        self.Modulus = 0            
        self.Angle = 0
        self.Theta = 0
        self.rTheta = 0



    # Checks for invalid inputs for floats
    def InputValidation_Float(self, ArgNumber):
        try:
            UserNumber = float(ArgNumber)
            return UserNumber
        except ValueError:
            ArgNumber = None
            return
        except Exception:
            ArgNumber = None
            return



    # Checks for invalid inputs for ints
    def InputValidation_Int(self, ArgNumber):
        try:
            UserNumber = int(ArgNumber)
            return UserNumber
        except ValueError:
            ArgNumber = None
            return
        except Exception:
            ArgNumber = None
            return
            
         

    # Note: When the user enters (0,0), the function produces an angle of 90 degrees...    
    # This function converts rectangular complex numbers into polar form
    def ComplexNumber_RecToPolar(self, a = "", b = ""):
        InputList = [a, b]
        InputStatus = False     # If the user's input is valid, the function will return true
        

        # Passses each number inside the InputList into the validation function
        for i in range(0, len(InputList)):
            InputList[i] = self.InputValidation_Float(InputList[i])

            if (InputList[i] == None):
                print("Invalid input. Please try again.")
                return InputStatus
        
        
        self.RealPart = float(InputList[0])   # Holds the real part
        self.ImagPart = float(InputList[1])   # Holds the imaginary part

        # The following two lines of code accounts for if the user enters 0 for the real part
        # 0 for the real part will cause an error, so this if statement accounts for it
        if (self.RealPart == 0 and self.ImagPart >= 0):
            self.Modulus = self.ImagPart
            self.Theta = 90     # 90° if i (vertical axis) is positive
            print(f"{self.Modulus}∠{self.Theta}°")

        # If the real part is 0 and the imaginary part is less than 0, run the code inside the
        # if statement
        elif (self.RealPart == 0 and self.ImagPart < 0):
            self.Modulus = self.ImagPart
            self.Theta = 270     # 270° if i (vertical axis) is positive
            print(f"{self.Modulus}∠{self.Theta}°")

            
        # The following if statements checks for which quadrant the point is in
        # Quadrant 1 - tan() = positive
        elif (self.RealPart > 0 and self.ImagPart >= 0):
            self.Angle = math.atan(self.ImagPart/self.RealPart)
            self.Theta = round(self.ComplexNumber_RadianToDegree(self.Angle), 3)
            self.Modulus = round(math.sqrt(math.pow(self.RealPart, 2) + math.pow(self.ImagPart, 2)), 3)
            print(f"{self.Modulus}∠{self.Theta}°")

            
        # Quadrant 2 - tan() = negative
        elif (self.RealPart < 0 and self.ImagPart > 0):
            self.Angle = math.atan(self.ImagPart/self.RealPart)
            self.Theta = round(self.ComplexNumber_RadianToDegree(self.Angle), 3) + 180
            self.Modulus = round(math.sqrt(math.pow(self.RealPart, 2) + math.pow(self.ImagPart, 2)), 3)
            print(f"{self.Modulus}∠{self.Theta}°")


        # Quadrant 3 - tan() = positive
        elif (self.RealPart < 0 and self.ImagPart < 0):
            self.Angle = math.atan(self.ImagPart/self.RealPart)
            self.Theta = round(self.ComplexNumber_RadianToDegree(self.Angle), 3) + 180
            self.Modulus = round(math.sqrt(math.pow(self.RealPart, 2) + math.pow(self.ImagPart, 2)), 3)
            print(f"{self.Modulus}∠{self.Theta}°")


        # Quadrant 4 - tan() = negative
        elif (self.RealPart > 0 and self.ImagPart < 0):
            self.Angle = math.atan(self.ImagPart/self.RealPart)
            self.Theta = round(self.ComplexNumber_RadianToDegree(self.Angle), 3) + 360
            self.Modulus = round(math.sqrt(math.pow(self.RealPart, 2) + math.pow(self.ImagPart, 2)), 3)
            print(f"{self.Modulus}∠{self.Theta}°")


        # The following lines of code account for when the user enters 0 for the imaginary part
        # The program will not crash if there was no if statement for such an instance
        elif (self.ImagPart == 0 and self.RealPart >= 0):
            self.Theta = 0
            self.Modulus = self.RealPart
            print(f"{self.Modulus}∠{self.Theta}°")


        elif (self.ImagPart == 0 and self.RealPart < 0):
            self.Theta = 180
            self.Modulus = self.RealPart
            print(f"{self.Modulus}∠{self.Theta}°")

        InputStatus = True
        return InputStatus




    # Converts Polar form to Rectangular form      
    def ComplexNumber_PolarToRec(self, Modulus = "", Theta = ""):
        InputList = [Modulus, Theta]
        InputStatus = False

        # Passses each number inside the InputList into the validation function
        for i in range(0, len(InputList)):
            InputList[i] = self.InputValidation_Float(InputList[i])

            if (InputList[i] == None):
                print("Invalid input. Please try again.")
                return InputStatus
                
        
        self.Modulus = float(InputList[0])      # Modulus is the absolute value
        self.Theta = float(InputList[1])          # Theta is an angle, assumed to be in degrees
        
        # math.cos(x) and math.sine(x) are both measured in radians, which is why they are being converted to degrees then stored in class variables
        self.rTheta = self.ComplexNumber_DegreeToRadian(self.Theta)

        # Imaginary part (Vertical axis) b_i = r * sine(Theta)
        # Real part (Horizantal axis) a = r * cos(Theta)
        self.ImagPart = round(self.Modulus * (math.sin(self.rTheta)), 2)
        self.RealPart = round(self.Modulus * (math.cos(self.rTheta)), 2)

        # This line of code rounds up the arguments and converts them into complex numbers
        # "self.z" stores the real and imaginary part together. ex: 3 + 4j
        self.z = complex(round(self.RealPart, 2), round(self.ImagPart, 2))

        print(f"{self.z}")

        InputStatus = True
        return InputStatus




    # Calculates the derivatives
    def Calculus_Derivatives(self, UserInput):
       InputStatus = False
       
       # The expression must contain one variable. For example: x**2 + cos(2*x)
       # There's another function for multivariable differentiation
       F_x = UserInput

       x = sym.Symbol('x')
       
       # The code will attempt to run the code inside the "try" block
       # If the user enters an expression the diff function can't interpret,
       # then the block will throw an "exception", but still carry on.
       try:
           self.D_f = diff(F_x, x)  
       except ValueError:
           self.D_f = None
           return InputStatus
       except Exception:
           self.D_f = None
           return InputStatus
       else:
           print(f"Expression: {F_x}")
           print(f"Derivative: {self.D_f}")
           
           InputStatus = True
           return InputStatus
        
           



    # Calculates the quotient rule for derivatives
    def Derivatives_QuotientRule(self, UserInput_1, UserInput_2):
        InputStatus = False

        # This variable (VERY IMPORTANT) checks the sign of the "TopRight" derivative.
        # Depending on the sign, the way the result is displayed onto the screen varies
        # in order to display correctly.
        # "N" represents negative, "P" represents positive
        self.CheckSign = "P"
        
        try:
            U = sympify(UserInput_1) #sympify turns the user-entered expression into something sympy can deal with
            V = sympify(UserInput_2)
        except SyntaxError:
            return InputStatus
        except Exception:
            return InputStatus

        x = Symbol('x')

        try:
            D_V = diff(V) # "diff" differentiates V and stores the input into D_V
            D_U = diff(U) 
        except ValueError:
            return InputStatus
        except Exception:
            return InputStatus
        else:
            self.V_Squared = expand(V**2) # This squares the input and stores it into V_Squared
            
            self.Derivative_TopLeft = expand(D_U*V)
            Derivative_TopRight = expand(D_V*U)
            self.Derivative_TopRight1 = Derivative_TopRight
            Df_Quotient = (self.Derivative_TopLeft + Derivative_TopRight)/self.V_Squared
            
            print(f"{Df_Quotient}\n\n")
            
            if (Derivative_TopRight.is_positive == True):
                self.SignCheck = "P"
                self.Derivative_TopRight1 = expand(Derivative_TopRight)
                print(f"[{self.Derivative_TopLeft} - {Derivative_TopRight1}]/{self.V_Squared}")
            else:
                self.SignCheck = "N"
                self.Derivative_TopRight1 = expand(Derivative_TopRight)
                print(f"[{self.Derivative_TopLeft} + {self.Derivative_TopRight1}]/{self.V_Squared}")
                
            InputStatus = True
            return InputStatus
        
        



    # Factors the quadratic equation
    def PolynomialFactorization_Calculator(self, UserInput):
        InputStatus = False

        x = sym.Symbol('x')

        try:
            # This line of code ensures the expression is in expanded form
            UserInput1 = expand(UserInput)
            # This adds all like-terms together in the expression
            PolynomialSimplified = collect(UserInput1, x)
            # The factor function is responsible for factoring the expression entered by the user
            self.FactoredPolynomial = factor(PolynomialSimplified)
        except ValueError:
            return InputStatus
        except Exception:
            return InputStatus
        else:
            if (PolynomialSimplified == self.FactoredPolynomial):
                InputStatus = "NO CHANGES"
                return InputStatus
            
            print(self.FactoredPolynomial)
            InputStatus = True
            return InputStatus



    # Find the roots of a polynomial
    def RootsOfEquation_Calculator(self, UserInput1, UserInput2):
        # Checks whether the user's input is valid
        InputStatus = False
        
        x = Symbol('x')

        #Converts the strings into sympy arguments so the equation can be solved.
        try:
            LHS_Equation = sympify(UserInput1)
            RHS_Equation = sympify(UserInput2)
        except ValueError:
            return InputStatus
        except Exception:
            return InputStatus
        
        # This variable stores information on whether the equation can be solved
        EquationStatus = "CAN BE SOLVED"

        #RealRoots = solvify(Eq(LHS_Equation, RHS_Equation), x, S.Reals)
        try:
            #
            ComplexRoots = solvify(Eq(LHS_Equation, RHS_Equation), x, S.Complexes)
        except ValueError:
            return InputStatus
        except NotImplementedError:
            InputStatus = "CANNOT BE SOLVED"
            print(InputStatus)
            return InputStatus
        except Exception:
            return InputStatus

        self.RootsOfEquation = ComplexRoots

        if (ComplexRoots == None):
            # If solvify returns "None", then that means the equation given has infinite number of solutions
            InputStatus = "INFINITE SOLUTIONS"
            return InputStatus
        elif (len(ComplexRoots) >= 5):
            # If the degree of the polynomial is greater than or equal to 5, then return with the string message "DEGREE TO HIGH"
            InputStatus = "DEGREE TOO HIGH"
            return InputStatus
        elif(len(ComplexRoots) == 0):
            # All polynomials have 
            InputStatus = "EMPTY LIST"
            return InputStatus
        
        #except NotImplementedError
        #print(ComplexRoots)
        
        InputStatus = True
        return InputStatus
   


        
    # MAKE SURE TO USE THE SYMPY DEGREE FUNCTION CHECK AND LIMIT THE DEGREES
    # OF POLYNOMIALS TO 4!!!
    
    # Calculates systems of linear equations
    def SystemOfEquations(self, LinearEquation1, LinearEquation2):
        InputStatus = False
        # This variable will hold the status of the user's input
        # If the degree of the symbolic variables 'x' or 'y' is not equal to 1
        # then the flag will be raised and the variable will be set to "1"
        #
        # if the degrees of the variables are correct, then the variable will be
        # set to "0"
        self.DegreeFlag = "1"
        x, y = symbols('x, y')

        try:
            Lin1 = sympify(LinearEquation1)
            Lin2 = sympify(LinearEquation2)
        except ValueError:
            return InputStatus
        except Exception:
            return InputStatus

           
        try:
            # This checks the degree of x
            # It seperately checks the degree of y
            Lin1Degree_x = degree(Lin1, gen = x)
            Lin1Degree_y = degree(Lin1, gen = y)

            # Repeats the above for line 2
            Lin2Degree_x = degree(Lin2, gen = x)
            Lin2Degree_y = degree(Lin2, gen = y)
        except Exception:
            return InputStatus


        # Checks to see if the symbolic variables (x and y) has a degree not equal
        # to 1, for each linear equation
        if (Lin1Degree_x != 1):
            print(f"Not valid {Lin1Degree_x}")
            InputStatus = True
            return InputStatus
        
        elif (Lin1Degree_y != 1):
            print(f"Not valid {Lin1Degree_y}")
            InputStatus = True
            return InputStatus

        elif (Lin2Degree_x != 1):
            print(f"Not valid {Lin2Degree_x}")
            InputStatus = True
            return InputStatus

        elif (Lin2Degree_y != 1):
            print(f"Not valid {Lin2Degree_x}")
            InputStatus = True
            return InputStatus
    
        # "poly" converts the expression into a polynomial that can manipulated by its sub-functions. Like .coeffs()
        # "collect" combines all like-terms
        SimLin1 = Poly(collect(Lin1, x), x, y)
        SimLin2 = Poly(collect(Lin2, x), x, y)

        # "coeffs" looks for all coeffcients returns a "list" of all the coefficients
        # Important note: Numbers AND LETTERS THAT IS NOT 'x' OR 'Y' will be considered coefficients.
        Coefficients_Lin1 = SimLin1.coeffs()
        Coefficients_Lin2 = SimLin2.coeffs()

        Coefficients_Lin1.append(0)
        Coefficients_Lin2.append(0)

        if (len(Coefficients_Lin1) < 3):
            return InputStatus
        elif (len(Coefficients_Lin2) < 3):
            return InputStatus
        # Create a multidimensional array
        Values = [[0.0 for i in range(0, 3)], [0.0 for i in range(0, 3)]]

        # This variable will be used to find out if the following for loop has reached
        # the end of the set of coefficients
        EndOfList_Flag = 0

        # This for loop will pass in all coefficients and constants from the user
        # into the multidimensional array, which will then be passed onto a function
        # that will calculate the points of intersection.
        for i in range(0, 2):
            for j in range(0, 3):
                if (EndOfList_Flag == 0):
                    try:
                        # Because letters that not x or y can be stored in the coeff list,
                        # the program will check each input to see if it's a number and then converts to float
                        Values[i][j] = float(Coefficients_Lin1[j])
                    except ValueError:
                        #print("Please enter a number and try again.\n\n")
                        return InputStatus
                    except Exception:
                        return InputStatus
                
                if (EndOfList_Flag == 1):
                    try:
                        # Goes through each input to ensure that it is a valid input
                        Values[i][j] = float(Coefficients_Lin2[j])
                    except ValueError:
                        return InputStatus
                    except Exception:
                        return InputStatus
            EndOfList_Flag = 1
                    
        
        EquationA = np.array( [[Values[0][0], Values[0][1]], [Values[1][0], Values[1][1]]] )    # 3x + 8y = 15, 2x - 8y = 10
        EquationB = np.array( [Values[0][2], Values[1][2]] )
        

        try:
            Result = np.linalg.solve(EquationA, EquationB)
        except ValueError:
            #print("The two lines have ethier no solutions or infinite solutions")
            return InputStatus
        except Exception:
            InputStatus = "LINES DOES NOT INTERSECT"
            return InputStatus
       
        # print(f"Point of intersection: ({-Result[0]} ,{-Result[1]})")
        self.LinearResult = Result
        
        # The degrees of each variable entered for both equations are valid
        # "0" represents valid
        self.DegreeFlag = "0"
        InputStatus = True
        return InputStatus

        #Zero solutions throws a ValueError



    # This function takes an expression an integrates it
    def Integration(self, Expression):
        InputStatus = False

        x = sym.Symbol('x')
        
        try:
            # Convert input into a sympy expression
            sympify(Expression)
            # Integrate with respect to x
            Integral = integrate(Expression, x)
        except ValueError:
            return InputStatus
        except Exception:
            return InputStatus
        else:
            print(f"Integral: {Integral}")
            self.Integral = Integral
            
            InputStatus = True
            return InputStatus

        


    # This function calculates the hyperbolic functions of sinh, cosh, tanh
    # It can also be used to evavluate function that are not hyperbolic expressions
    def HyperbolicFunction_Calculator(self, UserInput):
        InputStatus = False
        TestVariable = 0
        
        x = sym.Symbol('x')
        
        try:
            # Lambdify converts the expression an expression that can be numerically evaluated
            self.F = lambdify(x, UserInput)
        except NameError:
           print("Error")
           # When a user enters a function that cannot be recognised by the function
           # then return with the following status
           InputStatus = "UNRECOGNISED TERM"
           return InputStatus
        except Exception:
           return InputStatus

        # The block of code below is to re-check if the input is incorrect
        try:
            # If the user enters a function such as cosh(x) + sinh(2) or exp(x),
            # then return with a particular error status
            TestVariable = round(self.F(x), 3)
        except TypeError:
            # This is for when the user enters sinh(x) + tan(2) into the function
            InputStatus = "UNEVALUTED FUNCTION"
            return InputStatus
        except NameError:
            # This is for when the user enters a mathematical function that is not recognised
            InputStatus = "UNRECOGNISED TERM"
            return InputStatus
        except Exception:
            return InputStatus

        InputStatus = True
        return InputStatus
    

        


    # This function takes an expression an simplifies it
    def SimpificationFunction(self):
        pass
        #UserExpression = sympify(input("Please enter an expression to be simplified"))

        # More progress to be made...

        
    
    #The function converts radians to degrees
    def ComplexNumber_RadianToDegree(self, Radian):
        return Radian * (180/math.pi)


    # The function converts degrees to radians
    def ComplexNumber_DegreeToRadian(self, Degree):
        return Degree * (math.pi/180)

    
    # Get real number
    def GetRealNumber(self):
        return self.RealPart


    # Get Imaginary number
    def GetImaginaryNumber(self):
        return self.ImagPart


    # Get complex number(a + bi)
    def GetComplexNumber(self):
        return self.z
    

    # Get the absolute value(Total length)
    def GetModulus(self):
        return self.Modulus


    # Get theta (The angle)
    def GetTheta(self):
        return self.Theta


    # Get Derivative (Excludes the results of the quotient rule)
    def GetDerivative(self):
        return self.D_f
    

    # Get the derivative for the top left of the quotient rule
    def GetQuotientRule_LeftDerivative(self):
        return self.Derivative_TopLeft
    

    # Get the derivative for the top right of the quotient rule
    def GetQuotientRule_RightDerivative(self):
        return self.Derivative_TopRight1
    
    
    # Get the V^2
    def GetQuotientRule_V_Squared(self):
        return self.V_Squared


    # Get the sign of the top right derivative of the quotient
    def GetSignCheck_QuotientRule(self):
        return self.SignCheck


    # Get the factored quadratic function
    def GetFactoredPolynomial(self):
        return self.FactoredPolynomial


    # Get the points of intersection of two linear lines
    # x-coordinate
    def GetSystemOfEquation_LinearRoot_1(self):
        return self.LinearResult[0] # Contains two roots (Two numbers)


    # Get the points of intersection of two linear lines
    # y-coordinate
    def GetSystemOfEquation_LinearRoot_2(self):
        return self.LinearResult[1] # Contains two roots (Two numbers)
    

    # Get the status of the variables degree
    def GetSOE_Degree(self):
        return self.DegreeFlag


    # Get the integral of an expression
    def GetIntegral(self):
        return self.Integral


    # Get roots of equation
    def GetRoots(self):
        return self.RootsOfEquation

    # Get factored expression
    def GetFactoredExpression(self):
        return self.FactoredPolynomial


    # Get numeric result
    def GetHyperbolicResult(self):
        x = sym.Symbol('x')
        return round(self.F(x), 3)

        
#MyObject = Mathematics_Class()

#a = input("Enter a value: ")    # This represents the length of the line in the real-axis (x-axis)
#b = input("Enter another value: ") # This represents the length of the line in the imaginary-axis (y-axis)
#print(" ")

#MyObject.ComplexNumber_RecToPolar(a, b) 

#print("\n\n")
#AbsoluteValue = input("Enter a number for the modulus: ")
#Angle = input("Enter a number for the angle in degrees: ")

#MyObject.ComplexNumber_PolarToRec(AbsoluteValue, Angle)

#MyObject.Calculus_Derivatives() # Pretty much finished - Needs a bit more testing
#print(" ")
#print(" ")
#MyObject.Derivatives_QuotientRule(a, b)
#MyObject.SystemOfEquations()    # Mostly finished. Needs a bit more testing.
#print(" ")
#print(" ")
#print(" ")
#MyObject.PolynomialFactorization_Calculator() # **Finshed** - More notes needs to be made for what triggers errors for this function.
#print(" ")
#print(" ")
#MyObject.QuadraticSolution_Function()                  # **Finished** - More notes neeeds to be made on what triggers an error for this function
#print(" ")
#print(" ")
#MyObject.Integration()  #Needs to be tested more.
#print(" ")
#print(" ")
#MyObject.HyperbolicFunction_Calculator()   #**Finshed**
#print(" ")
#print(" ")

#NOTE:
#
# With the help of sympy, lambdify() method, we can convert a SymPy expressions
# to an expression that can be numerically evaluated.
# Lambdify acts like a lambda function, except it, converts the SymPy names
# to the names of the given numerical library, usually NumPy or math


# ********* To-do list *********
#
# Improve the input-checker function - (Needs more work)
# Add a function to calculate the quotient rule for derivatives - (Needs more work)
# Add a function to calculate sineh(x), cosh(x) and tanh(x)
# Add a function to calculate integration
#

# InputValidation_Float()
# InputValidation_Int()
# ComplexNumber_RecToPolar()
# ComplexNumber_PolarToRec()
# Calculus_Derivatives()
# Derivatives_QuotientRule()
# QuadraticFactorization_Calculator()
# QuadraticSolution_Function()
# SystemOfEquations()
# Integration()
# GetComlexNumber()
# GetTheta()
# GetModulus()
# GetDerivative()
# GetFactoredQuadratic()
# GetRealRoot()
# GetRealRoots()
# GetSystemOfEquation_LinearRoots()
# GetIntegral()
#
#

"""
 def SystemOfEquations(self):
        print("Please enter the numbers for A, B and C,")
        print("for the two functions in the form Ax + By = C \n")

        Values = [[0.0 for i in range(0, 3)], [0.0 for i in range(0, 3)]]
        
        for i in range(0, 2):
            for j in range(0, 3):
                try:
                    Values[i][j] = float(input(f"Please enter a number for [{i}][{j}] = "))
                except ValueError:
                    print("Please enter a number and try again.\n\n")
                    break
                    return
                except Exception:
                    print("Something went wrong.\n")
                    return
        
        EquationA = np.array( [[Values[0][0], Values[0][1]], [Values[1][0], Values[1][1]]] )    # 3x + 8y = 15, 2x - 8y = 10
        EquationB = np.array([Values[0][2], Values[1][2]])
        
        # Try and except needs to be put here...
        # To be tested more
        try:
            Result = np.linalg.solve(EquationA, EquationB)
        except Exception:
            print("The two lines have ethier no solutions or infinite solutions")
            return
        
        print(" ")
        print(f"Point of intersection: ({Result[0]} ,{Result[1]})")
        self.LinearResult = Result
        print(f"Point of intersection: ({self.LinearResult[0]} ,{self.LinearResult[1]})")


"""

#Helpful code
#
# for i in a.split(" "):
#   b.append(int(i))
#
# for i in range(0, len(b)):
#   print(f"{b[i]} is of type: ", type(b[i]))
#    
# This code takes a number and displays the data type
# If a person enters two numbers in the same line, the for loop will
# go through each number and whenever it meets a space, it will know
# to store the number in a seperate slot.
#
# The "split" function tells the program to split the numbers whenever
# it encounters a space.
#


#SymPy is a Python library for symbolic mathematics.
#It aims to become a full-featured computer algebra system (CAS) while keeping the code as simple as possible in order to be comprehensible and easily extensible.
#SymPy is written entirely in Python
#
#pollev.com/katerinachristofylakifines238

#Website used to produce flowchart: https://app.diagrams.net/
