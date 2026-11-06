def FormularioVentas(Nombre_emprendimiento, Capacidad, VentasHechas,PrecioUnitario):
    Formulario = {
        "Nombre del emprendimiento": Nombre_emprendimiento,
        "Stock": Capacidad,
        "VentasRealizadasCantidad": VentasHechas,
        "StockVendido (Bs)": VentasHechas * PrecioUnitario,
        "StockRestante (Bs)": Capacidad - VentasHechas,
        "Ganancias (Bs)": VentasHechas * PrecioUnitario,
    }
    return Formulario
