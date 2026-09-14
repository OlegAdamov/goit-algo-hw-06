# Система для управління адресною книгою.

from collections import UserDict
from re import findall

class Field:
    """
    Базовий клас для полів запису.
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)  # Повернення строки value


class Name(Field):
    """
    Клас для зберігання імені контакту. Обов'язкове поле.
    """
    
    def __init__(self, value):
        Field.__init__(self, value)
        self.name = value

class Phone(Field):
    """
    Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    """
    def __init__(self, value):
        Field.__init__(self, value)
        self.phones = []

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
    

class Record:
    """
    Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    """
    def __init__(self, name: str):

        self.name = Name(name)
        self.phones = Phone([])

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
            print(f"Phone number {phone} is not valid")
        
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
        for found_phone in self.phones.phones:

            if found_phone == phone:
                return found_phone

        return f"This phone number {phone} is not in the contact list."

    def __str__(self) -> str:
        return f"Contact in Record name: {self.name.name}, phones: {'; '.join(p for p in self.phones.phones)}"


class AddressBook(UserDict):
    """
    Клас для зберігання та управління записами.
    """
    def __init__(self):
        self.data = []  # Record(Name: Phone)

    def add_record(self, value: Record) -> None:
        """
        Метод додавання записів.
        """
        self.data.append(value)

    def find(self, name: str) -> Record:
        """
        Метод пошуку записів за іменем.
        """
        for data in self.data:

            if data.name:
                return data

        return f"Your name {name} is not found"
        
    def delete(self, name: str) -> None:
        """
        Видалення записів за іменем.
        """
        for data in self.data:
            if data.name.name == name:
                self.data.remove(data)
                print(f"The contact {name} is deleted")
                break
        print(f"This name {name} is not in the contacts book.")

    def __str__(self) -> str:
        """
        For printing our book
        """
        text = 'Contact in AddressBook'
        for data in self.data:
            text += f"\nname: {data.name}, phones: {data.phones.phones}"
        return text


def main():
    """
    The main menu for start script
    """
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

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

    # Виведення всіх записів у книзі
    print(book)


if __name__ == '__main__':
    main()
