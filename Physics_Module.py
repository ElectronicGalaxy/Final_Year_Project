from sympy import *
import math
import cmath

class Physics_Class:

    def __init__(self):
        self.G = 9.81   # Acceleration due to gravity in free space (In the absence of air resistance)
        self.Mass = 0   # Weight of an object without gravity (Amount of stuff in the object)
        self.Theta = 0  # Angle (In degrees)
        self.CoeffFriction = 0  # coefficient of friction (Inclined plane)


          
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


        
    # Calculates the acceleration and velocity of a object on a inclined plane
    def Mechanics_InclinedPlane(self, ArgMass = "", ArgAngle = "", ArgDistance = "", ArgFriction = ""):
        InputStatus = False
        

        InputList = [ArgMass, ArgAngle, ArgDistance, ArgFriction]

        # Checks to see if the user enters a valid number
        # If not, then the program will prompt the user with a "Input invalid" message
        for i in range(0, len(InputList)):
            InputList[i] = self.InputValidation_Float(InputList[i])

            if (InputList[i] == None):
                return InputStatus
                
        self.Mass = float(ArgMass)
        self.Theta = float(ArgAngle)
        self.Distance = float(ArgDistance)
        self.Friction = float(ArgFriction)
        
                
       # Check if the user enters 0 into any of these variables
        if (self.Mass and self.Theta and self.Distance <= 0):
            InputStatus = "INPUT BELOW ZERO"
            return InputStatus

        # Ensure the user
        if (self.Friction >= 1):
            InputStatus = "FRICTION TOO HIGH"
            return InputStatus

        elif (self.Friction < 0):
            InputStatus = "FRICTION TOO LOW"
            return InputStatus
            
        
        # Normal force = fμ*g*cos(x)
        # The trigonometric functions only accepts arguments in radians. 
        ForceOfFriction = self.Friction * self.G * math.cos(self.Theta*math.pi/180)

        # Force down the inclined plane = g*sine(x)
        ForceDownSlope = self.G * math.sin(self.Theta*math.pi/180) 

        # Calculate slope down the inclined plane
        self.Plane_Acceleration = (ForceDownSlope - ForceOfFriction)
        self.Velocity = math.sqrt(2*self.Plane_Acceleration*self.Distance)
        
        print(f"The acceleration of the inclined block: {self.Plane_Acceleration} m/s^2 \n")
        print(f"The velocity of the inclined block: {self.Velocity} m/s")



    def GetAcceleration_InclinedPlane(self):
            return round(self.Plane_Acceleration, 3)

    def GetVelocity_InclinedPlane(self):
            return round(self.Velocity, 3)



    # Projectile motion
    # This function takes 2 inputs
    def Mechanics_ProjectileMotion(self, Velocity, Angle):
        InputStatus = False
        
        try:
            ObjectVelocity = float(Velocity)
            AngleOfProjectile = float(Angle)
        except ValueError:
            return InputStatus
        except Exception:
            print("Sorry. Something went wrong.\n\n")
            return InputStatus

        if (ObjectVelocity < 0):
            print("The object velocity must not be less than zero.", "\n", "We assume forward is positive and back is negative.\n")
            return
        
        # Vertical speed is magnitude * sine(theta)
        Vertical_InitialVelocity = ObjectVelocity * math.sin(AngleOfProjectile * math.pi/180)
        
        # Horizantal speed is magitude * cos(theta)
        Horizantal_InitialVelocity = ObjectVelocity * math.cos(AngleOfProjectile * math.pi/180)
        
        # When the object reaches the maximum height during travel, the velocity equals 0
        Vertical_FinalVelocity = 0

        self.MaximumHeight = (math.pow(Vertical_InitialVelocity, 2))/19.62
        # (V - U)/-9.81 or (V - U)/a 
        self.MaxHeightTime = (Vertical_InitialVelocity)/9.81

        # The initial horizantal velocity is equal to the final velocity due to no air resistance
        Horizantal_FinalVelocity = Horizantal_InitialVelocity

        
        self.MaxHeightDisplacement = Horizantal_FinalVelocity * self.MaxHeightTime
        self.TotalHorizantalDisplacement = 2 * self.MaxHeightDisplacement
        self.TotalTime = 2 * self.MaxHeightTime

        InputStatus = True
        return InputStatus

        print("\n\nMaximum height of the object is: {}m".format(round(self.MaximumHeight, 2)))
        print("Time taken for the object to reach its maximum height: {}s".format(round(self.MaxHeightTime, 2)))
        print("Total distance travelled: {}m".format(round(self.TotalHorizantalDisplacement, 2)))
        print("Total time taken: {}s".format(round(self.TotalTime, 2)))




    def GetMaxHeight_ProjectileMotion(self):
        return round(self.MaximumHeight, 3)


    def GetMaxHeightTime_ProjectileMotion(self):
        return round(self.MaxHeightTime, 3)


    def GetTotalDistance_ProjectileMotion(self):
        return round(self.TotalHorizantalDisplacement, 3)


    def GetMaxHeightDisplacement_ProjectileMotion(self):
        return round(self.MaxHeightDisplacement, 3)


    def GetTotalTime_ProjectileMotion(self):
        return round(self.TotalTime, 3)


    # Projectile motion from platform
    # This function takes 2 inputs
    def Mechanics_PM_Platform(self, Velocity, PlatformHeight):
        InputStatus = False
        
        try:
            HeightOfPlatform = float(PlatformHeight)
            Horizantal_Velocity = float(Velocity)
        except ValueError:
            print("Input invalid. Please try again.")
            return InputStatus
        except Exception:
            print("Sorry. Something went wrong")
            return InputStatus

        if (HeightOfPlatform < 0):
            InputStatus = "HEIGHT BELOW ZERO"
            return InputStatus

        # Time taken for the object to reach the ground (water)
        # sqrt((2 * x)/a) - a (g in this case) is the acceleration due to
        self.TimeTaken = math.sqrt(2 * HeightOfPlatform / 9.81)

        # The horizantal distance travelled by the object would be d = v*t, since there is no air resistance
        self.Horizantal_Distance = Horizantal_Velocity * self.TimeTaken

        # The initial vertical velocity of the object is 0
        # The formula used is Vf^2 = U^2 + 2ax
        Vertical_Velocity = math.sqrt(2 * 9.81 * HeightOfPlatform)

        # The formula used is the Pythagorean Theorem. Where the squares of the horizantal
        # and vertical components are equal to the square magnitude of the velocity (hypotenuse)
        # This gives us the actual velocity of the object
        self.OverallVelocity = math.sqrt(Vertical_Velocity**2 + Horizantal_Velocity**2)
        self.ProjectileAngle = math.atan(Vertical_Velocity/Horizantal_Velocity) 

        InputStatus = True
        return InputStatus
        #print("\nHorizantal distance travelled: {}m\nTime taken to travel distance: {}s".format(round(self.Horizantal_Distance, 2), round(self.TimeTaken, 2)))
        #print("Overall final velocity and angle of the object: {}m/s\n{}°".format(round(OverallVelocity, 2), round(math.atan(math.pi/180 * Vertical_Velocity/Horizantal_Velocity ))))



    # Get velocity
    def GetFinalVelocity(self):
        return round(self.OverallVelocity, 3)

    # Get angle
    def GetProjectileAngle(self):
        return round((self.ProjectileAngle * 180/math.pi), 3)

    def GetTimeTaken(self):
        return round(self.TimeTaken, 3)

    def GetDistance(self):
        return round(self.Horizantal_Distance, 3)
    

    # This function calculates the angular velocity and the linear velocity
    # This function takes 3 inputs
    def AngularVelocityFunction(self, Angle, Time, ArgRadius):
        InputStatus = False

        # This list (array) will be used to pass all arguments into the input validation function.
        # To ensure no invalid inputs are entered.
        InputList = [Angle, Time, ArgRadius]

        for i in range(0, 3):
            InputList[i] = self.InputValidation_Float(InputList[i])

            if (InputList[i] == None):
                print("One of the inputs are invalid.")
                return InputStatus

            
        if (InputList[1] <= 0):
            InputStatus = "TIME LESS THAN ZERO"
            
        if (InputList[2] <= 0):
            InputStatus = "RADIUS LESS THAN ZERO"
            return InputStatus
            
        CIAngle = float(Angle)
        CITime = float(Time)
        Radius = float(ArgRadius)

        # ω = Δθ/Δt or ω = v/r
        self.AngularVelocity = (CIAngle * math.pi/180)/CITime
        
        # v = ω*r
        self.LinearVelocity = self.AngularVelocity * Radius

        InputStatus = True
        return InputStatus



    def GetAngular_Velocity(self):
        return round(self.AngularVelocity, 3)


    def GetLinearVelocity(self):
        return round(self.LinearVelocity, 3)



    # This function calculates the Angular accelaration
    # This function takes 2 inputs
    def AngularAccelaration(self):
        CIAngularVelocity = float(input("Please enter the change in angular velocity (m/s): "))
        CITime = float(input("Please enter the change in time (s): "))
        print("")

        AngularAccelaration = round(CIAngularVelocity/Time, 2)

        print("Angular accelaration: {}rad/s^2".format(AngularAccelaration))



    # Work on this last
    def OhmsLaw_Resistor(self, VoltageSource, Resistance1):
        InputStatus = False

        InputList = [VoltageSource, Resistance1]

        for i in range(0, len(InputList)):
            InputList[i] = self.InputValidation_Float(InputList[i])

            if (InputList[i] == None):
                print("Please try again")
                return InputStatus

            if (float(InputList[i]) <= 0):
                InputStatus = "NEGATIVE NUMBER DETECTED"
                return InputStatus

        VoltageSource = float(VoltageSource)
        Resistance1 = float(Resistance1)

        try:
            self.Current = VoltageSource/Resistance1
        except ZeroDivisionError:
            InputStatus = "DIVISION BY ZERO"
            return InputStatus
            
        self.ResVoltage1 = VoltageSource

        # Calculate power
        self.Power = self.Current**2 * Resistance1

        InputStatus = True
        return InputStatus


    
    def OhmsLaw_ResistorResistor(self, VoltageSource, Resistance1, Resistance2):
        InputStatus = False

        InputList = [VoltageSource, Resistance1, Resistance2]

        for i in range(0, len(InputList)):
            InputList[i] = self.InputValidation_Float(InputList[i])

            if (InputList[i] == None):
                print("Please try again")
                return InputStatus

            if (float(InputList[i]) <= 0):
                InputStatus = "NEGATIVE NUMBER DETECTED"
                return InputStatus

        VoltageSource = float(VoltageSource)
        Resistance1 = float(Resistance1)
        Resistance2 = float(Resistance2)

        try:
            self.Current = VoltageSource/(Resistance1 + Resistance2)
        except ZeroDivisionError:
            InputStatus = "DIVISION BY ZERO"
            return InputStatus
        
        self.ResVoltage1 = self.Current * Resistance1
        self.ResVoltage2 = self.Current * Resistance2
        
        # Calculate power
        self.Power = self.Current**2 * (Resistance1 + Resistance2)

        InputStatus = True
        return InputStatus



    def OhmsLaw_ResistorInductor(self, VoltageSource, Inductance, Resistance1, Frequency):
        InputStatus = False

        InputList = [VoltageSource, Inductance, Resistance1, Frequency]

        for i in range(0, len(InputList)):
            InputList[i] = self.InputValidation_Float(InputList[i])

            if (InputList[i] == None):
                print("Please try again")
                return InputStatus

            if (float(InputList[i]) <= 0):
                InputStatus = "NEGATIVE NUMBER DETECTED"
                return InputStatus

        VoltageSource = float(VoltageSource)
        Resistance1 = float(Resistance1)
        Inductance = float(Inductance)
        Frequency = float(Frequency)

        self.XL = 2 * math.pi * Frequency * Inductance*(10**-3)

        # Calculate total impedance and impedance angle
        self.TotalImpedence_Polar = math.sqrt((Resistance1)**2 + (self.XL)**2)
        self.PhaseAngle = (math.atan(self.XL/Resistance1)) * 180/math.pi

        # Calculate total current
        self.Current = VoltageSource/self.TotalImpedence_Polar
        self.Current_Angle = -self.PhaseAngle

        # Calculate voltage and angle
        self.ResVoltage1 = (self.Current) * (Resistance1)
        self.ResistorAngle = self.PhaseAngle

        self.InductorVoltage = (self.Current) * (self.XL)
        self.InductorAngle = self.Current_Angle + 90

        # Calculating "Power factor"
        self.Power = Resistance1/self.TotalImpedence_Polar

        InputStatus = True
        return InputStatus


        
    def OhmsLaw_ResistorCapacitor(self, VoltageSource, Capacitance, Resistance1, Frequency):
        InputStatus = False
        
        InputList = [VoltageSource, Capacitance, Resistance1, Frequency]

        for i in range(0, len(InputList)):
            InputList[i] = self.InputValidation_Float(InputList[i])

            if (InputList[i] == None):
                print("Please try again")
                return InputStatus

            if (float(InputList[i]) <= 0):
                InputStatus = "NEGATIVE NUMBER DETECTED"
                return InputStatus
            
        VoltageSource = float(VoltageSource)
        Resistance1 = float(Resistance1)
        Capacitance = float(Capacitance)
        Frequency = float(Frequency)

        # Normally Xc is negative
        self.Xc = 1/(2 * math.pi * Frequency * Capacitance*(10**-6))

        self.TotalImpedence_Polar = math.sqrt(Resistance1**2 + self.Xc**2)
        self.PhaseAngle = math.atan(-self.Xc/Resistance1) * 180/math.pi
        
        # Calculate total current
        self.Current = VoltageSource/self.TotalImpedence_Polar
        self.Current_Angle = -self.PhaseAngle

        # Calculate voltage and angle
        self.ResVoltage1 = (self.Current) * (Resistance1)
        self.ResistorAngle = self.PhaseAngle

        # Calculate capacitor voltage and angle
        self.CapacitorVoltage = (self.Current) * (self.Xc)
        self.CapacitorAngle = self.Current_Angle - 90

        # Calculating "Power factor"
        self.Power = Resistance1/self.TotalImpedence_Polar

        InputStatus = True
        return InputStatus



    def OhmsLaw_ResistorResistorResistor(self, VoltageSource, Resistance1, Resistance2, Resistance3):
        InputStatus = False

        InputList = [VoltageSource, Resistance1, Resistance2, Resistance3]

        for i in range(0, len(InputList)):
            InputList[i] = self.InputValidation_Float(InputList[i])

            if (InputList[i] == None):
                print("Please try again")
                return InputStatus

            if (float(InputList[i]) <= 0):
                InputStatus = "NEGATIVE NUMBER DETECTED"
                return InputStatus

        VoltageSource = float(VoltageSource)
        Resistance1 = float(Resistance1)
        Resistance2 = float(Resistance2)
        Resistance3 = float(Resistance3)

        try:
            self.Current = VoltageSource/(Resistance1 + Resistance2 + Resistance3)
        except ZeroDivisionError:
            InputStatus = "DIVISION BY ZERO"
            return InputStatus
        
        self.ResVoltage1 = self.Current * Resistance1
        self.ResVoltage2 = self.Current * Resistance2
        self.ResVoltage3 = self.Current * Resistance3
        
        # Calculate power
        self.Power = self.Current**2 * (Resistance1 + Resistance2 + Resistance3)

        InputStatus = True
        return InputStatus
        



    def OhmsLaw_ResistorResistorInductor(self, VoltageSource, Inductance, Resistance1, Frequency, Resistance2):
        InputStatus = False

        InputList = [VoltageSource, Inductance, Resistance1, Frequency, Resistance2]

        for i in range(0, len(InputList)):
            InputList[i] = self.InputValidation_Float(InputList[i])

            if (InputList[i] == None):
                print("Please try again")
                return InputStatus

            if (float(InputList[i]) <= 0):
                InputStatus = "NEGATIVE NUMBER DETECTED"
                return InputStatus

            elif (InputList[i] == ""):
                return InputStatus

        VoltageSource = float(VoltageSource)
        Resistance1 = float(Resistance1)
        Resistance2 = float(Resistance2)
        Inductance = float(Inductance)
        Frequency = float(Frequency)

        self.XL = 2 * math.pi * Frequency * Inductance*(10**-3)

        # Calculate total impedance and impedance angle
        self.TotalImpedence_Polar = math.sqrt((Resistance1 + Resistance2)**2 + (self.XL)**2)
        self.PhaseAngle = (math.atan(self.XL/Resistance1 + Resistance)) * 180/math.pi

        # Calculate total current
        self.Current = VoltageSource/self.TotalImpedence_Polar
        self.Current_Angle = -self.PhaseAngle

        # Calculate voltage and angle
        self.ResVoltage1 = (self.Current) * (Resistance1)
        self.ResistorAngle = self.PhaseAngle

        self.ResVoltage2 = (self.Current) * (Resistance2)
        self.ResistorAngle = self.PhaseAngle

        self.InductorVoltage = (self.Current) * (self.XL)
        self.InductorAngle = self.Current_Angle + 90

        # Calculating "Power factor"
        self.Power = Resistance1/self.TotalImpedence_Polar

        InputStatus = True
        return InputStatus


    
        
    def OhmsLaw_ResistorResistorCapacitor(self, VoltageSource, Capacitance, Resistance1, Frequency, Resistance2):
        InputStatus = False
        
        InputList = [VoltageSource, Capacitance, Resistance1, Frequency, Resistance2]

        for i in range(0, len(InputList)):
            InputList[i] = self.InputValidation_Float(InputList[i])

            if (InputList[i] == None):
                print("Please try again")
                return InputStatus

            if (float(InputList[i]) <= 0):
                InputStatus = "NEGATIVE NUMBER DETECTED"
                return InputStatus
            
        VoltageSource = float(VoltageSource)
        Resistance1 = float(Resistance1)
        Capacitance = float(Capacitance)
        Frequency = float(Frequency)
        Resistance2 = float(Resistance2)

        # Normally Xc is negative
        self.Xc = 1/(2 * math.pi * Frequency * Capacitance*(10**-6))

        self.TotalImpedence_Polar = math.sqrt((Resistance1 + Resistance2)**2 + self.Xc**2)
        self.PhaseAngle = math.atan(-self.Xc/Resistance1 + Resistance2) * 180/math.pi
        
        # Calculate total current
        self.Current = VoltageSource/self.TotalImpedence_Polar
        self.Current_Angle = -self.PhaseAngle

        # Calculate voltage and angle
        self.ResVoltage1 = (self.Current) * (Resistance1)
        self.ResistorAngle = self.PhaseAngle

        self.ResVoltage2 = (self.Current) * (Resistance2)
        self.ResistorAngle = self.PhaseAngle

        # Calculate capacitor voltage and angle
        self.CapacitorVoltage = (self.Current) * (self.Xc)
        self.CapacitorAngle = self.Current_Angle - 90

        # Calculating "Power factor"
        self.Power = Resistance1/self.TotalImpedence_Polar

        InputStatus = True
        return InputStatus
        


    # Voltage across resistor 1
    def GetRes_1(self):
        return round(self.ResVoltage1, 2)

    # Voltage across resistor 2
    def GetRes_2(self):
        return round(self.ResVoltage2, 2)

    # Voltage across resistor 3
    def GetRes_3(self):
        return round(self.ResVoltage3, 2)
        

        
    # This function calculates the inductive reactance (inductor resistance), capacitive reactance,
    # Overall reactance, overall impedance and phase angle (both polar and rectangular forms) and several more...
    #
    # This function takes 5 inputs (Currently takes the most arguments of all functions in the program)
    def RLC_Circuits(self, VoltageSource, Inductance, Capacitance, Resistance, Frequency):
        InputList = [VoltageSource, Resistance, Inductance, Capacitance, Frequency]
        InputStatus = False

        for i in range(0, len(InputList)):
            InputList[i] = self.InputValidation_Float(InputList[i])

            if (InputList[i] == None):
                print("Please try again")
                #self.RLC_Circuits()
                return InputStatus

            if (float(InputList[i]) <= 0):
                InputStatus = "NEGATIVE NUMBER DETECTED"
                return InputStatus

        # If the set of inputs are valid, then convert the following variables to floats
        VoltageSource = float(VoltageSource)
        Resistance = float(Resistance)
        Inductance = float(Inductance)
        Capacitance = float(Capacitance)
        Frequency = float(Frequency)
        
        # Xc is the capacitive reactance (the resistance of a capacitor)
        try:
            self.Xc = 1/(2*math.pi*Frequency*Capacitance*(10**-6))
        except ZeroDivisionError:
            InputStatus = "DIVISION BY ZERO"
            return InputStatus
        
        self.XL = 2*math.pi*Frequency*Inductance*(10**-3)

        # Find the difference bewteen the XL and Xc to calculate the overall
        # reactance in the imaginary axis.
        Reactance = self.XL - self.Xc

        # Z = Resistor**2 + Reactance**2, Where Z is the total impedance of the circuit
        # Polar form 
        self.TotalImpedence_Polar = math.sqrt(Resistance**2 + Reactance**2)
        # Angle of the circuit impendance (Impedance angle)
        self.PhaseAngle = (math.atan(Reactance/Resistance)) * 180/math.pi

        # Z = Resistor + Reactance*i
        # Rectangular form
        self.TotalImpedence_Rectangular = complex(Resistance, Reactance)
        print(f"{self.XL}, {self.Xc}")
        
        # This variable will store the circuit type (capacitive or reactive)
        CircuitType = ""

        if (self.XL > self.Xc):
            CircuitType = "inductive circuit"
        elif (self.Xc > self.XL):
            CircuitType = "capacitive circuit"
        elif (self.XL == self.Xc):
            CircuitType = "resonant circuit"

        # Calculating total current
        self.Current = VoltageSource/self.TotalImpedence_Polar
        # All voltages, currents and resistences have angles (even if they are 0)
        self.Current_Angle = -self.PhaseAngle

        # Calculate voltage and phase (angle) for each one
        self.ResistorVoltage = self.Current * Resistance
        self.ResistorAngle = self.Current_Angle

        self.CapacitorVoltage = self.Current * self.Xc
        self.CapacitorAngle = self.Current_Angle - 90

        self.InductorVoltage = self.Current * self.XL
        self.InductorAngle = self.Current_Angle + 90

        #Power is dissipated mainly through resistors in RLC circuits
        # P = I**2 * R
        VoltageRMS = VoltageSource * math.sqrt(2)/2
        CurrentRMS = VoltageRMS/self.TotalImpedence_Polar

        # Calculate power
        # Calculating power for an RC, RL or RLC circuit is "power factor".
        self.Power = Resistance/self.TotalImpedence_Polar
        #self.PF_Angle = math.atan(Resistance/self.TotalImpedence_Polar)

        #RealPower = VoltageRMS * CurrentRMS * math.cos(self.PF_Angle)
                
        print("Total impedence in the circuit: {}\nImepdence angle: {}\nTotal current in the circuit: {}".format(self.TotalImpedence_Polar, self.PhaseAngle, self.Current))
        print("Current Angle: {}\nCapacitor voltage {}\nCapacitor Angle: {}\nInductor voltage: {}".format(self.Current_Angle, self.CapacitorVoltage, self.CapacitorAngle, self.InductorVoltage))
        print("Inductor angle: {}".format(self.InductorAngle))
        
        InputStatus = True
        return InputStatus



    # Get capacitive reactance
    def GetXc(self):
        return round(self.Xc, 2)

    # Get inductive reactance
    def GetXL(self):
        return round(self.XL, 2)

    # Get voltage for the resistor
    def GetVr(self):
        return round(self.ResistorVoltage, 2)
    
    def GetR_Angle(self):
        return round(self.ResistorAngle, 2)
    
    # Get total impedance in a series circuit
    def GetZ(self):
        return round(self.TotalImpedence_Polar, 2)

    # Angle of the circuit impendance
    def GetZ_Angle(self):
        return round(self.PhaseAngle, 2)

    # Get total angle
    def GetTotal_I(self):
        return round(self.Current, 2)

    # Get the phase angle of the current
    def GetI_Angle(self):
        return round(self.Current_Angle, 2)

    # Capacitor voltage
    def GetVc(self):
        return round(self.CapacitorVoltage, 2)

    # Get angle of the capacitor
    def GetC_Angle(self):
        return round(self.CapacitorAngle, 2)

    # Get inductive voltage
    def GetVL(self):
        return round(self.InductorVoltage, 2)

    # Get inductive angle
    def GetL_Angle(self):
        return round(self.InductorAngle, 2)

    # Get power of series circuit
    def GetPower(self):
        return round(self.Power, 2)

    
    def Resonant_Circuits_Series(self, VoltageSource, Inductance, Capacitance, Resistance):
        InputList = [VoltageSource, Resistance, Inductance, Capacitance]
        InputStatus = False

        for i in range(0, len(InputList)):
            InputList[i] = self.InputValidation_Float(InputList[i])

            if (InputList[i] == None):
                #print("Please try again")
                #self.Resonant_Circuits_Series()
                return InputStatus
            
            if (InputList[i] < 0):
                InputStatus == "INPUT BELOW ZERO"
                return
            
        VoltageSource = float(VoltageSource)
        Resistance = float(Resistance)
        Inductance = float(Inductance)
        Capacitance = float(Capacitance)

        # Resonant frequency is the frequency where XL and XC cancels out.
        # 1/2*pi*sqrt(L*C)
        self.ResonantFrequency = 1/(2*math.pi*math.sqrt(Capacitance *(10**-6) * Inductance * (10**-3)))

        # At resonance frequency, the overall current flowing will be I = V/R, rather than I = V/Z
        self.Res_OverallCurrent = VoltageSource/Resistance
        # RMS current
        self.RMS_Current = (sqrt(2)/2) * self.Res_OverallCurrent
        # Resonant voltage drop across resistor
        self.Res_ResistorVoltage = (self.Res_OverallCurrent) * (Resistance)

        # Resonant overall power
        self.Res_OverallPower = self.RMS_Current**2 * Resistance

        self.QualityFactor = sqrt((Inductance * 10**-3)/(Capacitance * 10**-6))/(Resistance)

        self.Bandwidth = self.ResonantFrequency/self.QualityFactor

        self.FrequencyHigh = self.ResonantFrequency + (self.Bandwidth/2)
        self.FrequencyLow = self.ResonantFrequency - (self.Bandwidth/2)

        print(f"Resonant frequency: {self.ResonantFrequency}Hz\nTotal current flowing: {self.Res_OverallCurrent}A\nOverall power: {self.Res_OverallPower}W")
        print(f"Resistor voltage: {self.Res_ResistorVoltage}V\nQuality factor: {self.QualityFactor}\n Bandwidth: {self.Bandwidth}Hz")
        print(f"High frequency: {self.FrequencyHigh}Hz\nLow frequency: {self.FrequencyLow}Hz")


    def GetResonantFrequency(self):
        return round(self.ResonantFrequency, 3)


    def GetResonantCurrent(self):
        return round(self.Res_OverallCurrent, 3)


    def GetResonantResistorVoltage(self):
        return round(self.Res_ResistorVoltage, 3)


    def GetResonantPower(self):
        return round(self.Res_OverallPower, 3)


    def GetQualityFactor(self):
        return round(self.QualityFactor, 3)


    def GetBandwidth(self):
        return round(self.Bandwidth, 3)


    def GetHighFrequency(self):
        return round(self.FrequencyHigh, 3)


    def GetLowFrequency(self):
        return round(self.FrequencyLow, 3)


    def GetResonantRMS(self):
        return round(self.RMS_Current, 3)
    
        
    # This function calculates the resonant frequency, quality factor, total current and several more...
    # This function takes 4 inputs
    def RLC_Circuit_Parallel(self, VoltageSource, Inductance, Capacitance, Resistance, Frequency):
        InputStatus = False

        InputList = [VoltageSource, Resistance, Inductance, Capacitance, Frequency]

        for i in range(0, len(InputList)):
            InputList[i] = self.InputValidation_Float(InputList[i])

            if (InputList[i] == None):
                print("Please try again")
                self.Resonant_Circuits_Series()
                #return InputStatus
            
        VoltageSource = float(VoltageSource)
        Resistance = float(Resistance)
        Inductance = float(Inductance)
        Capacitance = float(Capacitance)
        Frequency = float(Frequency)

        # Xc is the capacitive reactance (the resistance of a capacitor)

        if (Frequency <= 0):
            InputStatus = "DIVISION BY ZERO"
            return InputStatus
        
        self.Xc = 1/(2*math.pi*Frequency*Capacitance*(10**-6))
        

        self.XL = 2*math.pi*Frequency*Inductance*(10**-3)

        # Find the difference bewteen the XL and Xc to calculate the overall
        # reactance in the imaginary axis.
        Reactance = 1/(self.XL) - 1/(self.Xc)
        Reactance_Difference = self.XL - self.Xc

        # Z = Resistor**2 + Reactance**2, Where Z is the total impedance of the circuit
        # Polar form 
        self.TotalImpedence_Polar = 1/math.sqrt(1/(Resistance)**2 + (Reactance)**2)
        # Angle of the circuit impendance (Impedance angle)
        self.PhaseAngle = (math.atan(Reactance_Difference/Resistance)) * 180/math.pi

        # Calculating total current
        self.Current = VoltageSource/self.TotalImpedence_Polar
        # All voltages, currents and resistences have angles (even if they are 0)
        self.Current_Angle = -self.PhaseAngle

        # Current flowing through the resistor
        self.ResistorCurrent = VoltageSource/Resistance

        # Current flowing through the inductor
        self.InductorCurrent = VoltageSource/self.XL

        # Current flowing through the capacitor
        self.CapacitorCurrent = VoltageSource/self.Xc

        self.TotalParallelCurrent = math.sqrt(self.ResistorCurrent**2 + (self.InductorCurrent - self.CapacitorCurrent)**2)

        # The RMS voltage and current
        VoltageRMS = VoltageSource * math.sqrt(2)/2
        CurrentRMS = VoltageRMS/self.TotalImpedence_Polar

        # Calculate power
        # Calculating power for an RC, RL or RLC circuit is "power factor".
        self.Power = Resistance/self.TotalImpedence_Polar
        #self.PF_Angle = math.atan(Resistance/self.TotalImpedence_Polar)

        #RealPower = VoltageRMS * CurrentRMS * math.cos(self.PF_Angle)
                
        #print("Total impedence in the circuit: {}\nImepdence angle: {}\nTotal current in the circuit: {}".format(self.TotalImpedence_Polar, self.PhaseAngle, self.Current))
        #print("Current Angle: {}\nCapacitor voltage {}\nCapacitor Angle: {}\nInductor voltage: {}".format(self.Current_Angle, self.CapacitorVoltage, self.CapacitorAngle, self.InductorVoltage))
        #print("Inductor angle: {}".format(self.InductorAngle))
        
        InputStatus = True
        return InputStatus


    def GetTotalCurrentInParallelCircuit(self):
        return round(self.TotalParallelCurrent, 3)


    def GetResistorCurrent(self):
        return round(self.ResistorCurrent, 3)


    def GetInductorCurrent(self):
        return round(self.InductorCurrent, 3)


    def GetCapacitorCurrent(self):
        return round(self.CapacitorCurrent, 3)


   
    def Magnetic_Flux(self, MagneticFieldStrength, SurfaceArea, Angle):
        InputStatus = False
        
        InputList = [MagneticFieldStrength, SurfaceArea, Angle]

        for i in range(0, len(InputList)):
            InputList[i] = self.InputValidation_Float(InputList[i])

            if (InputList[i] == None):
                #print("Please try again")
                #self.Magnetic_Flux_Density()
                return InputStatus

        MagneticFieldStrength = float(MagneticFieldStrength)
        SurfaceArea = float(SurfaceArea)
        Angle = float(Angle)

        if (MagneticFieldStrength <= 0):
            InputStatus = "INPUT BELOW ZERO"
            return InputStatus

        elif(SurfaceArea <= 0):
            InputStatus = "INPUT BELOW ZERO"
            return InputStatus
        
        # Calculate the magnetic flux
        # MagenticFlux = B*A*cos(theta)
        self.MagneticFlux = (MagneticFieldStrength) * (SurfaceArea) * math.cos(Angle * math.pi/180)

        #print(f"The magnetic flux is: {MagneticFlux}")

        InputStatus = True
        return InputStatus


    def GetMagneticFlux(self):
        return round(self.MagneticFlux, 3)



    # Note: B = Magnetic flux density = Magnetic field strength
    # This function calculates the magnetic flux density
    def Magnetic_Flux_Density(self, ForceOnTheWire, Current, LengthOfTheWire):
        # Force acting on the wire (or current in more correct terms)
        InputList = [ForceOnTheWire, Current, LengthOfTheWire]
        InputStatus = False

        for i in range(0, len(InputList)):
            InputList[i] = self.InputValidation_Float(InputList[i])

            if (InputList[i] == None):
                return InputStatus

        ForceOnTheWire = float(ForceOnTheWire)
        Current = float(Current)
        LengthOfTheWire = float(LengthOfTheWire)
        
        # Theta is the angle between the current and the magnetic field
        self.MagneticFluxDensity = ForceOnTheWire/(Current * LengthOfTheWire)

        print(f"The magnetic flux density equals {self.MagneticFluxDensity}T")



    # Faraday's law of electromagnetic induction
    def ElectronicInduction(self, NumberOfCoils, CIMagneticFlux, CITime):
        InputStatus = False

        InputList = [NumberOfCoils, CIMagneticFlux, CITime]

        for i in range(0, len(InputList)):
            InputList[i] = self.InputValidation_Float(InputList[i])

            if (InputList[i] == None):
                return InputStatus

        NumberOfCoils = float(NumberOfCoils)
        CIMagneticFlux = float(CIMagneticFlux)
        CITime = float(CITime)

        if (NumberOfCoils <= 0):
            InputStatus = "INPUT EQUAL OR BELOW ZERO"
            return InputStatus
        
        elif (CIMagneticFlux <= 0):
            InputStatus = "INPUT EQUAL OR BELOW ZERO"
            return InputStatus

        elif (CITime <= 0):
            InputStatus = "INPUT EQUAL OR BELOW ZERO"
            return InputStatus

        # Voltage
        self.ElectromotiveForce = -((NumberOfCoils) * (CIMagneticFlux))/(CITime)

        InputStatus = True
        return InputStatus


    def GetElectromotiveForce(self):
        return round(self.ElectromotiveForce, 3)


    def GetFinalVelocity_Kinematics(self):
        return self.FinalVelocity


    def GetDisplacement_Kinematics(self):
        return self.Displacement


    def TimeTaken_FromPlatform(self):
        return self.TimeTaken


    def HorizantalDistance_Fromplatform(self):
        return self.Horizantal_Distance


    def OverallVelocity_FromPlatform(self):
        return self.OverallVelocity


    def ProjectileAngle_FromPlatform(self):
        return self.ProjectileAngle
            
        

        

