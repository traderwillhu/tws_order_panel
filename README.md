# IB TWS Order Panel

A simple Python GUI application to place different types of stock orders (Market + 3 Stops, 3 Stops Only, Limit, Stop, Market + 1 Stop) via Interactive Brokers TWS using `ib_insync`.

---

## Features

- Connects to Interactive Brokers TWS 
- Place stock orders (Market + 3 Stops, 3 Stops Only, Limit, Stop, Market + 1 Stop)
- Support for order actions: Buy and Sell (Short)
- Modern dark-themed GUI with Tkinter and ttk
- Easy to customize order parameters: ticker, quantity, prices, order type

---

## Requirements

- Python 3.7+
- [ib_insync](https://github.com/erdewit/ib_insync) library
- Interactive Brokers TWS or IB Gateway running and API enabled
- tkinter (usually included with Python)


You can change the port according to the environment in which you want to use the panel. The default in the file is Paper trading 7497.

| Environment     | Default Port | Description        |
|-----------------|--------------|--------------------|
| TWS Paper       | 7497         | Paper Trading      |
| TWS Live        | 7496         | Live Trading       |
| IB Gateway      | 4001         | Typically for automated live trading |
