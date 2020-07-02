def verificador (ru):
    acum = 0
    multiplicador = 2
    
    for i in range ((len(ru))-1, -1,-1):
        acum += int(ru[i]) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    if 11 - acum % 11 < 10:
        return (11 - acum % 11)
    elif 11 - acum % 11 == 10:
        return ("K")
    else: 
        return (0)