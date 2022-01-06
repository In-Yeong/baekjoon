import collections, itertools

def tree_sort(n, tree):
    for i in range(n):
        for j in range(n):
            if tree[i][j] != 0:
                tree[i][j].sort()
                tree[i][j] = collections.deque(tree[i][j])
    return tree

def spring(n, tree, feed):
    dead = []
    for i in range(n):
        for j in range(n):
            if tree[i][j] != 0:
                cnt, new_tree, left_feed = spring_eat(tree[i][j], feed[i][j])
                tree[i][j] = new_tree
                feed[i][j] = left_feed
                if cnt < len(tree[i][j]):
                    dead.append([i, j, cnt])
    return dead, tree, feed

def spring_eat(tree_list, feed):
    cnt = 0
    for tree in tree_list:
        if tree <= feed:
            feed -= tree
            tree_list[cnt] += 1
            cnt += 1
        else:
            break
    return cnt, tree_list, feed


def summer(dead, tree, feed):
    for i, j, cnt in dead:
        target = collections.deque(itertools.islice(tree[i][j], cnt, None))
        new_feed = 0
        for k in target:
            new_feed += k // 2
        feed[i][j] += new_feed
        if cnt == 0:
            tree[i][j] = 0
        else:
            tree[i][j] = collections.deque(itertools.islice(tree[i][j],cnt))
    return tree, feed

def fall(n, tree):
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]
    tree_ready = []
    for i in range(n):
        for j in range(n):
            if tree[i][j] != 0:
                for k in tree[i][j]:
                    if fall_check_tree(k):
                        tree_ready.append([i,j])
    return fall_new_tree(n, tree, tree_ready)


def fall_check_tree(x):
    if x % 5 == 0:
        return True

def fall_new_tree(n, tree, tree_ready):
    d = [-1, 0, 1]
    for i, j in tree_ready:
        for x in d:
            for y in d:
                if x == 0 and y == 0:
                    continue
                elif i+x < 0 or i+x > n-1:
                    continue
                elif j+y < 0 or j+y > n-1:
                    continue
                else:
                    X = i+x
                    Y = j+y
                    if tree[X][Y] == 0:
                        tree[X][Y] = collections.deque([1])
                    else:
                        tree[X][Y].appendleft(1)
    return tree

def winter(n, feed, S2D2):
    for i in range(n):
        for j in range(n):
            feed[i][j] += S2D2[i][j]
    return feed

def year(n, tree, feed, S2D2):
    dead, tree, feed = spring(n, tree, feed)
    tree, feed = summer(dead, tree, feed)
    tree = fall(n, tree)
    feed = winter(n, feed, S2D2)
    return tree, feed

def count_tree(n, tree):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if tree[i][j] != 0:
                cnt += len(tree[i][j])
    return cnt

N, M, K = map(int, input().split())
S2D2 = []
tree = [[0]*N for _ in range(N)]
feed = [[5]*N for _ in range(N)]
for _ in range(N):
    S2D2.append(list(map(int, input().split())))
for _ in range(M):
    i, j, k = map(int, input().split())
    target = tree[i-1][j-1]
    if target == 0:
        tree[i-1][j-1] = [k]
    else:
        tree[i-1][j-1].append(k)
tree_sort(N, tree)
for _ in range(K):
    tree, feed = year(N, tree, feed, S2D2)
print(count_tree(N, tree))