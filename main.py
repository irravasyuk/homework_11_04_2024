# Завдання
# Користувач вводить з клавіатури набір чисел. Отримані
# числа необхідно зберегти до списку (тип списку оберіть в залежності від поставленого нижче завдання). Після чого покажіть меню, в якому запропонуєте користувачеві набір пунктів:
# 1. Додати нове число до списку (якщо таке число існує у
# списку, потрібно вивести повідомлення про це користувачеві без додавання числа).
# 2. Видалити усі входження числа зі списку (користувач вводить з клавіатури число для видалення)
# 3. Показати вміст списку (залежно від вибору користувача,
# покажіть список з початку або з кінця)
# 4. Перевірити, чи є значення у списку
# 5. Замінити значення у списку (користувач визначає, чи
# замінити тільки перше входження, чи всі)
# Дія виконується залежно від вибору користувача, після
# чого меню з’являється знову.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
        self.tail = new_node

    def delete(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print('None')

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def replace(self, old_value, new_value, replace_all=False):
        current = self.head
        while current.next:
            if current.data == old_value:
                current.data = new_value
                if not replace_all:
                    return
            current = current.next

    def menu(self):
        print('Введіть список чисел, розділених пробілами:')
        numbers = list(map(int, input().split()))
        for num in numbers:
            self.append(num)
        while True:
            print('\n1. Додати елементи.')
            print('2. Видалити елементи.')
            print('3. Показати вміст списку.')
            print('4. Перевірте, чи є значення у списку.')
            print('5. Замінити значення в списку.')
            print('6. Вийти.')
            choice = int(input('Введіть свій вибір: '))
            if choice == 1:
                value = int(input('Введіть значення для додавання: '))
                if self.search(value):
                    print('Це число вже існує в списку')
                else:
                    self.append(value)
            elif choice == 2:
                value = int(input('Введіть значення для видалення: '))
                self.delete(value)
            elif choice == 3:
                self.display()
            elif choice == 4:
                value = int(input('Введіть значення для перевірки: '))
                if self.search(value):
                    print('Значення є у списку.')
                else:
                    print('Такого значення немає в списку.')
            elif choice == 5:
                old_value = int(input("Введіть старе значення: "))
                new_value = int(input("Введіть нове значення: "))
                replace_all = input('Змінити всі входження? (y/n): ').lower() == 'y'
                self.replace(old_value, new_value, replace_all)
            elif choice == 6:
                break
            else:
                print('Неправильне значення, спробуйте ще раз.')


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.menu()
