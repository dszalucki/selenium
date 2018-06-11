import tkinter
from tkinter import messagebox

def przelicz_koszt_przejazdu():
    try:
        dystans = float(dystans_pole.get())
        spalanie = float(spalanie_pole.get())
        cena = float(cena_pole.get())
        koszt = (dystans / 100) * cena * spalanie
        wynik_pole.configure(text=f'{koszt:.2f} PLN')
        print(spalanie)
    except ValueError:
        messagebox.showerror(title='FATAL ERROR', message='Uzupełnij wszystkie pola')



# Tworzę nowego okno
okno = tkinter.Tk()
# Określam, że okno ma mieć 2 kolumny
okno.columnconfigure(1)

# Tworzę nowy obiekt etykiety
dystans_etykieta = tkinter.Label(master=okno, text='Dystans')
spalanie_etykieta = tkinter.Label(master=okno, text='Spalanie')
cena_etykieta = tkinter.Label(master=okno, text='Cena')
wynik_etykieta = tkinter.Label(master=okno, text='wynik')

# umieszczam etykietę w lewym górnym rogu okna
dystans_etykieta.grid(row=0, column=0)
spalanie_etykieta.grid(row=1, column=0)
cena_etykieta.grid(row=2, column=0)
wynik_etykieta.grid(row=3, column=0)

# Tworzę nowy obiekt Entry
dystans_pole = tkinter.Entry(master=okno)
spalanie_pole = tkinter.Entry(master=okno)
cena_pole = tkinter.Entry(master=okno)
wynik_pole = tkinter.Label(master=okno)

 # umieszczam Entry w drugiej kolumnie
dystans_pole.grid(row=0, column=1)
spalanie_pole.grid(row=1, column=1)
cena_pole.grid(row=2, column=1)
wynik_pole.grid(row=3, column=1)

# tworzymy button
guzik = tkinter.Button(master=okno, text='Oblicz', command=przelicz_koszt_przejazdu)
guzik.grid(row=4, column=0, columnspan=5)


okno.title('Przeliczanie spalania')
okno.mainloop()


