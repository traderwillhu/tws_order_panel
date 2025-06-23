import tkinter as tk
from tkinter import ttk, messagebox
from ib_insync import *

# ========== Connect to TWS ==========
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

# ========== Order Function ==========
def submit_order():
    try:
        ticker = entry_ticker.get().strip().upper()
        qty = int(entry_qty.get())
        user_stop_price = float(entry_stop.get())
        user_entry_price = float(entry_entry.get())
        action = action_var.get()
        order_type = order_type_var.get()

        contract = Stock(ticker, 'SMART', 'USD')
        ib.qualifyContracts(contract)

        if order_type == 'Market + 3 Stops':
            market_order = MarketOrder(action, qty)
            trade = ib.placeOrder(contract, market_order)
            while trade.isActive():
                ib.sleep(1)

            if trade.orderStatus.status != 'Filled':
                messagebox.showerror("Order Error", "Market order was not filled.")
                return

            avg_fill_price = trade.orderStatus.avgFillPrice
            price_diff = avg_fill_price - user_stop_price if action == 'BUY' else user_stop_price - avg_fill_price

            stop_prices = [
                round(user_stop_price + price_diff * 2 / 3, 2) if action == 'BUY' else round(user_stop_price - price_diff * 2 / 3, 2),
                round(user_stop_price + price_diff * 1 / 3, 2) if action == 'BUY' else round(user_stop_price - price_diff * 1 / 3, 2),
                round(user_stop_price, 2)
            ]
            stop_sizes = [qty // 3, qty // 3, qty - 2 * (qty // 3)]

            for stop_price, stop_qty in zip(stop_prices, stop_sizes):
                stop_order = StopOrder('SELL' if action == 'BUY' else 'BUY', stop_qty, stop_price, tif='GTC')
                ib.placeOrder(contract, stop_order)
                ib.sleep(0.5)

            messagebox.showinfo("Success",
                                f"{action} {qty} shares of {ticker} at ${avg_fill_price:.2f}.\n"
                                f"3 stop-loss orders submitted.")

        elif order_type == '3 Stops Only':
            price_diff = user_entry_price - user_stop_price if action == 'BUY' else user_stop_price - user_entry_price
            stop_prices = [
                round(user_stop_price + price_diff * 2 / 3, 2) if action == 'BUY' else round(user_stop_price - price_diff * 2 / 3, 2),
                round(user_stop_price + price_diff * 1 / 3, 2) if action == 'BUY' else round(user_stop_price - price_diff * 1 / 3, 2),
                round(user_stop_price, 2)
            ]
            stop_sizes = [qty // 3, qty // 3, qty - 2 * (qty // 3)]

            for stop_price, stop_qty in zip(stop_prices, stop_sizes):
                stop_order = StopOrder('SELL' if action == 'BUY' else 'BUY', stop_qty, stop_price, tif='GTC')
                ib.placeOrder(contract, stop_order)
                ib.sleep(0.5)

            messagebox.showinfo("Success",
                                f"3 stop-loss orders for {qty} shares of {ticker} submitted.")

        elif order_type == 'Limit Order':
            limit_price = float(entry_entry.get())
            order = LimitOrder(action, qty, limit_price)
            ib.placeOrder(contract, order)
            messagebox.showinfo("Success",
                                f"Limit order to {action} {qty} shares of {ticker} at ${limit_price:.2f} submitted.")

        elif order_type == 'Stop Order':
            stop_price = float(entry_stop.get())
            order = StopOrder(action, qty, stop_price)
            ib.placeOrder(contract, order)
            messagebox.showinfo("Success",
                                f"Stop order to {action} {qty} shares of {ticker} at stop ${stop_price:.2f} submitted.")

        elif order_type == 'Market + 1 Stop':
            market_order = MarketOrder(action, qty)
            trade = ib.placeOrder(contract, market_order)
            while trade.isActive():
                ib.sleep(1)

            if trade.orderStatus.status != 'Filled':
                messagebox.showerror("Order Error", "Market order was not filled.")
                return

            avg_fill_price = trade.orderStatus.avgFillPrice
            stop_order = StopOrder('SELL' if action == 'BUY' else 'BUY', qty, user_stop_price, tif='GTC')
            ib.placeOrder(contract, stop_order)

            messagebox.showinfo("Success",
                                f"{action} {qty} shares of {ticker} at ${avg_fill_price:.2f}.\n"
                                f"1 stop-loss order submitted at ${user_stop_price:.2f}.")

        else:
            messagebox.showerror("Error", "Unknown order type selected.")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ========== GUI Setup ==========
root = tk.Tk()
root.title("IB TWS Order Panel")
root.geometry("540x600")
root.configure(bg="#2E3440", padx=25, pady=25)

style = ttk.Style(root)
style.theme_use("clam")

# Fonts
FONT_LARGE = ("Segoe UI", 14)
FONT_TITLE = ("Segoe UI", 20, "bold")

# Colors
bg_color = "#2E3440"
fg_color = "#D8DEE9"
accent_color = "#88C0D0"
button_color = "#5E81AC"
entry_bg = "#3B4252"

# Style Configs
style.configure("TLabel", background=bg_color, foreground=fg_color, font=FONT_LARGE)
style.configure("TButton", background=button_color, foreground="white", font=("Segoe UI", 14, "bold"))
style.map("TButton", foreground=[('active', 'white')], background=[('active', '#81A1C1')])
style.configure("TEntry", fieldbackground=entry_bg, foreground=fg_color, font=FONT_LARGE)

# Title
title_label = ttk.Label(root, text="IB TWS Order Panel", font=FONT_TITLE)
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30))

