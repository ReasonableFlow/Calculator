from PyQt5 import QtWidgets 
from StandardGui88 import Ui_StandardCalc
from math import sqrt
from math import log10
from math import sin
from math import radians
from math import cos
from math import log
from math import tan




class StandardCalc(QtWidgets.QMainWindow,Ui_StandardCalc):

    firstVal = ""   #The first value the user inputs
    SecondValType = ""   #The second value the user inputs 

 ################################################################################################   

    def __init__(self):         #Shows the UI 
        super().__init__()
        self.setupUi(self)
        self.show()



 ##################################################################################################################
        
        
        
        #Number/Digits
        self.pushButton_p0.clicked.connect(self.numbersPressed)  #0
        self.pushButton_p1.clicked.connect(self.numbersPressed)  #1
        self.pushButton_p2.clicked.connect(self.numbersPressed)  #2  
        self.pushButton_p3.clicked.connect(self.numbersPressed)  #3
        self.pushButton_p4.clicked.connect(self.numbersPressed)  #4
        self.pushButton_p5.clicked.connect(self.numbersPressed)  #5
        self.pushButton_p6.clicked.connect(self.numbersPressed)  #6
        self.pushButton_p7.clicked.connect(self.numbersPressed)  #7
        self.pushButton_p8.clicked.connect(self.numbersPressed)  #8
        self.pushButton_p9.clicked.connect(self.numbersPressed)  #9
        


 #############################################################################################################



        #Dot
        self.pushButton_dot.clicked.connect(self.DecimalPushed)



 #################################################################################################



        #Operations
        self.pushButton_add.clicked.connect(self.OperationPressed)     #+
        self.pushButton_minus.clicked.connect(self.OperationPressed)   #-
        self.pushButton_times.clicked.connect(self.OperationPressed)   #x
        self.pushButton_divide.clicked.connect(self.OperationPressed)  #/
        self.pushButton_square.clicked.connect(self.OperationPressed)  #^2
        self.pushButton_root.clicked.connect(self.OperationPressed)    #Root

        #Makes sure the sender can be clicked

        self.pushButton_add.setCheckable(True)
        self.pushButton_minus.setCheckable(True)
        self.pushButton_times.setCheckable(True)
        self.pushButton_divide.setCheckable(True)
        self.pushButton_root.setCheckable(True)
        self.pushButton_square.setCheckable(True)
        self.pushButton_root.setCheckable(True)
        self.pushButton_15.setCheckable(True)
        self.pushButton_17.setCheckable(True)


 ##########################################################################################################3

        #Other stuff such as equals and clear 
        self.pushButton_equals.clicked.connect(self.Result)   #=

        self.pushButton_clear.clicked.connect(self.ClearPressed)   #Clear
        



 ##############################################################################################################################################
        
 #Function that binds the 

    def numbersPressed(self):
        sender = self.sender()
        #15g rounds the number to 15 digits.
        fix1 =  format(float(sender.text()), '.15g')
        fix2 = format(self.label_2.text() + sender.text(), '.15')
        fix3 = format(float(self.label_2.text() + sender.text()), '.15g')
        
         

        if ((self.pushButton_add.isChecked() or self.pushButton_minus.isChecked() or self.pushButton_times.isChecked() or self.pushButton_divide.isChecked()
            or self.pushButton_root.isChecked() or self.pushButton_square.isChecked()) and (not self.SecondValType)):
            LabelNew = fix1 

         # if ((self.pushButton_add.isChecked() or self.pushButton_minus.isChecked() or self.pushButton_times.isChecked() or self.pushButton_divide.isChecked()) and ( not self.SecondValType)):
            #LabelNew = format(float(sender.text()), '.15g')
            self.SecondValType = True
           

        else:
            if (("." in self.label_2.text() and sender.text() == '0')):
                LabelNew = fix2
            else:
                LabelNew = fix3    

        self.label_2.setText(LabelNew)  


 #############################################################################################################
    def DecimalPushed(self):            #Decimal Point 
        self.label_2.setText(self.label_2.text() + '.')
 ##################################################################################################



    def OperationPressed(self):          #All the operations 

        sender = self.sender()

        self.firstVal = float(self.label_2.text())

    
        sender.setChecked(True)

        

    def Result(self):          #Calculates the results 

        secondVal = float(self.label_2.text())


        if self.pushButton_add.isChecked():          #isChecked just makes sure that the sender pressed is actually what it is.
            LabelNum = self.firstVal + secondVal
            LabelNew = format(LabelNum, '.15g')
            self.label_2.setText(LabelNew)
            self.pushButton_add.setChecked(False)       #And then it becomes false after it is pressed, meaning it

        elif self.pushButton_minus.isChecked():
            LabelNum = self.firstVal - secondVal
            LabelNew = format(LabelNum, '.15g')
            self.label_2.setText(LabelNew)
            self.pushButton_minus.setChecked(False)
            
        elif self.pushButton_times.isChecked():
            LabelNum = self.firstVal * secondVal
            LabelNew = format(LabelNum, '.15g')
            self.label_2.setText(LabelNew)
            self.pushButton_times.setChecked(False)

        elif self.pushButton_divide.isChecked():
            LabelNum = self.firstVal / secondVal
            LabelNew = format(LabelNum, '.15g')
            self.label_2.setText(LabelNew)
            self.pushButton_divide.setChecked(False)


        elif self.pushButton_square.isChecked():
            LabelNum = self.firstVal**2
            LabelNew = format(LabelNum, '.15g')
            self.label_2.setText(LabelNew)
            self.pushButton_square.setChecked(False)

        elif self.pushButton_root.isChecked():
            LabelNum = sqrt(self.firstVal)
            LabelNew = format(LabelNum, '.15g')
            self.label_2.setText(LabelNew)
            self.pushButton_root.setChecked(False)
        
        elif self.pushButton_15.isChecked():
            a = eval(self.firstVal)
            LabelNum = sin(radians(a))
            LabelNew = format(LabelNum, '.15g')
            self.label_2.setText(LabelNew)
            self.pushButton_15.setChecked(False)

        elif self.pushButton_17.isChecked():
            #LabelString = float(str(self.firstVal))
            #LabelInt = str(LabelString)
           
            LabelString = float(self.firstVal)
            LabelNum = log10(LabelString)
            LabelNew = format(LabelNum, '.15g')
            self.label_2.setText(LabelNew)
            self.pushButton_17.setChecked(False)
        


        #elif self.pushButton_square.isChecked():
            #LabelNum = self.firstVal(square)
        
        self.SecondValType = False

    
        
    

    #Clear function
    def ClearPressed(self):
        self.pushButton_add.setChecked(False)
        self.pushButton_minus.setChecked(False)
        self.pushButton_times.setChecked(False)
        self.pushButton_divide.setChecked(False)
        self.pushButton_root.setChecked(False)
        self.pushButton_square.setChecked(False)

        self.SecondValType = False

        self.label_2.setText("0")

    def ce_pressed(self):
        self.label_2.backspace()
    
        
        