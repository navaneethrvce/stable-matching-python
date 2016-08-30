class stable_match (object):

    def __init__(self):
        self.men = [[2,1,0],[0,1,2],[0,2,1]]
        self.women = [[0,1,2],[2,1,0],[0,2,1]]
        self.m1 = [0,1,2]
        self.w1 = [999,999,999]

    def inverse_women(self):
        self.inv_women = []
        for woman in self.women:
            temp = woman
            for w in woman :
                #print woman.index(w)
                temp[w] = woman.index(w)
            self.inv_women.append(temp)

    def algorithm_exec(self):
        while  self.m1 :
            mic = self.m1.pop(0)
            wic = self.men[mic].pop(0)
            if self.w1[wic] == 999:
                self.w1[wic] = mic
            else :
                mie = self.w1[wic]
                if self.inv_women[wic][mie] > self.inv_women[wic][mic]:
                    self.w1[wic] = mic
                    self.m1.append(mie)
                else :
                    self.m1.append(mic)


if __name__ == '__main__':
    test = stable_match()
    #print test.men[1][1]
    test.inverse_women()
    #print test.inv_women
    test.algorithm_exec()
    print test.w1