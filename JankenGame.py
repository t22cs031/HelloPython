'''
2024/10/11
@uta

課題２．じゃんけんゲーム
'''

import random

# 手を表す辞書
hands = {0: "グー", 1: "チョキ", 2: "パー"}

# 勝敗を判定する関数
def determine_winner(a, b):
    if a == b:
        return "引き分け"
    elif (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
        return "Aの勝ち"
    else:
        return "Bの勝ち"

# じゃんけんをシミュレートする関数
def janken():
    # AとBの手をランダムに選択
    a_hand = random.randint(0, 2)
    b_hand = random.randint(0, 2)

    # 勝敗判定
    result = determine_winner(a_hand, b_hand)

    # 結果を出力
    print(f"Aの手: {hands[a_hand]} v.s. Bの手: {hands[b_hand]} → {result}")

# 実行
if __name__ == "__main__":
    janken()
