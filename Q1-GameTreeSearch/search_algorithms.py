import math
import random
import time
from copy import deepcopy
from collections import defaultdict



class TicTacToe:
    

    def __init__(self, board=None, current_player=1):
        self.board = board if board is not None else [0] * 9
        self.current_player = current_player   # 1=X, -1=O


    def clone(self):
        return TicTacToe(self.board[:], self.current_player)

    def get_legal_moves(self):
        return [i for i, v in enumerate(self.board) if v == 0]

    def make_move(self, move):
        
        new = self.clone()
        new.board[move] = self.current_player
        new.current_player = -self.current_player
        return new

    def check_winner(self):
        
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
            (0, 4, 8), (2, 4, 6),              # diagonals
        ]
        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] != 0:
                return self.board[a]
        return 0

    def is_terminal(self):
        return self.check_winner() != 0 or not self.get_legal_moves()

    def terminal_value(self):
        
        return self.check_winner()   # ties → 0

    def __str__(self):
        sym = {1: "X", -1: "O", 0: "."}
        rows = [" ".join(sym[self.board[r * 3 + c]] for c in range(3))
                for r in range(3)]
        return "\n".join(rows)



class MinimaxSearch:
    

    def __init__(self):
        self.nodes_explored = 0

    def search(self, state):
        
        self.nodes_explored = 0
        best_move = None

        if state.current_player == 1:          # MAX player
            best_val = -math.inf
            for move in state.get_legal_moves():
                val = self._min_value(state.make_move(move))
                if val > best_val:
                    best_val, best_move = val, move
        else:                                   # MIN player
            best_val = math.inf
            for move in state.get_legal_moves():
                val = self._max_value(state.make_move(move))
                if val < best_val:
                    best_val, best_move = val, move

        return best_move, best_val

    def _max_value(self, state):
        self.nodes_explored += 1
        if state.is_terminal():
            return state.terminal_value()
        v = -math.inf
        for move in state.get_legal_moves():
            v = max(v, self._min_value(state.make_move(move)))
        return v

    def _min_value(self, state):
        self.nodes_explored += 1
        if state.is_terminal():
            return state.terminal_value()
        v = math.inf
        for move in state.get_legal_moves():
            v = min(v, self._max_value(state.make_move(move)))
        return v



class AlphaBetaSearch:
    

    def __init__(self):
        self.nodes_explored = 0

    def search(self, state):
        
        self.nodes_explored = 0
        best_move = None

        alpha, beta = -math.inf, math.inf

        if state.current_player == 1:          # MAX
            best_val = -math.inf
            for move in state.get_legal_moves():
                val = self._min_value(state.make_move(move), alpha, beta)
                if val > best_val:
                    best_val, best_move = val, move
                alpha = max(alpha, best_val)
        else:                                   # MIN
            best_val = math.inf
            for move in state.get_legal_moves():
                val = self._max_value(state.make_move(move), alpha, beta)
                if val < best_val:
                    best_val, best_move = val, move
                beta = min(beta, best_val)

        return best_move, best_val

    def _max_value(self, state, alpha, beta):
        self.nodes_explored += 1
        if state.is_terminal():
            return state.terminal_value()
        v = -math.inf
        for move in state.get_legal_moves():
            v = max(v, self._min_value(state.make_move(move), alpha, beta))
            if v >= beta:          # β-cutoff
                return v
            alpha = max(alpha, v)
        return v

    def _min_value(self, state, alpha, beta):
        self.nodes_explored += 1
        if state.is_terminal():
            return state.terminal_value()
        v = math.inf
        for move in state.get_legal_moves():
            v = min(v, self._max_value(state.make_move(move), alpha, beta))
            if v <= alpha:         # α-cutoff
                return v
            beta = min(beta, v)
        return v



def ttt_heuristic(state):
    
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    ]
    score = 0
    for a, b, c in lines:
        vals = [state.board[a], state.board[b], state.board[c]]
        x_count = vals.count(1)
        o_count = vals.count(-1)
        if x_count > 0 and o_count > 0:
            continue                       # blocked line, no value
        if x_count == 2:
            score += 10
        elif x_count == 1:
            score += 1
        if o_count == 2:
            score -= 10
        elif o_count == 1:
            score -= 1
    return score


