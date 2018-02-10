import random
import json
import time
import sys

def getOpts():
    try:
        with open('config.json') as f:
            options = json.load(f)
    except FileNotFoundError:
        options = {'outputName': 'out.txt', 'tries': '3', 'questions': '5'}
    return options


def writeResuts(gameResults, outputName):
    with open(outputName, 'w', encoding='utf-8') as f:
        for i, q in enumerate(gameResults):
            f.write(f'Вопрос {i+1}: \n')
            success = 'да' if q['success'] == 'Yes' else 'нет'
            f.write(f'Успещно: {success} \n')
            f.write(f'Количество попыток: {q["tries"]} \n')
            f.write(f'Затраченное время: {q["time"]} \n\n\n')


if __name__ == "__main__":
    options = getOpts()
    outputName = options['outputName']
    tries = int(options['tries'])
    questions = int(options['questions'])
    try:
        leftRange = int(sys.argv[1])
    except (ValueError, IndexError):
        leftRange = 0
    try:
        rightRange = int(sys.argv[2])
    except (ValueError, IndexError):
        rightRange = 10
    print(f'Границы: {leftRange}, {rightRange}')
    gameResults = []

    for i in range(questions):
        roundResult = {}
        start_time = time.time()

        a = random.randint(leftRange, rightRange)
        b = random.randint(leftRange, rightRange)
        op = random.choice('+-*')
        results = {
            "+": a + b,
            '-': a - b,
            '*': a * b
        }
        c = results[op]
        print(str(a)+' '+op+' '+str(b)+'?')
        curTry = 0

        while curTry < tries:
            while True:
                try:
                    print('Ваш ответ: ', end='')
                    answer = int(input())
                    break
                except ValueError:
                    print('Некорректный ввод')
            if answer == c:
                break
            else:
                curTry += 1
                print('Неверно! Попробуйте ещё раз.')

        roundResult['time'] = round(time.time() - start_time, 2)

        if curTry == tries:
            print('Вы проиграли. Идите во второй класс, там вас научат считать.')
            roundResult['tries'] = curTry
            roundResult['success'] = 'No'
            gameResults.append(roundResult)
            break

        roundResult['tries'] = curTry + 1
        roundResult['success'] = 'Yes'
        gameResults.append(roundResult)
        print('Верно!')

    writeResuts(gameResults, outputName)