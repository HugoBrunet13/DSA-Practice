# Given a jumbled collection of segments, each of which is represented as a
# Pair(startPoint, endPoint), this function sorts the segments to make a continuous path.
# A few assumptions you can make:
# 1. Each particular segment goes in one direction only,
# i.e.: if you see (1, 2), you will not see (2, 1).
# 2. Each starting point only have one way to the end point,
# i.e.: if you see (6, 5), you will not see (6, 10), (6, 3), etc.
# For example, if you're passed a list containing the following int arrays:
# [(4, 5), (9, 4), (5, 1), (11, 9)]
# Then your implementation should sort it such:
# [(11, 9), (9, 4), (4, 5), (5, 1)]


def get_start(points):
    print(points)
    for i in points:
        start = i
        for j in range(0, len(points)):
            if points[j] == i:
                continue
            elif i[0] == points[j][1]:
                break 
    return start

def create_continuous_path(points):
    start = get_start(points)
    path = [start]
    points.remove(start)
    n = len(points)
    for i in range(0, n):
        next = [point for point in points if point[0] == path[i][1]]   
        path.append(next[0])
        points.remove(next[0])
        n = len(points)
    

    return path


points= [(4, 5), (9, 4), (5, 1), (11, 9)]
print("Path: ",create_continuous_path(points))