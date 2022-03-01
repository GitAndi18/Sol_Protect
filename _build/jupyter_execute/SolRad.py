#!/usr/bin/env python
# coding: utf-8

# # Solarstrahlung

# Mit folgender Gleichung lässt sich die pro m² und pro Wellenlängenintervall emittierte Strahlungsleistung eines schwarzen Körpers berechnen
# 
# $$
#     I(\lambda, T) = \frac{\lambda^{5}}{\mathrm{e}^{\lambda/T} + 1}
# $$

# ##### Übung 1: 
# Bevor man "click to show" drückt, schreibe man ein kleines Programm, 
# um den spektralen Verlauf der Schwarzkörperstrahlung zu berechnen und darzustellen. 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def SolRad(lam, T):
    h = 6.626e-34
    k = 1.38e-23
    c = 3e8
    return 2*np.pi*h*c**2/lam**5/(np.exp(h*c/(lam*T*k)) - 1)

lam = np.linspace(200, 2500, 2301)*1e-9
i  = SolRad(lam=lam, T=5800)
i2 = SolRad(lam=lam, T=3000)

plt.plot(lam, i, lam, i2)
plt.xlabel('$\lambda$ / /muem')
plt.ylabel('$I(\lambda, T)$ / (W/(m²nm)')
plt.grid()
plt.show()


# In[16]:


#Leistungsabgabe in den Bereichen uv (< 380 nm), vis (380 - 780 nm), nir (> 780 nm)
#Gesamt:
S_tot   = np.sum(i)*1e-9 * (1.32 / 2 / 146)**2 
S_uv    = np.sum(i[0:180])*1e-9/S_total
S_vis   = np.sum(i[180:580])*1e-9/S_total
S_nir   = np.sum(i[580:-1])*1e-9/S_total

df_B = pd.DataFrame(
    {" ":              ['Gesamt', 'f_UV', 'f_VIS', 'f_NIR'],
     "Boden":          [S_tot, S_uv, S_vis, S_nir],
    # "Dach" :          [U_D, q_D, U_Ds, q_Ds, q_D - q_Ds],
    # "Fassade":        [U_F, q_F, U_Fs, q_Fs, q_F - q_Fs],
    # "Fenster":        [U_W, q_W, U_Ws, q_Ws, q_W - q_Ws],
    # "Luftwechsel /h": [n, q_L, n_s, q_Ls, q_L - q_Ls],
    # "sol G" :         ['', -q_sol, '', -q_sols, -q_sol + q_sols],
    # "int G" :         ['', -q_int, '', -q_int, 0],
    # "gesamt":         ['', q_ges, '', qs_ges, q_ges - qs_ges]
    })
df_B
print(S_uv, S_vis, S_nir, S_uv + S_vis + S_nir)


# In[27]:


from IPython.display import Image
Image("fish.png")


# Some content {doc}`and here is my role's content! <intro>`
# #Näheres erfahren sie in {doc}`SolRad`

# In[24]:


lam


# In[29]:


2*3.14*0.5*0.04*0.03*750

