'''
2024/10/11
@uta

課題２発展．複数人じゃんけんゲーム
'''

import random

# 手を表す辞書
hands = {0: "グー", 1: "チョキ", 2: "パー"}

# じゃんけんの勝敗を判定する関数（最強の手を返す）
def get_winner_hand(players_hands):
    # 手を集計
    unique_hands = set(players_hands)
    
    # 同じ手だけなら引き分け
    if len(unique_hands) == 1:
        return "引き分け", None

    # 最強の手を決定するロジック
    if 0 in unique_hands and 1 in unique_hands and 2 in unique_hands:
        return "引き分け", None  # グー、チョキ、パー全員が揃うと引き分け

    if 0 in unique_hands and 1 in unique_hands:  # グーが勝つ
        return "グー", 0
    elif 1 in unique_hands and 2 in unique_hands:  # チョキが勝つ
        return "チョキ", 1
    elif 2 in unique_hands and 0 in unique_hands:  # パーが勝つ
        return "パー", 2

    # 他の場合は一つの手しか残らないはず
    return hands[players_hands[0]], players_hands[0]

# じゃんけんをシミュレートする関数（1回勝負）
def janken(num_players):
    players_hands = []

    print("\nじゃんけん開始:")
    
    # 各プレイヤーの手をランダムに選択
    for i in range(num_players):
        hand = random.randint(0, 2)
        players_hands.append(hand)
        print(f"プレイヤー{i + 1}の手: {hands[hand]}")

    # 最強の手を取得
    winner_hand, winner_index = get_winner_hand(players_hands)

    if winner_hand == "引き分け":
        print("→ この勝負は引き分け")
    else:
        print(f"→ {winner_hand}を出したプレイヤーの勝ち")
        # 勝者を出力
        winners = [i + 1 for i, hand in enumerate(players_hands) if hand == winner_index]
        print(f"プレイヤー{'、'.join(map(str, winners))}が勝者です！")

# 実行
if __name__ == "__main__":
    num_players = int(input("プレイヤーの人数を入力してください: "))
    janken(num_players)
