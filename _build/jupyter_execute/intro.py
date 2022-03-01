#!/usr/bin/env python
# coding: utf-8

# # Motivation
# 
# Der Sonnneschutz für Gebäude ist sehr wichtig für Behaglichkeit und Klimaschutz.
# 
# Tolle Info finden sie hier {cite}`bellia2014overview` und hier {cite}`lampert1998smart`
# 
# # Markdown content is written as regular markdown
# 
# Here is a note!
# 
# (label-name)=
# ## Execute Markdown
# 
#     print("Here is some code to execute")
# 
# ``` {code-cell}
# ---
# render:
#   image:
#     width: 200px
#     alt: fun-fish
#     classes: shadow bg-primary
#   figure:
#     caption: |
#       Hey everyone its **party** time!
#     name: fish
# ---
# from IPython.display import Image
# Image("fish.png")
# ```
# 
#     Some content {SolRad}`and here is my role's content!`
# 
# Näheres erfahren sie in {doc}`SolRad`
# 
# And here is a code block:

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

def SolRad(lam, T):
    return lam**5*1/(np.exp(lam/T) + 1)

lam = np.linspace(300, 3000, 100)
i  = SolRad(lam=lam, T=5800)

plt.plot(lam, i)

