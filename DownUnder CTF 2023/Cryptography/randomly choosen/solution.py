import random

for i in range(0, 1337):
    #Generate 0-60 numbers array
    x = []
    for n in range(0, 61):
        x.append(str(n))
        
    #Generate Combinations
    random.seed(i)
    print(i)
    out = (random.choices(x, k=61*5))
    #print(out)
    #print()

    #Reconstruction *wanna die :'( *
    reconstruction = []
    flag = open('output.txt', 'r').read().strip()
        #Generate list
    for w in range(len(x)):
        reconstruction.append(0)

    #print(reconstruction, len(reconstruction))

    for k in range(61*5):
        reconstruction[int(out[k])] = flag[k]
    
    try:
        toget = "".join(reconstruction)
        print(toget)

        if "DUCTF" in toget:
            break
        
    except TypeError:
        print("Ignore ", str(i))
