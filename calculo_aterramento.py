#Declarando as variavéis
import numpy as np
import math as mt
from math import log
from math import e

ro_A = 4225.48
ro_S = 3000
hs = 0.1
Rch = 1000
Lt = 328.5
A = 70
H = 0.6
k1 = 20
k2 = 1
Ig = 2549.34
D = 0.5
H = 0.6
n = 21
d = 0.008

#Calculo de corrente de curta duração
Icd = 0.116/(np.sqrt(0.5))
batata = Icd
print("Corrente de toque de curta duração é de:", batata)

#Calculo de Tensão de Toque 
Frd_1 = float(1-(ro_A/ro_S))
Frd_2 = (2*hs)+0.106
Frd_final = 1-0.106*(Frd_1/Frd_2)
Cs = float(Frd_final)
Etcd = (Rch+(1.5*Cs*ro_S))*Icd
print("Fator de redução é de:",Cs)
print("Tensão de toque é de:",Etcd)

#Calculo de Rg 
etapa_1_rg = 1/Lt
etapa_2_rg = 1/ np.sqrt(20* A)
etapa_3_rg = H*(np.sqrt(20*A))
etapa_4_rg = 1/(1+(etapa_3_rg))
etapa_5_rg = 1 + etapa_4_rg

Rg = ro_A*((etapa_1_rg+etapa_2_rg)*etapa_5_rg)

print("Rg é igual a:",Rg)

#Tensão de Passo Ep
Ep = (Rch+6*Cs*ro_S)*Icd
print("Tensão de passo é igual a:",Ep)


#Calculo do Km
etapa_1_KM = 1/(2*np.pi)
etapa_2_KM = np.square(D)/(16*H*d)
etapa_3_KM = np.square(D+(2*H))
etapa_4_KM = 8*D*d
etapa_5_KM = etapa_3_KM/etapa_4_KM
etapa_6_KM = H/(4*d)
etapa_7_KM = mt.log(etapa_2_KM+etapa_5_KM-etapa_6_KM)
etapa_8_KM = ((2*n)**(2/n))/np.sqrt(1+H)
etapa_9_KM = 8/(np.pi*(2*n-1))
etapa_10_KM = mt.log(etapa_9_KM)
etapa_11_KM = etapa_1_KM * (etapa_7_KM + (etapa_8_KM * etapa_10_KM))
Km = etapa_11_KM
print("O valor de Km é:", Km)

#Calculo do Ki
Ki = 0.65 + 0.172 * n
print("O valor de Ki é:", Ki)

#Calculo do Vt
Vt = ro_A* Ig * Km * Ki/Lt
print("O valor de Vt é:", Vt)

#Calculo do Ks
etapa_1_Ks = 1/np.pi
etapa_2_Ks = 1/(2*H)
etapa_3_Ks = 1/(D+H)
etapa_4_Ks = 1/D
etapa_5_Ks = 1-(0.5**(n-2))
Ks = etapa_1_Ks*(etapa_2_Ks + etapa_3_Ks + (etapa_4_Ks * etapa_5_Ks))
print("O valor de Ks é:",Ks)

#Calculo do Vp
Vp = ro_A * Ig * Ks * Ki/Lt
print("O valor de Vp é de:",Vp)
