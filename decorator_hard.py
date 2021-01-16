import time

class Timer:
    """Класс, который можно использовать как контекстный менеджер
    с методом timed(), являющимся декоратором для замера времени выполнения функции"""
    def __init__(self, num_runs):
        self.num_runs = num_runs
    
    def __enter__(self):
        self.total_time = 0
        self.avg_time = 0
        return self

    def __exit__(self, type, value, traceback):
        self.avg_time = self.total_time / self.num_runs
        print("Выполнение заняло %.9f секунд" % self.avg_time)

    def timed(self, func):
        def wrap(arg):
            for _ in range(self.num_runs):
                start = time.time()
                return_value = func(arg)
                end = time.time()
                self.total_time += (end - start)
            return return_value
        return wrap


my_timer = Timer(10)
@my_timer.timed
def fibo(arg):
    """Функция вычисления суммы чётных элементов 
    последовательности Фибоначчи от 1 до args"""
    previous_number = 1
    current_number = 2
    odd = 0
    while current_number < arg:
        if current_number % 2 == 0:
            odd += current_number
        next_number = current_number + previous_number
        previous_number, current_number = current_number, next_number
    return odd

def main():
    num = int(input("Введите число, до которого будет вычисляться сумма чётных элементов последовательности Фибоначчи: "))
    with my_timer as mt:
        result = fibo(num)
    print("Сумма чётных элементов: {}".format(result))

if __name__ == '__main__':
    main()