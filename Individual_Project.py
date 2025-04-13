from tkinter import *
from PIL import ImageTk,Image
from Mathematics_Module import Mathematics_Class
from Physics_Module import Physics_Class
from GraphingCalculator import Graphing_Calculator_Class


class GUI_Calculator:

    def __init__(self, root):
        self.root = root
        self.MainWindow()   # Calls the MainWindow method


    # The very first window to display to the user.
    def MainWindow(self):
        # Sets the size of the window equal to 440x440
        self.root.geometry("440x440")
        # Sets the main window equal to 
        root.title("Main Menu")


        # Finds the image (the image has to be in the same folder as the program) and reads it
        # User_Menu_Background
        self.MyImage = Image.open("Main_Window_Background.png")

        # This takes the image read and stored in MyImage and resizes it.
        # ANTIALIAS prevents it from looking blurred
        self.ResizeImage = self.MyImage.resize((440, 440), Image.ANTIALIAS)
        self.Image = ImageTk.PhotoImage(self.ResizeImage)

        # Create a canvas
        MyCanvas = Canvas(root, width = 440, height = 440)
        MyCanvas.pack(fill = "both", expand = True)

        # Displays the image onto the screen
        MyCanvas.create_image(0,0, image = self.Image, anchor = "nw")

        #self.HeaderLabel = Label(self.root, text = "User Menu", bg = "Cyan", fg = "White", font = ("Calibri", 20))
        MyCanvas.create_text(220, 40, text = "GUI Calculator", font = ("Calibri 40 bold"))
   

        # Main window buttons
        self.MathsPhysics_Button = Button(self.root, text = "Maths and Physics", height = 2, font = ("Arial 10 bold"), padx = 4, command = self.MathsPhysicsWindow)
        #self.MathsPhysics_Button.pack(side = TOP, padx = 15 ,pady = 30)

        self.GraphingCalculator_Button = Button(self.root, text = "Graphing Calculator", height = 2, font = ("Arial 10 bold"), padx = 4, command = self.GraphingCalculator)
        #self.GraphingCalculator_Button.pack(side = TOP, padx = 15 ,pady = 30)

        self.Electronics_Button = Button(self.root, text = "Electronics", height = 2, font = ("Arial 10 bold"), padx = 4, command = self.ElectronicSchematicWindow)

        self.TestAndGuidance_Button = Button(self.root, text = "Test and Explanations", height = 2, font = ("Arial 10 bold"), padx = 4, command = self.TestAndGuidanceWindow)

        # Place the buttons created above onto the screen
        # The first two arguments represent the x and y positions on the screen
        CanvasButton1 = MyCanvas.create_window(94, 180, window = self.MathsPhysics_Button)
        CanvasButton2 = MyCanvas.create_window(245, 180, window = self.GraphingCalculator_Button)
        CanvasButton3 = MyCanvas.create_window(370, 180, window = self.Electronics_Button)
        CanvasButton4 = MyCanvas.create_window(245, 240, window = self.TestAndGuidance_Button)



    ######## MATHS FUNCTIONS ########


