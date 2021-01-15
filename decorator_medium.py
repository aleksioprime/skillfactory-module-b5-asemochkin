import time

# декторатор в виде класса, позволяющий замерить время выполнения функции
class Timer:
    def __init__(self, num_runs):
        self.num_runs = num_runs
        
    def __call__(self, func):
        def wrap(arg):
            avg_time = 0
            for _ in range(self.num_runs):
                start = time.time()
                return_value = func(arg)
                end = time.time()
                avg_time += (end - start)
            avg_time /= self.num_runs
            print("Выполнение заняло %.9f секунд" % avg_time)
            return return_value
        return wrap


my_timer = Timer(10)
@my_timer
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
    print("Сумма чётных элементов: {}".format(fibo(num)))

if __name__ == '__main__':
    main()
