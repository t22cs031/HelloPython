'''
2024/10/11
@uta

課題２発展．３回戦じゃんけんゲーム
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

# じゃんけんをシミュレートする関数（3回勝負）
def janken():
    # 勝利回数をカウント
    a_wins = 0
    b_wins = 0

    for _ in range(3):
        # AとBの手をランダムに選択
        a_hand = random.randint(0, 2)
        b_hand = random.randint(0, 2)

        # 勝敗判定
        result = determine_winner(a_hand, b_hand)

        # 結果を出力
        print(f"Aの手: {hands[a_hand]} v.s. Bの手: {hands[b_hand]} → {result}")

        # 勝利カウント
        if result == "Aの勝ち":
            a_wins += 1
        elif result == "Bの勝ち":
            b_wins += 1

    # 最終結果を判定
    print("\n最終結果:")
    if a_wins > b_wins:
        print(f"Aが{a_wins}勝で最終勝者です！")
    elif b_wins > a_wins:
        print(f"Bが{b_wins}勝で最終勝者です！")
    else:
        print("3回勝負は引き分けです！")

# 実行
if __name__ == "__main__":
    janken()
