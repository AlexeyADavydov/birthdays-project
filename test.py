def sleep_one_sec():
    time.sleep(1)
    return 'Результат первой функции'

def time_of_function(func):
    def wrapper():
        start_time = time.time()
        print('Время пошло')
        result = func()
        execution_time = round(time.time() - start_time, 1)
        print(f'Через {execution_time} сек. функция вернула «{result}»')
        return result
    return wrapper

result = time_of_function(sleep_one_sec)
print(result)