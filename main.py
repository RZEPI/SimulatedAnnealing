import Annealing
from Gradient import Gradient

def f(x1,x2):
    # R1 = np.sqrt(0.3*(x1+3)**2 + (x2+4)**2)
    # R2 = np.sqrt(0.2*(x1-7)**2 + (x2-6)**2)
    # R3 = np.sqrt(0.2*(x1-7)**2 + 0.5*(x2-6)**2)
    # R4 = np.sqrt(0.7*(x1+7)**2 + 2*(x2-6)**2)
    # R5 = np.sqrt(0.2*(x1+3)**2 + 0.05*(x2+5)**4)


    # y = np.sin(x1*3)/(abs(x1)+1) + np.sin(x2*5-1)/(abs(x2/2-1)+1) + ((x1-5)**2+(x2-5)**2)/50 +4*np.sin(R1)/R1 + 4*np.sin(R2)/R2 - 3*np.sin(R4)/R4 - 3*np.sin(R5)/R5;
    # return y
    return 4*x1**2 - 3*x1*x2+2*x2**2
    #return (1-(x1**2+x2**3))*np.exp(-(x1**2+x2**2)/2)

def diff_f(x1, x2):
    return (8*x1 - 3*x2, 4*x2 - 3*x1)

annealing = Annealing.Annealing(f, 1000)
annealing.start()
gradient = Gradient(f, diff_f, 1000)
gradient.start()
ann_res = annealing.get_results()
grad_res = gradient.get_results()

if(len(ann_res) < len(grad_res)):
    print(f"Annealing method was faster and ended in \
          {len(ann_res)} iterations\nWhen gradient method ended in {len(grad_res)} iterations")
elif len(ann_res) > len(grad_res):
    print(f"Gradient method was faster and ended in \
          {len(grad_res)} iterations\nWhen annealing method ended in {len(ann_res)} iterations")
else:
    print(f"Both methods ended in {len(grad_res)} iterations")

print(f"Last result for Simulated Annealing is {ann_res[-1]}")
print(f"Last result for Gradient is {grad_res[-1]}")