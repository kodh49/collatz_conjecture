import numpy as np
from numpy.core.fromnumeric import ndim
import matplotlib.pyplot as plt

rmax = 10
rngvals = np.linspace(2, rmax, rmax-1, endpoint=True)
print(rngvals)

# Return the progress(steps and respective values) in 2D list
def collatz(num):
    step = 0
    x = [step]
    y = [num]
    # How Collatz Conjecture works
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num*3+1
        step += 1
        x.append(step)
        y.append(num)
    return [x, y]


# Graph the result
fig, ax = plt.subplots()
for i in rngvals:
    colz = collatz(i)
    ax.plot(colz[0], colz[1])

ax.grid()

ax.set(xlabel="Steps Taken (times)", ylabel="Number",
       title="Behavior of Collatz Number")
plt.show()
