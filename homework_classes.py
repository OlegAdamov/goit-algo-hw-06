# Система для управління адресною книгою.

from collections import UserDict
from re import findall

class Field:    # Базовий клас для полів запису.
    def __init__(self, value):
        self.value = value
        # print(f"Field self.value: {self.value}", type(self.value))

    def __str__(self):
        return str(self.value)  # Повернення строки value


class Name(Field):  # Клас для зберігання імені контакту. Обов'язкове поле.
    
    def __init__(self, value):
        Field.__init__(self, value)
        self.name = value
        # print(f"Name self.name: {self.name}", type(self.name))


class Phone(Field):     # Клас для зберігання номера телефону. Має валідацію формату (10 цифр).

    def __init__(self, value):
        Field.__init__(self, value)
        self.phones = []
        # print(f"Phone self.phones: {self.phones}", type(self.phones))

    def is_valid_number(self, phone: str) -> bool:
        """
        Метод перевірки номера на валідність
        """
        if len(phone) != 10:
            return False

        full_digits = findall('[0-9]+', phone)
        if len(full_digits[0]) == 10:
            return True

        return False
    

class Record:       # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.

    def __init__(self, name: str):

        self.name = Name(name)
        self.phones = []
        # print(f"Record self.name: {self.name}", type(self.name))
        # print(f"Record self.phones: {self.phones}", type(self.phones))

    def add_phone(self, phone: str) -> None:
        """
        Метод для додавання телефонів.
        """
        if not self.phones.is_valid_number(phone):
            print(f"Phone {phone} is not added")

        self.phones.phones.append(phone)
        print(f"Phone {phone} is added")

    def remove_phone(self, phone: str) -> None:
        """
        Метод для видалення телефонів.
        """
        if not self.phones.is_valid_number(phone):
            print('Phone number is not valid')
        
        self.phones.phones.remove(phone)
        print(f"The phone number {phone} has been removed.")

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """
        Метод для редагування телефонів.
        """
        if not self.phones.is_valid_number(old_phone) or not self.phones.is_valid_number(new_phone):
            print('Phone number is not valid')
                
        index_old = self.phones.phones.index(old_phone)
        self.phones.phones.remove(old_phone)
        self.phones.phones.insert(index_old, new_phone)
        print("Your phone number is changed")

    def find_phone(self, phone: str) -> str:
        """
        Метод поошуку телефону.
        """
        print(f"Find phone: {phone = }; {type(phone)}")
        print(f"Find phone: {self.phones.phones = }; {type(self.phones.phones)}")
        for found_phone in self.phones.phones:
            if found_phone == phone:
                print(f"Record Find phone: {found_phone = }; {type(found_phone)}")
                return found_phone
        return f"This phone number {phone} is not in the contact list."

    def __str__(self) -> str:
        return f"Contact in Record name: {self.name.name}, phones: {'; '.join(p for p in self.phones.phones)}"


class AddressBook(UserDict):    # Клас для зберігання та управління записами.
    # реалізація класу

    """
    Видалення записів за іменем.
    """
    # def __init__(self):
    #     self.data = {}  # Record(Name: Phone)
    #     # print(f"AddressBook Init: {self.data = }; {type(self.data)}")
    #     self.value = []
    #     # print(f"AddressBook Init: {self.value = }; {type(self.value)}")


    def add_record(self, value: Record) -> None:
        """
        Метод додавання записів.
        """

        self.data[value.name.name] = value.phones.phones
        print(f"AddressBook Add record self.data: {self.data}; {type(self.data)}")
        # self.value.append(value)
        # print(f"AddressBook Add record: {self.value = }; {type(self.value)}")

    # def find(self, name: str) -> Record:
    #     """
    #     Метод пошуку записів за іменем.
    #     """
        # print(f"Address Book Find: {self.value = }; {type(self.value)}")

        # for contact in self.value:
        #     # print(f"Address Book Find For: {contact = }; {type(contact)}")
        #     # print(f"Address Book Find For: {contact.name.name = }; {type(contact.name.name)}")
        #     # print(f"Address Book Find For: {contact.phones.phones = }; {type(contact.phones.phones)}")
        #     if contact.name.name == name:
        #         return contact

            # else:
            #     return f"Your name {name} is not found"
        
    def delete(self, name: str) -> None:
        
        try:
            deleted_name = self.data.pop(name)
            print(f"Address Book Delete: {deleted_name = }")
            print(f"Name {deleted_name} removed from the contact book.")
        except KeyError:
            print(f"This name {name} is not in the contacts book.")

    def __str__(self) -> str:
        return f"Contact in AddressBook name: {self.data}"


def main():

    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")

    # Додавання запису Jane до адресної книги
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    print(book)


if __name__ == '__main__':
    main()





    