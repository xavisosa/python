def app():
    print('Bienvenidos')
    nobr_ap = "Xavier Sosa" #input('Ingresa tu Nombre y Apellido: ')
    print('Cliente:', nobr_ap)
    cod_vuelo = "AN0123456789COR2204112034" #input('Ingresa tu código de vuelo: ')
    print('Codigo vuelo:', cod_vuelo)
    aerolinea = cod_vuelo[0:2]
    nro_vuelo = cod_vuelo[2:12]
    ciudad_dest = cod_vuelo[12:15]
    fh_vuelo = cod_vuelo[15:21]
    hr_vuelo = cod_vuelo[21:25]

    print('Aerolinea:', format_aerolinea(aerolinea))
    print('Número de Vuelo:', nro_vuelo)

    if (ciudad_dest == 'BAS'):
        print('Buenos Aires ')

    print('Ciudad de Destino:', ciudad_dest)
    print('Fecha:', fh_vuelo)
    print('Hora:', hr_vuelo)

def format_aerolinea(aero):
    if (aero == 'AA'):
        return 'Aerolineas Argentinas ✈😎'
    elif (aero == 'FB'):
        return 'Fly Bondi ✈🚌'
    elif (aero == 'AN'):
        return 'Aerolineas Andes ✈🗻'
    else:
        return 'Aerolinea desconocida 😅'

if __name__ == "__main__":
    app()