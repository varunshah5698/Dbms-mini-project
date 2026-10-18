from tkinter import *
from tkinter import messagebox
import mysql.connector

try:
    conn = mysql.connector.connect(
        user="root",
        password="Mysql@123",
        host="localhost",
        database="ParcelDeliveryDB"
    )
    cursor = conn.cursor()
except mysql.connector.Error as err:
    messagebox.showerror("Database Error", str(err))
    raise SystemExit


class Next:

    def __init__(self, root):
        self.root = root
        self.root.title("Parcel Delivery - View Products")
        self.root.geometry("850x450")

        Label(
            root,
            text="PARCEL DELIVERY MANAGEMENT SYSTEM",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        Button(
            root,
            text="Show Products",
            width=15,
            command=self.display
        ).pack(pady=10)

        self.table = Frame(root)
        self.table.pack(fill=BOTH, expand=True, padx=10, pady=10)

    def display(self):
        for widget in self.table.winfo_children():
            widget.destroy()

        try:
            cursor.execute(
                "SELECT p_id, p_wt, p_cat, p_des FROM Product LIMIT 10"
            )
            records = cursor.fetchall()

            headings = [
                "Product ID",
                "Weight (kg)",
                "Category",
                "Description"
            ]

            for j, heading in enumerate(headings):
                Label(
                    self.table,
                    text=heading,
                    font=("Arial", 10, "bold"),
                    bg="lightblue",
                    relief="solid",
                    width=22,
                    padx=5,
                    pady=5
                ).grid(row=0, column=j, sticky="nsew")

            if not records:
                Label(
                    self.table,
                    text="No product records found."
                ).grid(row=1, column=0, columnspan=4, pady=10)
                return

            for i, record in enumerate(records, start=1):
                for j, value in enumerate(record):
                    Label(
                        self.table,
                        text=value,
                        relief="solid",
                        width=22,
                        padx=5,
                        pady=5,
                        anchor="w"
                    ).grid(row=i, column=j, sticky="nsew")

            for j in range(4):
                self.table.grid_columnconfigure(j, weight=1)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))


root = Tk()
obj = Next(root)


def close_app():
    if conn.is_connected():
        cursor.close()
        conn.close()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", close_app)
root.mainloop()
 
