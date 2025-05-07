"""
Práctica 5: Sistema circulatorio

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Hernandez Ruiz Celia Lizette
Número de control: 22210415
Correo institucional: l22210415@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
# Instalar librerias en consola
#!pip install control
#!pip install slycot

# Librerías para cálculo numérico y generación de gráficas
import numpy as np
import math
import matplotlib.pyplot as plt
import control as ctrl

# Datos de la simulación

x0,t0,tF,dt,w,h =0,0,30,1E-3,10,5

N = round((tF-t0)/dt)+1

t = np.linspace(t0,tF,N)

t = np.linspace(t0,tF,N)

u = np.sin(2*math.pi*95/60*t) + 0.8

signal = ['Hipotenso', 'Normotenso', 'Hipertenso']

def sys_cardio(Z,C,R,L):
        num = [L*R,R*Z]
        den = [C*L*R*Z,L*R+L*Z,R*Z]
        sys = ctrl.tf(num,den)
        return sys

#Funcion de transferencia: Individuo Hipotenso (caso)
Z, C, R, L = 0.020, 0.250, 0.600, 0.005
sysH = sys_cardio(Z,C,R,L)
print('Individuo: Hipotenso')
print(sysH)

#Funcion de transferencia: Individuo Normotenso (control)
Z, C, R, L = 0.033, 1.500, 0.950, 0.010
sysN = sys_cardio(Z,C,R,L)
print('Individuo: Normotenso')
print(sysN)

#Funcion de transferencia: Individuo Hipertenso (caso)
Z, C, R, L = 0.050, 2.500, 1.400, 0.020
sysZ = sys_cardio(Z,C,R,L)
print('Individuo: Hipertenso')
print(sysZ)

def plotsignals(u, sysH, sysN, sysZ, signal):
    fig = plt.figure()
    ts,Vs = ctrl.forced_response(sysH,t,u,x0)
    plt.plot(t,Vs, ':', color = [0.3,0.5,0.2], label = '$P_P(t): Hipotenso$')
    ts,Ve = ctrl.forced_response(sysN,t,u,x0)
    plt.plot(t,Ve,'-', color = [0.5,0.05,0.05], label = '$P_P(t): Normotenso$')
    ts,pid = ctrl.forced_response(sysZ,t,Vs,x0)
    plt.plot(t,pid, ':', linewidth = 2, color = [0,0.25,0.4],
             label = '$P_P(t): Hipertenso$')
    plt.grid(False)
    plt.xlim(0, 10)
    plt.ylim(-.5, 1.5)
    plt.xticks(np.arange(0, 10, 1))
    plt.yticks(np.arange(-0.5, 2.5, 0.5))
    plt.xlabel('$t$ [s]')
    plt.ylabel('$V(t)$ [V]')
    plt.legend(bbox_to_anchor = (0.5,-0.3), loc = 'center', ncol = 4,
               fontsize = 8, frameon = False)
    plt.show()
    fig.set_size_inches(w,h)
    fig.tight_layout()
    namepng = 'python_' + signal + '.png'
    namepdf = 'python_' + signal + '.pdf'
    fig.savefig(namepng,dpi = 600, bbox_inches = 'tight')
    fig.savefig(namepdf,bbox_inches ='tight')
    return sysH, sysN, sysZ

plotsignals(u, sysH, sysN, sysZ, 'señal')
