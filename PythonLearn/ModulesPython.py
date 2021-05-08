import random
import time
import statistics
import re
import mysql.connector as my


scores = [6, 7, 2, 6, 3, 5, 5, 5, 2, 5, 6, 1, 2]
list_ = [10, 6, 4, 11, 1, 12, 17, 5, 7]
weights = [2, 5, 2, 5, 2, 5, 2, 5, 2]


def random_module():
    print('Random Float Number: ', random.random())
    print('Random Int between 5 and 20: ', random.randint(5, 20))
    print('Random value between 5 and 20 with step 3: ', random.randrange(5, 20, 3))
    print('Original List: ', list_)
    random.shuffle(list_)
    print('Shuffle List: ', list_)  # embaralhar
    # random com pesos diferentes para cada posição
    print('weighted choices: ', random.choices(list_, weights=(2, 5, 2, 5, 2, 5, 2, 5, 2), k=3))


def time_module():
    current_time = time.time()
    print("epoch time: ", current_time)
    local_time = str(time.ctime(current_time))
    print("local time: ", local_time)


def statistics_module():
    mean = statistics.mean(scores)
    median = statistics.median(scores)
    mode = statistics.mode(scores)
    variance = statistics.variance(scores, mean)
    standard_deviation = statistics.stdev(scores)
    print("mean: ", mean)
    print("median: ", median)
    print("mode: ", mode)
    print("variance: ", variance)
    print("standard deviation: ", standard_deviation)


def regex_module():
    string = "Hello my name is Rodolfo, I am 41 years old and I have 1 dog and I am 1.85 meters tall ;)"
    print(re.findall(r'Rodolfo', string))
    print('decimals: ', re.findall(r'\d', string))
    print('non-decimals: ', re.findall(r'\D', string))
    print('white spaces', re.findall(r'\s', string))
    print('non white spaces', re.findall(r'\S', string))
    print('alphanumeric characters:', re.findall(r'\w', string))
    print('non-alphanumeric characters:', re.findall(r'\W', string))
    print('Split string by spaces: ', re.split(r' ', string))


def mySQL_module():
    db = my.connect(host="localhost",
                       user="root",
                       password="")
    print(db)


def done_modules_test():
    time_module()
    random_module()
    statistics_module()
    regex_module()
    mySQL_module()


def main():
    try:
        done_modules_test()
    except NameError as e:
        print("There is a problem: ", e)
    finally:
        print("program end.")


main()