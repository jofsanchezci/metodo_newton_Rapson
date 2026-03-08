def raiz_cuadrada(a, tolerancia=1e-10, max_iter=1000):
    x = a / 2  # estimación inicial
    
    for i in range(max_iter):
        x_nuevo = 0.5 * (x + a / x)
        
        if abs(x_nuevo - x) < tolerancia:
            return x_nuevo
        
        x = x_nuevo
    
    return x

numero = 144
resultado = raiz_cuadrada(numero)
print("Raíz aproximada:", resultado)