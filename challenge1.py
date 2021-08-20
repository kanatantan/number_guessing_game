import random

name = input('名前を入力してください。: ')

print(f' {name}さん、こんにちは。さっそく数当てゲームを始めます。')
print(' 数字は1~100までの整数から選んでください。')

answer = random.randrange(start=1, stop=100)
sellected = int(input('数字を入力してください。: '))
counts = 1

low = []
high = []
lowerLimit = 0
upperLimit = 101

while answer != sellected:
    if (sellected < 1) or (sellected > 100):
        print(' 数字は1~100までの整数から選んでください。')
    elif answer > sellected:
        print(' ハズレ～!!')
        print(' ヒント：もっと大きい数字です。')
        low.append(sellected)
        low.sort()
        lowerLimit = low[-1]
        probability = 100 / (int(upperLimit) - int(lowerLimit) - 1)
        lowerLimitX = int(lowerLimit) + 1
        upperLimitX = int(upperLimit) - 1
        print(f' {lowerLimitX}から{upperLimitX}まで絞り込みました。')
        print(f' 次に正解する確率は、{probability:.2f}%です!')
        counts += 1
        print(f'次は{counts}回目の挑戦です。')
    else:
        print(' ハズレ～!!')
        print(' ヒント：もっと小さい数字です。')
        high.append(sellected)
        high.sort()
        upperLimit = high[0]
        probability = 100 / (int(upperLimit) - int(lowerLimit) - 1)
        lowerLimitX = int(lowerLimit) + 1
        upperLimitX = int(upperLimit) - 1
        print(f' {lowerLimitX}から{upperLimitX}まで絞り込みました。')
        print(f' 次に正解する確率は、{probability:.2f}%です')
        counts += 1
        print(f'次は{counts}回目の挑戦です。')

    sellected = int(input('数字を入力してください。 : '))

print(' 正解です！')
print(fr'{name}さん、あなたは "{counts}回目" で正解しました。')
print('遊んでくれてありがとう！')
