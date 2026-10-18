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


class First:

    def __init__(self, root):
        self.root = root
        self.root.title("Parcel Delivery Management System")
        self.root.geometry("550x400")
        self.root.resizable(False, False)

        self.f = Frame(root, height=380, width=520)
        self.f.pack(padx=15, pady=15)

        Label(
            self.f,
            text="PARCEL DELIVERY MANAGEMENT",
            font=("Arial", 14, "bold")
        ).place(x=65, y=10)

        Label(self.f, text="Product ID:").place(x=50, y=70)
        Label(self.f, text="Weight (kg):").place(x=50, y=110)
        Label(self.f, text="Category:").place(x=50, y=150)
        Label(self.f, text="Description:").place(x=50, y=190)

        self.e1 = Entry(self.f, width=28)
        self.e2 = Entry(self.f, width=28)
        self.e3 = Entry(self.f, width=28)
        self.e4 = Entry(self.f, width=28)

        self.e1.place(x=180, y=70)
        self.e2.place(x=180, y=110)
        self.e3.place(x=180, y=150)
        self.e4.place(x=180, y=190)

        Button(
            self.f, text="Insert", width=10,
            command=self.insert
        ).place(x=35, y=250)

        Button(
            self.f, text="Update", width=10,
            command=self.update
        ).place(x=140, y=250)

        Button(
            self.f, text="Delete", width=10,
            command=self.delete
        ).place(x=245, y=250)

        Button(
            self.f, text="Clear", width=10,
            command=self.clear
        ).place(x=350, y=250)

        Button(
            self.f, text="View Products", width=15,
            command=self.open_view
        ).place(x=175, y=300)

    def get_values(self):
        p_id = int(self.e1.get())
        p_wt = float(self.e2.get())
        p_cat = self.e3.get().strip()
        p_des = self.e4.get().strip()

        if p_wt <= 0 or not p_cat or not p_des:
            raise ValueError(
                "Enter a positive weight, category and description."
            )

        return p_id, p_wt, p_cat, p_des

    def insert(self):
        try:
            values = self.get_values()

            cursor.execute(
                """INSERT INTO Product (p_id, p_wt, p_cat, p_des)
                   VALUES (%s, %s, %s, %s)""",
                values
            )
            conn.commit()

            messagebox.showinfo(
                "Success", "Product inserted successfully!"
            )
            self.clear()

        except ValueError as err:
            messagebox.showerror("Input Error", str(err))
        except mysql.connector.Error as err:
            conn.rollback()
            messagebox.showerror("Database Error", str(err))

    def update(self):
        try:
            p_id, p_wt, p_cat, p_des = self.get_values()

            cursor.execute(
                """UPDATE Product
                   SET p_wt=%s, p_cat=%s, p_des=%s
                   WHERE p_id=%s""",
                (p_wt, p_cat, p_des, p_id)
            )
            conn.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo(
                    "Success", "Product updated successfully!"
                )
            else:
                messagebox.showwarning(
                    "Not Found", "Product ID not found or values unchanged."
                )

        except ValueError as err:
            messagebox.showerror("Input Error", str(err))
        except mysql.connector.Error as err:
            conn.rollback()
            messagebox.showerror("Database Error", str(err))

    def delete(self):
        try:
            p_id = int(self.e1.get())

            if not messagebox.askyesno(
                "Confirm Delete",
                f"Delete product with ID {p_id}?"
            ):
                return

            cursor.execute(
                "DELETE FROM Product WHERE p_id=%s",
                (p_id,)
            )
            conn.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo(
                    "Success", "Product deleted successfully!"
                )
                self.clear()
            else:
                messagebox.showwarning(
                    "Not Found", "Product ID not found."
                )

        except ValueError:
            messagebox.showerror(
                "Input Error", "Enter a valid integer Product ID."
            )
        except mysql.connector.Error as err:
            conn.rollback()
            messagebox.showerror(
                "Database Error",
                "Could not delete the product. It may be referenced "
                "by another table.\n\n" + str(err)
            )

    def clear(self):
        for entry in (self.e1, self.e2, self.e3, self.e4):
            entry.delete(0, END)

    def open_view(self):
        import subprocess
        import sys
        from pathlib import Path

        subprocess.Popen([
            sys.executable,
            str(Path(__file__).with_name("next_win.py"))
        ])


root = Tk()
obj = First(root)


def close_app():
    if conn.is_connected():
        cursor.close()
        conn.close()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", close_app)
root.mainloop()
