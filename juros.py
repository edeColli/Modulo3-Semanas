def decorator_imprimir(func):
    def interno(*args, **kargs):
        result = func(*args, **kargs)
        print("CAPITAL: ", args[0], " TAXA: ", args[1], " TEMPO:", args[2])
        print("RESULADO: ", result)
    return interno


@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo


juros_simples(1000, 5, 6)
