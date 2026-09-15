# Система для управління адресною книгою.
from collections import UserDict
from pprint import pprint

from colorama_printer_function import print_error, print_success


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
    pass


class Phone(Field):
    """
    Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    """
    def __init__(self, value):
        if len(value) == 10 and int(value):
            super().__init__(value)
        else:
            raise ValueError("Phone must be a string of 10 digits.")

class Record:
    """
    Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    """
    def __init__(self, name: str):

        self.name = Name(name)
        self.phones = []

        # print_success(f"Record Add phone, self.name: {self.name}, {type(self.name)}")

    def add_phone(self, phone: str) -> None:
        """
        Метод для додавання телефонів.
        """
        is_valid_phone = Phone(phone)
        self.phones.append(is_valid_phone)

    def remove_phone(self, phone: str) -> None:
        """
        Метод для видалення телефонів.
        """
        if not self.phones.is_valid_number(phone):
            return f"Phone number {phone} is not valid"
        
        self.phones.phones.remove(phone)
        return f"The phone number {phone} has been removed."

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """
        Метод для редагування телефонів.
        """
        is_valid_phone = Phone(new_phone)
        found_old_phone = self.find_phone(old_phone)

        if found_old_phone:
            found_old_phone.value = is_valid_phone.value
        else:
            raise ValueError(f"Phone number {old_phone} was not found for editing.")

    def find_phone(self, phone: str) -> str:
        """
        Метод поошуку телефону.
        """
        for found_phone in self.phones:
            print(found_phone)
            if found_phone.value == phone:
                return found_phone

        return None

    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """
    Клас для зберігання та управління записами.
    """
    def add_record(self, value: Record) -> None:
        """
        Метод додавання записів.
        """
        self.data[value.name.value] = value

    def find(self, name: str) -> Record:
        """
        Метод пошуку записів за іменем.
        """
        return self.data.get(name, None)

    def delete(self, name: str) -> None:
        """
        Видалення записів за іменем.
        """
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError(f"A contact with the name {name} was not found in the address book.")

    def __str__(self) -> str:
        """
        For printing our book
        """
        text = 'Contact in AddressBook:'
        new_values = self.data.values()

        for new_value in new_values:
            text += f" \n{new_value}"
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
    # print(john)
    # pprint(john)
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