# ComplexNumber_Button = Button(self.MPWindow, text = "Complex Numbers", height = 1, font = ("Arial 11 bold"), command = self.ComplexNumbersWindow, bg = "#2558f5", fg = "white", width = 15)
# Derivatives_Button = Button(self.MPWindow, text = "Differentiation", height = 1, font = ("Arial 11 bold"), command = self.DifferentiationWindow, bg = "#2558f5", fg = "white", width = 12)
# Integration_Button = Button(self.MPWindow, text = "Integration", height = 1, font = ("Arial 11 bold"), command = self.IntegrationWindow, bg = "#2558f5", fg = "white", width = 11)
# LinearEquations_Button = Button(self.MPWindow, text = "System Of Equations", height = 1, font = ("Arial 11 bold"), command = self.SystemsOfEquationsWindow, bg = "#2558f5", fg = "white", width = 17)
# EquationSolver = Button(self.MPWindow, text = "Equation Calculator", height = 1, font = ("Arial 11 bold"), command = self.EquationCalculatorWindow, bg = "#2558f5", fg = "white", width = 17)                                
# ExpressionFactorization_Button = Button(self.MPWindow, text = "Expression Factorisation", font = ("Arial 11 bold"), command = self.FactorisationWindow, bg = "#2558f5", fg = "white", width = 20)
# HyperbolicTrig_Button = Button(self.MPWindow, text = "Hyperbolic Functions", font = ("Arial 11 bold"), command = self.HyperbolicFunctions, bg = "#2558f5", fg = "white", width = 17) 
# InclinedPlane_Button = Button(self.MPWindow, text = "Inclined Plane", font = ("Arial 11 bold"), command = self.InclinedPlane_Window, bg = "#2558f5", fg = "white", width = 14)
# ProjectileMotion_Button = Button(self.MPWindow, text = "Projectile Motion", font = ("Arial 11 bold"), command = self.ProjectileMotion_Window, bg = "#2558f5", fg = "white", width = 14)
# AngularVelocity_Button = Button(self.MPWindow, text = "Angular Velocity", font = ("Arial 11 bold"), command = self.AngularVelocity_Window, bg = "#2558f5", fg = "white", width = 14)
# ResonantCircuit_Button = Button(self.MPWindow, text = "Resonant Circuit", font = ("Arial 11 bold"), command = self.RLCResonantCircuit_Window, bg = "#2558f5", fg = "white", width = 14)
# RLCParallelCircuit_Button = Button(self.MPWindow, text = "RLC Parallel Circuit", font = ("Arial 11 bold"), command = self.RLCParallelCircuit_Window, bg = "#2558f5", fg = "white", width = 17)
# MagneticFlux_Button = Button(self.MPWindow, text = "Magnetic Flux", font = ("Arial 11 bold"), command = self.MagneticFlux_Window, bg = "#2558f5", fg = "white", width = 12)
# ElectromagneticInduction = Button(self.MPWindow, text = "Electromagnetic Induction", font = ("Arial 11 bold"), command = self.ElectromagenticInduction_Window, bg = "#2558f5", fg = "white", width = 22)


    def TestAndGuidanceWindow(self):
        # Test and Guidance window
        self.TGWindow = Toplevel()

        self.TGWindow.title("Test and Explanations")
        self.TGWindow.geometry("700x490")

        # Finds the image (the image has to be in the same folder as the program) and reads it
        # User_Menu_Background
        PhysicsImage = Image.open("PhysicsImage.png")

        # This takes the image read and stored in MyImage and resizes it.
        # ANTIALIAS prevents it from looking blurred
        ResizeImage = PhysicsImage.resize((700, 490), Image.ANTIALIAS)
        self.PhysicsImage = ImageTk.PhotoImage(ResizeImage)

        # Create a canvas
        MyCanvas = Canvas(self.TGWindow, width = 700, height = 490)
        MyCanvas.pack(fill = "both", expand = True)

        # Displays the image onto the screen
        MyCanvas.create_image(0,0, image = self.PhysicsImage, anchor = "nw")

        MyCanvas.create_text(104, 24, text = "Quiz and Explanation of the \nMaths and Physics Topics", font = ("Calibri 32 bold"), anchor = "nw")


        ComplexNumber_Button = Button(self.TGWindow, text = "Complex Numbers", height = 1, font = ("Arial 11 bold"), command = self.ComplexNumbers_ExplanationWindow, bg = "#2558f5", fg = "white", width = 15)    
        Derivatives_Button = Button(self.TGWindow, text = "Differentiation", height = 1, font = ("Arial 11 bold"), command = self.Differentiation_ExplanationWindow, bg = "#2558f5", fg = "white", width = 12)
        Integration_Button = Button(self.TGWindow, text = "Integration", height = 1, font = ("Arial 11 bold"), command = self.Integration_ExplanationWindow, bg = "#2558f5", fg = "white", width = 11)
        LinearEquations_Button = Button(self.TGWindow, text = "System Of Equations", height = 1, font = ("Arial 11 bold"), command = self.SystemsOfEquation_ExplanationWindow, bg = "#2558f5", fg = "white", width = 17)
        EquationSolver_Button = Button(self.TGWindow, text = "Equation Calculator", height = 1, font = ("Arial 11 bold"), command = self.EquationSolver_ExplanationWindow, bg = "#2558f5", fg = "white", width = 17)                                
        ExpressionFactorization_Button = Button(self.TGWindow, text = "Expression Factorisation", font = ("Arial 11 bold"), command = self.FactorisationWindow, bg = "#2558f5", fg = "white", width = 20)
        HyperbolicTrig_Button = Button(self.TGWindow, text = "Hyperbolic Functions", font = ("Arial 11 bold"), command = self.HyperbolicFunctions, bg = "#2558f5", fg = "white", width = 17) 
        InclinedPlane_Button = Button(self.TGWindow, text = "Inclined Plane", font = ("Arial 11 bold"), command = self.InclinedPlane_Window, bg = "#2558f5", fg = "white", width = 14)
        ProjectileMotion_Button = Button(self.TGWindow, text = "Projectile Motion", font = ("Arial 11 bold"), command = self.ProjectileMotion_Window, bg = "#2558f5", fg = "white", width = 14)
        AngularVelocity_Button = Button(self.TGWindow, text = "Angular Velocity", font = ("Arial 11 bold"), command = self.AngularVelocity_Window, bg = "#2558f5", fg = "white", width = 14)
        ResonantCircuit_Button = Button(self.TGWindow, text = "Resonant Circuit", font = ("Arial 11 bold"), command = self.RLCResonantCircuit_Window, bg = "#2558f5", fg = "white", width = 14)
        RLCParallelCircuit_Button = Button(self.TGWindow, text = "RLC Parallel Circuit", font = ("Arial 11 bold"), command = self.RLCParallelCircuit_Window, bg = "#2558f5", fg = "white", width = 17)
        MagneticFlux_Button = Button(self.TGWindow, text = "Magnetic Flux", font = ("Arial 11 bold"), command = self.MagneticFlux_Window, bg = "#2558f5", fg = "white", width = 12)
        ElectromagneticInduction_Button = Button(self.TGWindow, text = "Electromagnetic Induction", font = ("Arial 11 bold"), command = self.ElectromagenticInduction_Window, bg = "#2558f5", fg = "white", width = 22) #1FB8D7
        TestButton = Button(self.TGWindow, text = "Test Yourself!!", height = 2, font = ("Arial 19 bold"), command = self.TestUserWindow, bg = "#1FB8D7", fg = "white", width = 14)

        # Place the buttons created above onto the screen
        # The first two arguments represent the x and y positions on the screen
        CanvasButton1 = MyCanvas.create_window(14, 170, window = ComplexNumber_Button, anchor = "nw")
        CanvasButton2 = MyCanvas.create_window(244, 170, window = Derivatives_Button, anchor = "nw")
        CanvasButton3 = MyCanvas.create_window(244, 220, window = Integration_Button, anchor = "nw")
        CanvasButton4 = MyCanvas.create_window(444, 170, window = LinearEquations_Button, anchor = "nw")
        CanvasButton5 = MyCanvas.create_window(14, 220, window = EquationSolver_Button, anchor = "nw")
        CanvasButton6 = MyCanvas.create_window(444, 320, window = ExpressionFactorization_Button, anchor = "nw")
        CanvasButton7 = MyCanvas.create_window(444, 220, window = HyperbolicTrig_Button, anchor = "nw")
        CanvasButton8 = MyCanvas.create_window(14, 270, window = InclinedPlane_Button, anchor = "nw")
        CanvasButton9 = MyCanvas.create_window(444, 270, window = ProjectileMotion_Button, anchor = "nw")
        CanvasButton10 = MyCanvas.create_window(244, 270, window = AngularVelocity_Button, anchor = "nw")
        CanvasButton11 = MyCanvas.create_window(244, 320, window = ResonantCircuit_Button, anchor = "nw")
        CanvasButton12 = MyCanvas.create_window(14, 320, window = RLCParallelCircuit_Button, anchor = "nw")
        CanvasButton13 = MyCanvas.create_window(14, 370, window = MagneticFlux_Button, anchor = "nw")
        CanvasButton14 = MyCanvas.create_window(14, 420, window = ElectromagneticInduction_Button, anchor = "nw")
        Canvas_TestButton = MyCanvas.create_window(324, 380, window = TestButton, anchor = "nw")



    def ComplexNumbers_ExplanationWindow(self):
        self.ComplexNumbers_Explanation = Toplevel()
        self.ComplexNumbers_Explanation.title("Test and Explanations")
        self.ComplexNumbers_Explanation.geometry("800x580")

        MyTitle = Label(self.ComplexNumbers_Explanation, text = "Explanation of Complex Numbers\n", font = ("Calibri", 32), pady = 8)
        MyTitle.pack(side = TOP)

        MyLabel_1 = Label(self.ComplexNumbers_Explanation, text = "Complex numbers are numbers in the form of a + bi. Where 'a' represents \nthe real number and 'bi' represents the imaginary number. \nThe imaginary number 'i' is equal to -1^1/2.", font = ("Arial", 14))
        MyLabel_1.pack(side = TOP, pady = 8)

        #MyLabel_2 = Label(self.ComplexNumbers_Explanation, text = "", font = ("Arial", 14))
        MyLabel_2 = Label(self.ComplexNumbers_Explanation, text = "Complex numbers are used to find solutions that contain an imaginary number.\n For example, x^2 + 1 cannot be solved with real numbers, because when you\n solve for x, the equation becomes x = (-1)^1/2. There is no real number\n that can satisfy the equation as you cannot take the \nsquare root of a negative number.", font = ("Arial", 14))
        MyLabel_2.pack(side = TOP, pady = 8)

        MyLabel_3 = Label(self.ComplexNumbers_Explanation, text = "However, using the definition of an imaginary number where i^2 = -1, (-1)^1/2 \nbecomes (i^2)^1/2. Which is then simplified to x = i.\n\nFor more information on Complex Numbers and how to convert complex numbers \nbetween rectangular and polar form, please use the link below: ", font = ("Arial", 14), pady = 8)
        MyLabel_3.pack(side = TOP, pady = 8)

        LinkLabel = Label(self.ComplexNumbers_Explanation, text = "https://brilliant.org/wiki/complex-numbers/ \n\n https://www.allaboutcircuits.com/textbook/alternating-current/chpt-2/polar-rectangular-notation/", font = ("Arial", 14), fg = "blue")
        LinkLabel.pack(side = TOP, pady = 8)



    def Differentiation_ExplanationWindow(self):
        self.Derivatives_Explanation = Toplevel()
        self.Derivatives_Explanation.title("Test and Explanations")
        self.Derivatives_Explanation.geometry("980x777")

        MyTitle = Label(self.Derivatives_Explanation, text = "Explanation of Differentiation", font = ("Calibri", 32), pady = 30)
        MyTitle.pack(side = TOP)

        MyLabel_1 = Label(self.Derivatives_Explanation, text = "A derivative of a mathematical function describes the rate of change \n(how much a quantity is increasing with respect to another quantity) of a function.\n\nDerivatives can be used to find the instantaneous rate of change at any point on the function.", font = ("Arial", 14))
        MyLabel_1.pack(side = TOP, pady = 8)

        MyLabel_2 = Label(self.Derivatives_Explanation, text = "There are several formulas used for calculating the derivative of a function, such as \nthe power rule, quotient rule, product rule and chain rule.\n\nThe function notation for derivatives is 'f'(x)'.\n", font = ("Arial", 14))
        MyLabel_2.pack(side = TOP, pady = 8)

        MyLabel_3 = Label(self.Derivatives_Explanation, text = "Power rule - is used differentiate a variable or a polynomial. If a variable x is raised to the \npower of a, where a is a constant, then the derivative of x^a will be ax^(a - 1).\n\nProduct rule - the product rule says that if two functions f(x) and g(x) are multiplied together, the derivative of\nthe product is f'(x)*g(x) + g'(x)*f(x).", font = ("Arial", 14))
        MyLabel_3.pack(side = TOP, pady = 8)

        Mylabel_4 = Label(self.Derivatives_Explanation, text = "Quotient rule - the quotient rule is used when a rational function in the form of f(x)/g(x) is to be differentiated\nThe derivative of a rational function is [f'(x)*g(x) - g'(x)*f(x)]/(g(x))^2.\n\nChain rule - the chain rule is used to differentiate a composite function (a function within a function). The derivative of\na composite function is f'(g(x))*g'(x).", font = ("Arial", 14))
        Mylabel_4.pack(side = TOP, pady = 8)

        MyLabel = Label(self.Derivatives_Explanation, text = "There is much more to differentiation than described here. \nFor more information on differentiation, please use the link provided below:", font = ("Arial", 14))
        MyLabel.pack(side = TOP, pady = 8)

        LinkLabel = Label(self.Derivatives_Explanation, text = "https://www.khanacademy.org/math/ap-calculus-bc/bc-differentiation-1-new", font = ("Arial", 14), fg = "blue")
        LinkLabel.pack(side = TOP, pady = 8)



    def Integration_ExplanationWindow(self):
        self.Integration_Explanation = Toplevel()
        self.Integration_Explanation.title("Test and Explanations")
        self.Integration_Explanation.geometry("990x740")

        MyTitle = Label(self.Integration_Explanation, text = "Explanation of Integration", font = ("Calibri", 32), pady = 30)
        MyTitle.pack(side = TOP)

        MyLabel_1 = Label(self.Integration_Explanation, text = "Integration (anti-derivative) is the inverse of differentiation (please refer to differentiation for more information).\n Integration is used to find the area underneath a curve of a function.\n\n", font = ("Arial", 14))
        MyLabel_1.pack(side = TOP, pady = 8)

        MyLabel_2 = Label(self.Integration_Explanation, text = "There are several formulas used for calculating the integral of a function. Such as the power rule, u-substitution and\nthe integration by parts.\n\nPower rule - power rules says that if a variable x is raised to the power n, then its anti-derivative (integral) is \n(x^(n + 1))/n + 1.", font = ("Arial", 14))
        MyLabel_2.pack(side = TOP, pady = 8)

        MyLabel_3 = Label(self.Integration_Explanation, text = "U-substitution - u-substitution is a method where a function f(g(x)), where g(x) is substituted with 'u'.\nU-substitution can be thought as the reverse chain-rule.\n\nIntegration by parts - Integration by parts is a formula that is applied when integrating two functions multiplied together.\nWhere one function is set equal to 'u' and the other is set equal to 'dv'. u is differentiated and dv is integrated and \nput in the form of 'uv -∫vdu'. ", font = ("Arial", 14))
        MyLabel_3.pack(side = TOP, pady = 8)

        MyLabel_4 = Label(self.Integration_Explanation, text = "For more information, please refer to the website below: \n", font = ("Arial", 14))
        MyLabel_4.pack(side = TOP, pady = 8)

        LinkLabel = Label(self.Integration_Explanation, text = "https://www.khanacademy.org/math/ap-calculus-bc/bc-integration-new", font = ("Arial", 14), fg = "blue")
        LinkLabel.pack(side = TOP, pady = 8)



    def SystemsOfEquation_ExplanationWindow(self):
        self.SOE_Explanation = Toplevel()
        self.SOE_Explanation.title("Explaining Systems of Equations")
        self.SOE_Explanation.geometry("970x480")

        MyTitle = Label(self.SOE_Explanation, text = "Explanation of Systems of Equations", font = ("Calibri", 32), pady = 30)
        MyTitle.pack(side = TOP)

        MyLabel_1 = Label(self.SOE_Explanation, text = "Systems of equations consists of two or more equations that have zero, one or n number of solutions \n(where n represents the highest degree of a variable). Systems of equations can be solved using the elimination \nor substitution method. Elimination involves manipulating the equations to get the like variables to cancel with \nanother until the equations combines and is left with one variable and numbers.\n ", font = ("Arial", 14))
        MyLabel_1.pack(side = TOP, pady = 8)

        MyLabel_2 = Label(self.SOE_Explanation, text = "Substitution is a method where equation is solved in terms of a variable. For example 2x + 5y = 3, when solved for \ny the equation becomes y = -2x/5 + 3/5.This equation would be substituted into another equation and replace all \ny's in the other equation/s with y = -2x/5 + 3/5. ", font = ("Arial", 14))
        MyLabel_2.pack(side = TOP, pady = 8)

        MyLabel_3 = Label(self.SOE_Explanation, text = "For more information on systems of equations, please visit the website below.", font = ("Arial", 14))
        MyLabel_3.pack(side = TOP, pady = 8)

        LinkLabel = Label(self.SOE_Explanation, text = "https://www.khanacademy.org/math/algebra-basics/alg-basics-systems-of-equations", font = ("Arial", 14), fg = "blue")
        LinkLabel.pack(side = TOP, pady = 8)



    def EquationSolver_ExplanationWindow(self):
        self.ES_Explanation = Toplevel()
        self.ES_Explanation.title("Explaining Equations")
        self.ES_Explanation.geometry("970x777")

        MyTitle = Label(self.ES_Explanation, text = "Explanation of Equations", font = ("Calibri", 32), pady = 30)
        MyTitle.pack(side = TOP)

        MyLabel_1 = Label(self.ES_Explanation, text = "An equation in simple terms is an algebraic expression equal to another algebraic expression. There are many \ndifferent kinds of expressions, such as polynomial equations, rational equations, trigonometric equations, \nlogarithmic equations and more.\n", font = ("Arial", 14))
        MyLabel_1.pack(side = TOP, pady = 8)

        MyLabel_2 = Label(self.ES_Explanation, text = "Main goal of every equation is to make the independent variable by itself on one side of the equation and\nthe other numbers (even variables) on the other side of the equation.\n\nFor example, let's say we have 4x + 1 = 5 - 12x.\n\nThe first step is subtract 1 from both sides which gives us\n\n4x = 4 - 12x.\n\nThen we add 12x to both sides.\n\n16x = 4\n\nThen we divide both sides by 16 to isolate x from the other numbers.\n\nx = 4/16 => 1/4.\n\nFor more information on solving equations, please use the link below.", font = ("Arial", 14))
        MyLabel_2.pack(side = TOP, pady = 8)

        LinkLabel = Label(self.ES_Explanation, text = "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:linear-equations-graphs\n\nhttps://www.khanacademy.org/math/algebra2", font = ("Arial", 14), fg = "blue")
        LinkLabel.pack(side = TOP, pady = 8)



    def Factorisation_Explanation(self):
        self.FE_Explanation = Toplevel()
        self.FE_Explanation.title("Explaining Equations")
        self.FE_Explanation.geometry("970x777")




    def TestUserWindow(self):
        self.TestWindow = Toplevel()
        self.TestWindow.title("Maths and Physics Test")
        self.TestWindow.geometry("700x400")

        self.Counter = 0
        self.CorrectAnswers = 0

        MyTitle = Label(self.TestWindow, text = "Maths and Physics Test", font = ("Calibri", 32), pady = 30)
        MyTitle.pack(side = TOP)

        self.QuestionLabel = Label(self.TestWindow, text = "What is 7 + 8i in polar form?", font = ("Arial", 14))
        self.QuestionLabel.pack(side = TOP, pady = 8)

        self.EntryBox = Entry(self.TestWindow, bd = 4, width = 12, font = ("Arial", 11))
        self.EntryBox.pack(side = TOP, pady = 8)

        self.NoteLabel = Label(self.TestWindow, text = "Please enter the answer the in form of a|b and round to the nearest unit.", font = ("Arial 12 bold"))
        self.NoteLabel.pack(side = TOP, pady = 8)

        self.MyButton = Button(self.TestWindow, width = 20, text = "Next Question", height = 2, bg = "#20bebe", fg = "White", font = ("Arial 12 bold"), command = lambda: self.CheckAnswer(self.EntryBox.get()), state = NORMAL)
        self.MyButton.pack(side = TOP, pady = 8)




    def CheckAnswer(self, UserInput):
        QuestionsList = ["What's the derivative of x^2 * cos(2x)?", "What is sinh(10) equal to?", "Completely factor x^2 + 7x + 10", "If a circuit had a voltage source of 10V and a resistor of 100Ω, what is the current?", "Determine the magnetic flux if the magnetic field strength is 10H,\nthe surface area is 12m^2 and the angle is 45 degrees.", "Solve 5x + 4 = 28 - 7x"]
        QuestionNote = ["Note:\n\nPlease type polynomials as 'x^2 + 2x + 4' and \nensure there is space between the operations symbols(*, + and -)", "Please round to the nearest unit", "Note:\n\nPlease type polynomials  'x^2 + 2x + 4'", "Please round to the nearest tenth.", "Please round to the nearest unit", "Please round to the nearest unit"]
        AnswersList = ["2x * cos(2x) - 2x^2 * sine(2x)", "11013", "(x + 2)(x + 5)", "0.1", "85", "2"]
        
        
        if (self.Counter == 0):
          if (UserInput == "11|49"):
                self.CorrectAnswers = self.CorrectAnswers + 1
                self.QuestionLabel.config(text = f"{QuestionsList[0]}")
                self.NoteLabel.config(text = f"{QuestionNote[0]}")
                self.Counter = self.Counter + 1
                print("Correct")

                self.EntryBox.delete(0, END)
                return


        while (self.Counter != 6):
            if (UserInput == AnswersList[self.Counter - 1]):
                self.CorrectAnswers = self.CorrectAnswers + 1
                
                self.QuestionLabel.config(text = f"{QuestionsList[self.Counter]}")
                self.NoteLabel.config(text = f"{QuestionNote[self.Counter]}")
                self.Counter = self.Counter + 1
                self.EntryBox.delete(0, END)
                print("Correct")
                return
            else:
                self.QuestionLabel.config(text = f"{QuestionsList[self.Counter]}")
                self.NoteLabel.config(text = f"{QuestionNote[self.Counter]}")
                self.Counter = self.Counter + 1
                self.EntryBox.delete(0, END)
                print("Wrong")
                return

        if (UserInput == AnswersList[5]):
            self.CorrectAnswers = self.CorrectAnswers + 1

        self.MyButton.config(state = DISABLED)

        self.ResultsWindow = Toplevel()
        self.ResultsWindow.title("Maths and Physics Test")
        self.ResultsWindow.geometry("400x340")

        MyTitle = Label(self.ResultsWindow, text = "Your results:", font = ("Calibri", 32), pady = 30)
        MyTitle.pack(side = TOP)

        if (self.CorrectAnswers == 0):
            Feedback = "Not great. Please go over everything and try again."
            ResultsLabel = Label(self.ResultsWindow, text = f"{self.CorrectAnswers}/{7}", font = ("Arial 18 bold"), fg = "red")
            FeedbackLabel = Label(self.ResultsWindow, text = f"{Feedback}", font = ("Arial", 12))

        if (self.CorrectAnswers < 2):
            Feedback = "Please go over what you struggled with and try again."
            ResultsLabel = Label(self.ResultsWindow, text = f"{self.CorrectAnswers}/{7}", font = ("Arial 18 bold"), fg = "orange")
            FeedbackLabel = Label(self.ResultsWindow, text = f"{Feedback}", font = ("Arial", 12))

        elif (self.CorrectAnswers == 2 or self.CorrectAnswers == 3):
            Feedback = "That was a decent understanding, \nbut please go over what you struggled with and \ntry again."
            ResultsLabel = Label(self.ResultsWindow, text = f"{self.CorrectAnswers}/{7}", font = ("Arial 18 bold"), fg = "#ABC13D")
            FeedbackLabel = Label(self.ResultsWindow, text = f"{Feedback}", font = ("Arial", 12))

        elif (self.CorrectAnswers >= 4 and self.CorrectAnswers <= 6):
            Feedback = "Great job!! You have solid understanding. \nKeep up the good work!"
            ResultsLabel = Label(self.ResultsWindow, text = f"{self.CorrectAnswers}/{7}", font = ("Arial 18 bold"), fg = "Green")
            FeedbackLabel = Label(self.ResultsWindow, text = f"{Feedback}", font = ("Arial", 12))

        elif (self.CorrectAnswers == 7):
            Feedback = "Perfect!!! Very well done!"
            ResultsLabel = Label(self.ResultsWindow, text = f"{self.CorrectAnswers}/{7}", font = ("Arial 18 bold"), fg = "#20bebe")
            FeedbackLabel = Label(self.ResultsWindow, text = f"{Feedback}", font = ("Arial", 12))

        ResultsLabel.pack(side = TOP, pady = 8)
        FeedbackLabel = Label(self.ResultsWindow, text = f"{Feedback}", font = ("Arial", 12))
        FeedbackLabel.pack(side = TOP, pady = 8)
        
        


        

    def GraphingCalculator(self):
        # This creates a new window
        # Graphing calculator window.
        self.GCWindow = Toplevel()

        self.GCWindow.title("Graphing Calculator")
        self.GCWindow.geometry("840x700")

        self.MainFrame = Frame(self.GCWindow, padx = 4, pady = 4)
        self.MainFrame.pack(side = TOP, fill = BOTH)

        # Create the title of the window (not title for the window)
        MyTitle = Label(self.MainFrame, text = "Graphing Calculator\n", font = ("Calibri", 32))
        MyTitle.pack(side = TOP)

        # Create labels and entry boxes
        MyLabel = Label(self.MainFrame, text = "Please enter a function you would like to graph", font = ("Arial", 18), pady = 4)
        MyLabel.pack(side = TOP)
        # Section #1
        EntryBox_Label = Label(self.MainFrame, text = "f(x) = \n", font = ("Arial 12 bold"), pady = 4)
        EntryBox_Label.pack()
        EntryBox = Entry(self.MainFrame, bd = 4, width = 20, font = ("Arial", 11))
        EntryBox.pack()
        self.ErrorLabel = Label(self.MainFrame, text = "\n", font = ("Arial", 12), pady = 10)
        self.ErrorLabel.pack(side = BOTTOM)
        ComputeButton = Button(self.MainFrame, text = "Produce Graph", width = 12, height = 2, bg = "#20bebe", fg = "White", font = ("Arial 14 bold"), command = lambda: self.GetGraph(EntryBox.get()))
        ComputeButton.pack(side = TOP, padx = 8, pady = 20)
        NoteLabel = Label(self.MainFrame, text = "Note:\n\nPlease type polynomials  'x^2 + 2x + 4' as x**2 + 2*x + 4.\nThe function e^x must be typed as exp(x).\n\nPlease ensure to use parentheses for exponential functions. 'x^5x + 1' should be typed as x**(5*x) + 1\n\nTo display multiple functions, Enter one function and press the button, then enter another function then press enter.\n Max number of functions that can be graphed together is 4.\n\n To clear the graphs, empty the entry box and press the 'Produce Graph' button.\n\n", fg = "black", font = "Calibri 13 bold" , relief = RIDGE, pady = 14)
        NoteLabel.pack(side = TOP, pady = 10)
        


    # Get input from the Graphing Calculator
    def GetGraph(self, UserInput = ""):
        CharStatus = True
        InputStatus = True

        CharStatus = self.InputLimiter(UserInput)

        if (CharStatus == False):
            self.ErrorLabel.config(text = f"?\nToo many characters.\n Maximum chararcters is 30", fg = "red")
            return

        InputStatus = GraphObject.GraphingFunction(UserInput)

        if (InputStatus == False):
            self.ErrorLabel.config(text = f"?\nYour input is not recognised. Please try again", fg = "red")
            return
        try:
            self.ErrorLabel.config(text = "The graph has been produced!!\n ", fg = "green")
        except Exception:
            UserInput = None



    # Create images for the Electronics Schematic to use
    def PrepareImages(self):
        
        ImageRLC = Image.open("Screenshot_1 - Resistor_Inductor_Capacitor.png")
        ImageR = Image.open("Screenshot_2 - Resistor.png")
        ImageRC = Image.open("Screenshot_3 - Resistor_Capacitor.png")
        ImageRR = Image.open("Screenshot_4 Resistor_Resistor.png")
        ImageRL = Image.open("Screenshot_8 - Resistor_Inductor.png")
        ImageRRR = Image.open("Screenshot_5 - Resistor_Resistor_Resistor.png")
        ImageRRL = Image.open("Screenshot_6 Resistor_Resistor_Inductor.png")
        ImageRRC = Image.open("Screenshot_7 - Resistor_Resistor_Capacitor.png")

        List = [ImageRLC, ImageR, ImageRR, ImageRL, ImageRC, ImageRRR, ImageRRL, ImageRRC]
        self.ImageList = []

        # Loop through each image inside the List
        # and resize each image and store inside new image
        for i in range(0, 8):
            self.ImageList.append(ImageTk.PhotoImage(List[i].resize((740, 240), Image.ANTIALIAS)))

        
            

    def ElectronicSchematicWindow(self):
        # Electronics Window
        self.EWindow = Toplevel()
        self.EWindow.title("Schematic Drawer")
        self.EWindow.geometry("820x900")

        # Set up frames to group similar widgets together
        CircuitFrame = Frame(self.EWindow, padx = 4)
        CircuitFrame.pack(side = BOTTOM)


        self.PrepareImages()

        # Place the image at the bottom
        self.CircuitSchematic = Label(CircuitFrame, image = self.ImageList[0])
        self.CircuitSchematic.grid(row = 0, column = 0, pady = 58)
        
        # Create the title of the window (not title for the window)
        MyTitle = Label(self.EWindow, text = "Schematic Designer", font = ("Calibri", 34), pady = 22)
        MyTitle.place(x = 224, y = 4, anchor = "nw")

        MyLabel = Label(self.EWindow, text = "Please enter the values for the voltage source, \n resistor/s and frequency (if capacitor or inductor is present).", font = ("Arial", 17))  
        MyLabel.place(x = 104, y = 100, anchor = "nw")

        VoltageLabel = Label(self.EWindow, text = "Voltage", font = ("Calibri", 14))
        VoltageLabel.place(x = 24, y = 200, anchor = "w")
        self.VoltageEntryBox = Entry(self.EWindow, bd = 4, width = 8, font = ("Calibri", 14))
        self.VoltageEntryBox.place(x = 94, y = 200, anchor = "w")

        InductorLabel = Label(self.EWindow, text = ", Inductance in mH", font = ("Calibri", 14))
        InductorLabel.place(x = 184, y = 200, anchor = "w")
        self.InductorEntryBox = Entry(self.EWindow, bd = 4, width = 8, font = ("Calibri", 14))
        self.InductorEntryBox.place(x = 339, y = 200, anchor = "w")

        CapacitorLabel = Label(self.EWindow, text = ", Capacitance in μF", font = ("Calibri", 14))
        CapacitorLabel.place(x = 428, y = 200, anchor = "w")
        self.CapacitorEntryBox = Entry(self.EWindow, bd = 4, width = 8, font = ("Calibri", 14))
        self.CapacitorEntryBox.place(x = 580, y = 200, anchor = "w")

        ResistorLabel1 = Label(self.EWindow, text = "Resistance (R1)", font = ("Calibri", 14))
        ResistorLabel1.place(x = 24, y = 260, anchor = "w")
        self.ResistorEntryBox1 = Entry(self.EWindow, bd = 4, width = 8, font = ("Calibri", 14))
        self.ResistorEntryBox1.place(x = 150, y = 260, anchor = "w")

        ResistanceLabel2 = Label(self.EWindow, text = ", Resistance (R2)", font = ("Calibri", 14))
        ResistanceLabel2.place(x = 240, y = 260, anchor = "w")
        self.ResistorEntryBox2 = Entry(self.EWindow, bd = 4, width = 8, font = ("Calibri", 14))
        self.ResistorEntryBox2.place(x = 380, y = 260, anchor = "w")

        ResistanceLabel3 = Label(self.EWindow, text = ", Resistance (R3)", font = ("Calibri", 14))
        ResistanceLabel3.place(x = 470, y = 260, anchor = "w")
        self.ResistorEntryBox3 = Entry(self.EWindow, bd = 4, width = 8, font = ("Calibri", 14))
        self.ResistorEntryBox3.place(x = 610, y = 260, anchor = "w")
        
        FrequencyLabel = Label(self.EWindow, text = "Frequency (Hz)", font = ("Calibri", 14))
        FrequencyLabel.place(x = 24, y = 320, anchor = "w")
        self.FrequencyEntryBox = Entry(self.EWindow, bd = 4, width = 8, font = ("Calibri", 14))
        self.FrequencyEntryBox.place(x = 148, y = 320, anchor = "w")

        InstructionLabel = Label(self.EWindow, text = "Please use the dropdown menu to choose the number of resistors.\nYou can also add a capacitor or inductor. The maximum components at once is 3.\n", font = ("Arial", 14))
        InstructionLabel.place(x = 24, y = 420, anchor = "w")

        R_Label = Label(self.EWindow, text = "R", font = ("Arial", 14))
        R_Label.place(x = 35, y = 470, anchor = "w")
        L_Label = Label(self.EWindow, text = "L", font = ("Arial", 14))
        L_Label.place(x = 104, y = 470, anchor = "w")
        C_Label = Label(self.EWindow, text = "C", font = ("Arial", 14))
        C_Label.place(x = 178, y = 470, anchor = "w")
        
        R_Clicked = IntVar()
        L_Clicked = IntVar()
        C_Clicked = IntVar()

        # The dropdown buttons will have "1" as its default value
        R_Clicked.set(1)
        L_Clicked.set(1)
        C_Clicked.set(1)
        
        # Creates a drop down menu
        ResistorDrop = OptionMenu(self.EWindow, R_Clicked, 1, 2, 3)
        ResistorDrop.place(x = 20, y = 494, anchor = "w")
        InductorDrop = OptionMenu(self.EWindow, L_Clicked, 0, 1)
        InductorDrop.place(x = 90, y = 494, anchor = "w")
        CapacitorDrop = OptionMenu(self.EWindow, C_Clicked, 0, 1)
        CapacitorDrop.place(x = 164, y = 494, anchor = "w")

        self.CircuitResultLabel = Label(self.EWindow, text = "Result:\n", font = ("Arial", 14), fg = "black" )
        self.CircuitResultLabel.place(x = 240, y = 494, anchor = "w")

        ComputeButton = Button(self.EWindow, text = "Calculate Circuit", width = 20, height = 2, bg = "#20bebe", fg = "White", font = ("Arial 12 bold"), command = lambda: self.GetCircuitValues(R_Clicked.get(), L_Clicked.get(), C_Clicked.get()))
        ComputeButton.place(x = 290, y = 335, anchor = "w")



    def DisplayCircuitValues(self, R_Input, L_Input, C_Input):
        
        if (R_Input == 1 and L_Input == 1 and C_Input == 1):
            self.CircuitResultLabel.config(text = f"Xc = {PhysicsObject.GetXc()}∠-90°Ω, XL = {PhysicsObject.GetXL()}∠90°Ω, Z = {PhysicsObject.GetZ()}∠{PhysicsObject.GetZ_Angle()}°Ω\nI = {PhysicsObject.GetTotal_I()}∠{PhysicsObject.GetI_Angle()}°A, Vc = {PhysicsObject.GetVc()}∠{PhysicsObject.GetC_Angle()}°V, VL = {PhysicsObject.GetVL()}∠{PhysicsObject.GetL_Angle()}°V\nVr = {PhysicsObject.GetVr()}∠{PhysicsObject.GetR_Angle()}°V, Power = {PhysicsObject.GetPower()}%", fg = "black")
            #self.CircuitResultLabel.config(text = f"Current = {PhysicsObject.GetTotal_I()}∠{PhysicsObject.GetC_Angle()}°, Vc = {PhysicsObject.GetVc()}∠{PhysicsObject.GetC_Angle()}°, VL = {PhysicsObject.GetVL()}∠{PhysicsObject.GetL_Angle()}°\n", fg = "black")
            #self.CircuitResultLabel.config(text = f"Vr = {PhysicsObject.GetVr()}∠{PhysicsObject.GetR_Angle()}°, Power = {PhysicsObject.GetPower()}", fg = "black")

        elif (R_Input == 1 and L_Input == 0 and C_Input == 0):
            self.CircuitResultLabel.config(text = f"Vr = {PhysicsObject.GetRes_1()}V, I = {PhysicsObject.GetTotal_I()}A, P = {PhysicsObject.GetPower()}W", fg = "black")

        elif (R_Input == 2 and L_Input == 0 and C_Input == 0):
            self.CircuitResultLabel.config(text = f"Vr1 = {PhysicsObject.GetRes_1()}V, Vr2 = {PhysicsObject.GetRes_2()}, I = {PhysicsObject.GetTotal_I()}A, P = {PhysicsObject.GetPower()}W", fg = "black")

        elif (R_Input == 1 and L_Input == 1 and C_Input == 0):
            self.CircuitResultLabel.config(text = f"XL = {PhysicsObject.GetXL()}∠90°Ω, Z = {PhysicsObject.GetZ()}∠{PhysicsObject.GetZ_Angle()}°Ω, I = {PhysicsObject.GetTotal_I()}∠{PhysicsObject.GetI_Angle()}°A\nVr = {PhysicsObject.GetRes_1()}∠{PhysicsObject.GetR_Angle()}°V, VL = {PhysicsObject.GetVL()}∠{PhysicsObject.GetL_Angle()}°V, Power Factor = {PhysicsObject.GetPower()}%", fg = "black")

        elif (R_Input == 1 and L_Input == 0 and C_Input == 1):
            self.CircuitResultLabel.config(text = f"Xc = {PhysicsObject.GetXc()}∠-90°Ω, Z = {PhysicsObject.GetZ()}∠{PhysicsObject.GetZ_Angle()}°Ω, I = {PhysicsObject.GetTotal_I()}∠{PhysicsObject.GetI_Angle()}°A\n Vr = {PhysicsObject.GetRes_1()}∠{PhysicsObject.GetR_Angle()}°V, Vc = {PhysicsObject.GetVc()}∠{PhysicsObject.GetC_Angle()}°V, Power Factor = {PhysicsObject.GetPower()}%", fg = "black")

        elif (R_Input == 3 and L_Input == 0 and C_Input == 0):
            self.CircuitResultLabel.config(text = f"Vr1 = {PhysicsObject.GetRes_1()}V, Vr2 = {PhysicsObject.GetRes_2()}V, Vr3 = {PhysicsObject.GetRes_3()}V,  I = {PhysicsObject.GetTotal_I()}A, P = {PhysicsObject.GetPower()}W", fg = "black")

        elif (R_Input == 2 and L_Input == 1 and C_Input == 0):
            self.CircuitResultLabel.config(text = f"XL = {PhysicsObject.GetXL()}∠90°Ω, Z = {PhysicsObject.GetZ()}∠{PhysicsObject.GetZ_Angle()}°Ω, \nI = {PhysicsObject.GetTotal_I()}∠{PhysicsObject.GetI_Angle()}°A, Vr1 = {PhysicsObject.GetRes_1()}∠{PhysicsObject.GetR_Angle()}°V, Vr2 = {PhysicsObject.GetRes_2()}∠{PhysicsObject.GetR_Angle()}°V, \nVL = {PhysicsObject.GetVL()}∠{PhysicsObject.GetL_Angle()}°V, Power Factor = {PhysicsObject.GetPower()}%", fg = "black")

        elif (R_Input == 2 and L_Input == 0 and C_Input == 1):
            self.CircuitResultLabel.config(text = f"Xc = {PhysicsObject.GetXc()}∠-90°Ω, Z = {PhysicsObject.GetZ()}∠{PhysicsObject.GetZ_Angle()}°Ω, \nI = {PhysicsObject.GetTotal_I()}∠{PhysicsObject.GetI_Angle()}°A, Vr1 = {PhysicsObject.GetRes_1()}∠{PhysicsObject.GetR_Angle()}°V, Vr2 = {PhysicsObject.GetRes_2()}∠{PhysicsObject.GetR_Angle()}V, \nVc = {PhysicsObject.GetVc()}∠{PhysicsObject.GetC_Angle()}°V, Power Factor = {PhysicsObject.GetPower()}%", fg = "black")



    # This function changes the circuit based on what the user chooses
    def GetCircuitValues(self, R_Input, L_Input, C_Input):        
        InputStatus = True
        CharStatus = True
        EntryNumber = 0

        # This will hold all the numbers entered from the user into a list
        InputList = [self.VoltageEntryBox.get(), self.InductorEntryBox.get(),
                     self.CapacitorEntryBox.get(), self.ResistorEntryBox1.get(),
                     self.FrequencyEntryBox.get(), self.ResistorEntryBox2.get(), self.ResistorEntryBox3.get()]

        # Holds the maximum number of components the user entered.
        NumberOfComponents = R_Input + L_Input + C_Input

        # If the maximum number of components exceed 3, then prompt the user
        # with a error message
        if (NumberOfComponents > 3):
            self.CircuitResultLabel.config(text = "Please choose a maximum \nof 3 components\n", fg = "red")
            return
        
        # Removes the previous schematic
        #self.CircuitSchematic.grid_forget()
        
        if (R_Input == 1 and L_Input == 1 and C_Input == 1):
            self.CircuitSchematic.config(image = self.ImageList[0])

            InputStatus = PhysicsObject.RLC_Circuits(InputList[0], InputList[1], InputList[2]
                                                     ,InputList[3], InputList[4])

            if (InputStatus == False):
                self.CircuitResultLabel.config(text = "Your input was not recognised. Please try again", fg = "red")
                return
            
            elif (InputStatus == "NEGATIVE NUMBER DETECTED"):
                self.CircuitResultLabel.config(text = "One of your inputs is '0' or less.\nPlease enter a number greater than 0.", fg = "red")
                return
            
            for i in range(0, 5):
                CharStatus = self.InputLimiter(InputList[i])

                if (CharStatus == False):
                    break
                EntryNumber = EntryNumber + 1

            if (CharStatus == False):
                self.CircuitResultLabel.config(text = "Your input for entry box {EntryNumber} has too many characters. Maximum characters is 30.", fg = "red")
                return

            self.DisplayCircuitValues(R_Input, L_Input, C_Input)
            return

            
        elif (R_Input == 1 and L_Input == 0 and C_Input == 0):
            self.CircuitSchematic.config(image = self.ImageList[1])

            InputStatus = PhysicsObject.OhmsLaw_Resistor(InputList[0], InputList[3])

            if (InputStatus == False):
                self.CircuitResultLabel.config(text = "Your input was not recognised.\nPlease try again", fg = "red")
                return

            elif (InputStatus == "NEGATIVE NUMBER DETECTED"):
                self.CircuitResultLabel.config(text = "One of your inputs is '0' or less. Please enter a number greater than 0.", fg = "red")
                return
            
            for i in range(0, 2):
                CharStatus = self.InputLimiter(InputList[i])

                if (CharStatus == False):
                    break
                #EntryNumber = EntryNumber + 1

            if (CharStatus == False):
                self.CircuitResultLabel.config(text = "Your input for one of the entry boxes has too many characters. Maximum characters is 30.", fg = "red")
                return

            self.DisplayCircuitValues(R_Input, L_Input, C_Input)
            return
            

        elif (R_Input == 2 and L_Input == 0 and C_Input == 0):
            self.CircuitSchematic.config(image = self.ImageList[2])

            InputStatus = PhysicsObject.OhmsLaw_ResistorResistor(InputList[0], InputList[3], InputList[5])

            if (InputStatus == False):
                self.CircuitResultLabel.config(text = "Your input was not recognised. Please try again", fg = "red")
                return

            elif (InputStatus == "NEGATIVE NUMBER DETECTED"):
                self.CircuitResultLabel.config(text = "One of your inputs is '0' or less.\nPlease enter a number greater than 0.", fg = "red")
                return
            
            for i in range(0, 3):
                CharStatus = self.InputLimiter(InputList[i])

                if (CharStatus == False):
                    break
                #EntryNumber = EntryNumber + 1

            if (CharStatus == False):
                self.CircuitResultLabel.config(text = "Your input for one of the entry boxes has too many characters. Maximum characters is 30.", fg = "red")
                return

            self.DisplayCircuitValues(R_Input, L_Input, C_Input)
            return


        elif (R_Input == 1 and L_Input == 1 and C_Input == 0):
            self.CircuitSchematic.config(image = self.ImageList[3])

            InputStatus = PhysicsObject.OhmsLaw_ResistorInductor(InputList[0], InputList[1], InputList[3], InputList[4])

            if (InputStatus == False):
                self.CircuitResultLabel.config(text = "Your input was not recognised. Please try again", fg = "red")
                return

            elif (InputStatus == "NEGATIVE NUMBER DETECTED"):
                self.CircuitResultLabel.config(text = "One of your inputs is '0' or less.\nPlease enter a number greater than 0.", fg = "red")
                return
            
            for i in range(0, 4):
                CharStatus = self.InputLimiter(InputList[i])

                if (CharStatus == False):
                    break
                #EntryNumber = EntryNumber + 1

            if (CharStatus == False):
                self.CircuitResultLabel.config(text = "Your input for one of the entry boxes has too many characters. Maximum characters is 30.", fg = "red")
                return

            self.DisplayCircuitValues(R_Input, L_Input, C_Input)
            return


        elif (R_Input == 1 and L_Input == 0 and C_Input == 1):
            self.CircuitSchematic.config(image = self.ImageList[4])

            InputStatus = PhysicsObject.OhmsLaw_ResistorCapacitor(InputList[0], InputList[2], InputList[3], InputList[4])

            if (InputStatus == False):
                self.CircuitResultLabel.config(text = "Your input was not recognised. Please try again", fg = "red")
                return

            elif (InputStatus == "NEGATIVE NUMBER DETECTED"):
                self.CircuitResultLabel.config(text = "One of your inputs is '0' or less.\nPlease enter a number greater than 0.", fg = "red")
                return
            
            for i in range(0, 4):
                CharStatus = self.InputLimiter(InputList[i])

                if (CharStatus == False):
                    break
                #EntryNumber = EntryNumber + 1

            if (CharStatus == False):
                self.CircuitResultLabel.config(text = "Your input for one of the entry boxes has too many characters. Maximum characters is 30.", fg = "red")
                return

            self.DisplayCircuitValues(R_Input, L_Input, C_Input)
            return


        elif (R_Input == 3 and L_Input == 0 and C_Input == 0):
            self.CircuitSchematic.config(image = self.ImageList[5])

            InputStatus = PhysicsObject.OhmsLaw_ResistorResistorResistor(InputList[0], InputList[3], InputList[5], InputList[6])

            if (InputStatus == False):
                self.CircuitResultLabel.config(text = "Your input was not recognised. Please try again", fg = "red")
                return

            elif (InputStatus == "NEGATIVE NUMBER DETECTED"):
                self.CircuitResultLabel.config(text = "One of your inputs is '0' or less.\nPlease enter a number greater than 0.", fg = "red")
                return
            
            for i in range(0, 4):
                CharStatus = self.InputLimiter(InputList[i])

                if (CharStatus == False):
                    break
                #EntryNumber = EntryNumber + 1

            if (CharStatus == False):
                self.CircuitResultLabel.config(text = "Your input for one of the entry boxes has too many characters. Maximum characters is 30.", fg = "red")
                return

            self.DisplayCircuitValues(R_Input, L_Input, C_Input)
            return
            

        elif (R_Input == 2 and L_Input == 1 and C_Input == 0):
            self.CircuitSchematic.config(image = self.ImageList[6])

            InputStatus = PhysicsObject.OhmsLaw_ResistorResistorInductor(InputList[0], InputList[1], InputList[3], InputList[4], InputList[5])

            if (InputStatus == False):
                self.CircuitResultLabel.config(text = "Your input was not recognised. Please try again", fg = "red")
                return

            elif (InputStatus == "NEGATIVE NUMBER DETECTED"):
                self.CircuitResultLabel.config(text = "One of your inputs is '0' or less.\nPlease enter a number greater than 0.", fg = "red")
                return
            
            for i in range(0, 5):
                CharStatus = self.InputLimiter(InputList[i])

                if (CharStatus == False):
                    break
                #EntryNumber = EntryNumber + 1

            if (CharStatus == False):
                self.CircuitResultLabel.config(text = "Your input for one of the entry boxes has too many characters. Maximum characters is 30.", fg = "red")
                return

            self.DisplayCircuitValues(R_Input, L_Input, C_Input)
            return
            

        elif (R_Input == 2 and L_Input == 0 and C_Input == 1):
            self.CircuitSchematic.config(image = self.ImageList[7])

            InputStatus = PhysicsObject.OhmsLaw_ResistorResistorCapacitor(InputList[0], InputList[2], InputList[3], InputList[4], InputList[5])

            if (InputStatus == False):
                self.CircuitResultLabel.config(text = "Your input was not recognised. Please try again", fg = "red")
                return

            elif (InputStatus == "NEGATIVE NUMBER DETECTED"):
                self.CircuitResultLabel.config(text = "One of your inputs is '0' or less.\nPlease enter a number greater than 0.", fg = "red")
                return
            
            for i in range(0, 5):
                CharStatus = self.InputLimiter(InputList[i])

                if (CharStatus == False):
                    break
                #EntryNumber = EntryNumber + 1

            if (CharStatus == False):
                self.CircuitResultLabel.config(text = "Your input for one of the entry boxes has too many characters. Maximum characters is 30.", fg = "red")
                return

            self.DisplayCircuitValues(R_Input, L_Input, C_Input)
            return
        


    # IMPORTANT WINDOW
    def MathsPhysicsWindow(self):
        # This creates a new window
        # Maths and Physics menu window.
        self.MPWindow = Toplevel()  

        # Set title of the image
        self.MPWindow.title("Mathematics and Physics")
        self.MPWindow.geometry("700x440")

        MathsImage = Image.open("Maths_Background3.jpg")
        MathsBackground = ImageTk.PhotoImage(MathsImage.resize((700, 540), Image.ANTIALIAS))
        
        self.MathsPicture = Label(self.MPWindow, image = MathsBackground)
        self.MathsPicture.place(x = 350, y = 0, anchor = "n")
                                            

        self.MPWindow.grid_columnconfigure(1, weight = 0)
        self.MPWindow.grid_columnconfigure(2, weight = 1)
        
        MyLabel = Label(self.MPWindow, text = "Mathematics", font = ("Calibri", 20))
        MyLabel.place(x = 4, y = 20, anchor = "nw")
        MyLabel2 = Label(self.MPWindow, text = "Physics", font = ("Calibri", 20))
        MyLabel2.place(x = 4, y = 224, anchor = "nw")
        
        # Place buttons on the "Maths and Physics" window
        ComplexNumber_Button = Button(self.MPWindow, text = "Complex Numbers", height = 1, font = ("Arial 11 bold"), command = self.ComplexNumbersWindow, bg = "#2558f5", fg = "white", width = 15)
        ComplexNumber_Button.place(x = 4, y = 90, anchor = "nw")
        
        Derivatives_Button = Button(self.MPWindow, text = "Differentiation", height = 1, font = ("Arial 11 bold"), command = self.DifferentiationWindow, bg = "#2558f5", fg = "white", width = 12)
        Derivatives_Button.place(x = 184, y = 90, anchor = "nw")
        
        Integration_Button = Button(self.MPWindow, text = "Integration", height = 1, font = ("Arial 11 bold"), command = self.IntegrationWindow, bg = "#2558f5", fg = "white", width = 11)
        Integration_Button.place(x = 340, y = 90, anchor = "nw")
        
        LinearEquations_Button = Button(self.MPWindow, text = "System Of Equations", height = 1, font = ("Arial 11 bold"), command = self.SystemsOfEquationsWindow, bg = "#2558f5", fg = "white", width = 17)
        LinearEquations_Button.place(x = 494, y = 90, anchor = "nw")
        
        EquationSolver = Button(self.MPWindow, text = "Equation Calculator", height = 1, font = ("Arial 11 bold"), command = self.EquationCalculatorWindow, bg = "#2558f5", fg = "white", width = 17)                                
        EquationSolver.place(x = 4, y = 140, anchor = "nw")
        
        ExpressionFactorization_Button = Button(self.MPWindow, text = "Expression Factorisation", font = ("Arial 11 bold"), command = self.FactorisationWindow, bg = "#2558f5", fg = "white", width = 20)
        ExpressionFactorization_Button.place(x = 204, y = 140, anchor = "nw")

        HyperbolicTrig_Button = Button(self.MPWindow, text = "Hyperbolic Functions", font = ("Arial 11 bold"), command = self.HyperbolicFunctions, bg = "#2558f5", fg = "white", width = 17) 
        HyperbolicTrig_Button.place(x = 430, y = 140, anchor = "nw")

        InclinedPlane_Button = Button(self.MPWindow, text = "Inclined Plane", font = ("Arial 11 bold"), command = self.InclinedPlane_Window, bg = "#2558f5", fg = "white", width = 14)
        InclinedPlane_Button.place(x = 4, y = 294, anchor = "nw")

        ProjectileMotion_Button = Button(self.MPWindow, text = "Projectile Motion", font = ("Arial 11 bold"), command = self.ProjectileMotion_Window, bg = "#2558f5", fg = "white", width = 14)
        ProjectileMotion_Button.place(x = 170, y = 294, anchor = "nw")

        AngularVelocity_Button = Button(self.MPWindow, text = "Angular Velocity", font = ("Arial 11 bold"), command = self.AngularVelocity_Window, bg = "#2558f5", fg = "white", width = 14)
        AngularVelocity_Button.place(x = 338, y = 294, anchor = "nw")

        ResonantCircuit_Button = Button(self.MPWindow, text = "Resonant Circuit", font = ("Arial 11 bold"), command = self.RLCResonantCircuit_Window, bg = "#2558f5", fg = "white", width = 14)
        ResonantCircuit_Button.place(x = 510, y = 294, anchor = "nw")

        RLCParallelCircuit_Button = Button(self.MPWindow, text = "RLC Parallel Circuit", font = ("Arial 11 bold"), command = self.RLCParallelCircuit_Window, bg = "#2558f5", fg = "white", width = 17)
        RLCParallelCircuit_Button.place(x = 4, y = 349, anchor = "nw")

        MagneticFlux_Button = Button(self.MPWindow, text = "Magnetic Flux", font = ("Arial 11 bold"), command = self.MagneticFlux_Window, bg = "#2558f5", fg = "white", width = 12)
        MagneticFlux_Button.place(x = 204, y = 349, anchor = "nw")

        ElectromagneticInduction = Button(self.MPWindow, text = "Electromagnetic Induction", font = ("Arial 11 bold"), command = self.ElectromagenticInduction_Window, bg = "#2558f5", fg = "white", width = 22)
        ElectromagneticInduction.place(x = 358, y = 349, anchor = "nw")


        # To keep the window running
        # ** MAKE SURE TO ADD THIS FOR EVERY FUNCTION THAT CREATES WINDOW EVEN IF IT WORKS WITHOUT ONE **
        self.MPWindow.mainloop()
        
        #Radiobutton(self.FirstFrame, text = "Complex Numbers", variable = Index, value = 1).grid(row = 1, column = 0)
        #Radiobutton(self.FirstFrame, text = "Other", variable = Index, value = 2).grid(row = 1, column = 1)

        #MyButton = Button(self.FirstFrame, text = "Button", command = lambda: print(Index.get()))
        #MyButton.grid(row = 2, column = 0)




        # This function will count the number of characters in an argument.
        # If the number of characters (numbers included) exceed 20, then the function will return false
    def InputLimiter(self, Arg):
        CharacterStatus = False
        NumOfChars = 0

        # "Arg.count("")" will count all the characters in the string inside the variable "Arg".
        # Because the count function includes the end of line character, we have to subtract by 1 in order to get the true char count.
        NumOfChars = Arg.count("") - 1

        if (NumOfChars > 30):
            return CharacterStatus
        else:
            CharacterStatus = True
            return CharacterStatus


        

    # This function receives inputs from the entry box when the button on the Complex Number window is pressed
    # This function belongs to the "ComplexNumbersWindow"
    def GetInput_ComplexWindow(self, UserInput_1, UserInput_2, ButtonNumber):
        CharStatus = True
        EntryList = [UserInput_1, UserInput_2]
    
        # This variable will identify which input had too many characters
        EntryNumber = 1
        
        # If the button on the bottom left is pressed, then run the code within this if statement.
        # This if statement is for rectangular - Polar conversion.
        if (ButtonNumber == 1):
            # This for loop passes the user's inputs into a function that will count the number of characters
            # If the CharStatus returns false, then the loop will break and tell the user there is too many characters
            for i in range(0, 2):
                CharStatus = self.InputLimiter(EntryList[i])

                if (CharStatus == False):
                    break
                EntryNumber = EntryNumber + 1

            # If CharStatus is false, then display the following string
            if (CharStatus == False):
                self.ComplexResultLabel.config(text = f"Polar coordinates = ?\nToo many characters for entry box {EntryNumber}.", fg = "red")
                return

            # Checks to see if the user's inputs are valid
            # The function returns true if all inputs are valid
            InputStatus_1 = MathsObject.ComplexNumber_RecToPolar(UserInput_1, UserInput_2)
            
            # This will check whether the inputs valid or not.
            if (InputStatus_1 == False):
                self.ComplexResultLabel.config(text = "Polar coordinates = ?\nYour input is not recognized. Please try again", fg = "red")
                return

            print(f"{MathsObject.GetModulus()}∠{MathsObject.Theta}°")
            # Update the label and display the results onto the screen
            self.ComplexResultLabel.config(text = f"Polar coordinates = {MathsObject.GetModulus()}∠{MathsObject.GetTheta()}°", fg = "black")
            
        elif (ButtonNumber == 2):
            # Pass each input in the entry list to Input limiter method
            for i in range(0, 2):
                CharStatus = self.InputLimiter(EntryList[i])

                # If an input has too many characters, then set CharStatus equal to False
                if (CharStatus == False):
                    break
                EntryNumber = EntryNumber + 1

            # If CharStatus is false, then display the following string
            if (CharStatus == False):
                self.ComplexResultLabel2.config(text = f"Rectangular coordinates = ?\nToo many characters for entry box {EntryNumber}.", fg = "red")
                return

            # Pass the inputs to the method to be converted to rectangular coordinates
            InputStatus_2 = MathsObject.ComplexNumber_PolarToRec(UserInput_1, UserInput_2)

            # If the inputs are valid, then display the following string
            if (InputStatus_2 == False):
                self.ComplexResultLabel2.config(text = "Rectangular coordinates = ?\nYour input is not recognised. Please try again", fg = "red")
                return
            
            print(f"{MathsObject.GetModulus()}∠{MathsObject.Theta}°")
            # Update the label and display the results onto the screen
            self.ComplexResultLabel2.config(text = f"Rectangular coordinates = {MathsObject.GetComplexNumber()}", fg = "black")




    # This creates a window to convert between rectanglar coordinates and polar coordinates and displays it on screen
    def ComplexNumbersWindow(self):
        self.ComplexWindow = Toplevel()
        self.ComplexWindow.title("Complex Numbers - Rectangular and Polar Forms")
        self.ComplexWindow.geometry("400x400")

        # Display the labels
        TitleLabel = Label(self.ComplexWindow, text = "Rectangular and Polar Forms", font = ("Calibri",22), pady = 18)
        TitleLabel.pack(side = TOP)
        MyLabel = Label(self.ComplexWindow, text = "Please enter the rectangular coordinates below (a, bi)", font = ("Arial", 11), pady = 10)
        MyLabel.pack(side = TOP)

        # Insert entry boxes onto the screen
        EntryBox_1 = Entry(self.ComplexWindow)
        EntryBox_1.pack(side = TOP, pady = 4)
        EntryBox_2 = Entry(self.ComplexWindow)
        EntryBox_2.pack(side = TOP, pady = 4)

        # This label will be updated each time the user press the "Rec - polar" buttion
        self.ComplexResultLabel = Label(self.ComplexWindow, text = "Polar coordinates = ", font = ("Arial", 11), pady = 8)
        self.ComplexResultLabel.pack(side = TOP)

        MyLabel2 = Label(self.ComplexWindow, text = "Please enter the polar coordinates below (r, θ)", font = ("Arial", 11), pady = 10)
        MyLabel2.pack(side = TOP)

        EntryBox_3 = Entry(self.ComplexWindow)
        EntryBox_3.pack(side = TOP, pady = 4)
        EntryBox_4 = Entry(self.ComplexWindow)
        EntryBox_4.pack(side = TOP, pady = 4)

        # This label will be updated each time the user press the "Rec - polar" buttion 
        self.ComplexResultLabel2 = Label(self.ComplexWindow, text = "Rectangular coordinates = ", font = ("Arial", 11), pady = 8)
        self.ComplexResultLabel2.pack(side = TOP)

        # This displays the buttions
        MyButton = Button(self.ComplexWindow, text = "Convert Rectangular - Polar", bg = "#20bebe", fg = "White", width = 20, height = 2, font = ("Arial 10 bold"), padx = 10, command = lambda: self.GetInput_ComplexWindow(EntryBox_1.get(), EntryBox_2.get(), 1))
        MyButton2 = Button(self.ComplexWindow, text = "Convert Polar - Rectangular", bg = "#20bebe", fg = "White", width = 20, height = 2, font = ("Arial 10 bold") ,padx = 10, command = lambda: self.GetInput_ComplexWindow(EntryBox_3.get(), EntryBox_4.get(), 2))
        MyButton.pack(side = LEFT)
        MyButton2.pack(side = RIGHT)



    # For derivatives
    def GetInput_DifferentiationWindow(self, UserInput, ButtonNumber):
        CharStatus = True
        
        # Checks if the number of inputs is equal to 1
        if (ButtonNumber == 1):
            CharStatus = self.InputLimiter(UserInput)

            if (CharStatus == False):
                self.DerivativeResultLabel.config(text = "f'(x) = ?\nToo many characters for entry box 1.\n Maximum chararcters is 30", fg = "red")
                return

            InputStatus_1 = MathsObject.Calculus_Derivatives(UserInput)

            if (InputStatus_1 == False):
                self.DerivativeResultLabel.config(text = "f'(x) = ?\nYour input is not recognised. Please try again", fg = "red")
                return

            self.DerivativeResultLabel.config(text = f"f'(x) = {MathsObject.GetDerivative()}", fg = "black")
            



    def GetInput_QuotientRule_DifferentiationWindow(self, UserInput_1, UserInput_2):
        # CharStatus will hold information on whether the user entered too many chars
        CharStatus = True
        EntryList = [UserInput_1, UserInput_2]
        
        # Will hold the corresponding entry box number.
        # If the input in box one has too many characters,
        # then this variable will be used to display the entry box number that had too mant chars
        EntryNumber = 2

        for i in range(0, 2):
            CharStatus = self.InputLimiter(EntryList[i])

            if (CharStatus == False):
                break
            EntryNumber = EntryNumber + 1

        # Check to see if one of the inputs have too many characters
        if (CharStatus == False):
            self.QuotientResultLabel.config(text = f"dy/dx = ?\nToo many characters for entry box {EntryBox}.\n Maximum chararcters is 30", fg = "red")
            return
        
        InputStatus = MathsObject.Derivatives_QuotientRule(UserInput_1, UserInput_2)

        # If user's input is invalid, display the following message
        if (InputStatus == False):
            self.QuotientResultLabel.config(text = f"dy/dx = ?\nYour input is not recognised. Please try again", fg = "red")
            return

        if (MathsObject.GetSignCheck_QuotientRule() == "N"):
            self.QuotientResultLabel.config(text = f"dy/dx = [ {MathsObject.GetQuotientRule_LeftDerivative()} + ({MathsObject.GetQuotientRule_RightDerivative()}) ]/{MathsObject.GetQuotientRule_V_Squared()}", fg = "black")
            
        elif (MathsObject.GetSignCheck_QuotientRule() == "P"):
            self.QuotientResultLabel.config(text = f"dy/dx = [ {MathsObject.GetQuotientRule_LeftDerivative()} - ({MathsObject.GetQuotientRule_RightDerivative()}) ]/{MathsObject.GetQuotientRule_V_Squared()}", fg = "black")




    # This function creates a window that will ask the user for an expression to calculate its derivative
    def DifferentiationWindow(self):
        self.DerivativeWindow = Toplevel()
        self.DerivativeWindow.geometry("540x720")
        self.DerivativeWindow.title("Derivative Calculator")

        # Create the title of the window (not title for the window)
        MyTitle = Label(self.DerivativeWindow, text = "Derivative Calculator", font = ("Calibri", 32), pady = 22)
        MyTitle.pack(side = TOP)
        
        # The rest of the code below creates the labels and entry boxes for the window
        # Order of when each label and entry box is important. Change with care if needed
        MyLabel = Label(self.DerivativeWindow, text = "Please enter an expression in terms of x", font = ("Arial", 14) ,pady = 8).pack(side = TOP)
        EntryBox = Entry(self.DerivativeWindow, bd = 4, width = 30, font = ("Arial", 11))
        EntryBox.pack(side = TOP)
        
        MyLabel2 = Label(self.DerivativeWindow, text = "Please enter expressions that involves the quotient rule below (f(x)/g(x))", font = "Arial 11 bold" ,pady = 10)
        MyLabel2.pack(side = TOP)
        
        self.DerivativeResultLabel = Label(self.DerivativeWindow, text = "f'(x) = \n", font = ("Arial", 14), pady = 4)
        self.DerivativeResultLabel.pack(side = TOP)
        
        MyLabel3 = Label(self.DerivativeWindow, text = "Please enter expressions for f(x) and g(x) respectively.", font = "Arial 12", pady = 10)
        MyLabel3.pack(side = TOP)
        
        MyLabelFX = Label(self.DerivativeWindow, text = "f(x): ", font = ("Arial", 11), pady = 2, padx = 2)
        MyLabelFX.pack(side = TOP)
        EntryBox2 = Entry(self.DerivativeWindow, bd = 4, width = 20, font = ("Arial", 11))
        EntryBox2.pack(side = TOP)
        
        MyLabelGX = Label(self.DerivativeWindow, text = "g(x): ", font = ("Arial", 11), pady = 2)
        MyLabelGX.pack(side = TOP)
        EntryBox3 = Entry(self.DerivativeWindow, bd = 4, width = 20, font = ("Arial", 11))
        EntryBox3.pack(side = TOP)
        
        self.QuotientResultLabel = Label(self.DerivativeWindow, text = "dy/dx = ", font = ("Arial", 14), pady = 18)
        self.QuotientResultLabel.pack(side = TOP)
        
        NoteLabel = Label(self.DerivativeWindow, text = "Note:\n\nPlease type polynomials such as 'x^2 + 2x + 4' as x**2 + 2*x + 4.\nThe function e^x must be typed as exp(x).\n\nPlease ensure to use parentheses for exponential functions.\n'x^5x + 1' should be typed as x**(5*x + 1) to avoid miscalculation", fg = "black", font = "Calibri 13 bold" ,relief = RIDGE, pady = 14)
        NoteLabel.pack(side = TOP)
        
        # Create the buttons that will retrieve inputs from the entry box
        ComputeButton = Button(self.DerivativeWindow, text = "Calculate Derivative", width = 20, height = 2, bg = "#20bebe", fg = "White", font = ("Arial 10 bold"), command = lambda: self.GetInput_DifferentiationWindow(EntryBox.get(), 1))
        ComputeButton.pack(side = LEFT)
        ComputeButton2 = Button(self.DerivativeWindow, text = "Calculate Quotient", width = 20, height = 2, bg = "#20bebe", fg = "White", font = ("Arial 10 bold"), command = lambda: self.GetInput_QuotientRule_DifferentiationWindow(EntryBox2.get(), EntryBox3.get()))
        ComputeButton2.pack(side = RIGHT)



        # Display integral result onto screen
    def GetIntegralFunction(self, UserInput):
        InputStatus = True
        CharStatus = True

        CharStatus = self.InputLimiter(UserInput)

        if (CharStatus == False):
            self.IntegralResult_Label.config(text = f"Integral = ?\nToo many characters.\n Maximum chararcters is 30", fg = "red")
            return

        InputStatus = MathsObject.Integration(UserInput)

        if (InputStatus == False):
            self.IntegralResult_Label.config(text = f"Integral = ?\nYour input is invalid. Please try again", fg = "red")
            return

        self.IntegralResult_Label.config(text = f"Integral = {MathsObject.GetIntegral()} + C", fg = "black")
            
        


    # Integration window
    def IntegrationWindow(self):
        self.IntegrationScreen = Toplevel()
        self.IntegrationScreen.title("Integration Calculator")
        self.IntegrationScreen.geometry("430x490")

        # Create the title of the window (not title for the window)
        MyTitle = Label(self.IntegrationScreen, text = "Integration Calculator", font = ("Calibri", 30), pady = 20)
        MyTitle.pack(side = TOP)

        # Create labels and entry boxes
        MyLabel = Label(self.IntegrationScreen, text = "Please enter an expression in terms of x", font = ("Arial", 14) ,pady = 8).pack(side = TOP)
        EntryBox = Entry(self.IntegrationScreen, bd = 4, width = 30, font = ("Arial", 11))
        EntryBox.pack(side = TOP)
        self.IntegralResult_Label = Label(self.IntegrationScreen, text = "Integral = \n", font = ("Arial", 13), pady = 12)
        self.IntegralResult_Label.pack(side = TOP)
        ComputeButton = Button(self.IntegrationScreen, text = "Calculate Integral", width = 14, height = 2, bg = "#20bebe", fg = "White", font = ("Arial 12 bold"), command = lambda: self.GetIntegralFunction(EntryBox.get()))
        ComputeButton.pack(side = TOP)
        NoteLabel = Label(self.IntegrationScreen, text = "Note:\n\nPlease type polynomials such as 'x^2 + 2x + 4' as x**2 + 2*x + 4.\nThe function e^x must be typed as exp(x).\n\nPlease ensure to use parentheses for exponential functions.\n'x^5x + 1' should be typed as x**(5*x + 1) to avoid miscalculation", fg = "black", font = "Calibri 11 bold" ,relief = RIDGE, pady = 14)
        NoteLabel.pack(side = TOP, pady = 10)



    # Get results for the systems of equations
    def GetLinearResult(self, UserInput1, UserInput2):
        InputStatus = True
        CharStatus = True
        # Put comment here
        EntryBoxNumber = 0

        # Check the input for entry box #1 exceeded 30 characters
        CharStatus = self.InputLimiter(UserInput1)

        # If the user entered more than 30 characters, then display the following error message
        if (CharStatus == False):
            EntryBoxNumber = 1
            self.LinearResult_Label.config(text = f"Points of intersection = (?, ?) = ?\nToo many characters for entry box {EntryBoxNumber}.\n Maximum chararcters is 30", fg = "red")
            return

        # Check the input for entry box #1 exceeded 30 characters
        CharStatus = self.InputLimiter(UserInput2)

        # Pass the inputs into the 'SystemsOfEquations' function inside the Mathematics_Module
        # If inputs are valid, return true. If not, return false
        InputStatus = MathsObject.SystemOfEquations(UserInput1, UserInput2)

        # If the second input has too many characters, then display error message
        if (CharStatus == False):
            EntryBoxNumber = 2
            self.LinearResult_Label.config(text = f"Points of intersection = (?, ?) = ?\nToo many characters for entry box {EntryBoxNumber}.\n Maximum chararcters is 30", fg = "red")
            return

        # If one of the inputs is invalid, display error message
        if (InputStatus == False):
            self.LinearResult_Label.config(text = "Points of intersection = (?, ?)\nYour input was not recognised. Please ensure to type linear functions \nlike '3x + 2y - 4' as '3*x + 2*y - 4' and try again.", fg = "red")
            return

        # If the lines do not intersect, then display a message
        elif (InputStatus == "LINES DOES NOT INTERSECT"):
            self.LinearResult_Label.config(text = "Points of intersection = (?, ?)\nThe lines are in parallel", fg = "orange")
            return

        # if one of the variables in the user's inputs has a degree not equal to 1, then display error message
        if (MathsObject.GetSOE_Degree() == "1"):
            self.LinearResult_Label.config(text = "Points of intersection = (?, ?)\nPlease make sure all variables have a degree of 1", fg = "red")
            return

        # Display the roots to the user
        self.LinearResult_Label.config(text = "Points of intersection = ({}, {})".format(round(-1*MathsObject.GetSystemOfEquation_LinearRoot_1(), 3), round(-1*MathsObject.GetSystemOfEquation_LinearRoot_2(), 3)), fg = "black")

        

    # Systems of equations
    def SystemsOfEquationsWindow(self):
        self.LinearScreen = Toplevel()
        self.LinearScreen.title("Systems Of Equations Calculator")
        self.LinearScreen.geometry("490x490")

        # First frame for the title
        self.TitleFrame = Frame(self.LinearScreen, padx = 4, pady = 20)
        self.TitleFrame.pack(side = TOP, fill = BOTH)
        # Second frame for the main body of the screen
        self.MainFrame = Frame(self.LinearScreen, padx = 4, pady = 4)
        self.MainFrame.pack(side = TOP, fill = BOTH, pady = 4)

        # Create the title of the window (not title for the window)
        MyTitle = Label(self.TitleFrame, text = "Systems Of Equations\nCalculator", font = ("Calibri", 32))
        MyTitle.pack(side = TOP)

        # Create labels and entry boxes
        MyLabel = Label(self.MainFrame, text = "Please enter two linear equations in the form of Ax + By + C.", font = ("Arial", 12), pady = 34)
        MyLabel.grid(row = 0, column = 0)
        # Section #1
        EntryBox_Label = Label(self.MainFrame, text = "Linear equation #1: \n", font = ("Arial", 11), pady = 4)
        EntryBox_Label.grid(row = 1, sticky = "W")
        EntryBox = Entry(self.MainFrame, bd = 4, width = 20, font = ("Arial", 10))
        EntryBox.grid(row = 1, sticky = "N", pady = 4)
        # Section #2
        EntryBox_Label2 = Label(self.MainFrame, text = "Linear equation #2: \n", font = ("Arial", 11), pady = 8)
        EntryBox_Label2.grid(row = 2, sticky = "W")
        EntryBox2 = Entry(self.MainFrame, bd = 4, width = 20, font = ("Arial", 10))
        EntryBox2.grid(row = 2, sticky = "N", pady = 4)

        self.LinearResult_Label = Label(self.MainFrame, text = "Points of intersection = (x, y) \n", font = ("Arial", 12), pady = 10)
        self.LinearResult_Label.grid(row = 3, sticky = "N", pady = 4)

        ComputeButton = Button(self.MainFrame, text = "Calculate system of equations", width = 24, height = 2, bg = "#20bebe", fg = "White", font = ("Arial 11 bold"), command = lambda: self.GetLinearResult(EntryBox.get(), EntryBox2.get()))
        ComputeButton.grid(row = 4, sticky = "N")


      
    def GetRootFunction(self, UserInput1, UserInput2):
        InputStatus = True 
        CharStatus = True
        EntryNumber = 1

        # Stores the user's inputs into a list
        EntryList = [UserInput1, UserInput2]

        # Loops through each element in the list and passes the element (one-by-one) into the InputLimiter function
        for i in range(0, 2):
            CharStatus = self.InputLimiter(EntryList[i])

            # If input has too many characters, then break loop
            if (CharStatus == False):
                break
            EntryNumber = EntryNumber + 1


        # If there are too many characters, display error message
        if (CharStatus == False):
            self.RootsLabel.config(text = f"Roots = ?\nToo many characters for entry box {EntryNumber}.\n Maximum chararcters is 30", fg = "red")
            return


        # Pass the user's inputs to 'RootsOfEquation_Calculator' function in the Mathematics_Module
        # If user's inputs are valid, then return true. If not, return false
        InputStatus = MathsObject.RootsOfEquation_Calculator(UserInput1, UserInput2)

        
        # If user's input is invalid, display error message
        if (InputStatus == False):
            self.RootsLabel.config(text = "Roots = ?\nYour input was not recognised. \nPlease ensure to type equations such as 'x^2 + 7x + 12'\n as 'x**2 + 7*x + 12' and try again", fg = "red")
            return

        # If the user's input cannot be solved by the function, then display a message to user
        if (InputStatus == "CANNOT BE SOLVED"):
            self.RootsLabel.config(text = "Roots = ?\nSorry. Cannot solve the equation.\n Please ensure to use similar functions with each other.", fg = "red")
            return
        
        # If the user's input variable/s are too high, then display error message
        elif (InputStatus == "DEGREE TOO HIGH"):
            self.RootsLabel.config(text = "Roots = ?\nPlease ensure the degree is below 5", fg = "red")
            return
        
        # If list is empty, then display message
        elif (InputStatus == "EMPTY LIST"):
            self.RootsLabel.config(text = "Roots = NO SOLUTIONS\n", fg = "red")
            return
        # 
        elif (InputStatus == "INFINITE SOLUTIONS"):
            self.RootsLabel.config(text = "Roots = Infinite solutions", fg = "black")
            return

        # Display the answer to the screen
        self.RootsLabel.config(text = f"Roots = {MathsObject.GetRoots()}", fg = "black")



    # This function is to display the Equation Calculator window
    def EquationCalculatorWindow(self):
        # Equation Calculator Window
        self.ECWindow = Toplevel()
        self.ECWindow.title("Equation Solver Calculator")
        self.ECWindow.geometry("540x510")

        # Create the title of the window (not title for the window)
        MyTitle = Label(self.ECWindow, text = "Equation Calculator", font = ("Calibri", 34), pady = 20)
        MyTitle.place(x = 280, y = 10, anchor = "n")

        # Create labels and entry boxes
        MyLabel = Label(self.ECWindow, text = "Please enter an equation in terms of x.\n(Other Letters will be treated as a type of number)\n\nPlease enter the left side of the equation to the left entry box\n and right side of the equation to the right entry box.", font = ("Arial", 14) , pady = 4)
        MyLabel.place(x = 270, y = 140, anchor = "n")
        EntryBox = Entry(self.ECWindow, bd = 4, width = 14, font = ("Arial", 12))
        EntryBox.place(x = 180, y = 280, anchor = "n")
        EqualSign = Label(self.ECWindow, text = "= \n", font = ("Arial", 14), pady = 10)
        EqualSign.place(x = 270, y = 270, anchor = "n")
        EntryBox2 = Entry(self.ECWindow, bd = 4, width = 14, font = ("Arial", 12))
        EntryBox2.place(x = 355, y = 280, anchor = "n")
        self.RootsLabel = Label(self.ECWindow, text = "Roots = \n", font = ("Arial", 14))
        self.RootsLabel.place(x = 250, y = 340, anchor = "n")
        ComputeButton = Button(self.ECWindow, text = "Solve Equation", width = 24, height = 2, bg = "#20bebe", fg = "White", font = ("Arial 14 bold"), command = lambda: self.GetRootFunction(EntryBox.get(), EntryBox2.get()))
        ComputeButton.place(x = 250, y = 440, anchor = "n")



    # Get expression from the Factorisation window
    def GetExpression(self, UserInput):
        InputStatus = True
        CharStatus = True

        CharStatus = self.InputLimiter(UserInput)

        if (CharStatus == False):
            self.FactorLabel.config(text = "Factored Expression = ?\nToo many characters.\n Maximum chararcters is 30", fg = "red")
            return

        InputStatus = MathsObject.PolynomialFactorization_Calculator(UserInput)

        if (InputStatus == False):
            self.FactorLabel.config(text = "Factored Expression = ?\nYour input is invalid. Please try again", fg = "red")
            return
        
        elif (InputStatus == "NO CHANGES"):
            self.FactorLabel.config(text = f"Factored Expression = {UserInput}\nCannot be factored any further.", fg = "orange")
            return

        self.FactorLabel.config(text = f"Factored Expression = {MathsObject.GetFactoredExpression()}", fg = "black")



    # Factoring Calculator Window
    # Gets a mathematical expression (Often polynomial) and factors the expression
    def FactorisationWindow(self):
        self.FactorisationWindow = Toplevel()
        self.FactorisationWindow.title("Factoring Calculator")
        self.FactorisationWindow.geometry("540x480")

        # Create the title of the window (not title for the window)
        MyTitle = Label(self.FactorisationWindow, text = "Factorising Calculator", font = ("Calibri", 32), pady = 20)
        MyTitle.pack(side = TOP)

        # Create labels and entry boxes
        MyLabel = Label(self.FactorisationWindow, text = "Please enter an expression in terms of x", font = ("Arial", 12) ,pady = 4).pack(side = TOP)
        EntryBox = Entry(self.FactorisationWindow, bd = 4, width = 30, font = ("Arial", 12))
        EntryBox.pack(side = TOP)
        self.FactorLabel = Label(self.FactorisationWindow, text = "Factored expression = \n", font = ("Arial", 12), pady = 10)
        self.FactorLabel.pack(side = TOP)
        ComputeButton = Button(self.FactorisationWindow, text = "Factor Expression", width = 17, height = 2, bg = "#20bebe", fg = "White", font = ("Arial 11 bold"), command = lambda: self.GetExpression(EntryBox.get()), padx = 2)
        ComputeButton.pack(side = TOP)
        NoteLabel = Label(self.FactorisationWindow, text = "Note:\n\nPlease type polynomials such as 'x^2 + 2x + 4' as x**2 + 2*x + 4.\nThe function e^x must be typed as exp(x).\n\nPlease ensure to use parentheses for exponential functions.\n'x^5x + 1' should be typed as x**(5*x + 1) to avoid miscalculation", fg = "black", font = "Calibri 11 bold" ,relief = RIDGE, pady = 14)
        NoteLabel.pack(side = TOP, pady = 14)



    def GetHyperbolicExpression(self, UserInput):
        InputStatus = True  
        CharStatus = True

        CharStatus = self.InputLimiter(UserInput)

        # If the number of characters are above 30, then prompt the user with an error message
        if (CharStatus == False):
            self.NumericExpression.config(text = "Result = ?\nToo many characters.\n Maximum chararcters is 30", fg = "red")
            return
        
        # Pass the input from the user to the 'HyperbolicFunction_Calculator' function inside the Mathematics_Module
        # If input is valid, return true. If not, return false
        InputStatus = MathsObject.HyperbolicFunction_Calculator(UserInput)

        # If input is false, then prompt user with an error message on screen
        if (InputStatus == False):
            self.NumericExpression.config(text = "Result = ?\nSorry. Your input is not recognised. \nPlease try again", fg = "red")
            return

        # If input has a term the code doesn't recogise, then prompt user with an error message on screen
        elif (InputStatus == "UNRECOGNISED TERM"):
            self.NumericExpression.config(text = f"Result = ?\nSorry, '{UserInput}' could not be recognised.\nPlease try again", fg = "red")
            return

        # If input has a variable that cannot be evaluated, then prompt user with an error message on screen
        elif (InputStatus == "UNEVALUTED FUNCTION"):
            self.NumericExpression.config(text = f"Result = ?\nThere was a term that could not be evaluated.\nPlease try again", fg = "orange")
            return

        # Display answer to the user
        self.NumericExpression.config(text = f"Result = {MathsObject.GetHyperbolicResult()}", fg = "black")
    

    
    def HyperbolicFunctions(self):
        self.HyperbolicWindow = Toplevel()
        self.HyperbolicWindow.title("Hyperbolic Function Calculator")
        self.HyperbolicWindow.geometry("580x480")

        # Create the title of the window (not title for the window)
        MyTitle = Label(self.HyperbolicWindow, text = "Hyperbolic Function Calculator", font = ("Calibri", 32), pady = 20)
        MyTitle.pack(side = TOP)

        # Create labels and entry boxes
        MyLabel = Label(self.HyperbolicWindow, text = "Please enter a numeric hyperbolic function\nyou would like to evaluate.", font = ("Arial", 12) , pady = 8)
        MyLabel.pack(side = TOP)
        EntryBox = Entry(self.HyperbolicWindow, bd = 4, width = 30, font = ("Arial", 12))
        EntryBox.pack(side = TOP)
        self.NumericExpression = Label(self.HyperbolicWindow, text = "Result = \n", font = ("Arial", 12), pady = 10)
        self.NumericExpression.pack(side = TOP)
        ComputeButton = Button(self.HyperbolicWindow, text = "Evaluate Expression", width = 17, height = 2, bg = "#20bebe", fg = "White", font = ("Arial 12 bold"), command = lambda: self.GetHyperbolicExpression(EntryBox.get()), padx = 4)
        ComputeButton.pack(side = TOP)
        NoteLabel = Label(self.HyperbolicWindow, text = "Note:\n\nPlease type polynomials such as 'x^2 + 2x + 4' as x**2 + 2*x + 4.\nThe function e^x must be typed as exp(x).\n\nPlease ensure to use parentheses for exponential functions.\n'x^5x + 1' should be typed as x**(5*x + 1) to avoid miscalculation", fg = "black", font = "Calibri 11 bold" ,relief = RIDGE, pady = 14)
        NoteLabel.pack(side = TOP, pady = 14)


        ######## PHYSICS FUNCTIONS ########


    def InclinedPlane_Window(self):
        # Inclined Plane Window
        self.IPWindow = Toplevel()
        self.IPWindow.title("Inclined Plane Calculator")
        self.IPWindow.geometry("730x570")

        PictureFrame = Frame(self.IPWindow, padx = 4, pady = 4)
        PictureFrame.pack(side = BOTTOM)

        # Create the title of the window (not title for the window)
        MyTitle = Label(self.IPWindow, text = "Inclined Plane Calculator", font = ("Calibri", 32), pady = 20)
        MyTitle.place(x = 110, y = 24, anchor = "nw")

        MyLabel = Label(self.IPWindow, text = "Please enter the mass of the block (in kg), the angle of the inclined plane in degrees,\nthe length of the plane (in m) and the coefficient of friction.", font = ("Arial", 14))
        MyLabel.place(x = 14, y = 130, anchor = "nw")
        ImageIP = Image.open("Inclined_plane.png")
        ResizedImage = ImageIP.resize((610, 210), Image.ANTIALIAS)
        self.InclinedPlane_Image = ImageTk.PhotoImage(ResizedImage)

        self.IPLabel = Label(self.IPWindow, image = self.InclinedPlane_Image)
        self.IPLabel.pack(side = BOTTOM)

        # Create labels and entry boxes
        MassLabel = Label(self.IPWindow, text = "Mass", font = ("Arial", 12))
        MassLabel.place(x = 24, y = 220, anchor = "nw")
        Entrybox1 = Entry(self.IPWindow, bd = 4, width = 8, font = ("Arial", 10))
        Entrybox1.place(x = 72, y = 220, anchor = "nw")

        AngleLabel = Label(self.IPWindow, text = "Angle (in °)", font = ("Arial", 12))
        AngleLabel.place(x = 184, y = 220, anchor = "nw")
        Entrybox2 = Entry(self.IPWindow, bd = 4, width = 8, font = ("Arial", 10))
        Entrybox2.place(x = 270, y = 220, anchor = "nw")

        DistanceLabel = Label(self.IPWindow, text = "Length", font = ("Arial", 12))
        DistanceLabel.place(x = 380, y = 220, anchor = "nw")
        Entrybox3 = Entry(self.IPWindow, bd = 4, width = 8, font = ("Arial", 10))
        Entrybox3.place(x = 439, y = 220, anchor = "nw")

        FrictionLabel = Label(self.IPWindow, text = "Friction", font = ("Arial", 12))
        FrictionLabel.place(x = 545, y = 220, anchor = "nw")
        Entrybox4 = Entry(self.IPWindow, bd = 4, width = 8, font = ("Arial", 10))
        Entrybox4.place(x = 620, y = 220, anchor = "nw")

        self.InclinedLabel = Label(self.IPWindow, text = "Results = ", font = ("Arial", 13))
        self.InclinedLabel.place(x = 184, y = 290, anchor = "nw")
        
        # Create button
        ComputeButton = Button(self.IPWindow, text = "Compute", width = 10, height = 2, bg = "#20bebe", fg = "White", font = ("Arial 12 bold"), command = lambda: self.GetInclinedPlane(Entrybox1.get(), Entrybox2.get(), Entrybox3.get(), Entrybox4.get()))
        ComputeButton.place(x = 34, y = 280, anchor = "nw")


        
    def GetInclinedPlane(self, UserInput1, UserInput2, UserInput3, UserInput4):
        InputStatus = True
        CharStatus = True
        EntryNumber = 1

        # If one of the inputs are greater than 30 characters, then it will
        # return false

        EntryList = [UserInput1, UserInput2, UserInput3, UserInput4]

        for i in range(0, 4):
            CharStatus = self.InputLimiter(EntryList[i])
            
            if (CharStatus == False):
                break
            EntryNumber = EntryNumber + 1
            

        if (CharStatus == False):
            self.InclinedLabel.config(text = f"Result = ?\nToo many characters for entry box {EntryNumber}.\n Maximum chararcters is 30", fg = "red")
            return

        InputStatus = PhysicsObject.Mechanics_InclinedPlane(UserInput1, UserInput2, UserInput3, UserInput4)

        if (InputStatus == False):
            self.InclinedLabel.config(text = "Result = ?\nSorry. Your input is not recognised. \nPlease try again", fg = "red")
            return
        
        elif (InputStatus == "INPUT BELOW ZERO"):
            self.InclinedLabel.config(text = "Result = ?\nPlease ensure all numbers are above 0.\n", fg = "red")

        elif (InputStatus == "FRICTION TOO LOW"):
            self.InclinedLabel.config(text = "Result = ?\nFriction cannot be below 0.\n", fg = "red")

        elif (InputStatus == "FRICTION TOO HIGH"):
            self.InclinedLabel.config(text = "Result = ?\nPlease ensure the friction is between 0 and 1.\n", fg = "red")
        
        self.InclinedLabel.config(text = f"Final velocity = {PhysicsObject.GetVelocity_InclinedPlane()}m/s\n\nAcceleration = {PhysicsObject.GetAcceleration_InclinedPlane()}m/s^2", fg = "black")
    
    

    def ProjectileMotion_Window(self):
        # Projectile Motion Window
        self.PMWindow = Toplevel()
        self.PMWindow.title("Projected Motion Calculator")
        self.PMWindow.geometry("590x640")

        PictureFrame = Frame(self.PMWindow, padx = 4, pady = 4)
        PictureFrame.pack(side = BOTTOM)

        # Create the title of the window (not title for the window)
        MyTitle = Label(self.PMWindow, text = "Projectile Motion Calculator", font = ("Calibri", 32), pady = 20)
        MyTitle.place(x = 57, y = 24, anchor = "nw")

        MyLabel = Label(self.PMWindow, text = "Please enter the initial velocity of the object in meters\nand the angle of flight in degrees.", font = ("Arial", 14))
        MyLabel.place(x = 74, y = 130, anchor = "nw")

        # Opens the image, resizes it and then assigns the image to the variable
        ImagePM = Image.open("ProjectileMotion.png")
        ResizedImage = ImagePM.resize((570, 230), Image.ANTIALIAS)
        self.ProjectileMotion_Image = ImageTk.PhotoImage(ResizedImage)

        # Display image on screen
        self.PMLabel = Label(self.PMWindow, image = self.ProjectileMotion_Image)
        self.PMLabel.pack(side = BOTTOM)

        # Create labels and entry boxes
        VelocityLabel = Label(self.PMWindow, text = "Velocity", font = ("Arial", 12))
        VelocityLabel.place(x = 24, y = 220, anchor = "nw")
        Entrybox1 = Entry(self.PMWindow, bd = 4, width = 8, font = ("Arial", 10))
        Entrybox1.place(x = 89, y = 220, anchor = "nw")

        AngleLabel = Label(self.PMWindow, text = "Angle (in °)", font = ("Arial", 12))
        AngleLabel.place(x = 201, y = 220, anchor = "nw")
        Entrybox2 = Entry(self.PMWindow, bd = 4, width = 8, font = ("Arial", 10))
        Entrybox2.place(x = 287, y = 220, anchor = "nw")

        self.ProjectileLabel = Label(self.PMWindow, text = "Results = ", font = ("Arial", 13))
        self.ProjectileLabel.place(x = 184, y = 270, anchor = "nw")
        
        # Create button
        ComputeButton = Button(self.PMWindow, text = "Compute", width = 10, height = 2, bg = "#20bebe", fg = "White", font = ("Arial 12 bold"), command = lambda: self.GetProjectileValues(Entrybox1.get(), Entrybox2.get()))
        ComputeButton.place(x = 34, y = 280, anchor = "nw")
        PlatformButton = Button(self.PMWindow, text = "Projectile Motion (Platform)", width = 24, height = 2, bg = "#3CA0EC", fg = "White", font = ("Arial 10 bold"), command = self.HeightPlatform_Window)
        PlatformButton.place(x = 380, y = 200, anchor = "nw")



    def GetProjectileValues(self, UserInput1, UserInput2):
        InputStatus = True
        CharStatus = True
        EntryNumber = 1

        # If one of the inputs are greater than 30 characters, then it will
        # return false
        EntryList = [UserInput1, UserInput2]

        for i in range(0, 2):
            CharStatus = self.InputLimiter(EntryList[i])
            
            if (CharStatus == False):
                break
            EntryNumber = EntryNumber + 1
            

        if (CharStatus == False):
            self.ProjectileLabel.config(text = f"Result = ?\nToo many characters for entry box {EntryNumber}.\n Maximum chararcters is 30", fg = "red")
            return

        InputStatus = PhysicsObject.Mechanics_ProjectileMotion(UserInput1, UserInput2)

        if (InputStatus == False):
            self.ProjectileLabel.config(text = "Result = ?\nSorry. Your input is not recognised. \nPlease try again", fg = "red")
            return
        
        elif (InputStatus == "INPUT BELOW ZERO"):
            self.ProjectileLabel.config(text = "Result = ?\nPlease ensure all numbers are above 0.\n", fg = "red")

        self.ProjectileLabel.config(text = f"Maximum height of the object = {PhysicsObject.GetMaxHeight_ProjectileMotion()}m\n\nTime taken to reach max height = {PhysicsObject.GetMaxHeightTime_ProjectileMotion()}s\n\nTotal Distance travelled: {PhysicsObject.GetTotalDistance_ProjectileMotion()}m\n\nTotal time in the air: {PhysicsObject.GetTotalTime_ProjectileMotion()}s", fg = "black")
        return



    def HeightPlatform_Window(self):
        # Projectile Motion Window
        self.HPWindow = Toplevel()
        self.HPWindow.title("Projectile Motion (Platform) Calculator")
        self.HPWindow.geometry("590x640")

        PictureFrame = Frame(self.PMWindow, padx = 4, pady = 4)
        PictureFrame.pack(side = BOTTOM)

        # Create the title of the window (not title for the window)
        MyTitle = Label(self.HPWindow, text = "Projectile Motion Calculator\n(with platform)", font = ("Calibri", 32), pady = 4)
        MyTitle.place(x = 40, y = 20, anchor = "nw")

        MyLabel = Label(self.HPWindow, text = "Please enter the initial velocity of the object and the height \nof the platform.", font = ("Arial", 14))
        MyLabel.place(x = 14, y = 143, anchor = "nw")

        # Opens the image, resizes it and then assigns the image to the variable
        ImageHP = Image.open("Platform.png")
        ResizedImage = ImageHP.resize((570, 220), Image.ANTIALIAS)
        self.PlatformMotion_Image = ImageTk.PhotoImage(ResizedImage)

        # Display image on screen
        self.PMLabel = Label(self.HPWindow, image = self.PlatformMotion_Image)
        self.PMLabel.pack(side = BOTTOM)

        # Create labels and entry boxes
        VelocityLabel = Label(self.HPWindow, text = "Velocity (m/s)", font = ("Arial", 12))
        VelocityLabel.place(x = 24, y = 220, anchor = "nw")
        Entrybox1 = Entry(self.HPWindow, bd = 4, width = 8, font = ("Arial", 10))
        Entrybox1.place(x = 128, y = 220, anchor = "nw")

        HeightLabel = Label(self.HPWindow, text = "Height (m)", font = ("Arial", 12))
        HeightLabel.place(x = 244, y = 220, anchor = "nw")
        Entrybox2 = Entry(self.HPWindow, bd = 4, width = 8, font = ("Arial", 10))
        Entrybox2.place(x = 338, y = 220, anchor = "nw")

        self.PlatformLabel = Label(self.HPWindow, text = "Results = ", font = ("Arial", 13))
        self.PlatformLabel.place(x = 184, y = 270, anchor = "nw")
        
        # Create button
        ComputeButton = Button(self.HPWindow, text = "Compute", width = 10, height = 2, bg = "#20bebe", fg = "White", font = ("Arial 12 bold"), command = lambda: self.GetPlatformMotionValues(Entrybox1.get(), Entrybox2.get()))
        ComputeButton.place(x = 34, y = 280, anchor = "nw")
        



    def GetPlatformMotionValues(self, UserInput1, UserInput2):
        InputStatus = True
        CharStatus = True
        EntryNumber = 1

        # If one of the inputs are greater than 30 characters, then it will
        # return false
        EntryList = [UserInput1, UserInput2]

        for i in range(0, 2):
            CharStatus = self.InputLimiter(EntryList[i])
            
            if (CharStatus == False):
                break
            EntryNumber = EntryNumber + 1
            

        if (CharStatus == False):
            self.PlatformLabel.config(text = f"Result = ?\nToo many characters for entry box {EntryNumber}.\n Maximum chararcters is 30", fg = "red")
            return

        InputStatus = PhysicsObject.Mechanics_PM_Platform(UserInput1, UserInput2)

        if (InputStatus == False):
            self.PlatformLabel.config(text = "Result = ?\nSorry. Your input is not recognised. \nPlease try again", fg = "red")
            return
        
        elif (InputStatus == "HEIGHT BELOW ZERO"):
            self.PlatformLabel.config(text = "Result = ?\nPlease ensure the height of the platform is above 0.\n", fg = "red")

        self.PlatformLabel.config(text = f"Final velocity = {PhysicsObject.GetFinalVelocity()}m/s\n\nTime taken in the air = {PhysicsObject.GetTimeTaken()}s\n\nTotal Distance travelled: {PhysicsObject.GetDistance()}m\n\nFinal of angle of descent: -{PhysicsObject.GetProjectileAngle()}°", fg = "black")
        #return



    def AngularVelocity_Window(self):
        # Angular Velocity Window
        self.AVWindow = Toplevel()
        self.AVWindow.title("Angular Velocity Calculator")
        self.AVWindow.geometry("590x640")

        PictureFrame = Frame(self.AVWindow, padx = 4, pady = 4)
        PictureFrame.pack(side = BOTTOM)

        # Create the title of the window (not title for the window)
        MyTitle = Label(self.AVWindow, text = "Angular Velocity Calculator", font = ("Calibri", 32), pady = 20)
        MyTitle.place(x = 58, y = 24, anchor = "nw")

        MyLabel = Label(self.AVWindow, text = "Please enter the change in angle in degrees, the time taken in\nseconds and the radius in meters.", font = ("Arial", 14))
        MyLabel.place(x = 34, y = 130, anchor = "nw")
        ImageAV = Image.open("Angular_Velocity_Circle.png")
        ResizedImage = ImageAV.resize((570, 240), Image.ANTIALIAS)
        self.AngularVelocity_Image = ImageTk.PhotoImage(ResizedImage)

        self.AVLabel = Label(self.AVWindow, image = self.AngularVelocity_Image)
        self.AVLabel.pack(side = BOTTOM)

        # Create labels and entry boxes
        AngleLabel = Label(self.AVWindow, text = "Angle", font = ("Arial", 12))
        AngleLabel.place(x = 24, y = 220, anchor = "nw")
        Entrybox1 = Entry(self.AVWindow, bd = 4, width = 8, font = ("Arial", 10))
        Entrybox1.place(x = 74, y = 220, anchor = "nw")

        TimeLabel = Label(self.AVWindow, text = "Time", font = ("Arial", 12))
        TimeLabel.place(x = 210, y = 220, anchor = "nw")
        Entrybox2 = Entry(self.AVWindow, bd = 4, width = 8, font = ("Arial", 10))
        Entrybox2.place(x = 258, y = 220, anchor = "nw")

        RadiusLabel = Label(self.AVWindow, text = "Radius", font = ("Arial", 12))
        RadiusLabel.place(x = 380, y = 220, anchor = "nw")
        Entrybox3 = Entry(self.AVWindow, bd = 4, width = 8, font = ("Arial", 10))
        Entrybox3.place(x = 439, y = 220, anchor = "nw")

        self.AngularLabel = Label(self.AVWindow, text = "Results = ", font = ("Arial", 13))
        self.AngularLabel.place(x = 184, y = 290, anchor = "nw")
        
        # Create button
        ComputeButton = Button(self.AVWindow, text = "Compute", width = 10, height = 2, bg = "#20bebe", fg = "White", font = ("Arial 12 bold"), command = lambda: self.GetAngularValues(Entrybox1.get(), Entrybox2.get(), Entrybox3.get()))
        ComputeButton.place(x = 34, y = 280, anchor = "nw")



    def GetAngularValues(self, UserInput1, UserInput2, UserInput3):
        InputStatus = True
        CharStatus = True
        EntryNumber = 1

        # If one of the inputs are greater than 30 characters, then it will
        # return false
       
        EntryList = [UserInput1, UserInput2, UserInput3]

        for i in range(0, 3):
            CharStatus = self.InputLimiter(EntryList[i])
            
            if (CharStatus == False):
                break
            EntryNumber = EntryNumber + 1
            

        if (CharStatus == False):
            self.AngularLabel.config(text = f"Result = ?\nToo many characters for entry box {EntryNumber}.\n Maximum chararcters is 30", fg = "red")
            return

        InputStatus = PhysicsObject.AngularVelocityFunction(UserInput1, UserInput2, UserInput3)

        if (InputStatus == False):
            self.AngularLabel.config(text = "Result = ?\nSorry. Your input is not recognised. \nPlease try again", fg = "red")
            return
        
        elif (InputStatus == "INPUT BELOW ZERO"):
            self.AngularLabel.config(text = "Result = ?\nPlease ensure all numbers are above 0.\n", fg = "red")
            return

        elif (InputStatus == "TIME LESS THAN ZERO"):
            self.AngularLabel.config(text = "Result = ?\nPlease ensure the time is not below or equal to 0", fg = "red")
            return

        elif (InputStatus == "RADIUS LESS THAN ZERO"):
            self.AngularLabel.config(text = "Result = ?\nPlease ensure the radius is not below or equal to 0", fg = "red")
            return

        self.AngularLabel.config(text = f"Angular velocity = {PhysicsObject.GetAngular_Velocity()}rad/s\n\nLinear velocity = {PhysicsObject.GetLinearVelocity()}m/s", fg = "black")



    def RLCResonantCircuit_Window(self):
        # Resonant Circuir Window
        self.RCWindow = Toplevel()
        self.RCWindow.title("Resonant RLC Circuit Calculator")
        self.RCWindow.geometry("670x640")

        PictureFrame = Frame(self.RCWindow, padx = 4, pady = 4)
        PictureFrame.pack(side = BOTTOM)

        ImageRC = Image.open("Screenshot_1 - Resistor_Inductor_Capacitor.png")
        ResizedImage = ImageRC.resize((640, 240), Image.ANTIALIAS)
        self.ResonantCircuit_Image = ImageTk.PhotoImage(ResizedImage)

        # Create the title of the window (not title for the window)
        MyTitle = Label(self.RCWindow, text = "Resonant Circuit Calculator", font = ("Calibri", 32), pady = 20)
        MyTitle.place(x = 88, y = 24, anchor = "nw")

        MyLabel = Label(self.RCWindow, text = "Please enter the values for the voltage source, inductance,\ncapacitance and the resistor's resistance.", font = ("Arial", 14))
        MyLabel.place(x = 80, y = 130, anchor = "nw")

        self.RCLabel = Label(self.RCWindow, image = self.ResonantCircuit_Image)
        self.RCLabel.pack(side = BOTTOM)

        VoltageLabel = Label(self.RCWindow, text = "Voltage Source", font = ("Arial", 12))
        VoltageLabel.place(x = 20, y = 210, anchor = "nw")
        EntryBox1 = Entry(self.RCWindow, bd = 4, width = 8, font = ("Arial", 10))
        EntryBox1.place(x = 140, y = 210, anchor = "nw")

        InductorLabel = Label(self.RCWindow, text = "Inductance (mH)", font = ("Arial", 12))
        InductorLabel.place(x = 230, y = 210, anchor = "nw")
        EntryBox2 = Entry(self.RCWindow, bd = 4, width = 8, font = ("Arial", 10))
        EntryBox2.place(x = 358, y = 210, anchor = "nw")

        CapacitorLabel = Label(self.RCWindow, text = "Capacitance (μF)", font = ("Arial", 12))
        CapacitorLabel.place(x = 444, y = 210, anchor = "nw")
        EntryBox3 = Entry(self.RCWindow, bd = 4, width = 8, font = ("Arial", 10))
        EntryBox3.place(x = 580, y = 210, anchor = "nw")

        ResistanceLabel = Label(self.RCWindow, text = "Resistance (R)", font = ("Arial", 12))
        ResistanceLabel.place(x = 20, y = 280, anchor = "nw")
        EntryBox4 = Entry(self.RCWindow, bd = 4, width = 8, font = ("Arial", 10))
        EntryBox4.place(x = 140, y = 280, anchor = "nw")

        self.ResonantLabel = Label(self.RCWindow, text = "Result = ?", font = ("Arial",12))
        self.ResonantLabel.place(x = 240, y = 280, anchor = "nw")

        # Create button
        ComputeButton = Button(self.RCWindow, text = "Compute", width = 10, height = 2, bg = "#20bebe", fg = "White", font = ("Arial 12 bold"), command = lambda: self.GetResonantResult(EntryBox1.get(), EntryBox2.get(), EntryBox3.get(), EntryBox4.get()))
        ComputeButton.place(x = 20, y = 332, anchor = "nw")



    def GetResonantResult(self, UserInput1, UserInput2, UserInput3, UserInput4):
        InputStatus = True
        CharStatus = True
        EntryNumber = 1

        # If one of the inputs are greater than 30 characters, then it will
        # return false

        EntryList = [UserInput1, UserInput2, UserInput3, UserInput4]

        for i in range(0, 4):
            CharStatus = self.InputLimiter(EntryList[i])
            
            if (CharStatus == False):
                break
            EntryNumber = EntryNumber + 1
            

        if (CharStatus == False):
            self.ResonantLabel.config(text = f"Result = ?\nToo many characters for entry box {EntryNumber}.\n Maximum chararcters is 30", fg = "red")
            return

        InputStatus = PhysicsObject.Resonant_Circuits_Series(UserInput1, UserInput2, UserInput3, UserInput4)

        if (InputStatus == False):
            self.ResonantLabel.config(text = "Result = ?\nSorry. Your input is not recognised. \nPlease try again", fg = "red")
            return
        
        elif (InputStatus == "INPUT BELOW ZERO"):
            self.ResonantLabel.config(text = "Result = ?\nPlease ensure all numbers are above 0.\n", fg = "red")
            return

        self.ResonantLabel.config(text = f"Resonant frequency = {PhysicsObject.GetResonantFrequency()}Hz\n\noverall current = {PhysicsObject.GetResonantCurrent()}A\n\nResistor voltage = {PhysicsObject.GetResonantResistorVoltage()}V", fg = "black")
        
        self.RC_Window = Toplevel()
        self.RC_Window.title("Resonant Current")
        self.RC_Window.geometry("590x540")

        PictureFrame = Frame(self.RCWindow, padx = 4, pady = 4)
        PictureFrame.pack(side = BOTTOM)

        # Open image
        Image_RC = Image.open("Frequency Responce.png")
        ResizedImage = Image_RC.resize((580, 300), Image.ANTIALIAS)
        self.ResonantFrequency_Image = ImageTk.PhotoImage(ResizedImage)

        # Display Image
        self.RCLabel = Label(self.RC_Window, image = self.ResonantFrequency_Image)
        self.RCLabel.pack(side = BOTTOM)

        MyTitle = Label(self.RC_Window, text = "Frequency Responce", font = ("Calibri", 32), pady = 20)
        MyTitle.pack(side = TOP)
        
        ResultLabel = Label(self.RC_Window, text = f"I_max = {PhysicsObject.GetResonantCurrent()}A, I_RMS = {PhysicsObject.GetResonantRMS()}A\n\nF_L = {PhysicsObject.GetLowFrequency()}Hz, F_H = {PhysicsObject.GetHighFrequency()}Hz, BW = {PhysicsObject.GetBandwidth()}Hz\n\nQ = {PhysicsObject.GetQualityFactor()}", font = ("Arial", 14))
        ResultLabel.pack(side = TOP)



    def RLCParallelCircuit_Window(self):
        # RLC Parallel Circuir Window
        self.RPWindow = Toplevel()
        self.RPWindow.title("RLC Parallel Circuit Calculator")
        self.RPWindow.geometry("680x724")

        PictureFrame = Frame(self.RPWindow, padx = 4, pady = 4)
        PictureFrame.pack(side = BOTTOM)

        ImageRP = Image.open("RLC_Parallel.png")
        ResizedImage = ImageRP.resize((640, 240), Image.ANTIALIAS)
        self.RLCParallelCircuit_Image = ImageTk.PhotoImage(ResizedImage)

        # Create the title of the window (not title for the window)
        MyTitle = Label(self.RPWindow, text = "RLC Parallel Circuit Calculator", font = ("Calibri", 32), pady = 20)
        MyTitle.place(x = 80, y = 24, anchor = "nw")

        MyLabel = Label(self.RPWindow, text = "Please enter the values for the voltage source, inductance,\ncapacitance and the resistor's resistance.", font = ("Arial", 14))
        MyLabel.place(x = 98, y = 130, anchor = "nw")

        self.RPLabel = Label(self.RPWindow, image = self.RLCParallelCircuit_Image)
        self.RPLabel.pack(side = BOTTOM)

        VoltageLabel = Label(self.RPWindow, text = "Voltage Source", font = ("Arial", 12))
        VoltageLabel.place(x = 20, y = 210, anchor = "nw")
        EntryBox1 = Entry(self.RPWindow, bd = 4, width = 8, font = ("Arial", 10))
        EntryBox1.place(x = 140, y = 210, anchor = "nw")

        InductorLabel = Label(self.RPWindow, text = "Inductance", font = ("Arial", 12))
        InductorLabel.place(x = 230, y = 210, anchor = "nw")
        EntryBox2 = Entry(self.RPWindow, bd = 4, width = 8, font = ("Arial", 10))
        EntryBox2.place(x = 318, y = 210, anchor = "nw")

        CapacitorLabel = Label(self.RPWindow, text = "Capacitance", font = ("Arial", 12))
        CapacitorLabel.place(x = 398, y = 210, anchor = "nw")
        EntryBox3 = Entry(self.RPWindow, bd = 4, width = 8, font = ("Arial", 10))
        EntryBox3.place(x = 500, y = 210, anchor = "nw")

        ResistanceLabel = Label(self.RPWindow, text = "Resistance (R)", font = ("Arial", 12))
        ResistanceLabel.place(x = 20, y = 280, anchor = "nw")
        EntryBox4 = Entry(self.RPWindow, bd = 4, width = 8, font = ("Arial", 10))
        EntryBox4.place(x = 140, y = 280, anchor = "nw")

        FrequencyLabel = Label(self.RPWindow, text = "Frequency", font = ("Arial", 12))
        FrequencyLabel.place(x = 230, y = 280, anchor = "nw")
        EntryBox5 = Entry(self.RPWindow, bd = 4, width = 8, font = ("Arial", 10))
        EntryBox5.place(x = 318, y = 280, anchor = "nw")

        LabelUnit = Label(self.RPWindow, text = "Inductance and capacitance\nare measured in mH and μF\nrespectively.", font = ("Arial", 11))
        LabelUnit.place(x = 412, y = 272, anchor = "nw")

        self.RLCPara_Label = Label(self.RPWindow, text = "Result = ?", font = ("Arial",12))
        self.RLCPara_Label.place(x = 148, y = 330, anchor = "nw")

        # Create button
        ComputeButton = Button(self.RPWindow, text = "Compute", width = 10, height = 2, bg = "#20bebe", fg = "White", font = ("Arial 12 bold"), command = lambda: self.GetParallelRLCResult(EntryBox1.get(), EntryBox2.get(), EntryBox3.get(), EntryBox4.get(), EntryBox5.get()))
        ComputeButton.place(x = 20, y = 332, anchor = "nw")



    def GetParallelRLCResult(self, UserInput1, UserInput2, UserInput3, UserInput4, UserInput5):
        InputStatus = True
        CharStatus = True
        EntryNumber = 1

        # If one of the inputs are greater than 30 characters, then it will
        # return false

        EntryList = [UserInput1, UserInput2, UserInput3, UserInput4, UserInput5]

        for i in range(0, 5):
            CharStatus = self.InputLimiter(EntryList[i])
            
            if (CharStatus == False):
                break
            EntryNumber = EntryNumber + 1
            

        if (CharStatus == False):
            self.RLCPara_Label.config(text = f"Result = ?\nToo many characters for entry box {EntryNumber}.\n Maximum chararcters is 30", fg = "red")
            return

        InputStatus = PhysicsObject.RLC_Circuit_Parallel(UserInput1, UserInput2, UserInput3, UserInput4, UserInput5)

        if (InputStatus == False):
            self.RLCPara_Label.config(text = "Result = ?\nSorry. Your input is not recognised. \nPlease try again", fg = "red")
            return
        
        elif (InputStatus == "INPUT BELOW ZERO"):
            self.RLCPara_Label.config(text = "Result = ?\nPlease ensure all numbers are above 0.\n", fg = "red")
            return

        self.RLCPara_Label.config(text = f"\nXc = {PhysicsObject.GetXc()}∠-90°Ω, XL = {PhysicsObject.GetXL()}∠90°Ω, Impedance = {PhysicsObject.GetZ()}∠{PhysicsObject.GetZ_Angle()}°Ω\n\nResistor current = {PhysicsObject.GetResistorCurrent()}A, Inductor current = {PhysicsObject.GetInductorCurrent()}A,\n\nCapacitor current = {PhysicsObject.GetCapacitorCurrent()}A, Total current = {PhysicsObject.GetTotalCurrentInParallelCircuit()}A", fg = "black")
        


    def MagneticFlux_Window(self):
        # Magnetic Flux Window
        self.MFWindow = Toplevel()
        self.MFWindow.title("Magnetic Flux Calculator")
        self.MFWindow.geometry("610x640")

        PictureFrame = Frame(self.MFWindow, padx = 4, pady = 4)
        PictureFrame.pack(side = BOTTOM)

        # Create the title of the window (not title for the window)
        MyTitle = Label(self.MFWindow, text = "Magnetic Flux Calculator", font = ("Calibri", 32), pady = 20)
        MyTitle.place(x = 58, y = 24, anchor = "nw")

        MyLabel = Label(self.MFWindow, text = "Please enter the magnetic field strength, the surface area in m^2\nand the angle in degrees.", font = ("Arial", 14))
        MyLabel.place(x = 34, y = 130, anchor = "nw")
        ImageMF = Image.open("Magnetic Flux Picture.png")
        ResizedImage = ImageMF.resize((570, 240), Image.ANTIALIAS)
        self.MagneticFlux_Image = ImageTk.PhotoImage(ResizedImage)

        self.MFLabel = Label(self.MFWindow, image = self.MagneticFlux_Image)
        self.MFLabel.pack(side = BOTTOM)

        # Create labels and entry boxes
        MagneticFieldStrengthLabel = Label(self.MFWindow, text = "Magnetic field strength", font = ("Arial", 12))
        MagneticFieldStrengthLabel.place(x = 24, y = 220, anchor = "nw")
        Entrybox1 = Entry(self.MFWindow, bd = 4, width = 8, font = ("Arial", 10))
        Entrybox1.place(x = 192, y = 220, anchor = "nw")

        SurfaceArea_Label = Label(self.MFWindow, text = "Surface area", font = ("Arial", 12))
        SurfaceArea_Label.place(x = 279, y = 220, anchor = "nw")
        Entrybox2 = Entry(self.MFWindow, bd = 4, width = 8, font = ("Arial", 10))
        Entrybox2.place(x = 382, y = 220, anchor = "nw")

        AngleLabel = Label(self.MFWindow, text = "Angle", font = ("Arial", 12))
        AngleLabel.place(x = 474, y = 220, anchor = "nw")
        Entrybox3 = Entry(self.MFWindow, bd = 4, width = 8, font = ("Arial", 10))
        Entrybox3.place(x = 524, y = 220, anchor = "nw")

        self.MagenticFlux_Label = Label(self.MFWindow, text = "Results = ", font = ("Arial", 13))
        self.MagenticFlux_Label.place(x = 184, y = 290, anchor = "nw")
        
        # Create button
        ComputeButton = Button(self.MFWindow, text = "Compute", width = 10, height = 2, bg = "#20bebe", fg = "White", font = ("Arial 12 bold"), command = lambda: self.GetMagneticFluxValues(Entrybox1.get(), Entrybox2.get(), Entrybox3.get()))
        ComputeButton.place(x = 34, y = 280, anchor = "nw")



    def GetMagneticFluxValues(self, UserInput1, UserInput2, UserInput3):
        InputStatus = True
        CharStatus = True
        EntryNumber = 1

        # If one of the inputs are greater than 30 characters, then it will
        # return false

        EntryList = [UserInput1, UserInput2, UserInput3]

        for i in range(0, 3):
            CharStatus = self.InputLimiter(EntryList[i])
            
            if (CharStatus == False):
                break
            EntryNumber = EntryNumber + 1
            

        if (CharStatus == False):
            self.MagenticFlux_Label.config(text = f"Result = ?\nToo many characters for entry box {EntryNumber}.\n Maximum chararcters is 30", fg = "red")
            return

        InputStatus = PhysicsObject.Magnetic_Flux(UserInput1, UserInput2, UserInput3)

        if (InputStatus == False):
            self.MagenticFlux_Label.config(text = "Result = ?\nSorry. Your input is not recognised. \nPlease try again", fg = "red")
            return
        
        elif (InputStatus == "INPUT BELOW ZERO"):
            self.MagenticFlux_Label.config(text = "Result = ?\nPlease ensure all numbers are above 0.\n", fg = "red")
            return

        self.MagenticFlux_Label.config(text = f"Magentic Flux = {PhysicsObject.GetMagneticFlux()}Wb", fg = "black")


        
    def ElectromagenticInduction_Window(self):
        # Electromagnetic Induction Window
        self.EIWindow = Toplevel()
        self.EIWindow.title("Electromagnetic Induction Calculator")
        self.EIWindow.geometry("610x640")

        PictureFrame = Frame(self.EIWindow, padx = 4, pady = 4)
        PictureFrame.pack(side = BOTTOM)

        # Create the title of the window (not title for the window)
        MyTitle = Label(self.EIWindow, text = "Electromagnetic Induction\nCalculator", font = ("Calibri", 32), pady = 20)
        MyTitle.place(x = 58, y = 9, anchor = "nw")

        MyLabel = Label(self.EIWindow, text = "Please enter the number of turns on the coil, the change in \nmagentic flux (Wb) and the change in time (seconds).", font = ("Arial", 14))
        MyLabel.place(x = 54, y = 144, anchor = "nw")
        ImageEI = Image.open("Electromagnetic_Induction_Image.png")
        ResizedImage = ImageEI.resize((590, 274), Image.ANTIALIAS)
        self.ElectromagneticInduction_Image = ImageTk.PhotoImage(ResizedImage)

        self.EILabel = Label(self.EIWindow, image = self.ElectromagneticInduction_Image)
        self.EILabel.pack(side = BOTTOM)

        # Create labels and entry boxes
        NumberOfTurnsLabel = Label(self.EIWindow, text = "Number of turns", font = ("Arial", 12))
        NumberOfTurnsLabel.place(x = 24, y = 220, anchor = "nw")
        Entrybox1 = Entry(self.EIWindow, bd = 4, width = 8, font = ("Arial", 10))
        Entrybox1.place(x = 148, y = 220, anchor = "nw")

        MagneticFluxLabel = Label(self.EIWindow, text = "Magnetic flux", font = ("Arial", 12))
        MagneticFluxLabel.place(x = 250, y = 220, anchor = "nw")
        Entrybox2 = Entry(self.EIWindow, bd = 4, width = 8, font = ("Arial", 10))
        Entrybox2.place(x = 352, y = 220, anchor = "nw")

        TimeLabel = Label(self.EIWindow, text = "Time", font = ("Arial", 12))
        TimeLabel.place(x = 454, y = 220, anchor = "nw")
        Entrybox3 = Entry(self.EIWindow, bd = 4, width = 8, font = ("Arial", 10))
        Entrybox3.place(x = 498, y = 220, anchor = "nw")

        self.Electromagnetic_Label = Label(self.EIWindow, text = "Results = ", font = ("Arial", 13))
        self.Electromagnetic_Label.place(x = 184, y = 290, anchor = "nw")
        
        # Create button
        ComputeButton = Button(self.EIWindow, text = "Compute", width = 10, height = 2, bg = "#20bebe", fg = "White", font = ("Arial 12 bold"), command = lambda: self.GetElectromagneticInductionValues(Entrybox1.get(), Entrybox2.get(), Entrybox3.get()))
        ComputeButton.place(x = 34, y = 280, anchor = "nw")



    def GetElectromagneticInductionValues(self, UserInput1, UserInput2, UserInput3):
        InputStatus = True
        CharStatus = True
        EntryNumber = 1

        # If one of the inputs are greater than 30 characters, then it will
        # return false

        EntryList = [UserInput1, UserInput2, UserInput3]

        for i in range(0, 3):
            CharStatus = self.InputLimiter(EntryList[i])
            
            if (CharStatus == False):
                break
            EntryNumber = EntryNumber + 1
            

        if (CharStatus == False):
            self.Electromagnetic_Label.config(text = f"Result = ?\nToo many characters for entry box {EntryNumber}.\n Maximum chararcters is 30", fg = "red")
            return

        InputStatus = PhysicsObject.ElectronicInduction(UserInput1, UserInput2, UserInput3)

        if (InputStatus == False):
            self.Electromagnetic_Label.config(text = "Result = ?\nSorry. Your input is not recognised. \nPlease try again", fg = "red")
            return
        
        elif (InputStatus == "INPUT EQUAL OR BELOW ZERO"):
            self.Electromagnetic_Label.config(text = "Result = ?\nPlease ensure all numbers are above 0.\n", fg = "red")
            return

        self.Electromagnetic_Label.config(text = f"EMF = {PhysicsObject.GetElectromotiveForce()}V", fg = "black")

        
        

        
