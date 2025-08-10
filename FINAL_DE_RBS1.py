from tkinter import *
import math, random
from tkinter import messagebox
import os, time, tempfile
import ast

import csv
from pathlib import Path


class Bill_App:
    current_time = time.localtime(time.time())
    formatted_time = time.strftime("%d-%m-%Y %a %H:%M:%S", current_time)

    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing System")
        bg_color = "#074463"
        title = Label(self.root, text="Silver Heights Restaurant", bd=12, relief=GROOVE, bg=bg_color, fg="white",font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        # ================Variables=======================
        # ================Snacks========================
        self.samosa = IntVar()
        self.idli = IntVar()
        self.upma = IntVar()
        self.dosa = IntVar()
        self.puff = IntVar()
        self.pakoda = IntVar()
        # ================Specialities==========================
        self.dalfry = IntVar()
        self.burger = IntVar()
        self.sspsandwich = IntVar()
        self.fries = IntVar()
        self.sspnoodles = IntVar()
        self.biryani = IntVar()
        # ================Beverages======================
        self.tea = IntVar()
        self.coffee = IntVar()
        self.drinks = IntVar()
        self.buttermilk = IntVar()
        self.lassi = IntVar()
        self.coco = IntVar()

        # =======total product====================
        self.snacks_p = StringVar()
        self.specialities_p = StringVar()
        self.bevarages_p = StringVar()

        self.gst = StringVar()
        self.total_gst = StringVar()
        # =================Customer=======================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
        self.t_no = StringVar()
        self.bill_time = StringVar()

        # ================customer details frame==============
        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,column=3,padx=10, pady=5)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.bill_no, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, padx=10, pady=5)

        T_no_lbl = Label(F1, text="Table Number", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0, column=6, padx=20, pady=5)
        T_no_txt = Entry(F1, width=15, textvariable=self.t_no, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,column=7,padx=10,pady=5)

        # ===================Snacks============================
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Snacks", font=("times new roman", 15, "bold"), fg="gold",bg=bg_color)
        F2.place(x=5, y=170, width=325, height=380)

        sa_lbl = Label(F2, text="Samosa", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        sa_txt = Entry(F2, width=10, textvariable=self.samosa, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        idli_lbl = Label(F2, text="Idli", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        idli_txt = Entry(F2, width=10, textvariable=self.idli, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        ua_lbl = Label(F2, text="Upma", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        ua_txt = Entry(F2, width=10, textvariable=self.upma, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        da_lbl = Label(F2, text="Dosa", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        da_txt = Entry(F2, width=10, textvariable=self.dosa, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        pu_lbl = Label(F2, text="Puff", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        pu_txt = Entry(F2, width=10, textvariable=self.puff, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        pk_lbl = Label(F2, text="Pakoda", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        pk_txt = Entry(F2, width=10, textvariable=self.pakoda, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ===================specialities============================
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Specialities", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F3.place(x=335, y=170, width=325, height=380)

        g1_lbl = Label(F3, text="DalFry", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10, textvariable=self.dalfry, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        g2_lbl = Label(F3, text="Burger", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10, textvariable=self.burger, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        g3_lbl = Label(F3, text="SSPSandwich", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10, textvariable=self.sspsandwich, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        g4_lbl = Label(F3, text="Fries", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt = Entry(F3, width=10, textvariable=self.fries, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        g5_lbl = Label(F3, text="SSPNoodles", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10, textvariable=self.sspnoodles, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        g6_lbl = Label(F3, text="Biryani", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10, textvariable=self.biryani, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ===================Bevarages============================
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Beverages", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F4.place(x=665, y=170, width=325, height=380)

        c1_lbl = Label(F4, text="Tea", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=0,column=0,padx=30,pady=10,sticky="w")
        c1_txt = Entry(F4, width=10, textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        c2_lbl = Label(F4, text="Coffee", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=10, textvariable=self.coffee, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        c3_lbl = Label(F4, text="Drinks", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10, textvariable=self.drinks, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        c4_lbl = Label(F4, text="Buttermilk", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=10, textvariable=self.buttermilk, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        c5_lbl = Label(F4, text="Lassi", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt = Entry(F4, width=10, textvariable=self.lassi, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        c6_lbl = Label(F4, text="Coco", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt = Entry(F4, width=10, textvariable=self.coco, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ==================Bill Area===================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1000, y=170, width=528, height=620)
        bill_title = Label(F5, text="Bill Area", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.textarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # =================Button Frame=================

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 16, "bold"),pady=18,fg="gold", bg=bg_color)
        F6.place(x=0, y=556, relwidth=0.65, height=215)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=50, width=730, relwidth=0.13, height=115)

        Cbill_btn = Button(btn_F, text="Calculate Bill", command=self.total, bg="cadetblue", fg="white", bd=2, pady=15,width=10,font="arial 14 bold").grid(row=0, column=0, padx=5, pady=13)
        ViewBill_btn = Button(btn_F, text="View Bill", command=self.bill_area, bg="cadetblue", fg="white", bd=2,pady=15, width=10, font="arial 14 bold").grid(row=0, column=1, padx=5, pady=5)
        s_btn = Button(btn_F, text="Save Bill", bg="cadetblue", command=self.save_bill, fg="white", bd=2, pady=15,width=10,font="arial 14 bold").grid(row=0, column=2, padx=5, pady=5)
        Clear_btn = Button(btn_F, text="Clear", command=self.clear_data, bg="cadetblue", fg="white", bd=2, pady=15, width=10, font="arial 14 bold").grid(row=0, column=3, padx=5, pady=5)
        Exit_btn = Button(btn_F, text="Exit", bg="cadetblue", command=self.Exit_app, fg="white", bd=2, pady=15,width=10, font="arial 14 bold").grid(row=0, column=4, padx=5, pady=5)
        Print_btn = Button(btn_F, text="Print", bg="cadetblue", fg="white", bd=2, pady=15, width=10,font="arial 14 bold").grid(row=0, column=5, padx=5, pady=5)

        self.welcome_bill()

    def total(self):
        self.s_s_p = self.samosa.get() * 40
        self.s_i_p = self.idli.get() * 50
        self.s_u_p = self.upma.get() * 80
        self.s_d_p = self.dosa.get() * 120
        self.s_pf_p = self.puff.get() * 90
        self.s_pd_p = self.pakoda.get() * 70

        self.total_snacks_p = float(
            self.s_s_p +
            self.s_i_p +
            self.s_u_p +
            self.s_d_p +
            self.s_pf_p +
            self.s_pd_p
        )
        self.snacks_p.set("Rs. " + str(self.total_snacks_p))

        self.sp_d_p = self.dalfry.get() * 100
        self.sp_b_p = self.burger.get() * 50
        self.sp_s_p = self.sspsandwich.get() * 120
        self.sp_f_p = self.fries.get() * 90
        self.sp_n_p = self.sspnoodles.get() * 190
        self.sp_by_p = self.biryani.get() * 200

        self.total_specialities_p = float(
            self.sp_d_p +
            self.sp_b_p +
            self.sp_s_p +
            self.sp_f_p +
            self.sp_n_p +
            self.sp_by_p
        )
        self.specialities_p.set("Rs. " + str(self.total_specialities_p))

        self.b_t_p = self.tea.get() * 30
        self.b_co_p = self.coffee.get() * 40
        self.b_d_p = self.drinks.get() * 20
        self.b_b_p = self.buttermilk.get() * 40
        self.b_l_p = self.lassi.get() * 60
        self.b_c_p = self.coco.get() * 80

        self.total_drinks_p = float(
            self.b_t_p +
            self.b_co_p +
            self.b_d_p +
            self.b_b_p +
            self.b_l_p +
            self.b_c_p
        )
        self.bevarages_p.set("Rs. " + str(self.total_drinks_p))
        self.item_bill = float(self.total_snacks_p +
                               self.total_specialities_p +
                               self.total_drinks_p)
        self.gst_tax = round((self.item_bill * 0.025), 2)
        self.gst.set("Rs. " + str(self.gst_tax))
        self.total_gst = self.gst_tax
        self.Total_bill = float(self.item_bill + self.total_gst)

    def welcome_bill(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, "\tWelcome To Silver Heights Restaurant\n")
        self.textarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer name : {self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number : {self.c_phone.get()}")
        self.textarea.insert(END, f"\n Table Number : {self.t_no.get()}")
        self.textarea.insert(END, f"\n Time : {self.formatted_time}")
        self.textarea.insert(END, f"\n GST Number : 22AAAA0000A1Z5")
        self.textarea.insert(END, f"\n======================================================")
        self.textarea.insert(END, f"\n Products\t\t\tQTY\t\t\tPrice ")
        self.textarea.insert(END, f"\n======================================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are must")
        else:
            if (self.c_name.get().isalpha()):
                if (len(self.c_phone.get()) == 10 or self.c_phone.get() == "NA"):
                    self.welcome_bill()
                    # =====snacks===
                    if self.samosa.get() != 0:
                        self.textarea.insert(END, f"\n Samosa\t\t\t{self.samosa.get()}\t\t Rs.{self.s_s_p}")
                    if self.idli.get() != 0:
                        self.textarea.insert(END, f"\n Idli\t\t\t{self.idli.get()}\t\t Rs.{self.s_i_p}")
                    if self.upma.get() != 0:
                        self.textarea.insert(END, f"\n Upma\t\t\t{self.upma.get()}\t\t Rs.{self.s_u_p}")
                    if self.dosa.get() != 0:
                        self.textarea.insert(END, f"\n Dosa\t\t\t{self.dosa.get()}\t\t Rs.{self.s_d_p}")
                    if self.puff.get() != 0:
                        self.textarea.insert(END, f"\n Puff\t\t\t{self.puff.get()}\t\t Rs.{self.s_pf_p}")
                    if self.pakoda.get() != 0:
                        self.textarea.insert(END, f"\n pakoda\t\t\t{self.pakoda.get()}\t\t Rs.{self.s_pd_p}")

                        # =====specialities===
                    if self.dalfry.get() != 0:
                        self.textarea.insert(END, f"\n DalFry\t\t\t{self.dalfry.get()}\t\t Rs.{self.sp_d_p}")
                    if self.burger.get() != 0:
                        self.textarea.insert(END, f"\n Burger\t\t\t{self.burger.get()}\t\t Rs.{self.sp_b_p}")
                    if self.sspsandwich.get() != 0:
                        self.textarea.insert(END, f"\n SSPSandwich\t\t\t{self.sspsandwich.get()}\t\t Rs.{self.sp_s_p}")
                    if self.fries.get() != 0:
                        self.textarea.insert(END, f"\n Fries\t\t\t{self.fries.get()}\t\t Rs.{self.sp_f_p}")
                    if self.sspnoodles.get() != 0:
                        self.textarea.insert(END, f"\n SSPNoodles\t\t\t{self.puff.get()}\t\t Rs.{self.sp_n_p}")
                    if self.biryani.get() != 0:
                        self.textarea.insert(END, f"\n Biryani\t\t\t{self.biryani.get()}\t\t Rs.{self.sp_by_p}")

                    # =====Drinks===
                    if self.tea.get() != 0:
                        self.textarea.insert(END, f"\n Tea\t\t\t{self.tea.get()}\t\t Rs.{self.b_t_p}")
                    if self.coffee.get() != 0:
                        self.textarea.insert(END, f"\n Coffee\t\t\t{self.coffee.get()}\t\t Rs.{self.b_co_p}")
                    if self.drinks.get() != 0:
                        self.textarea.insert(END, f"\n Drinks\t\t\t{self.drinks.get()}\t\t Rs.{self.b_d_p}")
                    if self.buttermilk.get() != 0:
                        self.textarea.insert(END, f"\n ButterMilk\t\t\t{self.buttermilk.get()}\t\t Rs.{self.b_b_p}")
                    if self.lassi.get() != 0:
                        self.textarea.insert(END, f"\n Lassi\t\t\t{self.lassi.get()}\t\t Rs.{self.b_l_p}")
                    if self.coco.get() != 0:
                        self.textarea.insert(END, f"\n Coco\t\t\t{self.coco.get()}\t\t Rs.{self.b_c_p}")
                        self.textarea.insert(END, f"\n------------------------------------")

                    self.textarea.insert(END, f"\n------------------------------------------------")
                    self.textarea.insert(END, f"\n GST : \t\t\t Rs. {self.total_gst}")
                    self.textarea.insert(END, f"\n Item Total : \t\t\t Rs. {self.item_bill}")
                    self.textarea.insert(END, f"\n-------------------------------------------")
                    self.textarea.insert(END, f"\n Total Bill : \t\t\t Rs. {self.Total_bill}")
                    self.textarea.insert(END, f"\n-------------------------------------------")
                    self.textarea.insert(END, f"\n-----------Thank You For Visiting----------")
                    self.textarea.insert(END, f"\n-------------------------------------------")

                    # self.save_bill()
                    path = Path('D:/VS CODE/VS Python/Restaurant_Billing_Syatem/hotel.csv') #change as per your location
                    if (not (path.is_file())):
                        f = open('hotel.csv', 'w')
                        writer = csv.writer(f)
                        fn = ['Bill_Number', 'Customer_Name', 'Phone_Number', 'Table_Number', 'Total_GST', 'Total_Bill',
                              'Date&Time']
                        writer.writerow(fn)
                        writer = csv.DictWriter(f, fieldnames=fn)
                        writer.writerow({fn[0]: self.bill_no.get(), fn[1]: self.c_name.get(), fn[2]: self.c_phone.get(),
                                         fn[3]: self.t_no.get(), fn[4]: self.total_gst, fn[5]: self.Total_bill,
                                         fn[6]: self.formatted_time})
                        f.close()
                    else:
                        f = open('hotel.csv', 'a')
                        fn = ['Bill_Number', 'Customer_Name', 'Phone_Number', 'Table_Number', 'Total_GST', 'Total_Bill',
                              'Date&Time']
                        writer = csv.DictWriter(f, fieldnames=fn)
                        writer.writerow({fn[0]: self.bill_no.get(), fn[1]: self.c_name.get(), fn[2]: self.c_phone.get(),
                                         fn[3]: self.t_no.get(), fn[4]: self.total_gst, fn[5]: self.Total_bill
                                            , fn[6]: self.formatted_time})
                        f.close()

                    csv_file_path = path

                    if not Path(csv_file_path).is_file():
                        # Create a new CSV file and write the header row
                        with open(csv_file_path, 'w', newline='') as csv_file:
                            fieldnames = ['Bill_Number', 'Customer_Name', 'Phone_Number', 'Table_Number', 'Total_GST',
                                          'Total_Bill', 'Date&Time']
                            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                            writer.writeheader()

                            # Write the data for the current bill
                            writer.writerow({
                                'Bill_Number': self.bill_no.get(),
                                'Customer_Name': self.c_name.get(),
                                'Phone_Number': self.c_phone.get(),
                                'Table_Number': self.t_no.get(),
                                'Total_GST': self.total_gst,
                                'Total_Bill': self.Total_bill,
                                'Date&Time': self.formatted_time
                            })
                    else:
                        # Append data to existing CSV file
                        with open(csv_file_path, 'a', newline='') as csv_file:
                            fieldnames = ['Bill_Number', 'Customer_Name', 'Phone_Number', 'Table_Number', 'Total_GST',
                                          'Total_Bill', 'Date&Time']
                            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                            # Write the data for the current bill
                            writer.writerow({
                                'Bill_Number': self.bill_no.get(),
                                'Customer_Name': self.c_name.get(),
                                'Phone_Number': self.c_phone.get(),
                                'Table_Number': self.t_no.get(),
                                'Total_GST': self.total_gst,
                                'Total_Bill': self.Total_bill,
                                'Date&Time': self.formatted_time
                            })
                else:
                    messagebox.showerror("Error", "phone no should be length 10")

            else:
                messagebox.showerror("Error", "Customer name should be in Character")

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op > 0:
            self.bill_data = self.textarea.get('1.0', END)
            f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no. : {self.bill_no.get()} saved successfully")
        else:
            return

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear Data?")
        if op > 0:
            # ================Cosmatic========================
            self.samosa.set(0)
            self.idli.set(0)
            self.upma.set(0)
            self.dosa.set(0)
            self.puff.set(0)
            self.pakoda.set(0)
            # ================specialities==========================
            self.dalfry.set(0)
            self.burger.set(0)
            self.sspsandwich.set(0)
            self.fries.set(0)
            self.sspnoodles.set(0)
            self.biryani.set(0)
            # ================Cold Drinks======================
            self.tea.set(0)
            self.coffee.set(0)
            self.drinks.set(0)
            self.buttermilk.set(0)
            self.lassi.set(0)
            self.coco.set(0)

            # =======total product pdalfry====================
            self.snacks_p.set("")
            self.specialities_p.set("")
            self.bevarages_p.set("")

            # =================Customer=======================
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            self.t_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()
    def Print_bill(self):
        file = tempfile.mktemp('.txt')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(self.textarea.get('1.0', END))
        try:
            os.startfile(file, 'print')  # This should open default text editor in print mode
        except AttributeError:
            print("Printing is only supported on Windows with os.startfile.")


root = Tk()
obj = Bill_App(root)
root.mainloop()
