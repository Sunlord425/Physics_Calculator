#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 21:41:33 2022

@author: lorenzomazzeo
@last updated: 2/13/23
"""
import math
import sys
version = "6.0.1" 
g = 9.81
pi = 3.14159265359
displayStatus = True
def csc(theta):
    return 1/math.sin(theta)
def cot(theta):
    return 1/math.tan(theta)
def sec(theta):
    return 1/math.cos(theta)
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
def notGate(status):
    if status == True:
        return False
    if status == False:
        return True

def console():
    
    global displayStatus
    o = 0
    i = o
    def statusFail():
        global displayStatus
        if (displayStatus != True):
            print(f"attempt {i+1} opperation {o} failed, proceeding to next")
    def statusSuccess():
        global displayStatus
        if displayStatus != True:
            print(f"attempt {i+1} opperation {o} successful, proceeding to next")
    def setStatus():
        global displayStatus
        status = input("Display Indvidual Calculation Status? (y/n): ")
        if status.upper() == "Y": 
            return False
        elif status.upper() == "N":
            return True
        else:
            print("ERROR: INVALID INPUT")
            setStatus()
    print("/help for help")
    cmd = input("Enter Command: ")
    
    ###################
    def AxBisC(product, factor1, factor2):
        print("please enter values below, entering \"null\" if it is not given")
        print()
        f = input(f"{product}: ").upper()
        m = input(f"{factor1}: ").upper()
        a = input(f"{factor2}: ").upper()
        o = 0
        i = o
        while (i < 10) and ((isfloat(f) and isfloat(m) and isfloat(a)) == False):
            o +=1
            try:
                f = float(m)*float(a)
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            try:
                m = float(f)/float(a)
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            try:
                a = float(f)/float(m)
                statusSuccess()
            except:
                statusFail()
                pass
            o = 0
            print(f"""
                  Loop {i+1} Completed. Results:
                      {product} = {f}
                      {factor1} = {m}
                      {factor2} = {a}
                  """)
            i += 1
        console()
    def projectiles():
        print("/help for help")
        print()
        pcmd = input("Enter Command(projectile calulator): ")
        if pcmd == "/help":
            print("""
        /noAngleX - calculates position/time equations for x that do not require an angle
        /noAngleY - calculates position/time equations for y that do not require an angle
        /angle - position/velocity vs time with angles
        /range - range equations
        /exit - return to main console
                  """)
            projectiles()
        elif pcmd == "/noAngleX":
            print("please enter values below, entering \"null\" if it is not given")
            print()
            xf = input("Final Position: ")
            xi = input("Inital Position: ")
            vxi = input("Inital Velocity:")
            t = input("Time: ")
            o = 0
            i = o
            while (i < 10) and ((isfloat(xf) and isfloat(xi) and isfloat(vxi) and isfloat(t)) == False):
                o +=1
                try:
                   xf = float(xi) + float(vxi)*float(t)
                   statusSuccess()
                except:
                   statusFail()
                   pass
                o +=1
                try:
                   xi = float(xf) - float(vxi)*float(t)
                   statusSuccess()
                except:
                   statusFail()
                   pass
                o +=1
                try:
                   vxi = (float(xf)/float(t)) - (float(xi)/float(t))
                   statusSuccess()
                except:
                   statusFail()
                   pass
                o +=1
                try:
                   t = (float(xf)/float(vxi)) - (float(xi)/float(vxi))
                   statusSuccess()
                except:
                   statusFail()
                   pass
                o = 0
                print(f"""
                      Loop {i+1} Completed. Results:
                          Final Position: {xf}
                          Inital Position: {xi}
                          Inital Velocity: {vxi}
                          Time: {t}
                      """)
                i += 1
            projectiles()
        elif pcmd == "/noAngleY":
            print("please enter values below, entering \"null\" if it is not given")
            print()
            yf = input("Final Position: ")
            yi = input("Inital Position: ")
            vyi = input("Inital Velocity:")
            t = input("Time: ")
            o = 0
            i = o
            while (i < 10) and ((isfloat(yf) and isfloat(yi) and isfloat(vyi) and isfloat(t)) == False):
                o +=1
                try:
                   yf = float(yi) + float(vyi)*float(t)+ g*pow(float(t), 2)
                   statusSuccess()
                except:
                   statusFail()
                   pass
                o +=1
                try:
                   yi = float(yf) - float(vyi)*float(t)+ g*pow(float(t), 2)
                   statusSuccess()
                except:
                   statusFail()
                   pass
                o +=1
                try:
                   vyi = float(yf)/float(t) + float(yi)/float(t)+ g*t
                   statusSuccess()
                except:
                   statusFail()
                   pass
                o +=1
                try:
                   t = (float(vyi)+math.sqrt(pow(float(vyi), 2)+4*g*float(yi) - 4*g*float(yf)))/g*2
                   statusSuccess()
                except:
                   statusFail()
                   pass
                o = 0
                print(f"""
                      Loop {i+1} Completed. Results:
                          Final Position: {yf}
                          Inital Position: {yi}
                          Inital Velocity: {vyi}
                          Time: {t}
                      """)
                i += 1
            projectiles()
        elif pcmd == "/angle":
          print("please enter values below, entering \"null\" if it is not given")
          print()
          xf = input("Final Position(x): ")
          yf = input("Final Position(y)")
          xi = input("Inital Position(x): ")
          yi = input("Inital Position(y): ")
          vi = input("Inital Velocity: ")
          vxf = input("Final Velocity(x): ")
          vyf = input("Final Velocity(y): ")
          a = input("Launch Angle: ")
          t = input("Time: ")
          o = 0
          i = o
          while (i < 10) and ((isfloat(xf) and isfloat(xi) and isfloat(vi) and isfloat(t) and isfloat(a)) == False):
              o +=1
              try:
                 xf = float(xi)+(float(vi)*math.cos(math.radians(float(a))))*float(t)
                 statusSuccess()
              except:
                 statusFail()
                 pass
              o +=1
              try:
                 xi = float(xf)-(float(vi)*math.cos(math.radians(float(a))))*float(t)
                 statusSuccess()
              except:
                 statusFail()
                 pass
              o +=1
              try:
                 vi = ((float(xf)*sec(math.radians(float(a))))/float(t))-((float(xi)*sec(math.radians(float(a))))/float(t))
                 statusSuccess()
              except:
                 statusFail()
                 pass
              o +=1
              try:
                 a = math.degrees(math.acos(((float(xf))/(float(vi)*float(t)))-((float(xi))/(float(vi)*float(t)))))
                 statusSuccess()
              except:
                 statusFail()
                 pass
              o += 1
              #############
              try:
                 yf = float(yi) + (float(vi)*math.sin(math.degrees(float(a))))*t - 0.5*g*math.pow(float(t), 2)
                 statusSuccess()
              except:
                 statusFail()
                 pass
              o +=1
              try:
                 yi = float(yf) - float(vi)*float(t)*math.sin(float(a)) + ((math.pow(float(t), 2)*g)/(2))
                 statusSuccess()
              except:
                 statusFail()
                 pass
              o +=1
              try:
                 a = math.degrees((math.asin(math.radians(((float(yf))/(float(vi)*float(t)))-((float(yi))/(float(vi)*float(t)))+((g*float(t))/(2*float(vi)))))))
                 statusSuccess()
              except:
                 statusFail()
                 pass
              o +=1
              ################
              try:
                 vxf = float(vi)*math.cos(math.radians(float(a)))
                 statusSuccess()
              except:
                 statusFail()
                 pass
              o +=1
              try:
                 vi = float(vxf)*sec(math.radians(float(a)))
                 statusSuccess()
              except:
                 statusFail()
                 pass
              o +=1
              try:
                 a = math.degrees(math.acos((float(vxf))/(float(vi))))
                 statusSuccess()
              except:
                 statusFail()
                 pass
              o +=1
              try:
                 a = math.degrees((math.asin(math.radians(((float(vyf))/(float(vi)))+((g*float(t))/(float(vi)))))))
                 statusSuccess()
              except:
                 statusFail()
                 pass
              o = 0
              print(f"""
                    Loop {i+1} Completed. Results:
                        Final Position: {xf}
                        Final Positon(y): {yf}
                        Inital Position(x): {xi}
                        Inital Position(y): {yi}
                        Inital Velocity: {vi}
                        Final Velocity(x): {vxf}
                        Final Velocity(y): {vyf}
                        Time: {t}
                        Launch Angle: {a}
                    """)
              i += 1
              
          projectiles()
        elif pcmd == "/range":
            print("please enter values below, entering \"null\" if it is not given")
            print()
            pRange = input("Range: ")
            vi = input("Inital Velocity:  ")
            a = input("Launch Angle: ")
            o = 0
            i = o
            while (i < 10) and ((isfloat(a) and isfloat(vi) and isfloat(pRange)) == False): 
                o +=1
                try:
                   pRange = ((math.pow(float(vi), 2))/(g))*math.sin((math.radians(2*float(a))))
                   statusSuccess()
                except:
                   statusFail()
                   pass
                o +=1
                try:
                   vi = math.sqrt(float(pRange)*math.sin(math.radians(2*float(a))))*(csc(math.radians(2*float(a))))
                   statusSuccess()
                except:
                   statusFail()
                   pass
                o +=1
                try:
                   a = math.degrees((math.asin(((float(pRange)*g)/(math.pow(float(vi), 2)))))/2)
                   statusSuccess()
                except:
                   statusFail()
                   pass
                o = 0
                print(f"""
                      Loop {i+1} Completed. Results:
                          Range: {pRange}
                          Inital Velocity: {vi}
                          Launch Angle: {a}
                      """)
                i += 1
            projectiles()
        
        elif ((pcmd == "/exit") or (pcmd == "/e")):
            console()
        elif ((pcmd == "/quit") or (pcmd == "/q")):
            sys.exit("User Terminated the Program")
        else:
            print("ERROR: INVALID COMMAND")
            projectiles()
        
            
    def vectorCalc():
        vecCmd = input("Enter Command (Vector Calc): ")
        if vecCmd == "/help":
            print("""
            list of commands:
                /comp - convert from mag/dir to compY/compX and back
                /add - add two vectors
                /scalar - multiply a vector by a scalar

                /help - command list
                /exit - exit vector calculator  
                """)
            vectorCalc()
        elif (vecCmd == "/exit") or (vecCmd == "/e"):
            console()
        elif vecCmd == "/comp":
            mag = input("Magnitude: ")
            dir = input("Direction: ")
            compX = input("X Component: ")
            compY = input("Y Component: ")
            o = 0
            i = o
            while (i < 10) and ((isfloat(mag) and isfloat(dir) and isfloat(compX) and isfloat(compY)) == False):
                o +=1
                try:
                    compX = abs(float(mag))*(math.cos(math.radians(float(dir))))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    compY = abs(float(mag))*(math.sin(math.radians(float(dir))))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    mag = math.sqrt(math.pow(float(compX), 2)+math.pow(float(compY), 2))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    dir = math.degrees(math.acos((float(compX))/(float(mag))))
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    dir = math.degrees(math.asin((float(compY))/(float(mag))))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o = 0
                print(f"""
                  Loop {i+1} Completed. Results:
                      Magnitude = {mag}
                      Direction = {dir}
                      X Component = {compX}
                      Y Component = {compY}
                      
                  """)
                i += 1
            vectorCalc()
        elif vecCmd == "/add":
            mag1 = input("Magnitude 1: ")
            dir1 = input("Direction 1: ")
            compX1 = input("X Component 1: ")
            compY1 = input("Y Component 1: ")
            mag2 = input("Magnitude 2: ")
            dir2 = input("Direction 2: ")
            compX2 = input("X Component 2: ")
            compY2 = input("Y Component 2: ")
            resX = input("Resultant X Component: ")
            resY = input("Resultant Y Component: ")
            resMag = input("Resultant Magnitude: ")
            resDir = input("Resultant Direction: ")
            o = 0
            i = o
            while (i < 20) and ((isfloat(mag1) and isfloat(dir1) and isfloat(compX1) and isfloat(compY1) and isfloat(mag2) and isfloat(dir2) and isfloat(compX2) and isfloat(compY2) and isfloat(resX) and isfloat(resY) and isfloat(resDir) and isfloat(resMag)) == False):
                o +=1
                try:
                    compX1 = abs(float(mag1))*(math.cos(math.radians(float(dir1))))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    compY1 = abs(float(mag1))*(math.sin(math.radians(float(dir1))))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    mag1 = math.sqrt(math.pow(float(compX1), 2)+math.pow(float(compY1), 2))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    dir1 = math.degrees(math.acos((float(compX1))/(float(mag1))))
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    dir1 = math.degrees(math.asin((float(compY1))/(float(mag1))))
                    statusSuccess()
                except:
                    statusFail()
                    pass

                o += 1
                
                try:
                    compX2 = abs(float(mag2))*(math.cos(math.radians(float(dir2))))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    compY2 = abs(float(mag2))*(math.sin(math.radians(float(dir2))))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    mag2 = math.sqrt(math.pow(float(compX2), 2)+math.pow(float(compY2), 2))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    dir2 = math.degrees(math.acos((float(compX2))/(float(mag2))))
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    dir2 = math.degrees(math.asin((float(compY2))/(float(mag2))))
                    statusSuccess()
                except:
                    statusFail()
                    pass


                o +=1
                try:
                    resX = float(compX1) + float(compX2)
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    resY = float(compY1) + float(compY2)
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    resMag = math.sqrt(math.pow(float(resX), 2)+math.pow(float(resY), 2))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    resDir = math.degrees(math.acos((float(resX))/(float(resMag))))
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    resDir = math.degrees(math.asin((float(resY))/(float(resMag))))
                    statusSuccess()
                except:
                    statusFail()
                    pass

                o +=1
                try:
                    compX1 = float(resX) - float(compX2)
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    compY1 = float(resY) - float(compY2)

                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    compX2 = float(resX) - float(compX1)
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    compY2 = float(resY) - float(compY1)

                    statusSuccess()
                except:
                    statusFail()
                    pass

                o = 0
                print(f"""
                  Loop {i+1} Completed. Results:
                      Magnitude 1 = {mag1}
                      Direction 1 = {dir1}
                      X Component 1 = {compX1}
                      Y Component 1 = {compY1}

                      Magnitude 2 = {mag2}
                      Direction 2 = {dir2}
                      X Component 2 = {compX2}
                      Y Component 2 = {compY2}

                      Resultant Magnitude  = {resMag}
                      Resultant Direction  = {resDir}
                      Resultant X Component = {resX}
                      Resultant Y Component = {resY}
                      
                  """)
                i += 1
            vectorCalc()
        elif vecCmd == "/scalar":
            mag = input("Magnitude: ")
            dir = input("Direction: ")
            compX = input("X Component: ")
            compY = input("Y Component: ")
            scal = input("Scalar: ")
            magR = input("Resultant Magnitude: ")
            dirR = input("Resultant Direction: ")
            compXR = input("Resultant X Component: ")
            compYR = input("Resultant Y Component: ")
            o = 0
            i = o
            while (i < 10) and ((isfloat(mag) and isfloat(dir) and isfloat(compX) and isfloat(compY) and isfloat(magR) and isfloat(dirR) and isfloat(compXR) and isfloat(compYR) and isfloat(scal)) == False):
                o +=1
                try:
                    compX = abs(float(mag))*(math.cos(math.radians(float(dir))))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    compY = abs(float(mag))*(math.sin(math.radians(float(dir))))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    mag = math.sqrt(math.pow(float(compX), 2)+math.pow(float(compY), 2))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    dir = math.degrees(math.acos((float(compX))/(float(mag))))
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    dir = math.degrees(math.asin((float(compY))/(float(mag))))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                
                o +=1
                try:
                    dirR = float(dir)
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    compXR = float(compX)*float(scal)
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    compYR = float(compY)*float(scal)
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    magR = float(mag)*float(scal)
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    magR = (float(scal)/abs(float(scal)))*(math.sqrt(math.pow(float(compXR), 2)+math.pow(float(compYR), 2)))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    scal = float(compXR)/float(compX)
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    scal = float(compYR)/float(compY)
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o = 0
                print(f"""
                  Loop {i+1} Completed. Results:
                      Magnitude = {mag}
                      Direction = {dir}
                      X Component = {compX}
                      Y Component = {compY}
                      Scalar = {scal}
                      Resultant Magnitude = {magR}
                      Resultant Direction = {dirR}
                      Resultant X Component = {compXR}
                      Resultant Y Component = {compYR}
                  """)
                i += 1
            vectorCalc()

        elif ((vecCmd == "/quit") or (vecCmd == "/q")):
            sys.exit("User Terminated the Program")
        else:
            print("ERROR: INVALID COMMAND")
            vectorCalc()
    
    def col():
        print("/help for help")
        print()
        clCmd = input("Enter Command (Collisions): ")
        if clCmd == "/help":
            print("""
                /cinc - Completely Inelastic Collision
                /inc - Inelastic Collisions
                /ec - Elastic Collisions

                /help - Shows help
                /exit - Return to Main Calculator
                /quit - quits the program 

                """)
            col()
        elif clCmd == "/cinc":
            print("please enter values below, entering \"null\" if it is not given")
            print()
            m1 = input("Mass 1: ")
            m2 = input("Mass 2: ")
            vi = input("Inital Velocity: ")
            vf = input("Final Velocity: ")
            o = 0
            i = o
            while (i < 10) and ((isfloat(m1) and isfloat(m2) and isfloat(vi) and isfloat(vf)) == False):
                o +=1
                try:
                    vf = (float(m1)*float(vi))/(float(m1)+float(m2))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    vi = float(vf) + (float(vf)*float(m2))/(float(m1))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    m1 = (float(vf)*float(m2))/(float(vi)-float(vf))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                try:
                    m2 = (float(vi)*float(m1))/(float(vf)) + float(m1)
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o = 0
                print(f"""
                  Loop {i+1} Completed. Results:
                        Mass 1 = {m1}
                        Mass 2 = {m2}
                        Inital Velocity = {vi}
                        Final Velocity = {vf} 
                  """)
                i += 1
                col()

        elif clCmd =="/inc":
            print("please enter values below, entering \"null\" if it is not given")
            print()
            m1 = input("Mass 1: ")
            m2 = input("Mass 2: ")
            v1 = input("Velocity 1 : ")
            v2 = input("Velocity 2: ")
            vf = input("Final Velocity: ")
            o = 0
            i = o
            while (i < 10) and ((isfloat(m1) and isfloat(m2) and isfloat(v1) and isfloat(v2) and isfloat(vf)) == False):
                o +=1
                try:
                    vf = (float(m1)*float(v1)+float(m2)*float(v2))/(float(m1)+float(m2))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    v1 = float(vf) + (float(m2)*float(vf))/(float(m1)) - (float(m2)*float(v2))/(float(m1))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    v2 = float(vf) + (float(m1)*float(vf))/(float(m2)) - (float(m1)*float(v1))/(float(m2))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    m1 = (float(m2)*(float(vf)-float(v2)))/(float(v1)-float(vf))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    m2 = (float(m1)*(float(vf)-float(v2)))/(float(v1)-float(vf))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o = 0
                print(f"""
                  Loop {i+1} Completed. Results:
                        Mass 1 = {m1}
                        Mass 2 = {m2}
                        Velocity 1 = {v1}
                        Velocity 2 = {v2}
                        Final Velocity = {vf} 
                  """)
                i += 1  
            col()
        
        elif clCmd == "/ec":
            print("please enter values below, entering \"null\" if it is not given")
            print()
            m1 = input("Mass 1: ")
            m2 = input("Mass 2: ")
            v1i = input("Inital Velocity 1: ")
            v1f = input("Final Velocity 1: ")
            v2i = input("Inital Velocity 2: ")
            v2f = input("Final Velocity 2: ")
            o = 0
            i = o
            while (i < 10) and ((isfloat(m1) and isfloat(m2) and isfloat(v1i) and isfloat(v1f) and isfloat(v2i) and isfloat(v2f)) == False):
                o +=1
                try:
                    m1 = (float(m2)*(float(v2f)-float(v2i)))/(float(v1i)-float(v1f))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    m2 = (float(m1)*(float(v1f)-float(v1i)))/(float(v2i)-float(v2f))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o +=1
                try:
                    v1i = float(v1f) + (float(m2)*float(v2f))/(float(m1)) - (float(m2)*float(v2i))/(float(m1))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o += 1
                try:
                    v1f = ((float(m1)-float(m2))/(float(m1)+float(m2)))*float(v1i)
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o += 1
                try:
                    v1f = float(v1i) + (float(m2)*float(v2i))/(float(m1)) - (float(m2)*float(v2f))/(float(m1))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o += 1
                try:
                    v1i = float(v2f) + (float(m1)*float(v1f))/(float(m2)) - (float(m1)*float(v1i))/(float(m2))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o += 1
                try:
                    v2f = float(v2i) + (float(m1)*float(v1i))/(float(m2)) - (float(m1)*float(v1f))/(float(m2))
                    statusSuccess()
                except:
                    statusFail()
                    pass
                o += 1
                try:
                    v2f = ((2*float(m1))/(float(m1)+float(m2)))*float(v1i)
                    statusSuccess()
                except:
                    statusFail()
                    pass
                
                o = 0
                print(f"""
                  Loop {i+1} Completed. Results:
                        Mass 1 = {m1}
                        Mass 2 = {m2}
                        Inital Velocity 1 = {v1i}
                        Final Velocity 1 = {v1f} 
                        Inital Velocity 2 = {v2i}
                        Final Velocity = {v2f}
                  """)
                i += 1
            col()
            
        elif ((clCmd == "/quit") or (clCmd == "/q")):
            sys.exit("User Terminated the Program")
        elif (clCmd == "/exit") or (clCmd) == "/e":
            console()
        else:
            print("ERROR: INVALID COMMAND")
            
            col()


    ###################
    if cmd == "/help":
        print("""
              list of commands:
                  /posT - position vs time equations
                  /force - force equations
                  /spring - spring equations
                  /friction - friction equations
                  /work - work equations
                  /workAngle - work equations that involve angles
                  /projectile - projectile calculator
                  /kineticE - kinetic energy equations
                  /potentialGE - gravitational potential energy equations
                  /penPeriod - calulates period of pendulum 
                  /mechNRG - total mechanical energy equations
                  /power - power equations
                  /momentum - momentum equations
                  /impulse - impulse equations
                  /vec - vector calculator
                  /col - collision calculator
                  /AvAV - Average Angular Velocity
                  /AvAA - Average Angular Acceleration
                  /MoI - Moment of Inertia
                  /TanSpeed -  Tangential Speed
                  /TanTorque - Tangential Torque
                  /NonTanTorque - Non-Tangential Torque
                  /sumTor - Sum of All Torques
                  /RotKE - Rotational Kinetic Energy
                  /AM - Angular Momentum

                  
                  /status - display operation success readout
                  /faq - displays frequently ask questions
                  /changelog - displays the changelog
                  /quit - exit the program
              """)
        console()
        
    ###################
    elif cmd == "/vec":
        vectorCalc()
    
    elif cmd == "/posT":
        print("please enter values below, entering \"null\" if it is not given")
        a = input("Acceleration: ").upper()
        t = input("Time: ").upper()
        xi = input("Inital Position: ").upper()
        xf = input("Final Position: ").upper()
        vi = input("Inital Velocity: ").upper()
        vf = input("Final Velocity: ").upper()
        vav = input("Average Velocity: ").upper()
        o = 0
        i = o
    
        
        while (i < 21) and ((isfloat(a) and isfloat(t) and isfloat(xi) and isfloat(xf) and isfloat(vi) and isfloat(xf) and isfloat(vav)) == False):
            ### vf = vi+at
            o +=1
            try:
                vf = float(vi)+float(a)*float(t)
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            try:
                vi = float(vf)-float(a)*float(t)
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            try:
                a = (float(vf)-float(vi))/float(t)
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            try:
                t = (float(vf)-float(vi))/float(a)
                statusSuccess()
            except:
                statusFail()
                pass
            ### vav = 1/2(vi+vfv)
            o +=1
            try:
                vav = 0.5*(float(vi)+float(vf))
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            try:
                vi = 2*float(vav)-float(vf)
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            try:
                vf = 2*float(vav)-float(vi)
                statusSuccess()
            except:
                statusFail()
                pass
            ### xf = xi + 1/2(vi+vf)t
            o +=1
            try:
                xf = float(xi) + 0.5*(float(vi)+float(vf))*float(t)
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            try:
                xi = float(xf) - ((float(vi)*float(t))/(2)) - ((float(vf)*float(t))/(2))
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            try:
                vi = (2*float(xf))/float(t) - (2*float(xi))/float(t) - float(vf)
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            try:
                vf = (2*float(xf))/(float(t)) - (2*float(xi))/(float(t)) - float(vi)
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            try:
                t = (float(xf)-float(xi))/(0.5*(float(vi)+float(vf)))
                statusSuccess()
            except:
                statusFail()
                pass
            ### xf =  xi + vi*t+1/2a*t^2
            o +=1
            try:
                xf = float(xi)+(float(vi)*float(t))+0.5*(float(a))*math.pow(float(t), 2)
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            try:
                xi = float(xf)-float(vi)*float(t)-0.5*(float(a)*math.pow(float(t), 2))
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            try:
                vi = float(xf)/float(t)-float(xi)/float(t)-(float(a)*float(t))/2
                statusSuccess()
            except:
                statusFail()
            o += 1
            try:
                a = (2*float(xf))/(math.pow(float(t), 2))-(2*float(xi))/(math.pow(float(t), 2))-(2*float(vi))/(float(t))
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            try:
                t = ((float(vi)-math.sqrt(math.pow(float(vi), 2)+(2*(float(a))*float(xf))-(2*(float(a)))*float(xi)))/float(a))
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            
            ### vf^2 = vi^2 +2a(xf-xi)
            
            try:
                vf = math.sqrt(math.pow(float(vi), 2)+2*float(a)*float(xf)-2*float(a)*float(xi))
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            try:
                a = (math.pow(float(vf), 2))/(2*(float(xf)-float(xi)))-(math.pow(float(vi), 2))/(2*(float(xf)-float(xi)))
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            try:
                vi = math.sqrt(math.pow(float(vf), 2)-2*float(a)*float(xf)+2*float(xi)*float(a))
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            try:
                xf = ((math.pow(float(vf), 2))/(2*float(a))) - ((math.pow(float(vi),2))/(2*float(a))) + float(xi)
                statusSuccess()
            except:
                statusFail()
                pass
            o +=1
            try:
                xi = -1*(math.pow(float(vf), 2))/(2*float(a))+(math.pow(float(vi), 2))/(2*float(a))+float(xf)
                statusSuccess()
            except:
                statusFail()
                pass
            o = 0
            print(f"""
                  Loop {i+1} Completed. Results:
                      Acceleration = {a}
                      Time = {t}
                      Initial Position = {xi}
                      Final Position = {xf}
                      Initial Velocity = {vi}
                      Final Velocity = {vf}
                      Average Velocity = {vav}
                  """)
            i += 1
        console()
    ##################
    elif cmd == "/projectile":
        projectiles()
    ##################
    elif cmd == "/force":
       AxBisC("Force", "Mass", "Acceleration")
        
    #######################
    elif cmd == "/spring":
       AxBisC("Force", "Spring Coefficient", "Change in Length")
        
    #######################
    elif cmd == "/friction":
        AxBisC("Maximum Force/Kinetic Force", "Coefficent of Friction", "Normal Force")
        
    ###########
    elif cmd == "/work":
       AxBisC("Work", "Force", "Distance")
    ##############
    elif cmd == "/workAngle":
        print("please enter values below, entering \"null\" if it is not given")
        print()
        w = input("Work: ")
        d = input("Distance:  ")
        f = input("Force: ")
        a = input("Angle: ")
        o = 0
        i = o
        while (i < 10) and ((isfloat(a) and isfloat(d) and isfloat(w) and isfloat(f)) == False): 
            o +=1
            try:
               w = float(f)*float(d)*math.cos(math.radians(float(a)))
               statusSuccess()
            except:
               statusFail()
               pass
            o +=1
            try:
               f = (float(w)*sec(math.radians(a)))/(float(d))
               statusSuccess()
            except:
               statusFail()
               pass
            o +=1
            try:
               d = (float(w)*sec(math.radians(a)))/(float(f))
               statusSuccess()
            except:
               statusFail()
               pass
            o += 1
            try:
               a = math.degrees(math.acos((float(w))/(float(f)*float(d))))
               statusSuccess()
            except:
               statusFail()
               pass
            o = 0
            print(f"""
                  Loop {i+1} Completed. Results:
                      Work: {w}
                      Distance: {d}
                      Force: {f}
                      Angle: {a}
                  """)
            i += 1
        console()
    ##############
    elif cmd == "/kineticE":
        print("please enter values below, entering \"null\" if it is not given")
        print()
        k = input("Kinetic Energy: ")
        m = input("Mass:  ")
        v = input("Velocity: ")
        o = 0
        i = o
        while (i < 10) and ((isfloat(k) and isfloat(m) and isfloat(v)) == False): 
            o +=1
            try:
               k = 0.5*float(m)*math.pow(float(v), 2)
               statusSuccess()
            except:
               statusFail()
               pass
            o +=1
            try:
               m = (2*float(k))/(math.pow(float(v), 2))
               statusSuccess()
            except:
               statusFail()
               pass
            o +=1
            try:
               v = (math.sqrt(2*float(k)*float(m)))/(float(m))
               statusSuccess()
            except:
               statusFail()
               pass
            o = 0
            print(f"""
                  Loop {i+1} Completed. Results:
                      Kinetic Energy: {k}
                      Mass: {m}
                      Velocity: {v}
                  """)
            i += 1
        console() 
    ##############
    elif cmd == "/AvAV":
        AxBisC("Change in Angular Position","Average Angular Velocity", "Change in Time")
    ############
    elif cmd == "/TanSpeed":
        AxBisC("Tangential Speed", "Radius", "Angular Speed")
    ###########
    elif cmd == "/AvAA":
        AxBisC("Change in Angular Velocity", "Change in Time", "Average Angular Acceleration")
    ###########
    elif cmd == "/MoI":
        print("please enter values below, entering \"null\" if it is not given")
        print()
        iner = input("Moment of Inertia: ")
        m = input("Mass:  ")
        r = input("Radius: ")
        o = 0
        i = o
        while (i < 10) and ((isfloat(iner) and isfloat(m) and isfloat(r)) == False): 
            o +=1
            try:
               iner = float(m)*math.pow(float(r),2)
               statusSuccess()
            except:
               statusFail()
               pass
            o +=1
            try:
               m = (float(iner))/math.pow(float(r),2)
               statusSuccess()
            except:
               statusFail()
               pass
            o +=1
            try:
               r = math.sqrt(float(iner)*float(m))/float(m)
               statusSuccess()
            except:
               statusFail()
               pass
            o = 0
            print(f"""
                  Loop {i+1} Completed. Results:
                        Moment of Inertia: {iner}
                        Mass: {m}
                        Radius: {r}
                  """)
            i += 1
        console()
    ###########
    elif cmd == "/TanTorque":
        AxBisC("Torque","Radius","Force")
    ###########
    elif cmd == "/NonTanTorque":
        print("please enter values below, entering \"null\" if it is not given")
        print()
        t = input("Torque: ")
        r = input("Radius: ")
        f = input("Force:  ")
        a = input("Angle: ")
        o = 0
        i = o
        while (i < 10) and ((isfloat(t) and isfloat(r) and isfloat(f) and isfloat(a)) == False): 
            o +=1
            try:
               t = float(r)*float(f)*math.sin(math.radians(float(a)))
               statusSuccess()
            except:
               statusFail()
               pass
            o +=1
            try:
               r = (float(t)*csc(float(a)))/(float(f))
               statusSuccess()
            except:
               statusFail()
               pass
            o +=1
            try:
               f = (float(t)*csc(float(a)))/(float(r))
               statusSuccess()
            except:
               statusFail()
               pass
            o +=1
            try:
               a = math.asin(math.radians((float(t))/(float(r)*float(f))))
               statusSuccess()
            except:
               statusFail()
               pass
            o = 0
            print(f"""
                  Loop {i+1} Completed. Results:
                        Torque: {t}
                        Radius: {r}
                        Force: {f}
                        Angle: {a}
                  """)
            i += 1
        console()
    ###########
    elif cmd == "/RotKE":
        print("please enter values below, entering \"null\" if it is not given")
        print()
        rKE = input("Rotational Kinetic Energy: ")
        m = input("Moment of Inertia:  ")
        a = input("Angular Speed: ")
        o = 0
        i = o
        while (i < 10) and ((isfloat(rKE) and isfloat(m) and isfloat(a)) == False): 
            o +=1
            try:
               rKE = 0.5*float(m)*math.pow(float(a),2)
               statusSuccess()
            except:
               statusFail()
               pass
            o +=1
            try:
               m = (2*float(rKE))/math.pow(float(a),2)
               statusSuccess()
            except:
               statusFail()
               pass
            o +=1
            try:
               a = (math.sqrt(2*float(rKE)*float(m)))/(float(m))
               statusSuccess()
            except:
               statusFail()
               pass
            o = 0
            print(f"""
                  Loop {i+1} Completed. Results:
                        Rotational Kinetic Energy: {rKE}
                        Moment of Inertia: {m}
                        Angular Speed: {a}
                  """)
            i += 1
        console()
    ###########
    elif cmd == "/AM":
        AxBisC("Angular Momentum","Moment of Inertia", "Angular Speed")
    ###########
    elif cmd == "/sumTor":
        AxBisC("Sum of All Torques","Moment of Inertia","Angular Acceleration")
    ###########
    elif cmd == "/potentialGE":
        print("please enter values below, entering \"null\" if it is not given")
        print()
        p = input("Potential Gravitational Energy: ")
        m = input("Mass:  ")
        h = input("Height: ")
        o = 0
        i = o
        while (i < 10) and ((isfloat(p) and isfloat(m) and isfloat(h)) == False): 
            o +=1
            try:
               p = float(m)*g*float(h)
               statusSuccess()
            except:
               statusFail()
               pass
            o +=1
            try:
               m = (float(p))/(g*float(h))
               statusSuccess()
            except:
               statusFail()
               pass
            o +=1
            try:
               h = float(p)*(1)/(float(m)*g)
               statusSuccess()
            except:
               statusFail()
               pass
            o = 0
            print(f"""
                  Loop {i+1} Completed. Results:
                      Potential Gravitational Energy: {p}
                      Mass: {m}
                      height: {h}
                  """)
            i += 1
        console()
    ##############
    elif cmd == "/power":
        AxBisC("Work","Power","Time")
    ##############
    
    # m*g*h1 + 1/2*m*vi^2 = m*g*h2 + 1/2*m*v^2
    elif cmd == "/mechNRG":
        print("please enter values below, entering \"null\" if it is not given")
        print()
        h1 = input("Height 1: ")
        h2 = input("Height 2: ")
        v1 = input("Velocity 1: ")
        v2 = input("Velocity 2: ")
        o = 0
        i = o
        while (i < 5) and ((isfloat(h1) and isfloat(h2) and isfloat(v1) and isfloat(v2)) == False): 
            o +=1
            try:
               h1 = float(h2) + (math.pow(float(v2), 2))/(2*g) - (math.pow(float(v1), 2))/(2*g)
               statusSuccess()
            except:
               statusFail()
               pass
            o +=1
            try:
               h2 = float(h1) + (math.pow(float(v2), 2))/(2*g) - (math.pow(float(v1), 2))/(2*g)
               statusSuccess()
            except:
               statusFail()
               pass
            try:
               v1 = math.sqrt(2*g*float(h2)+math.pow(float(v2), 2) - 2*g*float(h1))
               statusSuccess()
            except:
               statusFail()
               pass
            o +=1
            try:
               v2 = math.sqrt(2*g*float(h1)-2*g*float(h2)+math.pow(float(v1), 2))
               statusSuccess()
            except:
               statusFail()
               pass
            o +=1
            o = 0
            print(f"""
                  Loop {i+1} Completed. Results:
                      Height 1: {h1}
                      Height 2: {h2}
                      Velocity 1: {v1}
                      Velocity 2 {v2}
                  """)
            console()
    ##############
    elif cmd =="/penPeriod":
        print("please enter values below, entering \"null\" if it is not given")
        print()
        t = input("Period: ")
        l = input("Length:  ")
        o = 0
        i = o
        while (i < 4) and ((isfloat(t) and isfloat(l)) == False): 
            o +=1
            try:
               t = 2*pi*math.sqrt(float(l)/g)
               statusSuccess()
            except:
               statusFail()
               pass
            o +=1
            try:
               l = (math.pow(float(t), 2)*g)/(4*math.pow(pi, 2))
               statusSuccess()
            except:
               statusFail()
               pass
            o = 0
            print(f"""
                  Loop {i+1} Completed. Results:
                      Period: {t}
                      Length: {l}
                  """)
            console()
    ##############
    elif cmd == "/momentum":
        AxBisC("Momentum", "Mass", "Velocity")
    ##############
    elif cmd == "/impulse":
        AxBisC("Impulse/Change in Momentum", "Force", "Time") 
    ##############
    elif cmd == "/col":
        col()
    ##############
    elif cmd == "/changelog" :                                                                              ### ?/?/? ###
        print(""" 
              2.0.0 - added projectile calculations
              2.1.0 - 2.6.0 - I forgor, mostly just bug fixes and added more
                              stuff to the projectile calculator, optimization
              2.7.0 - fixed some bugs that arose from the stupid math module not having 
                      trig functions besides sin, cos, and tan
              2.8.1 - added work/angle equations
              2.8.2 - fixed a bug where work/angle equations would open projectile
                      calculation terminal after finishing
              3.0.0 - added potential and kinetic energy equations
              3.1.0 - added /faq because I don't want to explain floating point errors
                      to people
              3.1.1 - made it so /faq wouldn't also quit the program
              3.1.2 - fixed a bug with the potential energy equations
              3.2.0 - added pendulum period equation
              3.2.1 - cool spacing thing on initalization 
              3.2.2 - fixed a bugs with pendulum period calculator
              3.3.0 - redid some posT equations
              3.4.0 - added total mechanical energy equations
              3.4.1 - fixed a bug in the potential GE equations
              3.4.2 - fixed a bug in the mechnical energy equations
              3.5.0 - added power equation
              4.0.0 - added function to enable and disable readout
              4.1.0 - refactored readout command
              4.2.0 - fixed bug with readout command
              4.2.1 - added confirmation that is given to user after 
                      readout command is executed
              4.2.2 - more readout command bug fixes
              4.2.3 - fixed a bug with the projectile calculator 
              4.3.0 - added momentum equations
              4.4.0 - added impulse equations
              4.4.1 - formating
              4.4.2 - formating 2: electric bogaloo
              5.0.0 - added vector calculator
              5.0.1 - vector scalar bug fixes 
              6.0.0 - added collison calculator
              6.0.1 - inelastic collison bug fixed
              6.1.0 - added equation to elastic collision solver, added 
                        /col to help
              6.1.2 - fixed display bug with /col, fixed a bug with /posT where xf would be
                        calculated wrongly
              7.0.0 - added a bunch of rotational equations
              """)
        console()
    ##############
    elif cmd == "/faq":
        print("""
             Q: "why am I getting answers like 3.000000000001?" 
             A: It's a fun thing that computers do called a floating point error,
             due to how the IEEE 754 standard for repersenting floating point (decimal) numbers works
             (TL:DR - just round bro I can't really fix it)
              
              """)
        console()
    ##############
    elif cmd == "/status": 
       displayStatus = setStatus()
       print(f"configuration set to: {notGate(displayStatus)}")
       console()
    ##############
    elif ((cmd == "/quit") or (cmd == "/q")):
       sys.exit("User Terminated the Program")
            
    ######################################
     
    else:
        print("ERROR: INVALID COMMAND")
        console()
print()
print()
print("Scuffed Physics Calculator/Terminal Thing")
print(f"Version: {version}")
console()