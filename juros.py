def decorator_imprimir(func):
    def wrapper(*args, **kargs):
        result = func(*args, **kargs)
        print("CAPITAL: ", args[0], " TAXA: ", args[1], " TEMPO:", args[2])
        print("RESULADO: ", result)
    return wrapper


@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo


juros_simples(1000, 5, 6)
