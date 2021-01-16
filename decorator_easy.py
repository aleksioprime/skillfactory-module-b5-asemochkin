import time

# декоратор, позволяющий замерить время выполнения функции, в котором
# считается среднее время, определённое при нескольких повторов, 
# количество которых указано в num_runs
def run(num_runs):
    def timer(func):
        def wrap(arg):
            avg_time = 0
            for _ in range(num_runs):
                start = time.time()
                return_value = func(arg)
                end = time.time()
                avg_time += (end - start)
            avg_time /= num_runs
            print("Выполнение заняло %.9f секунд" % avg_time)
            return return_value
        return wrap
    return timer

@run(num_runs=10)
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
