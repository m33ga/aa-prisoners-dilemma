def strategy_round_2(opponent_id: int, my_history: dict[int, list[int]], opponents_history: dict[int, list[int]]) -> tuple[int, int]:
    def is_toxic(history):
        return history[:5].count(0) >= 3

    def is_fibonacci(n):
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        return b == n

    current_round = len(my_history.get(opponent_id, []))
    opp_hist = opponents_history.get(opponent_id, [])
    toxic = is_toxic(opp_hist)

    if current_round == 0:
        move = 1
    elif toxic:
        if current_round >= 51:
            move = 0
        elif is_fibonacci(current_round):
            move = 0
        elif current_round % 6 == 0:
            move = 1
        elif opp_hist[-1] == 0:
            move = 0
        else:
            move = 1
    else:
        if opp_hist[-1] == 0:
            if current_round % 7 == 0:
                move = 1
            else:
                move = 0
        else:
            move = 1

    candidates = []
    for pid in opponents_history:
        if len(my_history.get(pid, [])) < 200:
            coop_score = opponents_history[pid].count(1)
            candidates.append((coop_score, -len(my_history.get(pid, [])), pid))
    if candidates:
        next_opponent = max(candidates)[2]
    else:
        next_opponent = opponent_id

    return move, next_opponent

