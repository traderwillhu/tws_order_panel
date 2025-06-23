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


## Port modification
You can adjust the port based on the environment in which you intend to use the panel. By default, the script is configured for paper trading using port 7497.

| Environment     | Default Port | Description        |
|-----------------|--------------|--------------------|
| TWS Paper       | 7497         | Paper Trading      |
| TWS Live        | 7496         | Live Trading       |
| IB Gateway      | 4001         | Typically for automated live trading |


## Usage
Open your IB TWS first.
Make sure your IB TWS is running with API enabled and listening on the correct port (default 7497 for paper trading, 7496 for live).
Fill in the ticker symbol, quantity, entry price, stop price, select Buy or Sell, choose the order type, and click Place Order.
You can also make it as an executable.

![image](https://github.com/user-attachments/assets/87be72cf-0033-4bc7-bab5-8ad5926862d9)


## Contact Me
https://x.com/traderwillhu
