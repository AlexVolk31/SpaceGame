def intersection(list):
        x1_1 = list[0]
        y1_1 = list[1]
        x1_2 = list[2]
        y1_2 = list[3]
        x2_1 = list[4]
        y2_1 = list[5]
        x2_2 = list[6]
        y2_2 = list[7]


        A1 = y1_1 - y1_2
        B1 = x1_2 - x1_1
        C1 = x1_1 * y1_2 - x1_2 * y1_1
        A2 = y2_1 - y2_2
        B2 = x2_2 - x2_1
        C2 = x2_1 * y2_2 - x2_2 * y2_1

        def point(x, y):
                if min(x1_1, x1_2) <= x <= max(x1_1, x1_2):
                        print(x,y)
                        return True
                else:
                        return False



        if B1 * A2 - B2 * A1 and A1:
                y = (C2 * A1 - C1 * A2) / (B1 * A2 - B2 * A1)
                x = (-C1 - B1 * y) / A1
                return point(x, y)
        elif B1 * A2 - B2 * A1 and A2:
                y = (C2 * A1 - C1 * A2) / (B1 * A2 - B2 * A1)
                x = (-C2 - B2 * y) / A2
                return point(x, y)
        else:
                return False

if __name__ == "__main__":
        print(intersection(0,0,5,5,0,5,5,0))