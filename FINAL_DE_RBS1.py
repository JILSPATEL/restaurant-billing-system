import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import random
import os, time, tempfile

import mysql.connector
from mysql.connector import Error


class Bill_App:
    def __init__(self, root: tb.Window):
        self.root = root
        self.root.title("Silver Heights Restaurant - Billing System")
        self.root.minsize(1200, 650)

        # ----------- variables -----------
        # Snacks
        self.samosa = tk.IntVar()
        self.idli = tk.IntVar()
        self.upma = tk.IntVar()
        self.dosa = tk.IntVar()
        self.puff = tk.IntVar()
        self.pakoda = tk.IntVar()
        self.poha = tk.IntVar()
        self.kachori = tk.IntVar()

        # Specialities
        self.dalfry = tk.IntVar()
        self.burger = tk.IntVar()
        self.sspsandwich = tk.IntVar()
        self.fries = tk.IntVar()
        self.sspnoodles = tk.IntVar()
        self.biryani = tk.IntVar()
        self.paneer_butter_masala = tk.IntVar()
        self.veg_handi = tk.IntVar()

        # Beverages
        self.tea = tk.IntVar()
        self.coffee = tk.IntVar()
        self.drinks = tk.IntVar()
        self.buttermilk = tk.IntVar()
        self.lassi = tk.IntVar()
        self.coco = tk.IntVar()
        self.masala_chaas = tk.IntVar()
        self.faluda = tk.IntVar()

        # Totals
        self.snacks_p = tk.StringVar()
        self.specialities_p = tk.StringVar()
        self.bevarages_p = tk.StringVar()
        self.gst = tk.StringVar()
        self.total_gst = 0.0
        self.item_bill = 0.0
        self.Total_bill = 0.0

        # customer
        self.c_name = tk.StringVar()
        self.c_phone = tk.StringVar()
        self.bill_no = tk.StringVar()
        self.t_no = tk.StringVar()
        self.search_bill = tk.StringVar()
        self.bill_no.set(str(random.randint(1000, 9999)))

        # theme state
        self.current_theme = "flatly"

        # db
        self.db_conn = None
        self.db_cursor = None

        # ----------- root layout grid -----------
        self.root.grid_rowconfigure(1, weight=1)   # middle row grows
        self.root.grid_columnconfigure(0, weight=1)

        # ----------- title bar with theme toggle -----------
        title_bar = tb.Frame(self.root, padding=(10, 5))
        title_bar.grid(row=0, column=0, sticky="ew")
        title_bar.grid_columnconfigure(0, weight=1)
        title_bar.grid_columnconfigure(1, weight=0)

        title = tb.Label(
            title_bar,
            text="Silver Heights Restaurant",
            font=("Times New Roman", 28, "bold"),
            anchor="w",
            bootstyle="inverse-primary",
            padding=(10, 5)
        )
        title.grid(row=0, column=0, sticky="w")

        self.theme_btn = tb.Button(
            title_bar,
            text="Dark Mode",
            bootstyle="secondary-outline",
            command=self.toggle_theme
        )
        self.theme_btn.grid(row=0, column=1, padx=10, sticky="e")

        # ----------- main content frame -----------
        main_frame = tb.Frame(self.root, padding=5)
        main_frame.grid(row=1, column=0, sticky="nsew")
        main_frame.grid_rowconfigure(1, weight=1)  # row with 4 panels grows
        for c in range(4):
            # items columns slightly wider than bill column
            main_frame.grid_columnconfigure(c, weight=1 if c == 3 else 2)

        # ====== Customer details (row 0, spans all columns) ======
        self._build_customer_frame(main_frame)

        # ====== Left 3 panels + Bill area (row 1) ======
        snacks_frame = self._build_items_frame(main_frame, "Snacks")
        snacks_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        special_frame = self._build_items_frame(main_frame, "Specialities")
        special_frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        beverages_frame = self._build_items_frame(main_frame, "Beverages")
        beverages_frame.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

        self._populate_items(snacks_frame, special_frame, beverages_frame)

        bill_frame = self._build_bill_frame(main_frame)
        bill_frame.grid(row=1, column=3, sticky="nsew", padx=5, pady=5)

        # ====== Bottom button bar (row 2) ======
        button_frame = self._build_button_bar(self.root)
        button_frame.grid(row=2, column=0, sticky="ew", padx=5, pady=(0, 5))

        # setup db + welcome text
        self.setup_database()
        self.welcome_bill()

    # ------------------------------------------------------------------
    # THEME TOGGLE
    # ------------------------------------------------------------------
    def toggle_theme(self):
        if self.current_theme == "flatly":
            self.root.style.theme_use("darkly")
            self.current_theme = "darkly"
            self.theme_btn.configure(text="Light Mode")
        else:
            self.root.style.theme_use("flatly")
            self.current_theme = "flatly"
            self.theme_btn.configure(text="Dark Mode")

    # ------------------------------------------------------------------
    # UI BUILDERS
    # ------------------------------------------------------------------
    def _build_customer_frame(self, parent):
        frame = tb.Labelframe(
            parent,
            text="Customer Details",
            padding=8,
            bootstyle="primary"
        )
        frame.grid(row=0, column=0, columnspan=4, sticky="ew", padx=5, pady=(0, 5))
        for c in range(8):
            frame.grid_columnconfigure(c, weight=1)

        tb.Label(frame, text="Customer Name", font=("Times New Roman", 11, "bold")).grid(
            row=0, column=0, padx=5, pady=3, sticky="w"
        )
        tb.Entry(frame, textvariable=self.c_name, font=("Arial", 11)).grid(
            row=0, column=1, padx=5, pady=3, sticky="ew"
        )

        tb.Label(frame, text="Phone No.", font=("Times New Roman", 11, "bold")).grid(
            row=0, column=2, padx=5, pady=3, sticky="w"
        )
        tb.Entry(frame, textvariable=self.c_phone, font=("Arial", 11)).grid(
            row=0, column=3, padx=5, pady=3, sticky="ew"
        )

        tb.Label(frame, text="Bill Number", font=("Times New Roman", 11, "bold")).grid(
            row=0, column=4, padx=5, pady=3, sticky="w"
        )
        tb.Entry(frame, textvariable=self.bill_no, font=("Arial", 11), state="readonly").grid(
            row=0, column=5, padx=5, pady=3, sticky="ew"
        )

        tb.Label(frame, text="Table Number", font=("Times New Roman", 11, "bold")).grid(
            row=0, column=6, padx=5, pady=3, sticky="w"
        )
        tb.Entry(frame, textvariable=self.t_no, font=("Arial", 11)).grid(
            row=0, column=7, padx=5, pady=3, sticky="ew"
        )

    def _build_items_frame(self, parent, title):
        frame = tb.Labelframe(
            parent,
            text=title,
            padding=8,
            bootstyle="info"
        )
        for r in range(8):
            frame.grid_rowconfigure(r, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        return frame

    def _create_item_row(self, parent, text, var, row):
        tb.Label(parent, text=text, font=("Times New Roman", 11, "bold")).grid(
            row=row, column=0, padx=5, pady=3, sticky="w"
        )
        tb.Entry(parent, textvariable=var, width=6, font=("Arial", 11)).grid(
            row=row, column=1, padx=5, pady=3, sticky="ew"
        )

    def _populate_items(self, snacks_frame, special_frame, beverages_frame):
        # Snacks
        self._create_item_row(snacks_frame, "Samosa", self.samosa, 0)
        self._create_item_row(snacks_frame, "Idli", self.idli, 1)
        self._create_item_row(snacks_frame, "Upma", self.upma, 2)
        self._create_item_row(snacks_frame, "Dosa", self.dosa, 3)
        self._create_item_row(snacks_frame, "Puff", self.puff, 4)
        self._create_item_row(snacks_frame, "Pakoda", self.pakoda, 5)
        self._create_item_row(snacks_frame, "Poha", self.poha, 6)
        self._create_item_row(snacks_frame, "Kachori", self.kachori, 7)

        # Specialities
        self._create_item_row(special_frame, "DalFry", self.dalfry, 0)
        self._create_item_row(special_frame, "Burger", self.burger, 1)
        self._create_item_row(special_frame, "SSPSandwich", self.sspsandwich, 2)
        self._create_item_row(special_frame, "Fries", self.fries, 3)
        self._create_item_row(special_frame, "SSPNoodles", self.sspnoodles, 4)
        self._create_item_row(special_frame, "Biryani", self.biryani, 5)
        self._create_item_row(special_frame, "Paneer Butter Masala", self.paneer_butter_masala, 6)
        self._create_item_row(special_frame, "Veg Handi", self.veg_handi, 7)

        # Beverages
        self._create_item_row(beverages_frame, "Tea", self.tea, 0)
        self._create_item_row(beverages_frame, "Coffee", self.coffee, 1)
        self._create_item_row(beverages_frame, "Drinks", self.drinks, 2)
        self._create_item_row(beverages_frame, "Buttermilk", self.buttermilk, 3)
        self._create_item_row(beverages_frame, "Lassi", self.lassi, 4)
        self._create_item_row(beverages_frame, "Coco", self.coco, 5)
        self._create_item_row(beverages_frame, "Masala Chaas", self.masala_chaas, 6)
        self._create_item_row(beverages_frame, "Faluda", self.faluda, 7)

    def _build_bill_frame(self, parent):
        frame = tb.Labelframe(
            parent,
            text="Bill Area",
            padding=5,
            bootstyle="secondary"
        )
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        scroll_y = tb.Scrollbar(frame, orient=tk.VERTICAL)
        scroll_y.grid(row=0, column=1, sticky="ns")

        self.textarea = tk.Text(
            frame,
            font=("Consolas", 10),
            width=35,              # narrower bill area
            yscrollcommand=scroll_y.set
        )
        self.textarea.grid(row=0, column=0, sticky="nsew")
        scroll_y.config(command=self.textarea.yview)
        return frame

    def _build_button_bar(self, parent):
        frame = tb.Frame(parent, padding=5)
        frame.grid_columnconfigure(tuple(range(8)), weight=1)

        tb.Button(frame, text="Calculate Bill",
                  command=self.total, bootstyle="success-outline").grid(
            row=0, column=0, padx=4, pady=4, sticky="ew"
        )
        tb.Button(frame, text="View Bill",
                  command=self.bill_area, bootstyle="info-outline").grid(
            row=0, column=1, padx=4, pady=4, sticky="ew"
        )
        tb.Button(frame, text="Save Bill (TXT)",
                  command=self.save_bill, bootstyle="secondary-outline").grid(
            row=0, column=2, padx=4, pady=4, sticky="ew"
        )
        tb.Button(frame, text="View All Bills",
                  command=self.show_all_bills, bootstyle="secondary").grid(
            row=0, column=3, padx=4, pady=4, sticky="ew"
        )
        tb.Button(frame, text="Search Bill",
                  command=self.search_bills, bootstyle="info").grid(
            row=0, column=4, padx=4, pady=4, sticky="ew"
        )
        tb.Button(frame, text="Clear",
                  command=self.clear_data, bootstyle="warning-outline").grid(
            row=0, column=5, padx=4, pady=4, sticky="ew"
        )
        tb.Button(frame, text="Print",
                  command=self.Print_bill, bootstyle="secondary").grid(
            row=0, column=6, padx=4, pady=4, sticky="ew"
        )
        tb.Button(frame, text="Exit",
                  command=self.Exit_app, bootstyle="danger").grid(
            row=0, column=7, padx=4, pady=4, sticky="ew"
        )
        return frame

    # ------------------------------------------------------------------
    # UTILITIES / DB
    # ------------------------------------------------------------------
    def get_current_time_str(self):
        return time.strftime("%d-%m-%Y %a %H:%M:%S", time.localtime())

    def setup_database(self):
        try:
            self.db_conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Jils@1863",
                database="rbs"
            )
            self.db_cursor = self.db_conn.cursor()
            self.db_cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS bills (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    bill_number VARCHAR(20),
                    customer_name VARCHAR(100),
                    phone_number VARCHAR(20),
                    table_number VARCHAR(20),
                    total_gst DECIMAL(10,2),
                    total_bill DECIMAL(10,2),
                    datetime_str VARCHAR(40)
                )
                """
            )
            self.db_conn.commit()
        except Error as e:
            messagebox.showerror(
                "Database Error",
                f"Could not connect to MySQL.\n\nError: {e}"
            )
            self.db_conn = None
            self.db_cursor = None

    # ------------------------------------------------------------------
    # BILL CALCULATION & DISPLAY
    # ------------------------------------------------------------------
    def total(self):
        # snacks
        self.s_s_p = self.samosa.get() * 40
        self.s_i_p = self.idli.get() * 50
        self.s_u_p = self.upma.get() * 80
        self.s_d_p = self.dosa.get() * 120
        self.s_pf_p = self.puff.get() * 90
        self.s_pd_p = self.pakoda.get() * 70
        self.poha_p = self.poha.get() * 40
        self.kachori_p = self.kachori.get() * 30

        self.total_snacks_p = (
            self.s_s_p + self.s_i_p + self.s_u_p +
            self.s_d_p + self.s_pf_p + self.s_pd_p +
            self.poha_p + self.kachori_p
        )
        self.snacks_p.set(f"Rs. {self.total_snacks_p}")

        # specialities
        self.sp_d_p = self.dalfry.get() * 100
        self.sp_b_p = self.burger.get() * 50
        self.sp_s_p = self.sspsandwich.get() * 120
        self.sp_f_p = self.fries.get() * 90
        self.sp_n_p = self.sspnoodles.get() * 190
        self.sp_by_p = self.biryani.get() * 200
        self.sp_pbm_p = self.paneer_butter_masala.get() * 180
        self.sp_vh_p = self.veg_handi.get() * 160

        self.total_specialities_p = (
            self.sp_d_p + self.sp_b_p + self.sp_s_p +
            self.sp_f_p + self.sp_n_p + self.sp_by_p +
            self.sp_pbm_p + self.sp_vh_p
        )
        self.specialities_p.set(f"Rs. {self.total_specialities_p}")

        # beverages
        self.b_t_p = self.tea.get() * 30
        self.b_co_p = self.coffee.get() * 40
        self.b_d_p = self.drinks.get() * 20
        self.b_b_p = self.buttermilk.get() * 40
        self.b_l_p = self.lassi.get() * 60
        self.b_c_p = self.coco.get() * 80
        self.b_mc_p = self.masala_chaas.get() * 30
        self.b_f_p = self.faluda.get() * 80

        self.total_drinks_p = (
            self.b_t_p + self.b_co_p + self.b_d_p +
            self.b_b_p + self.b_l_p + self.b_c_p +
            self.b_mc_p + self.b_f_p
        )
        self.bevarages_p.set(f"Rs. {self.total_drinks_p}")

        self.item_bill = float(
            self.total_snacks_p +
            self.total_specialities_p +
            self.total_drinks_p
        )
        self.total_gst = round(self.item_bill * 0.025, 2)
        self.gst.set(f"Rs. {self.total_gst}")
        self.Total_bill = float(self.item_bill + self.total_gst)

    def welcome_bill(self):
        self.textarea.delete("1.0", tk.END)
        t = self.get_current_time_str()

        self.textarea.insert(tk.END, "\tWelcome To Silver Heights Restaurant\n")
        self.textarea.insert(tk.END, f"\n Bill Number   : {self.bill_no.get()}")
        self.textarea.insert(tk.END, f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(tk.END, f"\n Phone Number  : {self.c_phone.get()}")
        self.textarea.insert(tk.END, f"\n Table Number  : {self.t_no.get()}")
        self.textarea.insert(tk.END, f"\n Time          : {t}")
        self.textarea.insert(tk.END, f"\n GST Number    : 22AAAA0000A1Z5")
        self.textarea.insert(tk.END, "\n==============================================")
        self.textarea.insert(tk.END, "\n Products\t\tQTY\tPrice")
        self.textarea.insert(tk.END, "\n==============================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are required")
            return
        if not self.c_name.get().isalpha():
            messagebox.showerror("Error", "Customer name should contain only letters")
            return
        if not (len(self.c_phone.get()) == 10 or self.c_phone.get() == "NA"):
            messagebox.showerror("Error", "Phone number must be 10 digits or 'NA'")
            return

        self.welcome_bill()

        # snacks
        if self.samosa.get():
            self.textarea.insert(tk.END, f"\n Samosa\t\t{self.samosa.get()}\tRs.{self.s_s_p}")
        if self.idli.get():
            self.textarea.insert(tk.END, f"\n Idli\t\t{self.idli.get()}\tRs.{self.s_i_p}")
        if self.upma.get():
            self.textarea.insert(tk.END, f"\n Upma\t\t{self.upma.get()}\tRs.{self.s_u_p}")
        if self.dosa.get():
            self.textarea.insert(tk.END, f"\n Dosa\t\t{self.dosa.get()}\tRs.{self.s_d_p}")
        if self.puff.get():
            self.textarea.insert(tk.END, f"\n Puff\t\t{self.puff.get()}\tRs.{self.s_pf_p}")
        if self.pakoda.get():
            self.textarea.insert(tk.END, f"\n Pakoda\t\t{self.pakoda.get()}\tRs.{self.s_pd_p}")
        if self.poha.get():
            self.textarea.insert(tk.END, f"\n Poha\t\t{self.poha.get()}\tRs.{self.poha_p}")
        if self.kachori.get():
            self.textarea.insert(tk.END, f"\n Kachori\t\t{self.kachori.get()}\tRs.{self.kachori_p}")

        # specialities
        if self.dalfry.get():
            self.textarea.insert(tk.END, f"\n DalFry\t\t{self.dalfry.get()}\tRs.{self.sp_d_p}")
        if self.burger.get():
            self.textarea.insert(tk.END, f"\n Burger\t\t{self.burger.get()}\tRs.{self.sp_b_p}")
        if self.sspsandwich.get():
            self.textarea.insert(tk.END, f"\n SSPSandwich\t{self.sspsandwich.get()}\tRs.{self.sp_s_p}")
        if self.fries.get():
            self.textarea.insert(tk.END, f"\n Fries\t\t{self.fries.get()}\tRs.{self.sp_f_p}")
        if self.sspnoodles.get():
            self.textarea.insert(tk.END, f"\n SSPNoodles\t{self.sspnoodles.get()}\tRs.{self.sp_n_p}")
        if self.biryani.get():
            self.textarea.insert(tk.END, f"\n Biryani\t\t{self.biryani.get()}\tRs.{self.sp_by_p}")
        if self.paneer_butter_masala.get():
            self.textarea.insert(tk.END, f"\n Paneer Butter Masala\t{self.paneer_butter_masala.get()}\tRs.{self.sp_pbm_p}")
        if self.veg_handi.get():
            self.textarea.insert(tk.END, f"\n Veg Handi\t{self.veg_handi.get()}\tRs.{self.sp_vh_p}")

        # drinks
        if self.tea.get():
            self.textarea.insert(tk.END, f"\n Tea\t\t{self.tea.get()}\tRs.{self.b_t_p}")
        if self.coffee.get():
            self.textarea.insert(tk.END, f"\n Coffee\t\t{self.coffee.get()}\tRs.{self.b_co_p}")
        if self.drinks.get():
            self.textarea.insert(tk.END, f"\n Drinks\t\t{self.drinks.get()}\tRs.{self.b_d_p}")
        if self.buttermilk.get():
            self.textarea.insert(tk.END, f"\n Buttermilk\t{self.buttermilk.get()}\tRs.{self.b_b_p}")
        if self.lassi.get():
            self.textarea.insert(tk.END, f"\n Lassi\t\t{self.lassi.get()}\tRs.{self.b_l_p}")
        if self.coco.get():
            self.textarea.insert(tk.END, f"\n Coco\t\t{self.coco.get()}\tRs.{self.b_c_p}")
        if self.masala_chaas.get():
            self.textarea.insert(tk.END, f"\n Masala Chaas\t{self.masala_chaas.get()}\tRs.{self.b_mc_p}")
        if self.faluda.get():
            self.textarea.insert(tk.END, f"\n Faluda\t\t{self.faluda.get()}\tRs.{self.b_f_p}")

        self.textarea.insert(tk.END, "\n----------------------------------------------")
        self.textarea.insert(tk.END, f"\n GST        : Rs. {self.total_gst}")
        self.textarea.insert(tk.END, f"\n Item Total : Rs. {self.item_bill}")
        self.textarea.insert(tk.END, "\n----------------------------------------------")
        self.textarea.insert(tk.END, f"\n Total Bill : Rs. {self.Total_bill}")
        self.textarea.insert(tk.END, "\n----------------------------------------------")
        self.textarea.insert(tk.END, "\n     Thank You For Visiting!     ")
        self.textarea.insert(tk.END, "\n----------------------------------------------")

        self.save_bill_to_db()

    # ------------------------------------------------------------------
    # DB + FILE SAVE / SEARCH
    # ------------------------------------------------------------------
    def save_bill_to_db(self):
        if self.db_conn is None or self.db_cursor is None:
            return
        try:
            t = self.get_current_time_str()
            sql = """
                INSERT INTO bills (
                    bill_number, customer_name, phone_number,
                    table_number, total_gst, total_bill, datetime_str
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            vals = (
                self.bill_no.get(),
                self.c_name.get(),
                self.c_phone.get(),
                self.t_no.get(),
                float(self.total_gst),
                float(self.Total_bill),
                t
            )
            self.db_cursor.execute(sql, vals)
            self.db_conn.commit()
        except Error as e:
            messagebox.showerror("Database Error", f"Could not save bill to MySQL.\n\nError: {e}")

    def save_bill(self):
        if not self.textarea.get("1.0", tk.END).strip():
            messagebox.showerror("Error", "Bill area is empty. Generate the bill first.")
            return
        if messagebox.askyesno("Save Bill", "Do you want to save this bill as a text file?"):
            os.makedirs("bills", exist_ok=True)
            path = os.path.join("bills", f"{self.bill_no.get()}.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.textarea.get("1.0", tk.END))
            messagebox.showinfo("Saved", f"Bill saved successfully:\n{path}")

    def show_all_bills(self):
        if self.db_conn is None or self.db_cursor is None:
            messagebox.showerror("Database Error", "MySQL connection not available.")
            return

        top = tb.Toplevel(self.root)
        top.title("All Saved Bills")
        top.geometry("900x400")

        cols = ("bill_number", "customer_name", "phone_number",
                "table_number", "total_gst", "total_bill", "datetime_str")

        frame = tb.Frame(top, padding=5)
        frame.pack(fill="both", expand=True)

        tree_scroll = tb.Scrollbar(frame, orient="vertical")
        tree_scroll.pack(side="right", fill="y")

        tree = ttk.Treeview(frame, columns=cols, show="headings",
                            yscrollcommand=tree_scroll.set)
        tree.pack(fill="both", expand=True)
        tree_scroll.config(command=tree.yview)

        headings = {
            "bill_number": "Bill No",
            "customer_name": "Customer",
            "phone_number": "Phone",
            "table_number": "Table",
            "total_gst": "GST",
            "total_bill": "Total Bill",
            "datetime_str": "Date & Time",
        }
        widths = {
            "bill_number": 80,
            "customer_name": 140,
            "phone_number": 100,
            "table_number": 60,
            "total_gst": 80,
            "total_bill": 90,
            "datetime_str": 180,
        }
        anchors = {
            "bill_number": "center",
            "customer_name": "w",
            "phone_number": "center",
            "table_number": "center",
            "total_gst": "e",
            "total_bill": "e",
            "datetime_str": "w",
        }

        for col in cols:
            tree.heading(col, text=headings[col])
            tree.column(col, width=widths[col], anchor=anchors[col])

        try:
            self.db_cursor.execute(
                """
                SELECT bill_number, customer_name, phone_number,
                       table_number, total_gst, total_bill, datetime_str
                FROM bills
                ORDER BY id DESC
                """
            )
            for row in self.db_cursor.fetchall():
                tree.insert("", "end", values=row)
        except Error as e:
            messagebox.showerror("Database Error", f"Could not fetch bills.\n\nError: {e}")

    def search_bills(self):
        if self.db_conn is None or self.db_cursor is None:
            messagebox.showerror("Database Error", "MySQL connection not available.")
            return

        top = tb.Toplevel(self.root)
        top.title("Search Bills")
        top.geometry("900x450")

        bill_var = tk.StringVar()
        phone_var = tk.StringVar()

        search_frame = tb.Labelframe(top, text="Search Criteria",
                                     padding=8, bootstyle="info")
        search_frame.pack(fill="x", padx=5, pady=5)

        tb.Label(search_frame, text="Bill Number:").grid(
            row=0, column=0, padx=5, pady=3, sticky="w"
        )
        tb.Entry(search_frame, textvariable=bill_var, width=18).grid(
            row=0, column=1, padx=5, pady=3
        )

        tb.Label(search_frame, text="Phone Number:").grid(
            row=0, column=2, padx=5, pady=3, sticky="w"
        )
        tb.Entry(search_frame, textvariable=phone_var, width=18).grid(
            row=0, column=3, padx=5, pady=3
        )

        cols = ("bill_number", "customer_name", "phone_number",
                "table_number", "total_gst", "total_bill", "datetime_str")

        table_frame = tb.Frame(top, padding=5)
        table_frame.pack(fill="both", expand=True)

        scroll = tb.Scrollbar(table_frame, orient="vertical")
        scroll.pack(side="right", fill="y")

        tree = ttk.Treeview(table_frame, columns=cols, show="headings",
                            yscrollcommand=scroll.set)
        tree.pack(fill="both", expand=True)
        scroll.config(command=tree.yview)

        headings = {
            "bill_number": "Bill No",
            "customer_name": "Customer",
            "phone_number": "Phone",
            "table_number": "Table",
            "total_gst": "GST",
            "total_bill": "Total Bill",
            "datetime_str": "Date & Time",
        }
        widths = {
            "bill_number": 80,
            "customer_name": 140,
            "phone_number": 100,
            "table_number": 60,
            "total_gst": 80,
            "total_bill": 90,
            "datetime_str": 180,
        }
        anchors = {
            "bill_number": "center",
            "customer_name": "w",
            "phone_number": "center",
            "table_number": "center",
            "total_gst": "e",
            "total_bill": "e",
            "datetime_str": "w",
        }

        for col in cols:
            tree.heading(col, text=headings[col])
            tree.column(col, width=widths[col], anchor=anchors[col])

        def do_search():
            for item in tree.get_children():
                tree.delete(item)

            bill = bill_var.get().strip()
            phone = phone_var.get().strip()
            if not bill and not phone:
                messagebox.showerror("Error", "Enter Bill Number and/or Phone Number.")
                return

            conditions, vals = [], []
            if bill:
                conditions.append("bill_number = %s")
                vals.append(bill)
            if phone:
                conditions.append("phone_number = %s")
                vals.append(phone)

            sql = """
                SELECT bill_number, customer_name, phone_number,
                       table_number, total_gst, total_bill, datetime_str
                FROM bills
            """
            if conditions:
                sql += " WHERE " + " AND ".join(conditions)
            sql += " ORDER BY id DESC"

            try:
                self.db_cursor.execute(sql, tuple(vals))
                rows = self.db_cursor.fetchall()
                if not rows:
                    messagebox.showinfo("No Results", "No matching bills found.")
                for row in rows:
                    tree.insert("", "end", values=row)
            except Error as e:
                messagebox.showerror("Database Error", f"Could not search bills.\n\nError: {e}")

        tb.Button(search_frame, text="Search", bootstyle="success",
                  command=do_search).grid(row=0, column=4, padx=10, pady=3)

    # ------------------------------------------------------------------
    # CLEAR / EXIT / PRINT
    # ------------------------------------------------------------------
    def clear_data(self):
        if not messagebox.askyesno("Clear", "Do you really want to clear all data?"):
            return

        for var in [
            self.samosa, self.idli, self.upma, self.dosa, self.puff, self.pakoda,
            self.poha, self.kachori,
            self.dalfry, self.burger, self.sspsandwich, self.fries, self.sspnoodles,
            self.biryani, self.paneer_butter_masala, self.veg_handi,
            self.tea, self.coffee, self.drinks, self.buttermilk,
            self.lassi, self.coco, self.masala_chaas, self.faluda
        ]:
            var.set(0)

        self.snacks_p.set("")
        self.specialities_p.set("")
        self.bevarages_p.set("")
        self.gst.set("")
        self.item_bill = 0.0
        self.total_gst = 0.0
        self.Total_bill = 0.0

        self.c_name.set("")
        self.c_phone.set("")
        self.t_no.set("")
        self.search_bill.set("")
        self.bill_no.set(str(random.randint(1000, 9999)))

        self.welcome_bill()

    def Exit_app(self):
        if messagebox.askyesno("Exit", "Do you really want to exit?"):
            if self.db_conn is not None:
                self.db_conn.close()
            self.root.destroy()

    def Print_bill(self):
        data = self.textarea.get("1.0", tk.END)
        if not data.strip():
            messagebox.showerror("Error", "Bill area is empty.")
            return

        tmp = tempfile.mktemp(".txt")
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(data)

        try:
            os.startfile(tmp, "print")  # Windows only
        except AttributeError:
            messagebox.showinfo("Print", "Printing supported only on Windows with os.startfile().")


if __name__ == "__main__":
    win = tb.Window(themename="flatly")
    app = Bill_App(win)
    win.mainloop()
