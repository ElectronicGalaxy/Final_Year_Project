#   Author: David Rich-Seam - w1692467
#   Last updated: 23/04/2022
#

import numpy as np
import matplotlib.pyplot as plt
from sympy import *


class Graphing_Calculator_Class:

    # This constructor defines the class variables
    def __init__(self):
        # Holds the maximum number of graphs
        self.MaxNumberOfGraphs = 4
        #Holds the number of functions graph on the screen
        self.NumberOfGraphs = 0


        
    def WindowConfigure(self):
        # The following lines of code configures the cartesian coordinate plane
        
        plt.xlabel("x-axis")  # This defines the label of the x-axis
        plt.ylabel("y-axis")  # Thia defines the label for the y-axis
        plt.title("Graphing Calculator")    # This defines the title of graphing window
        plt.axhline(color = "black")    # This defines the colour of the vertical axis
        plt.axvline(color = "black")    # This defines the colour of the horizantal axis
        plt.grid(linestyle = '--')  # Adds grid lines to the graph
    


        
    # The function produces the graph entered by the user
    def GraphingFunction(self, UserInput = ""):
        # Determines if the input is not valid
        InputStatus = False

        self.WindowConfigure()

        # If number of graphs on screen is 4, then reset screen while still 
        # keeping any function still in the entry box.
        if (self.NumberOfGraphs == 4):
            plt.clf()                   # Clears the graphs on the canvas
            self.WindowConfigure()      # This reconstructs the screen
            self.NumberOfGraphs = 0     # Reset the number of graphs to 0
            InputStatus = True

        # If the user enters nothing, then clear the screen 
        if (UserInput == ""):
            plt.clf()
            self.WindowConfigure()      # Reconstruct screen
            xlist = []                  # Empty all the x-coordinates
            ylist = []                  # Empty all the y-coordinates
            plt.plot(xlist, ylist)      # plot the empty list which produces nothing
            plt.show()                  # Display the new empty screen graph.
            self.NumberOfGraphs = 0
            InputStatus = True
            return InputStatus

        # Converts expression to a Sympy expression
        UserInput = sympify(UserInput)
        
        # First two numbers refer to the range of the x-axis.
        # "linspace" creates 1000 numbers between the first two numbers.
        xlist = np.linspace(-4, 4, num=1000)
        
        x = Symbol('x')
        # Converts the sympy expression into a numerical function
        try:
            UserFunction = lambdify(x, UserInput)
        except ValueError:
            print("Error.")
            return InputStatus
        except Exception:
            return InputStatus

        
        try:
            ylist = UserFunction(xlist) # Pass the large list of numbers into the UserFunction
        except ValueError:
            return InputStatus
        except NameError:
            return InputStatus
        except Exception:
            return InputStatus
        
        
        if (self.NumberOfGraphs == 4):
            xlist = []
            ylist = []
        
        try:
             plt.plot(xlist, ylist, label = str(UserInput))  # Plot points onto the graph
        except ValueError:
            print("Error.")
            return InputStatus
        except Exception:
            return InputStatus

        # Adds 1 to the variable which will keep track of the number of graphs on screen.
        self.NumberOfGraphs = self.NumberOfGraphs + 1
        
        plt.legend() # When a function is graphed, each function will be labeled with colours
        plt.show() # Show graph

        

        InputStatus = True
        return InputStatus
    


    def MaxNumberOfGraphs(self):
        return self.MaxNumberOfGraphs
