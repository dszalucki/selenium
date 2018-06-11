import tkinter


class Okno:

    def uwierzytelnianie(self):

        okno = tkinter.Tk()
        okno.columnconfigure(4)

        login_label = tkinter.Label(master=okno, text='Login')
        login_label.grid(row=0, column=0)

        haslo_label = tkinter.Label(master=okno, text='Hasło')
        haslo_label.grid(row=1, column=0)


        login_entry = tkinter.Entry(master=okno)
        login_entry.grid(row=0, column=1)


        haslo_entry = tkinter.Entry(master=okno)
        haslo_entry.grid(row=1, column=1)


        send_button = tkinter.Button(master=okno, text='Wyślij', command=okno.quit())
        send_button.grid(row=4, column=1, columnspan=2)

        okno.title('UWIERZYTELNIANIE')
        okno.mainloop()




Okno().uwierzytelnianie()