# Input Helper
def add_input(label_text, default_val, row):
    ttk.Label(root, text=label_text).grid(row=row, column=0, sticky="e", pady=10, padx=(0,10))
    entry = ttk.Entry(root, font=FONT_LARGE)
    entry.insert(0, default_val)
    entry.grid(row=row, column=1, sticky="ew", pady=10)
    return entry

entry_ticker = add_input("Ticker Symbol:", "AAPL", 1)
entry_qty = add_input("Order Quantity:", "99", 2)
entry_entry = add_input("Entry Price:", "200", 3)
entry_stop = add_input("Stop Price:", "190", 4)

# Action Selection
action_var = tk.StringVar(value='BUY')
ttk.Label(root, text="Action:").grid(row=5, column=0, sticky="e", pady=10, padx=(0,10))
action_frame = ttk.Frame(root)
action_frame.grid(row=5, column=1, sticky="w", pady=10)
style.configure("TRadiobutton", font=("Segoe UI", 14))
ttk.Radiobutton(action_frame, text="Buy", variable=action_var, value='BUY', style="TRadiobutton").pack(side="left", padx=15)
ttk.Radiobutton(action_frame, text="Sell (Short)", variable=action_var, value='SELL', style="TRadiobutton").pack(side="left", padx=15)

# Order Type
order_type_var = tk.StringVar(value='Market + 3 Stops')
ttk.Label(root, text="Order Type:").grid(row=6, column=0, sticky="e", pady=10, padx=(0,10))
order_type_combo = ttk.Combobox(root, textvariable=order_type_var, state='readonly',
                                values=['Market + 3 Stops', '3 Stops Only', 'Limit Order', 'Stop Order', 'Market + 1 Stop'],
                                font=FONT_LARGE)
order_type_combo.grid(row=6, column=1, sticky="ew", pady=10)

# Submit Button
submit_btn = ttk.Button(root, text="Place Order", command=submit_order)
submit_btn.grid(row=7, column=0, columnspan=2, pady=40, ipadx=20, ipady=10)

root.grid_columnconfigure(1, weight=1)
root.mainloop()

# ========== Disconnect ==========
ib.disconnect()
