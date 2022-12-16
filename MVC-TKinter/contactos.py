

class Contacto(object):
    def __init__(self, last_name, first_name, email, phone):
        self._last_name = last_name
        self._first_name = first_name
        self._email = email
        self._phone = phone
        
    #Getter
    @property
    def last_name(self):
        return self._last_name
    
    #Setter
    @last_name.setter
    def last_name(self, value):
        self._last_name = value
      
      
    #Getter
    @property
    def first_name(self):
        return self._first_name
    
    #Setter
    @first_name.setter
    def first_name(self, value):
        self._first_name = value
       
        
    #Getter
    @property
    def email(self):
        return self._email
    
    #Setter
    @email.setter
    def email(self, value):
        self._email = value
        
    #Getter
    @property
    def phone(self):
        return self._phone
    
    #Setter
    @phone.setter
    def phone(self, value):
        self._phone = value