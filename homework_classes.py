# Система для управління адресною книгою.

from collections import UserDict
from re import findall

class Field:    # Базовий клас для полів запису.
    def __init__(self, value):
        self.value = value
        print(f"Field: {self.value = }")

    def __str__(self):
        return str(self.value)  # Повернення строки value


class Name(Field):  # Клас для зберігання імені контакту. Обов'язкове поле.
    
    def __init__(self, name):
        self.name = name
        # print(f"Name: {self.name = }")


class Phone(Field):     # Клас для зберігання номера телефону. Має валідацію формату (10 цифр).

    def __init__(self):
        self.phones = []
        # print(f"Phone: {self.phones = }")

    def is_valid_number(self, phone: str) -> bool:
        if len(phone) != 10:
            return False

        full_digits = findall('[0-9]+', phone)
        if len(full_digits[0]) == 10:
            return True

        return False
    

class Record:       # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = Phone()
        print(f"Record: {self.name.name = }")
        print(f"Record: {self.phones.phones = }")

    def add_phone(self, phone: str):
        """
        Функція для додавання телефонів.
        """
        if not self.phones.is_valid_number(phone):
            print(f"Phone {phone} is not added")

        self.phones.phones.append(phone)
        print(f"Phone {phone} is added")

    def remove_phone(self, phone: str):
        """
        Функція для видалення телефонів.
        """
        if not self.phones.is_valid_number(phone):
            print('Phone number is not valid')
        
        self.phones.phones.remove(phone)
        print(f"The phone number {phone} has been removed.")

    def edit_phone(self, old_phone: str, new_phone: str):
        """
        Функція для редагування телефонів.
        """
        if not self.phones.is_valid_number(old_phone) or not self.phones.is_valid_number(new_phone):
            print('Phone number is not valid')
                
        index_old = self.phones.phones.index(old_phone)
        self.phones.phones.remove(old_phone)
        self.phones.phones.insert(index_old, new_phone)
        print("Your phone number is changed")

    def find_phone(self, phone: str):
        """
        Функція поошуку телефону.
        """
        print(f"Find phone: {phone = }")
        find_phone_index = self.phones.phones.index(phone)

        print(f"Find phone: {self.phones.phones[find_phone_index] = }")
        return self.phones.phones[find_phone_index]

    def __str__(self):
        return f"Contact name: {self.name.name}, phones: {'; '.join(p for p in self.phones.phones)}"


# class AddressBook(UserDict):    # Клас для зберігання та управління записами.
#     # реалізація класу

#     """
#     Додавання записів.
#     Пошук записів за іменем.
#     Видалення записів за іменем.
#     """
#     def __init__(self, name: str):
#         self.data = {}

#     def add_record(self, data):
#         self.data.append(data)
#         self.data[name] = Record.name.value

#     def find(self, name):
#         self.data.find(name)
#         return Record or None

#     def delete(self, name):
#         self.data.delete(name)

#     def __str__(self):
#         return super().__str__()


def main():
# Створення нової адресної книги
    # book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_phone("3333333333")
    john_record.remove_phone("3333333333")

    # Додавання запису John до адресної книги
    # book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    # book.add_record(jane_record)

    # Виведення всіх записів у книзі
    # print(book)

    # Знаходження та редагування телефону для John
    # john = book.find("John")
    john_record.edit_phone("1234567890", "1112223333")

    print(john_record)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # # Пошук конкретного телефону у записі John
    found_phone = john_record.find_phone("5555555555")
    print(found_phone)
    # print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # # Видалення запису Jane
    # book.delete("Jane")


if __name__ == '__main__':
    main()





    