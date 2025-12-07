#Isaiah Wolf 5-15-24
#Isaiah_Exam_3

import tkinter

class TipGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.subtotal_frame = tkinter.Frame(self.main_window)
        self.percent_frame = tkinter.Frame(self.main_window)
        self.tip_frame = tkinter.Frame(self.main_window)
        self.total_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.subtotal_label = tkinter.Label(self.subtotal_frame, \
                                text = 'Enter the amount of the ticket:')
        self.subtotal_entry = tkinter.Entry(self.subtotal_frame, width = 10)

        self.subtotal_label.pack(side = 'left')
        self.subtotal_entry.pack(side = 'left')

        self.percent_label = tkinter.Label(self.percent_frame, \
                                text = 'Enter the tip as a percentage:')
        self.percent_entry = tkinter.Entry(self.percent_frame, width = 10)

        self.percent_label.pack(side = 'left')
        self.percent_entry.pack(side = 'left')

        self.tipAmount_label = tkinter.Label(self.tip_frame, \
                                text = 'Tip Amount: $')
        self.tip = tkinter.StringVar()
        self.tip_label = tkinter.Label(self.tip_frame, \
                            textvariable = self.tip)

        self.tipAmount_label.pack(side = 'left')
        self.tip_label.pack(side = 'left')

        self.totalAmount_label = tkinter.Label(self.total_frame, \
                                text = 'Total Amount: $')
        self.total = tkinter.StringVar()
        self.total_label = tkinter.Label(self.total_frame, \
                            textvariable = self.total)

        self.totalAmount_label.pack(side = 'left')
        self.total_label.pack(side = 'left')

        self.tip_button = tkinter.Button(self.button_frame, \
                    text = 'Calculate', command = self.calculate_tip)
        self.quit_button = tkinter.Button(self.button_frame, \
                    text = 'Exit', command = self.main_window.destroy)

        self.tip_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        self.subtotal_frame.pack()
        self.percent_frame.pack()
        self.tip_frame.pack()
        self.total_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def calculate_tip(self):
        self.subtotal = float(self.subtotal_entry.get())
        self.percent = float(self.percent_entry.get()) / 100
        self.tip_amount = float(self.subtotal) * self.percent
        self.tip.set(format(self.tip_amount, ',.2f'))
        self.total_amount = float(self.subtotal) + self.tip_amount
        self.total.set(format(self.total_amount, ',.2f'))

tip = TipGUI()
