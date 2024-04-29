from collections import deque

def is_palindrome(input_string):
    # Перетворення рядка в нижній регістр та видалення пробілів
    input_string = input_string.lower().replace(" ", "")
    # Створення двосторонньої черги
    char_queue = deque(input_string)
    
    # Порівняння символів з обох кінців черги
    while len(char_queue) > 1:
        # Порівняння першого та останнього символів черги
        if char_queue.popleft() != char_queue.pop():
            return False  # Якщо символи не співпадають, рядок не є паліндромом
    return True  # Якщо всі символи співпадають, рядок є паліндромом

# Приклад використання
input_string = "A man a plan a canal Panama"
print(is_palindrome(input_string))  # Виведе: True
