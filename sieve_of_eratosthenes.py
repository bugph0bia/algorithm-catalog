
# 扱う数の上限
NUMS = 100
NUMS += 1

# 添字が数値、値が素数判定結果のリストを初期化
fprimes = [True] * NUMS

# エラトステネスの篩
for i in range(2, NUMS):
    # √NUMS まで判定すれば十分
    if i > NUMS * 0.5:
        break
    # 既に素数ではないと判定されている数値はスキップ
    if not fprimes[i]:
        continue
    # その数自身を含まない倍数値はすべて素数ではないと判定する
    np = i * 2
    while np <= NUMS:
        fprimes[np] = False
        np += i

# 素数を表示
for i, flag in enumerate(fprimes):
    # 0, 1 は素数ではない
    if i < 2:
        continue
    if flag:
        print(f'{i}')
