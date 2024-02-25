class Dsu:
    def __init__(self, n):
        self.comp_count = n
        self.parents = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.parents[x] == x:
            return x
        ans = self.find(self.parents[x])
        self.parents[x] = ans
        return ans

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return

        if self.size[x_parent] > self.size[y_parent]:
            self.parents[y_parent] = x_parent
            self.size[x_parent] += self.size[y_parent]
        else:
            self.parents[x_parent] = y_parent
            self.size[y_parent] += self.size[x_parent]

        self.comp_count -= 1

    def get_comp_count(self):
        return self.comp_count

