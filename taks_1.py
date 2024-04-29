import queue
from random import Random
import time
import threading

# Створення черги заявок
request_queue = queue.Queue()


def generate_request():
    request_id = 1
    while True:
        # Створення нової заявки
        request = f"Request {request_id}"
        # Додавання заявки до черги
        request_queue.put(request)
        print(f"Заявка {request} додана до черги")
        request_id += 1
        # Затримка перед наступною генерацією заявки
        time_to_sleep = Random().randint(1, 10) * 0.2
        time.sleep(time_to_sleep)


def process_request():
    while True:
        # Перевірка, чи черга не пуста
        if not request_queue.empty():
            # Видалення заявки з черги
            request = request_queue.get()
            print(f"Заявка {request} оброблена")
        else:
            print("Черга порожня, очікування нових заявок...")
        # Затримка перед наступною перевіркою черги
        time.sleep(1)


# Створення та запуск потоків для генерації та обробки заявок
generate_thread = threading.Thread(target=generate_request)
process_thread = threading.Thread(target=process_request)
generate_thread.start()
process_thread.start()

# Очікування завершення роботи потоків
generate_thread.join()
process_thread.join()
