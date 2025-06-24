# Disclaimer
This application is intended for educational and informational purposes only. It is provided "as is" without warranty of any kind. Use of this tool for live trading is entirely at your own risk.
Trading in financial markets involves substantial risk. You may lose all or more than your initial investment. This tool does not guarantee execution, profitability, or freedom from bugs and errors.
Before using this tool in a live trading environment, it is strongly recommended to test thoroughly in a paper trading account.
The developer is not liable for any losses, damages, or errors arising from the use of this software.
This application is not affiliated with, endorsed by, or supported by Interactive Brokers.

---

# IB TWS Order Panel

A simple Python GUI application to place different types of stock orders (Market + 3 Stops, 3 Stops Only, Limit, Stop, Market + 1 Stop, Market order) via Interactive Brokers TWS or IB Gateway using `ib_insync`.

---

## Features

- Connects to Interactive Brokers TWS or IB Gateway
- Place stock orders (Market + 3 Stops, 3 Stops Only, Limit, Stop, Market + 1 Stop, Market)
- Support for order actions: Buy and Sell (Short)
- Modern dark-themed GUI with Tkinter and ttk
- Easy to customize order parameters: ticker, quantity, prices, order type

---

## Requirements

- Python 3.7+
- [ib_insync](https://github.com/erdewit/ib_insync) library
- Interactive Brokers TWS or IB Gateway running and API enabled
- tkinter (usually included with Python)

---


## Port modification
You can adjust the port based on the environment in which you intend to use the panel. By default, the script is configured for paper trading using port 7497.

| Environment     | Default Port | Description        |
|-----------------|--------------|--------------------|
| TWS Paper       | 7497         | Paper Trading      |
| TWS Live        | 7496         | Live Trading       |
| IB Gateway      | 4001         | Typically for automated live trading |

---


## Usage
Open your IB TWS first.
Make sure your IB TWS is running with API enabled and listening on the correct port (default 7497 for paper trading, 7496 for live).
Fill in the ticker symbol, quantity, entry price, stop price, select Buy or Sell, choose the order type, and click Place Order.
You can also make it as an executable.
Before live trading, you would better try it in paper trading account.

![image](https://github.com/user-attachments/assets/87be72cf-0033-4bc7-bab5-8ad5926862d9)

---

## Exe. File
If you are not familiar with Python or related tools, the easiest way to use this application is to simply download and run the pre-built .exe file.
However, please be aware that .exe files are often flagged as high-risk by antivirus software or Windows SmartScreen. This is a normal reaction to unsigned executables distributed over the internet.
You should only run the file if you trust the source and understand the risks.
Alternatively, you can run the Python script directly from source after reviewing the code.
https://drive.google.com/drive/folders/1EkSJ7_YFlDAHdHhOz2n_JhGhsMcVxLEI?usp=drive_link


---

## Contact Me
https://x.com/traderwillhu

---

## Buy me a coffee
![image](https://github.com/user-attachments/assets/19d06efa-0b06-4195-843a-b9a6c10f8675)

You can support by buying a coffee ☕️ here —
[buymeacoffee.com/willhu 
](https://buymeacoffee.com/willhu)
