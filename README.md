# 📈 Portfolio Rebalancer (Stock & Portfolio Simulator)

Este proyecto implementa una simulación sencilla de un portafolio de
inversiones con acciones, permitiendo:

-   Comprar y vender acciones
-   Calcular el valor total del portafolio
-   Definir una asignación objetivo (target allocation)
-   Rebalancear automáticamente el portafolio según porcentajes deseados

El objetivo principal es demostrar cómo un portafolio puede ajustarse
dinámicamente para mantener una distribución específica de activos.

------------------------------------------------------------------------

## 🚀 Funcionalidades

### ✅ Clase `Stock`

Representa una acción individual con:

-   Nombre (ticker)
-   Precio actual

#### Métodos principales:

-   `update_price(new_price)`: actualiza el precio
-   `__str__()`: imprime información legible de la acción

Ejemplo:

``` python
stock_a = Stock("AAPL", 150.00)
```

------------------------------------------------------------------------

### ✅ Clase `Portafolio`

Representa un portafolio con:

-   Caja disponible (`cash`)
-   Acciones mantenidas (`stocks`)
-   Asignación objetivo (`allocation`)

------------------------------------------------------------------------

## 💰 Operaciones disponibles

### Comprar acciones

``` python
portfolio.buy_stock(stock_a, 10)
```

Verifica si hay suficiente caja antes de comprar.

------------------------------------------------------------------------

### Vender acciones

``` python
portfolio.sell_stock(stock_a, 5)
```

Aumenta el efectivo disponible en el portafolio.

------------------------------------------------------------------------

### Valor total del portafolio

Incluye:

-   Caja disponible\
-   Valor de todas las acciones

``` python
portfolio.total_value()
```

------------------------------------------------------------------------

## 🎯 Rebalanceo Automático

Una de las partes centrales del proyecto es el método:

``` python
portfolio.rebalance()
```

Este proceso realiza:

1.  Cálculo de diferencias entre el valor actual y el valor objetivo
2.  Generación de órdenes de compra y venta necesarias
3.  Ejecución ordenada de trades

------------------------------------------------------------------------

### 📌 Importante: Primero vender, luego comprar

El rebalanceo se ejecuta en dos pasos:

1.  **Primero se venden acciones que están sobre-ponderadas**
2.  **Luego se compran acciones sub-ponderadas**

Esto se hizo intencionalmente para asegurar que el portafolio tenga
suficiente caja antes de intentar compras.

``` python
def execute_trades(self, sell_actions, buy_actions):
    # first sell stocks that are over the target allocation
    ...

    # then buy stocks that are under the target allocation
    ...
```

✅ Esta estrategia evita errores de liquidez cuando el portafolio está
completamente invertido.

------------------------------------------------------------------------

## 🧪 Ejemplo de uso

El bloque principal crea 3 acciones:

-   AAPL
-   GOOGL
-   AMZN

Luego:

-   Se crea un portafolio con $10,000
-   Se define una asignación objetivo
-   Se rebalancea automáticamente

``` python
portfolio.set_allocation({
    stock_a: 0.5,
    stock_b: 0.3,
    stock_c: 0.2
})

portfolio.rebalance()
print(portfolio)
```

------------------------------------------------------------------------

## 📌 Output esperado

El programa imprimirá transacciones como:

    Bought 33.33 of AAPL for $5000.00
    Bought 1.07 of GOOGL for $3000.00
    Bought 0.59 of AMZN for $2000.00

Y luego el estado final del portafolio.

------------------------------------------------------------------------

## 🔧 Posibles mejoras futuras

-   Validar que no se vendan más acciones de las que se poseen
-   Permitir rebalanceo parcial si no hay suficiente caja
-   Agregar comisiones de trading
-   Manejar precios dinámicos en el tiempo
-   Mejorar el `__str__` del portafolio (actualmente imprime mal los
    stocks)



made with ❤️ by Cristóbal Pérez-Cotapos
