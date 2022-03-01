#!/usr/bin/env python
# coding: utf-8

# # Solarstrahlung - 2

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

def SolRad(lam, T):
    return lam**5*1/(np.exp(lam/T) + 1)

lam = np.linspace(300, 3000, 100)
i  = SolRad(lam=lam, T=5800)
plt.xlabel('\lambda')

plt.plot(lam, i)


# In[ ]:




