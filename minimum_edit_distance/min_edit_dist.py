import numpy as np

def minimum_edit_distance(source: str,
                          target: str, 
                          del_c : int, 
                          ins_c : int, 
                          subs_c: int,
                          retrackt_path: bool=True):

    n = len(source)
    m = len(target)

    dist_mat = np.zeros((n+1, m+1), dtype=int)
    path     = np.zeros((n+1, m+1), dtype=int)

    for i in range(1,dist_mat.shape[0]):
        dist_mat[i,0] = dist_mat[i-1,0] + del_c
    for j in range(1,dist_mat.shape[1]):
        dist_mat[0,j] = dist_mat[0,j-1] + ins_c

    for i in range(1,dist_mat.shape[0]):
        for j in range(1,dist_mat.shape[1]):
            c = (dist_mat[i-1,j-1] + subs_c) if source[i-1] != target[j-1] else dist_mat[i-1,j-1]
            l = dist_mat[i,j-1] + ins_c
            t = dist_mat[i-1,j] + del_c
            curr = min(c,l,t)
            if curr == c:
                path[i,j] = 0
            elif curr == t:
                path[i,j] = -1
            else:
                path[i,j] = 1
            dist_mat[i,j] = curr

    if retrackt_path:
        src = ''
        trg = ''

        path_best = []
        i = path.shape[0] - 1
        j = path.shape[1] - 1
        path_best.append((i,j))

        while i != 0 and j != 0:
            if path[i,j] == 1:
                src = src + '|'
                trg = trg + target[j-1]
                j -= 1
            elif path[i,j] == -1:
                src = src + source[i-1]
                trg = trg + '|'
                i -= 1
            else:
                src = src + source[i-1]
                trg = trg + target[j-1]
                i -= 1
                j -= 1

            path_best.append((i,j))

        print('Minimum Edit Distance: ', dist_mat[n,m])
        print('Best path is: ', path_best[::-1])
        print('Alignment:')
        print(src[::-1])
        print(trg[::-1])

    

