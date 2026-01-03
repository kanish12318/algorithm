def kanish__pairs(n):
    steps=0
    for i in range(n):

        for j in range(n):
            steps+=1
    return steps
def single_loop(n):
    steps=0
    for i in range(n):
        
    
        steps+=1
    return steps
print("n\t0(n)\t0(n^2)")
print("-"*25)
for n in[10,20,5,26,48,18]:
 linear__steps=single_loop(n)
 quadratic_steps=kanish__pairs(n)
 print(f"{n}\t{linear__steps}\t{quadratic_steps}")