# This creates a blank window for main menu    
root = Tk()

# This creates an object of the Mathematics_Class that is found in the Mathematics_Module.
MathsObject = Mathematics_Class()
# This creates an object of the Physics_Class that is found in the Physics_Module
PhysicsObject = Physics_Class()
# Create an object to use the functions in the Graphing module
GraphObject = Graphing_Calculator_Class()
# This passes the root object to a constructor in the GUI_Calculator class
MyObject = GUI_Calculator(root)
# Title of the main window
root.title("Main Menu")

# This ensures the window stays on the window until closed down by the user.
root.mainloop()


# Website used to create circuit schematic diagrams: https://www.circuit-diagram.org/editor/

#DO NOT FORGET TO IMPLEMENT A FUNCTION THAT LIMITS THE NUMBER OF CHARACTERS

# def refresh(self):
#   self.destroy()
#   self.__init__()
#
#
"""
    List of functions within the Mathematics Class

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
    # GetQuotientRule_LeftDerivative()
    # GetQuotientRule_LeftDerivative()
    # GetQuotientRule_V_Squared()
    # GetSignCheck_QuotientRule()
    

    More to be made...

"""
# **IMPORTANT**

# Please download Pillow version 10 before ruuning code.
# Any versions above Pillow 10 will cause an error.

"""
  MyHeaderLabel_1 = Label(self.ComplexWindow, text = "Complex Numbers - Conversion Between", font = ("Calibri", 18))
        MyHeaderLabel_1.grid(row = 0, column = 0)
        MyHeaderLabel_2 = Label(self.ComplexWindow, text = " Polar Form and Rectangular Form", font = ("Calibri", 18))
        MyHeaderLabel_2.grid(row = 1, column = 0)

        
"""
