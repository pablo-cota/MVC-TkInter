import tkinter as tk
import tkinter.messagebox as mb
from contactos import Contacto

#1 Creación de la clase ContactList
class ContactosList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.list = tk.Listbox(self, **kwargs)
        bar = tk.Scrollbar(self, command=self.list.yview)
        
        self.list.config(yscrollcommand=bar.set)
        bar.pack(side = tk.RIGHT, fill=tk.Y)
        self.list.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        
    def insert(self, contact, index=tk.END):
        text = "{}, {}".format(contact.last_name, contact.first_name)
        self.list.insert(index, text)
        
    def delete(self, index):
        self.list.delete(index, index)
    
    def update(self, contact, index):
        self.delete(index)
        self.insert(contact, index)
        
    def double_click(self, callback):
        handler = lambda _: callback(self.list.curselection()[0])
        self.list.bind("<Double-Button-1>", handler)

#
class ContactosForm(tk.LabelFrame):
    campos = ("Last Name", "First Name", "Email", "Phone")
    
    def __init__(self, master, **kwargs):
        super().__init__(master, text = "Contactos", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.frame.pack()
        self.campos = list(map(self.create_campo, enumerate(self.campos)))
        
        
    def create_campo(self, campo):
        posicion, texto = campo
        label = tk.Label(self.frame, text=texto)
        entry = tk.Entry(self.frame)
        label.grid(row=posicion, column=0, pady=10)
        entry.grid(row=posicion, column=1, pady=10)
        return entry
    
    #10
    def get_data(self):
        values = [e.get() for e in self.campos]
        print("values", values)
        try:
            return Contacto(*values)
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e), parent=self)
            
    def load_details(self, contact):
        values = (contact.last_name, contact.first_name, contact.email, contact.phone)
        for entry, value in zip(self.campos,values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
            
    def clear(self):
        for entry in self.campos:
            entry.delete(0, tk.END)
    
#
class ContactoNuevo(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        #Previo a 9
        self.contact=None
        self.form = ContactosForm(self)
        self.form.pack(padx=10, pady=10)
        self.button_add = tk.Button(self, text = "Agregar Contacto", command=self.confirm)
        self.button_add.pack()
        
    def confirm(self):
        print("Confirm contact")
        #9
        print("Adding new contact...")
        self.contact=self.form.get_data()
        if self.contact:
            self.destroy()
        
    def show(self):
        self.grab_set()
        self.wait_window()
        return self.contact
    

#3 Formulario para actualizar contacto en Master
class ActualizarContactosForm(ContactosForm):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.button_save = tk.Button(self, text="Save")
        self.button_delete = tk.Button(self, text="Delete")
        
        self.button_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.button_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)

#
class ContactosView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(" .::: LISTA DE CONTACTOS :::.")
        #self.geometry('500x500')
        self.button_new = tk.Button(self, text="New Contact")
        self.button_new.pack(side=tk.BOTTOM, pady=5)
        
        #2 Agregar a la clase Contactos View la lista para poder hacer uso de ella
        self.list = ContactosList(self, height=15)
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        
        #4Agregar el formulario para actualizar
        self.updateform = ActualizarContactosForm(self)
        self.updateform.pack(padx=10, pady=10)
        
        
    def set_controller(self,controller):
        self.button_new.config(command=controller.create_contact)
        #5 Enlazar con el controlador
        self.updateform.button_save.config(command=controller.update_contact)
        self.updateform.button_delete.config(command=controller.delete_contact)
        self.list.double_click(controller.select_contact)

    def add_contact(self, contact):
        self.list.insert(contact)
        
    def update_contacts(self, contact, index):
        self.list.update(contact, index)
            
    def remove_contact(self, index):
        self.updateform.clear()
        self.list.delete(index)
        
    def get_data(self):
        return self.updateform.get_data()
    
    def load_details(self, contact):
        self.updateform.load_details(contact)
    
    







