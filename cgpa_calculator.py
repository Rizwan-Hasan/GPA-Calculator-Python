# -*- coding: utf-8 -*-

import pandas as pd


class CGPA_Calculator():

    def __init__(self, subGrades=None, labGrades=None, totalCredit=None):
        # Variables
        self.cgpa = float()
        self.subGrades = subGrades.split(',')
        self.labGrades = labGrades.split(',')
        self.totalCredit = float(totalCredit)

        # Calling Functions
        self.pointVar()
        self.creditVar()
        self.calculation()

    def pointVar(self):
        # Pandas Variables
        gpa = pd.read_csv('Grading_System.csv')
        gpa = gpa.drop(['Percentage'], axis=1)

        # Grade's Variables
        self.A = gpa.values[0][1]
        self.A_Minus = gpa.values[1][1]
        self.B_Plus = gpa.values[2][1]
        self.B = gpa.values[3][1]
        self.B_Minus = gpa.values[4][1]
        self.C_Plus = gpa.values[5][1]
        self.C = gpa.values[6][1]
        self.C_Minus = gpa.values[7][1]
        self.D_Plus = gpa.values[8][1]
        self.D = gpa.values[9][1]
        self.F = gpa.values[10][1]

    def creditVar(self):
        # Credit's Variables
        self.subCredit = 3.0
        self.labCredit = 1.5

    def calculation(self):
        total = 0

        for x in self.subGrades:
            if(x == 'A' or x == 'a'):
                temp = self.A * self.subCredit
            elif(x == 'A-' or x == 'a-'):
                temp = self.A_Minus * self.subCredit
            elif(x == 'B+' or x == 'b+'):
                temp = self.B_Plus * self.subCredit
            elif(x == 'B' or x == 'b'):
                temp = self.B * self.subCredit
            elif(x == 'B-' or x == 'b-'):
                temp = self.B_Minus * self.subCredit
            elif(x == 'C+' or x == 'c+'):
                temp = self.C_Plus * self.subCredit
            elif(x == 'C' or x == 'c'):
                temp = self.C * self.subCredit
            elif(x == 'C-' or x == 'c-'):
                temp = self.C_Minus * self.subCredit
            elif(x == 'D+' or x == 'd+'):
                temp = self.D_Plus * self.subCredit
            elif(x == 'D' or x == 'd'):
                temp = self.D * self.subCredit
            elif(x == 'F' or x == 'f'):
                temp = self.F * self.subCredit
            else:
                print("Rizwan Hasan")
            total = total + temp

        for x in self.labGrades:
            if(x == 'A' or x == 'a'):
                temp = self.A * self.labCredit
            elif(x == 'A-' or x == 'a-'):
                temp = self.A_Minus * self.labCredit
            elif(x == 'B+' or x == 'b+'):
                temp = self.B_Plus * self.labCredit
            elif(x == 'B' or x == 'b'):
                temp = self.B * self.labCredit
            elif(x == 'B-' or x == 'b-'):
                temp = self.B_Minus * self.labCredit
            elif(x == 'C+' or x == 'c+'):
                temp = self.C_Plus * self.labCredit
            elif(x == 'C' or x == 'c'):
                temp = self.C * self.labCredit
            elif(x == 'C-' or x == 'c-'):
                temp = self.C_Minus * self.labCredit
            elif(x == 'D+' or x == 'd+'):
                temp = self.D_Plus * self.labCredit
            elif(x == 'D' or x == 'd'):
                temp = self.D * self.labCredit
            elif(x == 'F' or x == 'f'):
                temp = self.F * self.labCredit
            else:
                print("Rizwan Hasan")
            total = total + temp
            del(temp)

            self.cgpa = total / self.totalCredit
            self.cgpa = '{:.2f}'.format(self.cgpa)

    def getCGPA(self):
        return self.cgpa


def main():
    subGrades = input("\nEnter subject grades: (Use comma for seperation)\n=>")
    labGrades = input("\nEnter lab grades: (Use comma for seperation)\n=>")
    totalCredit = input("\nEnter total credit: \n=>")
    cgpa = CGPA_Calculator(subGrades, labGrades, totalCredit)
    print(cgpa.getCGPA())


if __name__ == '__main__':
    main()