class HeuristicAlphaBetaSearch:
    

    def __init__(self, max_depth=4, eval_fn=ttt_heuristic):
        self.max_depth = max_depth
        self.eval_fn = eval_fn
        self.nodes_explored = 0

    def search(self, state):
        
        self.nodes_explored = 0
        best_move = None
        alpha, beta = -math.inf, math.inf

        if state.current_player == 1:
            best_val = -math.inf
            for move in state.get_legal_moves():
                val = self._min_value(state.make_move(move),
                                      alpha, beta, self.max_depth - 1)
                if val > best_val:
                    best_val, best_move = val, move
                alpha = max(alpha, best_val)
        else:
            best_val = math.inf
            for move in state.get_legal_moves():
                val = self._max_value(state.make_move(move),
                                      alpha, beta, self.max_depth - 1)
                if val < best_val:
                    best_val, best_move = val, move
                beta = min(beta, best_val)

        return best_move, best_val

    def _max_value(self, state, alpha, beta, depth):
        self.nodes_explored += 1
        if state.is_terminal():
            return state.terminal_value() * 100  # scale to match heuristic
        if depth == 0:
            return self.eval_fn(state)            # ← heuristic cutoff
        v = -math.inf
        for move in state.get_legal_moves():
            v = max(v, self._min_value(state.make_move(move),
                                       alpha, beta, depth - 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def _min_value(self, state, alpha, beta, depth):
        self.nodes_explored += 1
        if state.is_terminal():
            return state.terminal_value() * 100
        if depth == 0:
            return self.eval_fn(state)            # ← heuristic cutoff
        v = math.inf
        for move in state.get_legal_moves():
            v = min(v, self._max_value(state.make_move(move),
                                       alpha, beta, depth - 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v



class MCTSNode:
    

    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move           # move that led to this node
        self.children = []
        self.wins = 0.0
        self.visits = 0
        self._untried_moves = state.get_legal_moves()

    def is_fully_expanded(self):
        return len(self._untried_moves) == 0

    def is_terminal(self):
        return self.state.is_terminal()

    def uct_score(self, c=1.414):
        
        if self.visits == 0:
            return math.inf
        exploit = self.wins / self.visits
        explore = c * math.sqrt(math.log(self.parent.visits) / self.visits)
        return exploit + explore

    def best_child(self, c=1.414):
        return max(self.children, key=lambda n: n.uct_score(c))

    def expand(self):
        
        move = self._untried_moves.pop(random.randrange(
            len(self._untried_moves)))
        child = MCTSNode(self.state.make_move(move), parent=self, move=move)
        self.children.append(child)
        return child

    def update(self, result):
        
        self.visits += 1
        self.wins += result


class MCTSSearch:
    

    def __init__(self, n_iterations=1000, c=1.414):
        self.n_iterations = n_iterations
        self.c = c

    def search(self, state):
        
        root = MCTSNode(state)

        for _ in range(self.n_iterations):
            node = self._select(root)
            if not node.is_terminal():
                node = node.expand()
            result = self._simulate(node.state)
            self._backpropagate(node, result, state.current_player)

        best = max(root.children, key=lambda n: n.visits)
        win_rate = best.wins / best.visits if best.visits else 0
        return best.move, win_rate


    def _select(self, node):
        while not node.is_terminal():
            if not node.is_fully_expanded():
                return node
            node = node.best_child(self.c)
        return node

    def _simulate(self, state):
        
        s = state.clone()
        while not s.is_terminal():
            s = s.make_move(random.choice(s.get_legal_moves()))
        return s.terminal_value()

    def _backpropagate(self, node, result, root_player):
        
        while node is not None:
            node.visits += 1
            if result == root_player:
                node.wins += 1
            elif result == 0:
                node.wins += 0.5   # draw worth half a win
            node = node.parent



def run_tests():
    results = []

    def record(name, passed, detail=""):
        status = "PASS" if passed else "FAIL"
        results.append((name, status, detail))
        print(f"  [{status}] {name}" + (f" — {detail}" if detail else ""))

    print("=" * 60)
    print("  RUNNING TEST SUITE")
    print("=" * 60)


    def make_board(symbols):
        
        m = {"X": 1, "O": -1, ".": 0}
        return [m[c] for c in symbols]

    print("\n[1] Terminal & utility tests")

    s = TicTacToe(make_board("XXX......"), current_player=-1)
    record("TTT: X wins top row", s.check_winner() == 1)
    record("TTT: is_terminal after win", s.is_terminal())

    s = TicTacToe(make_board("O..O..O.."), current_player=1)
    record("TTT: O wins left column", s.check_winner() == -1)

    s = TicTacToe(make_board("XOXOOXXXO"), current_player=-1)
    record("TTT: draw detected", s.check_winner() == 0 and s.is_terminal())

    print("\n[2] Minimax tests")
    mm = MinimaxSearch()

    move, val = mm.search(TicTacToe())
    record("Minimax: perfect play from empty = draw (val=0)", val == 0,
           f"val={val}")
    record("Minimax: move is valid (0-8)", move in range(9), f"move={move}")

    s = TicTacToe(make_board("XX......."), current_player=1)
    move, val = mm.search(s)
    record("Minimax: X takes winning move (top row)", move == 2, f"move={move}")
    record("Minimax: value = +1 (X wins)", val == 1, f"val={val}")

    s = TicTacToe(make_board("OO.XX...."), current_player=1)
    move, val = mm.search(s)
    record("Minimax: X blocks O winning move", move == 2, f"move={move}")

    mm.search(TicTacToe())
    record("Minimax: nodes explored > 0", mm.nodes_explored > 0,
           f"nodes={mm.nodes_explored}")

    print("\n[3] Alpha-Beta tests")
    ab = AlphaBetaSearch()
    mm2 = MinimaxSearch()

    ab_move, ab_val = ab.search(TicTacToe())
    mm_move, mm_val = mm2.search(TicTacToe())
    record("AlphaBeta: same value as Minimax from empty", ab_val == mm_val,
           f"ab={ab_val} mm={mm_val}")

    mismatches = 0
    for _ in range(50):
        board = [0] * 9
        player = 1
        state = TicTacToe(board[:], player)
        for __ in range(3):
            if state.is_terminal():
                break
            state = state.make_move(random.choice(state.get_legal_moves()))
        if not state.is_terminal():
            _, v_ab = AlphaBetaSearch().search(state)
            _, v_mm = MinimaxSearch().search(state)
            if v_ab != v_mm:
                mismatches += 1
    record("AlphaBeta: consistent with Minimax on 50 random states",
           mismatches == 0, f"mismatches={mismatches}")

    ab2 = AlphaBetaSearch()
    mm3 = MinimaxSearch()
    ab2.search(TicTacToe())
    mm3.search(TicTacToe())
    record("AlphaBeta: fewer nodes than Minimax",
           ab2.nodes_explored < mm3.nodes_explored,
           f"ab={ab2.nodes_explored} mm={mm3.nodes_explored}")

    s = TicTacToe(make_board("XX......."), current_player=1)
    move, val = ab.search(s)
    record("AlphaBeta: finds winning move (top row)", move == 2, f"move={move}")

    print("\n[4] Heuristic Alpha-Beta tests")

    hab_full = HeuristicAlphaBetaSearch(max_depth=9)
    hab_move, hab_val = hab_full.search(TicTacToe())
    record("HeuristicAB depth=9: returns a valid move", hab_move in range(9),
           f"move={hab_move}")

    hab1 = HeuristicAlphaBetaSearch(max_depth=1)
    m1, v1 = hab1.search(TicTacToe())
    record("HeuristicAB depth=1: returns valid move", m1 in range(9),
           f"move={m1}")

    s = TicTacToe(make_board("XX......."), current_player=1)
    move, _ = HeuristicAlphaBetaSearch(max_depth=2).search(s)
    record("HeuristicAB depth=2: finds winning move", move == 2, f"move={move}")

    hab_shallow = HeuristicAlphaBetaSearch(max_depth=3)
    hab_deep = HeuristicAlphaBetaSearch(max_depth=9)
    hab_shallow.search(TicTacToe())
    hab_deep.search(TicTacToe())
    record("HeuristicAB: shallow explores fewer nodes than deep",
           hab_shallow.nodes_explored <= hab_deep.nodes_explored,
           f"shallow={hab_shallow.nodes_explored} deep={hab_deep.nodes_explored}")

    s_good = TicTacToe(make_board("XX......."), current_player=-1)
    s_bad  = TicTacToe(make_board("OO......."), current_player=1)
    record("Heuristic: X two-in-row > 0", ttt_heuristic(s_good) > 0,
           f"score={ttt_heuristic(s_good)}")
    record("Heuristic: O two-in-row < 0", ttt_heuristic(s_bad) < 0,
           f"score={ttt_heuristic(s_bad)}")

    print("\n[5] MCTS tests")
    random.seed(42)
    mcts = MCTSSearch(n_iterations=2000)

    move, wr = mcts.search(TicTacToe())
    record("MCTS: returns valid move from empty", move in range(9),
           f"move={move}")
    record("MCTS: win rate in [0,1]", 0.0 <= wr <= 1.0, f"wr={wr:.3f}")

    random.seed(0)
    s = TicTacToe(make_board("XX......."), current_player=1)
    move, _ = MCTSSearch(n_iterations=4000).search(s)
    won = s.make_move(move).check_winner() == 1
    record("MCTS: selected move is a winning move", won, f"move={move}")

    random.seed(0)
    s = TicTacToe(make_board("OO.XX...."), current_player=1)
    move, _ = MCTSSearch(n_iterations=8000).search(s)
    record("MCTS: blocks O's winning move (cell 2)", move == 2, f"move={move}")

    def play_vs_random(algo, n=20):
        wins = 0
        for g in range(n):
            state = TicTacToe()
            while not state.is_terminal():
                if state.current_player == 1:
                    m, _ = algo.search(state)
                else:
                    m = random.choice(state.get_legal_moves())
                state = state.make_move(m)
            if state.check_winner() == 1:
                wins += 1
        return wins / n

    random.seed(0)
    win_rate = play_vs_random(MCTSSearch(n_iterations=500), n=20)
    record("MCTS: wins >50% vs random in 20 games", win_rate > 0.5,
           f"win_rate={win_rate:.2f}")

    print("\n[6] Cross-algorithm agreement tests")

    mm_e  = MinimaxSearch()
    ab_e  = AlphaBetaSearch()
    hab_e = HeuristicAlphaBetaSearch(max_depth=9)

    _, v_mm  = mm_e.search(TicTacToe())
    _, v_ab  = ab_e.search(TicTacToe())
    _, v_hab = hab_e.search(TicTacToe())

    record("Cross: MM=AB=HAB on empty board",
           v_mm == v_ab == 0,
           f"MM={v_mm} AB={v_ab}")

    algos = [
        ("Minimax",   MinimaxSearch()),
        ("AlphaBeta", AlphaBetaSearch()),
        ("HeurAB",    HeuristicAlphaBetaSearch(max_depth=4)),
        ("MCTS",      MCTSSearch(n_iterations=500)),
    ]
    for name, algo in algos:
        m, _ = algo.search(TicTacToe())
        record(f"{name}: legal move on empty board", m in range(9),
               f"move={m}")

    print("\n" + "=" * 60)
    passed = sum(1 for _, s, _ in results if s == "PASS")
    total  = len(results)
    print(f"  RESULTS: {passed}/{total} tests passed")
    print("=" * 60)
    return results



def performance_comparison():
    
    print("\n" + "=" * 60)
    print("  PERFORMANCE COMPARISON  (empty 3×3 board)")
    print("=" * 60)
    state = TicTacToe()

    configs = [
        ("Minimax",               MinimaxSearch()),
        ("Alpha-Beta",            AlphaBetaSearch()),
        ("Heuristic AB (d=4)",    HeuristicAlphaBetaSearch(max_depth=4)),
        ("Heuristic AB (d=9)",    HeuristicAlphaBetaSearch(max_depth=9)),
        ("MCTS (500 iters)",      MCTSSearch(n_iterations=500)),
        ("MCTS (2000 iters)",     MCTSSearch(n_iterations=2000)),
    ]

    for label, algo in configs:
        t0 = time.perf_counter()
        move, val = algo.search(state)
        elapsed = time.perf_counter() - t0
        nodes = getattr(algo, "nodes_explored", algo.n_iterations
                        if isinstance(algo, MCTSSearch) else "—")
        print(f"  {label:<25}  move={move}  val={val:.3f}  "
              f"nodes={nodes}  time={elapsed*1000:.1f}ms")



if __name__ == "__main__":
    random.seed(42)
    run_tests()
    performance_comparison()
