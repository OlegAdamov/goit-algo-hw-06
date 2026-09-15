# Система для управління адресною книгою.
from collections import UserDict


class Field:
    """
    Base class for record fields.
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)  # Повернення строки value


class Name(Field):
    """
    A class for storing the contact name. Mandatory field.
    """
    pass


class Phone(Field):
    """
    A class for storing a phone number. It includes format validation (10 digits).
    """
    def __init__(self, value):
        if len(value) == 10 and int(value):
            super().__init__(value)
        else:
            raise ValueError("Phone must be a string of 10 digits.")

class Record:
    """
    A class for storing contact information, including the name and a list of phones.
    """
    def __init__(self, name: str):

        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone: str) -> None:
        """
        Method for adding phone.
        """
        is_valid_phone = Phone(phone)
        self.phones.append(is_valid_phone)

    def remove_phone(self, phone: str) -> None:
        """
        Method for removing phone.
        """
        phone_to_remove = self.find_phone(phone)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
        else:
            raise ValueError(f"Phone number {phone} was not found in this record.")
        
    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """
        Method for editing phone.
        """
        is_valid_phone = Phone(new_phone)
        found_old_phone = self.find_phone(old_phone)

        if found_old_phone:
            found_old_phone.value = is_valid_phone.value
        else:
            raise ValueError(f"Phone number {old_phone} was not found for editing.")

    def find_phone(self, phone: str) -> str:
        """
        Phone search method.
        """
        for found_phone in self.phones:
            if found_phone.value == phone:
                return found_phone

        return None

    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """
    A class for storing and managing records.
    """
    def add_record(self, value: Record) -> None:
        """
        Method for adding record.
        """
        self.data[value.name.value] = value

    def find(self, name: str) -> Record:
        """
        Method for searching record by name.
        """
        return self.data.get(name, None)

    def delete(self, name: str) -> None:
        """
        Deleting record by name.
        """
        if name in self.data:
            del self.data[name]
        # else:
        #     raise KeyError(f"A contact with the name {name} was not found in the address book.")

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
