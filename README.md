# IB TWS Order Panel

A simple Python GUI application to place different types of stock orders (market, limit, stop, bracket) via Interactive Brokers TWS using `ib_insync`.

---

## Features

- Connects to Interactive Brokers TWS or IB Gateway API
- Place Market, Limit, Stop, and Bracket orders with multiple stop-loss orders
- Support for order actions: Buy and Sell (Short)
- Modern dark-themed GUI with Tkinter and ttk
- Easy to customize order parameters: ticker, quantity, prices, order type

---

## Requirements

- Python 3.7+
- [ib_insync](https://github.com/erdewit/ib_insync) library
- Interactive Brokers TWS or IB Gateway running and API enabled
- tkinter (usually included with Python)
