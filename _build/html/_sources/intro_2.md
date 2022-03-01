# Motivation

Der Sonnneschutz für Gebäude ist sehr wichtig für Behaglichkeit und Klimaschutz.

:::{note}
Here is a note!
:::

And here is a code block:

```
import numpy as np
import matplotlib.pyplot as plt

def SolRad(lam, T):
    return lam**5*1/(np.exp(lam/T) + 1)

lam = np.linspace(300, 3000, 100)
i  = SolRad(lam=lam, T=5800)

plt.plot(lam, i)
```

Check out the content pages bundled with this sample book to see more.
