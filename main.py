class Sol:
    def __init__(self) -> None:
        self.path = "Dane_2212/mecz.txt"
    def zad1(self): 
        with open(self.path, "r") as f:
            a = ""
            con = 0
            for i in f.readlines():
                for j in i:
                    if j != a and a!= "":
                        con += 1
                    a = j
        return con
    def zad2(self):
        a = 0
        b = 0
        with open(self.path, "r") as f:
            for i in f.read():
                if i == "A":
                    a += 1
                else:
                    b += 1
                if a > 999 and b < a - 3:
                    return ["A", a, b]
                elif b > 999 and a < b - 3:
                    return ["B", a, b]
        return -1
    def zad3(self):
        mpass = 0
        apass = 0
        bpass = 0
        acount = 0
        bcount = 0
        lg = False
        with open(self.path, "r") as f:
            s = f.read()
            for i in range(len(s)-1):
                if s[i] == s[i+1] and s[i] == "A":
                    acount += 1
                    bcount = 0
                elif s[i] == s[i+1] and s[i] == "B":
                    bcount += 1
                    acount = 0
                if acount == 10:
                    apass = 10
                    bpass == 0
                elif bcount == 10:
                    bpass = 10
                    apass = 0
                elif acount > 10:
                    apass += 1
                elif bcount > 10:
                    bpass += 1
        ans = ""
        if apass > bpass:
            mpass = apass
            ans = "A"
        else:
            mpass = bpass
            ans = "B"
        return [mpass+1, ans]           

                
sol = Sol()
print(sol.zad1())
print()
print(sol.zad2())
print()
print(sol.zad3())
            