def validate_city(data):
    cities = ('São Paulo', 'Jaú', 'Florianópolis')
    ceps = ('04117-091', '02248-001', '88035-350')
    cep_city = dict(zip(ceps, cities))
    city = data['localidade']
    cep = data['cep']
    if cep == '04117-091' and city == cep_city[cep]:
        return True
    if cep == '02248-001' and city == cep_city[cep]:
        return True
    if cep == '88035-350' and city == cep_city[cep]:
        return True
    else:
        return False
