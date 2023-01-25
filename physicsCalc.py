#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 21:41:33 2022

@author: lorenzomazzeo
@last updated: 1/13/22
"""
import math
import sys
version = "4.2.3" 
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
    

def console():
    
    global displayStatus
    o = 0
    i = o
    def statusFail():
        global displayStatus
        if (displayStatus == True):
            print(f"attempt {i+1} opperation {o} failed, proceeding to next")
    def statusSuccess():
        global displayStatus
        if displayStatus == True:
            print(f"attempt {i+1} opperation {o} successful, proceeding to next")
    def setStatus():
        global displayStatus
        status = input("Display Indvidual Calculation Status? (y/n): ")
        if status.upper() == "Y": 
            return True
        elif status.upper() == "N":
            return False
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
        
        elif pcmd == "/exit":
            console()
        else:
            print("ERROR: INVALID COMMAND")
            projectiles()
        
            
            
            
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
                  /projectile - projectile equations
                  /kineticE - kinetic energy equations
                  /potentialGE - gravitational potential energy equations
                  /penPeriod - calulates period of pendulum 
                  /mechNRG - total mechanical energy equations
                  /power - power equations
                  
                  /status - display operation success readout
                  /faq - displays frequently ask questions
                  /changelog - displays the changelog
                  /quit - exit the program
              """)
        console()
        
    ###################
    
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
                xf = float(xi)+float(vi)*float(t)+0.5*(float(a))*math.pow(float(t), 2)
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
                xf = (math.pow(float(vf), 2))/(2*float(a))-(math.pow(float(vi), 2))/(2*float(a))+float(xi)
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
        l = input("length:  ")
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
    elif cmd == "/changelog" :
        print(""" 
              2.0.0 - added projectile calculations
              2.1.0-2.6.0 - I forgor, mostly just bug fixes and added more
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
       print(f"configuration set to: {displayStatus}")
       console()
    ##############
    elif cmd == "/quit":
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