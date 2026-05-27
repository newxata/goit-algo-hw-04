# Функція яка приймає рядок вводу користувача
def parse_input(user_input):
    # Повертаємо перше слово як команду та зберігаємо у змінній cmd, решту зберігаємо як список аргументів *args
    cmd, *args = user_input.split(' ')
    # Видаляємо зайві пробіли та перетворюємо на нижній регістр
    cmd = cmd.strip().lower()
    return cmd, args

# Функція додавання нового контакту до словника контактів
def add_contact(args, contacts):
    # Обмеження на введення більше значень ніж двох значень
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return 'Contact added.'
    else:
        return 'Enter name and phone.'

# Функція зміни номера телефону для контакту який вже існує в списку
def change_contact(args, contacts):
    # Обмеження на введення більше значень ніж двох значень
    if len(args) == 2:
        name, phone = args
        # Перевірка існування контакту в списку
        if name not in contacts:
            return 'Contact not found.'
        contacts[name] = phone
        return 'Contact updated.'
    else:
        return 'Enter name and phone.'

# Функція виведення номера телефону
def show_phone(args, contacts):
    # Обмеження на введення більше значень ніж одного значення
    if len(args) == 1:
        name = args[0]
        # Перевірка існування контакту в списку
        if name not in contacts:
            return 'Contact not found.'
        return contacts[name]
    else:
        return 'Enter the name.'

# Функція виведення усіх збережених контактів
def show_all(args, contacts):
    if len(args) == 0:
        return '\n'.join(f'{name}: {phone}' for name, phone in contacts.items())
    else:
        return 'Enter only "all".'

def main():
    # Створюємо словник контактів
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        # Змінна command отримує перше введене слово та стає командою, а змінна args списком з усіх інших значень
        command, args = parse_input(user_input)

        # Команда close або exit зупиняємо цикл і виходить з програми
        if command in ['close', 'exit']:
            print('Good bye!')
            break

        # Команди програми
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(args, contacts))
        else:
            print('Invalid command.')


if __name__ == '__main__':
    main()
