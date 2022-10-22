import numpy as np
X = np.array(([20.0,10.0],[80.0, 60.0],[-20.0, 10.0])) #amostras 
D = np.array(([0.0,1.0,1.0])) #Saida desejada 
W = np.array([0.1, 0.1, 0.1]) #pesos 
n = 0.1 # taxa de aprendizado
bias = 1 
epocas = 0

def funcaoDegrau(soma):
    if soma <= 0:
        return 0
    else:
        return 1

def perceptron(X, D, W):

    for i in range(0, len(X)):
        y = np.sun(X[i]*W) +(bias*n)
        saida = funcaoDegrau(y)
        erro = D[i] - saida

        #Atualizar pesos 
        for j in range(0, len(W)):
            W[j] = W[j] + n*erro*X[i][j]
            print(W[j])

    epocas += 1
    print(epocas)

while(True):
    perceptron(X, D, W)