#MyObject = Physics_Class()

#MyObject.Mechanics_InclinedPlane()

# Kinematics formulae
# Formulas: Vf = V0 + at, Δx = t*(v + v0)/2, Δx = V0*t + (a*t^2)/2,
# Vf^2 = V0^2 + 2a*Δx
# Vf = Final velocity, V0 = Initial velocity, x = Displacement
#MyObject.Mechanics_ProjectileMotion()
#MyObject.Mechanics_KinematicEquations()
#MyObject.Mechanics_PM_Platform()
#MyObject.AngularVelocityAndAccelaration()
#MyObject.RLC_Circuits()
#MyObject.Resonant_Circuits_Parallel()


"""
########### Key Reminder ############

MAKE SURE YOU CHECK WHICH VARIABLES SHOULD STORE NEGATIVE OR POSITIVE NUMBERS!!!
YOU CAN'T HAVE NEGATIVE DISTANCE, BUT YOU CAN HAVE NEGATIVE DISPLACEMENT.

GO THROUGH EVERY FUNCTION AND ENSURE NO LOGICALLY INVALID INPUT IS ALLOWED!!!!

######################################

inclined plane, kinematic equations, projectile motion, angular velocity and acceleration,
ohm's law (For series and parallel circuits), RLC circuits, resonant circuits, ac theory,
magnetic flux density, magnetic flux and electromagnetic induction.


"""

