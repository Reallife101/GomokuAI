from graphics import *
import numpy as np


def isClicked(rect, mousePos):
    p1 = rect.getP1()
    p2 = rect.getP2()
    # print(p2.x)
    if (mousePos.x > p2.x) & (mousePos.x < p1.x) & (mousePos.y > p1.y) & (mousePos.y < p2.y):
        return 1
    else:
        return 0

def main():
    i = 1
    # a = np.array([[15],[15],[15],[15],[15],[15],[15],[15][15][15][15][15][15][15][15]])
    # a = [15]
    # for x in a:
    #     if x <= 14:
    #         a[i] = 'p'
        # for x in i:
        #     a[i][x] = 'p'
    # print(a[0])
    win = GraphWin('ExampleWindow', 750, 750)
    rect = Rectangle(Point(50, 0), Point(0, 50))
    rect.setFill('purple')
    rect2 = Rectangle(Point(100, 0), Point(50, 50))
    rect2.setFill('purple')
    rect3 = Rectangle(Point(150, 0), Point(100, 50))
    rect3.setFill('purple')
    rect4 = Rectangle(Point(200, 0), Point(150, 50))
    rect4.setFill('purple')
    rect5 = Rectangle(Point(250, 0), Point(200, 50))
    rect5.setFill('purple')
    rect6 = Rectangle(Point(300, 0), Point(250, 50))
    rect6.setFill('purple')
    rect7 = Rectangle(Point(350, 0), Point(300, 50))
    rect7.setFill('purple')
    rect8 = Rectangle(Point(400, 0), Point(350, 50))
    rect8.setFill('purple')
    rect9 = Rectangle(Point(450, 0), Point(400, 50))
    rect9.setFill('purple')
    rect10 = Rectangle(Point(500, 0), Point(450, 50))
    rect10.setFill('purple')
    rect11 = Rectangle(Point(550, 0), Point(500, 50))
    rect11.setFill('purple')
    rect12 = Rectangle(Point(600, 0), Point(550, 50))
    rect12.setFill('purple')
    rect13 = Rectangle(Point(650, 0), Point(600, 50))
    rect13.setFill('purple')
    rect14 = Rectangle(Point(700, 0), Point(650, 50))
    rect14.setFill('purple')
    rect15 = Rectangle(Point(750, 0), Point(700, 50))
    rect15.setFill('purple')

    rect21 = Rectangle(Point(50, 50), Point(0, 100))
    rect21.setFill('purple')
    rect22 = Rectangle(Point(100, 50), Point(50, 100))
    rect22.setFill('purple')
    rect23 = Rectangle(Point(150, 50), Point(100, 100))
    rect23.setFill('purple')
    rect24 = Rectangle(Point(200, 50), Point(150, 100))
    rect24.setFill('purple')
    rect25 = Rectangle(Point(250, 50), Point(200, 100))
    rect25.setFill('purple')
    rect26 = Rectangle(Point(300, 50), Point(250, 100))
    rect26.setFill('purple')
    rect27 = Rectangle(Point(350, 50), Point(300, 100))
    rect27.setFill('purple')
    rect28 = Rectangle(Point(400, 50), Point(350, 100))
    rect28.setFill('purple')
    rect29 = Rectangle(Point(450, 50), Point(400, 100))
    rect29.setFill('purple')
    rect210 = Rectangle(Point(500, 50), Point(450, 100))
    rect210.setFill('purple')
    rect211 = Rectangle(Point(550, 50), Point(500, 100))
    rect211.setFill('purple')
    rect212 = Rectangle(Point(600, 50), Point(550, 100))
    rect212.setFill('purple')
    rect213 = Rectangle(Point(650, 50), Point(600, 100))
    rect213.setFill('purple')
    rect214 = Rectangle(Point(700, 50), Point(650, 100))
    rect214.setFill('purple')
    rect215 = Rectangle(Point(750, 50), Point(700, 100))
    rect215.setFill('purple')

    rect31 = Rectangle(Point(50, 100), Point(0, 150))
    rect31.setFill('purple')
    rect32 = Rectangle(Point(100, 100), Point(50, 150))
    rect32.setFill('purple')
    rect33 = Rectangle(Point(150, 100), Point(100, 150))
    rect33.setFill('purple')
    rect34 = Rectangle(Point(200, 100), Point(150, 150))
    rect34.setFill('purple')
    rect35 = Rectangle(Point(250, 100), Point(200, 150))
    rect35.setFill('purple')
    rect36 = Rectangle(Point(300, 100), Point(250, 150))
    rect36.setFill('purple')
    rect37 = Rectangle(Point(350, 100), Point(300, 150))
    rect37.setFill('purple')
    rect38 = Rectangle(Point(400, 100), Point(350, 150))
    rect38.setFill('purple')
    rect39 = Rectangle(Point(450, 100), Point(400, 150))
    rect39.setFill('purple')
    rect310 = Rectangle(Point(500, 100), Point(450, 150))
    rect310.setFill('purple')
    rect311 = Rectangle(Point(550, 100), Point(500, 150))
    rect311.setFill('purple')
    rect312 = Rectangle(Point(600, 100), Point(550, 150))
    rect312.setFill('purple')
    rect313 = Rectangle(Point(650, 100), Point(600, 150))
    rect313.setFill('purple')
    rect314 = Rectangle(Point(700, 100), Point(650, 150))
    rect314.setFill('purple')
    rect315 = Rectangle(Point(750, 100), Point(700, 150))
    rect315.setFill('purple')

    rect41 = Rectangle(Point(50, 150), Point(0, 200))
    rect41.setFill('purple')
    rect42 = Rectangle(Point(100, 150), Point(50, 200))
    rect42.setFill('purple')
    rect43 = Rectangle(Point(150, 150), Point(100, 200))
    rect43.setFill('purple')
    rect44 = Rectangle(Point(200, 150), Point(150, 200))
    rect44.setFill('purple')
    rect45 = Rectangle(Point(250, 150), Point(200, 200))
    rect45.setFill('purple')
    rect46 = Rectangle(Point(300, 150), Point(250, 200))
    rect46.setFill('purple')
    rect47 = Rectangle(Point(350, 150), Point(300, 200))
    rect47.setFill('purple')
    rect48 = Rectangle(Point(400, 150), Point(350, 200))
    rect48.setFill('purple')
    rect49 = Rectangle(Point(450, 150), Point(400, 200))
    rect49.setFill('purple')
    rect410 = Rectangle(Point(500, 150), Point(450, 200))
    rect410.setFill('purple')
    rect411 = Rectangle(Point(550, 150), Point(500, 200))
    rect411.setFill('purple')
    rect412 = Rectangle(Point(600, 150), Point(550, 200))
    rect412.setFill('purple')
    rect413 = Rectangle(Point(650, 150), Point(600, 200))
    rect413.setFill('purple')
    rect414 = Rectangle(Point(700, 150), Point(650, 200))
    rect414.setFill('purple')
    rect415 = Rectangle(Point(750, 150), Point(700, 200))
    rect415.setFill('purple')

    rect51 = Rectangle(Point(50, 200), Point(0, 250))
    rect51.setFill('purple')
    rect52 = Rectangle(Point(100, 200), Point(50, 250))
    rect52.setFill('purple')
    rect53 = Rectangle(Point(150, 200), Point(100, 250))
    rect53.setFill('purple')
    rect54 = Rectangle(Point(200, 200), Point(150, 250))
    rect54.setFill('purple')
    rect55 = Rectangle(Point(250, 200), Point(200, 250))
    rect55.setFill('purple')
    rect56 = Rectangle(Point(300, 200), Point(250, 250))
    rect56.setFill('purple')
    rect57 = Rectangle(Point(350, 200), Point(300, 250))
    rect57.setFill('purple')
    rect58 = Rectangle(Point(400, 200), Point(350, 250))
    rect58.setFill('purple')
    rect59 = Rectangle(Point(450, 200), Point(400, 250))
    rect59.setFill('purple')
    rect510 = Rectangle(Point(500, 200), Point(450, 250))
    rect510.setFill('purple')
    rect511 = Rectangle(Point(550, 200), Point(500, 250))
    rect511.setFill('purple')
    rect512 = Rectangle(Point(600, 200), Point(550, 250))
    rect512.setFill('purple')
    rect513 = Rectangle(Point(650, 200), Point(600, 250))
    rect513.setFill('purple')
    rect514 = Rectangle(Point(700, 200), Point(650, 250))
    rect514.setFill('purple')
    rect515 = Rectangle(Point(750, 200), Point(700, 250))
    rect515.setFill('purple')

    rect61 = Rectangle(Point(50, 250), Point(0, 300))
    rect61.setFill('purple')
    rect62 = Rectangle(Point(100, 250), Point(50, 300))
    rect62.setFill('purple')
    rect63 = Rectangle(Point(150, 250), Point(100, 300))
    rect63.setFill('purple')
    rect64 = Rectangle(Point(200, 250), Point(150, 300))
    rect64.setFill('purple')
    rect65 = Rectangle(Point(250, 250), Point(200, 300))
    rect65.setFill('purple')
    rect66 = Rectangle(Point(300, 250), Point(250, 300))
    rect66.setFill('purple')
    rect67 = Rectangle(Point(350, 250), Point(300, 300))
    rect67.setFill('purple')
    rect68 = Rectangle(Point(400, 250), Point(350, 300))
    rect68.setFill('purple')
    rect69 = Rectangle(Point(450, 250), Point(400, 300))
    rect69.setFill('purple')
    rect610 = Rectangle(Point(500, 250), Point(450, 300))
    rect610.setFill('purple')
    rect611 = Rectangle(Point(550, 250), Point(500, 300))
    rect611.setFill('purple')
    rect612 = Rectangle(Point(600, 250), Point(550, 300))
    rect612.setFill('purple')
    rect613 = Rectangle(Point(650, 250), Point(600, 300))
    rect613.setFill('purple')
    rect614 = Rectangle(Point(700, 250), Point(650, 300))
    rect614.setFill('purple')
    rect615 = Rectangle(Point(750, 250), Point(700, 300))
    rect615.setFill('purple')

    rect71 = Rectangle(Point(50, 300), Point(0, 350))
    rect71.setFill('purple')
    rect72 = Rectangle(Point(100, 300), Point(50, 350))
    rect72.setFill('purple')
    rect73 = Rectangle(Point(150, 300), Point(100, 350))
    rect73.setFill('purple')
    rect74 = Rectangle(Point(200, 300), Point(150, 350))
    rect74.setFill('purple')
    rect75 = Rectangle(Point(250, 300), Point(200, 350))
    rect75.setFill('purple')
    rect76 = Rectangle(Point(300, 300), Point(250, 350))
    rect76.setFill('purple')
    rect77 = Rectangle(Point(350, 300), Point(300, 350))
    rect77.setFill('purple')
    rect78 = Rectangle(Point(400, 300), Point(350, 350))
    rect78.setFill('purple')
    rect79 = Rectangle(Point(450, 300), Point(400, 350))
    rect79.setFill('purple')
    rect710 = Rectangle(Point(500, 300), Point(450, 350))
    rect710.setFill('purple')
    rect711 = Rectangle(Point(550, 300), Point(500, 350))
    rect711.setFill('purple')
    rect712 = Rectangle(Point(600, 300), Point(550, 350))
    rect712.setFill('purple')
    rect713 = Rectangle(Point(650, 300), Point(600, 350))
    rect713.setFill('purple')
    rect714 = Rectangle(Point(700, 300), Point(650, 350))
    rect714.setFill('purple')
    rect715 = Rectangle(Point(750, 300), Point(700, 350))
    rect715.setFill('purple')

    rect81 = Rectangle(Point(50, 350), Point(0, 400))
    rect81.setFill('purple')
    rect82 = Rectangle(Point(100, 350), Point(50, 400))
    rect82.setFill('purple')
    rect83 = Rectangle(Point(150, 350), Point(100, 400))
    rect83.setFill('purple')
    rect84 = Rectangle(Point(200, 350), Point(150, 400))
    rect84.setFill('purple')
    rect85 = Rectangle(Point(250, 350), Point(200, 400))
    rect85.setFill('purple')
    rect86 = Rectangle(Point(300, 350), Point(250, 400))
    rect86.setFill('purple')
    rect87 = Rectangle(Point(350, 350), Point(300, 400))
    rect87.setFill('purple')
    rect88 = Rectangle(Point(400, 350), Point(350, 400))
    rect88.setFill('purple')
    rect89 = Rectangle(Point(450, 350), Point(400, 400))
    rect89.setFill('purple')
    rect810 = Rectangle(Point(500, 350), Point(450, 400))
    rect810.setFill('purple')
    rect811 = Rectangle(Point(550, 350), Point(500, 400))
    rect811.setFill('purple')
    rect812 = Rectangle(Point(600, 350), Point(550, 400))
    rect812.setFill('purple')
    rect813 = Rectangle(Point(650, 350), Point(600, 400))
    rect813.setFill('purple')
    rect814 = Rectangle(Point(700, 350), Point(650, 400))
    rect814.setFill('purple')
    rect815 = Rectangle(Point(750, 350), Point(700, 400))
    rect815.setFill('purple')

    rect91 = Rectangle(Point(50, 400), Point(0, 450))
    rect91.setFill('purple')
    rect92 = Rectangle(Point(100, 400), Point(50, 450))
    rect92.setFill('purple')
    rect93 = Rectangle(Point(150, 400), Point(100, 450))
    rect93.setFill('purple')
    rect94 = Rectangle(Point(200, 400), Point(150, 450))
    rect94.setFill('purple')
    rect95 = Rectangle(Point(250, 400), Point(200, 450))
    rect95.setFill('purple')
    rect96 = Rectangle(Point(300, 400), Point(250, 450))
    rect96.setFill('purple')
    rect97 = Rectangle(Point(350, 400), Point(300, 450))
    rect97.setFill('purple')
    rect98 = Rectangle(Point(400, 400), Point(350, 450))
    rect98.setFill('purple')
    rect99 = Rectangle(Point(450, 400), Point(400, 450))
    rect99.setFill('purple')
    rect910 = Rectangle(Point(500, 400), Point(450, 450))
    rect910.setFill('purple')
    rect911 = Rectangle(Point(550, 400), Point(500, 450))
    rect911.setFill('purple')
    rect912 = Rectangle(Point(600, 400), Point(550, 450))
    rect912.setFill('purple')
    rect913 = Rectangle(Point(650, 400), Point(600, 450))
    rect913.setFill('purple')
    rect914 = Rectangle(Point(700, 400), Point(650, 450))
    rect914.setFill('purple')
    rect915 = Rectangle(Point(750, 400), Point(700, 450))
    rect915.setFill('purple')

    rect101 = Rectangle(Point(50, 450), Point(0, 500))
    rect101.setFill('purple')
    rect102 = Rectangle(Point(100, 450), Point(50, 500))
    rect102.setFill('purple')
    rect103 = Rectangle(Point(150, 450), Point(100, 500))
    rect103.setFill('purple')
    rect104 = Rectangle(Point(200, 450), Point(150, 500))
    rect104.setFill('purple')
    rect105 = Rectangle(Point(250, 450), Point(200, 500))
    rect105.setFill('purple')
    rect106 = Rectangle(Point(300, 450), Point(250, 500))
    rect106.setFill('purple')
    rect107 = Rectangle(Point(350, 450), Point(300, 500))
    rect107.setFill('purple')
    rect108 = Rectangle(Point(400, 450), Point(350, 500))
    rect108.setFill('purple')
    rect109 = Rectangle(Point(450, 450), Point(400, 500))
    rect109.setFill('purple')
    rect1010 = Rectangle(Point(500, 450), Point(450, 500))
    rect1010.setFill('purple')
    rect1011 = Rectangle(Point(550, 450), Point(500, 500))
    rect1011.setFill('purple')
    rect1012 = Rectangle(Point(600, 450), Point(550, 500))
    rect1012.setFill('purple')
    rect1013 = Rectangle(Point(650, 450), Point(600, 500))
    rect1013.setFill('purple')
    rect1014 = Rectangle(Point(700, 450), Point(650, 500))
    rect1014.setFill('purple')
    rect1015 = Rectangle(Point(750, 450), Point(700, 500))
    rect1015.setFill('purple')

    rect111 = Rectangle(Point(50, 500), Point(0, 550))
    rect111.setFill('purple')
    rect112 = Rectangle(Point(100, 500), Point(50, 550))
    rect112.setFill('purple')
    rect113 = Rectangle(Point(150, 500), Point(100, 550))
    rect113.setFill('purple')
    rect114 = Rectangle(Point(200, 500), Point(150, 550))
    rect114.setFill('purple')
    rect115 = Rectangle(Point(250, 500), Point(200, 550))
    rect115.setFill('purple')
    rect116 = Rectangle(Point(300, 500), Point(250, 550))
    rect116.setFill('purple')
    rect117 = Rectangle(Point(350, 500), Point(300, 550))
    rect117.setFill('purple')
    rect118 = Rectangle(Point(400, 500), Point(350, 550))
    rect118.setFill('purple')
    rect119 = Rectangle(Point(450, 500), Point(400, 550))
    rect119.setFill('purple')
    rect1110 = Rectangle(Point(500, 500), Point(450, 550))
    rect1110.setFill('purple')
    rect1111 = Rectangle(Point(550, 500), Point(500, 550))
    rect1111.setFill('purple')
    rect1112 = Rectangle(Point(600, 500), Point(550, 550))
    rect1112.setFill('purple')
    rect1113 = Rectangle(Point(650, 500), Point(600, 550))
    rect1113.setFill('purple')
    rect1114 = Rectangle(Point(700, 500), Point(650, 550))
    rect1114.setFill('purple')
    rect1115 = Rectangle(Point(750, 500), Point(700, 550))
    rect1115.setFill('purple')

    rect121 = Rectangle(Point(50, 550), Point(0, 600))
    rect121.setFill('purple')
    rect122 = Rectangle(Point(100, 550), Point(50, 600))
    rect122.setFill('purple')
    rect123 = Rectangle(Point(150, 550), Point(100, 600))
    rect123.setFill('purple')
    rect124 = Rectangle(Point(200, 550), Point(150, 600))
    rect124.setFill('purple')
    rect125 = Rectangle(Point(250, 550), Point(200, 600))
    rect125.setFill('purple')
    rect126 = Rectangle(Point(300, 550), Point(250, 600))
    rect126.setFill('purple')
    rect127 = Rectangle(Point(350, 550), Point(300, 600))
    rect127.setFill('purple')
    rect128 = Rectangle(Point(400, 550), Point(350, 600))
    rect128.setFill('purple')
    rect129 = Rectangle(Point(450, 550), Point(400, 600))
    rect129.setFill('purple')
    rect1210 = Rectangle(Point(500, 550), Point(450, 600))
    rect1210.setFill('purple')
    rect1211 = Rectangle(Point(550, 550), Point(500, 600))
    rect1211.setFill('purple')
    rect1212 = Rectangle(Point(600, 550), Point(550, 600))
    rect1212.setFill('purple')
    rect1213 = Rectangle(Point(650, 550), Point(600, 600))
    rect1213.setFill('purple')
    rect1214 = Rectangle(Point(700, 550), Point(650, 600))
    rect1214.setFill('purple')
    rect1215 = Rectangle(Point(750, 550), Point(700, 600))
    rect1215.setFill('purple')

    rect131 = Rectangle(Point(50, 600), Point(0, 650))
    rect131.setFill('purple')
    rect132 = Rectangle(Point(100, 600), Point(50, 650))
    rect132.setFill('purple')
    rect133 = Rectangle(Point(150, 600), Point(100, 650))
    rect133.setFill('purple')
    rect134 = Rectangle(Point(200, 600), Point(150, 650))
    rect134.setFill('purple')
    rect135 = Rectangle(Point(250, 600), Point(200, 650))
    rect135.setFill('purple')
    rect136 = Rectangle(Point(300, 600), Point(250, 650))
    rect136.setFill('purple')
    rect137 = Rectangle(Point(350, 600), Point(300, 650))
    rect137.setFill('purple')
    rect138 = Rectangle(Point(400, 600), Point(350, 650))
    rect138.setFill('purple')
    rect139 = Rectangle(Point(450, 600), Point(400, 650))
    rect139.setFill('purple')
    rect1310 = Rectangle(Point(500, 600), Point(450, 650))
    rect1310.setFill('purple')
    rect1311 = Rectangle(Point(550, 600), Point(500, 650))
    rect1311.setFill('purple')
    rect1312 = Rectangle(Point(600, 600), Point(550, 650))
    rect1312.setFill('purple')
    rect1313 = Rectangle(Point(650, 600), Point(600, 650))
    rect1313.setFill('purple')
    rect1314 = Rectangle(Point(700, 600), Point(650, 650))
    rect1314.setFill('purple')
    rect1315 = Rectangle(Point(750, 600), Point(700, 650))
    rect1315.setFill('purple')

    rect141 = Rectangle(Point(50, 650), Point(0, 700))
    rect141.setFill('purple')
    rect142 = Rectangle(Point(100, 650), Point(50, 700))
    rect142.setFill('purple')
    rect143 = Rectangle(Point(150, 650), Point(100, 700))
    rect143.setFill('purple')
    rect144 = Rectangle(Point(200, 650), Point(150, 700))
    rect144.setFill('purple')
    rect145 = Rectangle(Point(250, 650), Point(200, 700))
    rect145.setFill('purple')
    rect146 = Rectangle(Point(300, 650), Point(250, 700))
    rect146.setFill('purple')
    rect147 = Rectangle(Point(350, 650), Point(300, 700))
    rect147.setFill('purple')
    rect148 = Rectangle(Point(400, 650), Point(350, 700))
    rect148.setFill('purple')
    rect149 = Rectangle(Point(450, 650), Point(400, 700))
    rect149.setFill('purple')
    rect1410 = Rectangle(Point(500, 650), Point(450, 700))
    rect1410.setFill('purple')
    rect1411 = Rectangle(Point(550, 650), Point(500, 700))
    rect1411.setFill('purple')
    rect1412 = Rectangle(Point(600, 650), Point(550, 700))
    rect1412.setFill('purple')
    rect1413 = Rectangle(Point(650, 650), Point(600, 700))
    rect1413.setFill('purple')
    rect1414 = Rectangle(Point(700, 650), Point(650, 700))
    rect1414.setFill('purple')
    rect1415 = Rectangle(Point(750, 650), Point(700, 700))
    rect1415.setFill('purple')

    rect151 = Rectangle(Point(50, 700), Point(0, 750))
    rect151.setFill('purple')
    rect152 = Rectangle(Point(100, 700), Point(50, 750))
    rect152.setFill('purple')
    rect153 = Rectangle(Point(150, 700), Point(100, 750))
    rect153.setFill('purple')
    rect154 = Rectangle(Point(200, 700), Point(150, 750))
    rect154.setFill('purple')
    rect155 = Rectangle(Point(250, 700), Point(200, 750))
    rect155.setFill('purple')
    rect156 = Rectangle(Point(300, 700), Point(250, 750))
    rect156.setFill('purple')
    rect157 = Rectangle(Point(350, 700), Point(300, 750))
    rect157.setFill('purple')
    rect158 = Rectangle(Point(400, 700), Point(350, 750))
    rect158.setFill('purple')
    rect159 = Rectangle(Point(450, 700), Point(400, 750))
    rect159.setFill('purple')
    rect1510 = Rectangle(Point(500, 700), Point(450, 750))
    rect1510.setFill('purple')
    rect1511 = Rectangle(Point(550, 700), Point(500, 750))
    rect1511.setFill('purple')
    rect1512 = Rectangle(Point(600, 700), Point(550, 750))
    rect1512.setFill('purple')
    rect1513 = Rectangle(Point(650, 700), Point(600, 750))
    rect1513.setFill('purple')
    rect1514 = Rectangle(Point(700, 700), Point(650, 750))
    rect1514.setFill('purple')
    rect1515 = Rectangle(Point(750, 700), Point(700, 750))
    rect1515.setFill('purple')

    rect.draw(win)
    rect2.draw(win)
    rect3.draw(win)
    rect4.draw(win)
    rect5.draw(win)
    rect6.draw(win)
    rect7.draw(win)
    rect8.draw(win)
    rect9.draw(win)
    rect10.draw(win)
    rect11.draw(win)
    rect12.draw(win)
    rect13.draw(win)
    rect14.draw(win)
    rect15.draw(win)

    rect21.draw(win)
    rect22.draw(win)
    rect23.draw(win)
    rect24.draw(win)
    rect25.draw(win)
    rect26.draw(win)
    rect27.draw(win)
    rect28.draw(win)
    rect29.draw(win)
    rect210.draw(win)
    rect211.draw(win)
    rect212.draw(win)
    rect213.draw(win)
    rect214.draw(win)
    rect215.draw(win)

    rect31.draw(win)
    rect32.draw(win)
    rect33.draw(win)
    rect34.draw(win)
    rect35.draw(win)
    rect36.draw(win)
    rect37.draw(win)
    rect38.draw(win)
    rect39.draw(win)
    rect310.draw(win)
    rect311.draw(win)
    rect312.draw(win)
    rect313.draw(win)
    rect314.draw(win)
    rect315.draw(win)

    rect41.draw(win)
    rect42.draw(win)
    rect43.draw(win)
    rect44.draw(win)
    rect45.draw(win)
    rect46.draw(win)
    rect47.draw(win)
    rect48.draw(win)
    rect49.draw(win)
    rect410.draw(win)
    rect411.draw(win)
    rect412.draw(win)
    rect413.draw(win)
    rect414.draw(win)
    rect415.draw(win)

    rect51.draw(win)
    rect52.draw(win)
    rect53.draw(win)
    rect54.draw(win)
    rect55.draw(win)
    rect56.draw(win)
    rect57.draw(win)
    rect58.draw(win)
    rect59.draw(win)
    rect510.draw(win)
    rect511.draw(win)
    rect512.draw(win)
    rect513.draw(win)
    rect514.draw(win)
    rect515.draw(win)

    rect61.draw(win)
    rect62.draw(win)
    rect63.draw(win)
    rect64.draw(win)
    rect65.draw(win)
    rect66.draw(win)
    rect67.draw(win)
    rect68.draw(win)
    rect69.draw(win)
    rect610.draw(win)
    rect611.draw(win)
    rect612.draw(win)
    rect613.draw(win)
    rect614.draw(win)
    rect615.draw(win)

    rect71.draw(win)
    rect72.draw(win)
    rect73.draw(win)
    rect74.draw(win)
    rect75.draw(win)
    rect76.draw(win)
    rect77.draw(win)
    rect78.draw(win)
    rect79.draw(win)
    rect710.draw(win)
    rect711.draw(win)
    rect712.draw(win)
    rect713.draw(win)
    rect714.draw(win)
    rect715.draw(win)

    rect81.draw(win)
    rect82.draw(win)
    rect83.draw(win)
    rect84.draw(win)
    rect85.draw(win)
    rect86.draw(win)
    rect87.draw(win)
    rect88.draw(win)
    rect89.draw(win)
    rect810.draw(win)
    rect811.draw(win)
    rect812.draw(win)
    rect813.draw(win)
    rect814.draw(win)
    rect815.draw(win)

    rect91.draw(win)
    rect92.draw(win)
    rect93.draw(win)
    rect94.draw(win)
    rect95.draw(win)
    rect96.draw(win)
    rect97.draw(win)
    rect98.draw(win)
    rect99.draw(win)
    rect910.draw(win)
    rect911.draw(win)
    rect912.draw(win)
    rect913.draw(win)
    rect914.draw(win)
    rect915.draw(win)

    rect101.draw(win)
    rect102.draw(win)
    rect103.draw(win)
    rect104.draw(win)
    rect105.draw(win)
    rect106.draw(win)
    rect107.draw(win)
    rect108.draw(win)
    rect109.draw(win)
    rect1010.draw(win)
    rect1011.draw(win)
    rect1012.draw(win)
    rect1013.draw(win)
    rect1014.draw(win)
    rect1015.draw(win)

    rect111.draw(win)
    rect112.draw(win)
    rect113.draw(win)
    rect114.draw(win)
    rect115.draw(win)
    rect116.draw(win)
    rect117.draw(win)
    rect118.draw(win)
    rect119.draw(win)
    rect1110.draw(win)
    rect1111.draw(win)
    rect1112.draw(win)
    rect1113.draw(win)
    rect1114.draw(win)
    rect1115.draw(win)

    rect121.draw(win)
    rect122.draw(win)
    rect123.draw(win)
    rect124.draw(win)
    rect125.draw(win)
    rect126.draw(win)
    rect127.draw(win)
    rect128.draw(win)
    rect129.draw(win)
    rect1210.draw(win)
    rect1211.draw(win)
    rect1212.draw(win)
    rect1213.draw(win)
    rect1214.draw(win)
    rect1215.draw(win)

    rect131.draw(win)
    rect132.draw(win)
    rect133.draw(win)
    rect134.draw(win)
    rect135.draw(win)
    rect136.draw(win)
    rect137.draw(win)
    rect138.draw(win)
    rect139.draw(win)
    rect1310.draw(win)
    rect1311.draw(win)
    rect1312.draw(win)
    rect1313.draw(win)
    rect1314.draw(win)
    rect1315.draw(win)

    rect141.draw(win)
    rect142.draw(win)
    rect143.draw(win)
    rect144.draw(win)
    rect145.draw(win)
    rect146.draw(win)
    rect147.draw(win)
    rect148.draw(win)
    rect149.draw(win)
    rect1410.draw(win)
    rect1411.draw(win)
    rect1412.draw(win)
    rect1413.draw(win)
    rect1414.draw(win)
    rect1415.draw(win)

    rect151.draw(win)
    rect152.draw(win)
    rect153.draw(win)
    rect154.draw(win)
    rect155.draw(win)
    rect156.draw(win)
    rect157.draw(win)
    rect158.draw(win)
    rect159.draw(win)
    rect1510.draw(win)
    rect1511.draw(win)
    rect1512.draw(win)
    rect1513.draw(win)
    rect1514.draw(win)
    rect1515.draw(win)

    while(1):
        mousePos = win.getMouse()
        if isClicked(rect, mousePos):
            if i == 1:
                rect.setFill("black")
                i = 2
            else:
                rect.setFill("white")
                i = 1
        elif isClicked(rect2, mousePos):
            if i == 1:
                rect2.setFill("black")
                i = 2
            else:
                rect2.setFill("white")
                i = 1
        elif isClicked(rect3, mousePos):
            if i == 1:
                rect3.setFill("black")
                i = 2
            else:
                rect3.setFill("white")
                i = 1
        elif isClicked(rect4, mousePos):
            if i == 1:
                rect4.setFill("black")
                i = 2
            else:
                rect4.setFill("white")
                i = 1

        elif isClicked(rect5, mousePos):
            if i == 1:
                rect5.setFill("black")
                i = 2
            else:
                rect5.setFill("white")
                i = 1
        elif isClicked(rect6, mousePos):
            if i == 1:
                rect6.setFill("black")
                i = 2
            else:
                rect6.setFill("white")
                i = 1
        elif isClicked(rect7, mousePos):
            if i == 1:
                rect7.setFill("black")
                i = 2
            else:
                rect7.setFill("white")
                i = 1
        elif isClicked(rect8, mousePos):
            if i == 1:
                rect8.setFill("black")
                i = 2
            else:
                rect8.setFill("white")
                i = 1

        elif isClicked(rect9, mousePos):
            if i == 1:
                rect9.setFill("black")
                i = 2
            else:
                rect9.setFill("white")
                i = 1
        elif isClicked(rect10, mousePos):
            if i == 1:
                rect10.setFill("black")
                i = 2
            else:
                rect10.setFill("white")
                i = 1
        elif isClicked(rect11, mousePos):
            if i == 1:
                rect11.setFill("black")
                i = 2
            else:
                rect11.setFill("white")
                i = 1
        elif isClicked(rect12, mousePos):
            if i == 1:
                rect12.setFill("black")
                i = 2
            else:
                rect12.setFill("white")
                i = 1
        elif isClicked(rect13, mousePos):
            if i == 1:
                rect13.setFill("black")
                i = 2
            else:
                rect13.setFill("white")
                i = 1
        elif isClicked(rect14, mousePos):
            if i == 1:
                rect14.setFill("black")
                i = 2
            else:
                rect14.setFill("white")
                i = 1
        elif isClicked(rect15, mousePos):
            if i == 1:
                rect15.setFill("black")
                i = 2
            else:
                rect15.setFill("white")
                i = 1

        elif isClicked(rect21, mousePos):
            if i == 1:
                rect21.setFill("black")
                i = 2
            else:
                rect21.setFill("white")
                i = 1
        elif isClicked(rect22, mousePos):
            if i == 1:
                rect22.setFill("black")
                i = 2
            else:
                rect22.setFill("white")
                i = 1
        elif isClicked(rect23, mousePos):
            if i == 1:
                rect23.setFill("black")
                i = 2
            else:
                rect23.setFill("white")
                i = 1
        elif isClicked(rect24, mousePos):
            if i == 1:
                rect24.setFill("black")
                i = 2
            else:
                rect24.setFill("white")
                i = 1

        elif isClicked(rect25, mousePos):
            if i == 1:
                rect25.setFill("black")
                i = 2
            else:
                rect25.setFill("white")
                i = 1
        elif isClicked(rect26, mousePos):
            if i == 1:
                rect26.setFill("black")
                i = 2
            else:
                rect26.setFill("white")
                i = 1
        elif isClicked(rect27, mousePos):
            if i == 1:
                rect27.setFill("black")
                i = 2
            else:
                rect27.setFill("white")
                i = 1
        elif isClicked(rect28, mousePos):
            if i == 1:
                rect28.setFill("black")
                i = 2
            else:
                rect28.setFill("white")
                i = 1

        elif isClicked(rect29, mousePos):
            if i == 1:
                rect29.setFill("black")
                i = 2
            else:
                rect29.setFill("white")
                i = 1
        elif isClicked(rect210, mousePos):
            if i == 1:
                rect210.setFill("black")
                i = 2
            else:
                rect210.setFill("white")
                i = 1
        elif isClicked(rect211, mousePos):
            if i == 1:
                rect211.setFill("black")
                i = 2
            else:
                rect211.setFill("white")
                i = 1
        elif isClicked(rect212, mousePos):
            if i == 1:
                rect212.setFill("black")
                i = 2
            else:
                rect212.setFill("white")
                i = 1
        elif isClicked(rect213, mousePos):
            if i == 1:
                rect213.setFill("black")
                i = 2
            else:
                rect213.setFill("white")
                i = 1
        elif isClicked(rect214, mousePos):
            if i == 1:
                rect214.setFill("black")
                i = 2
            else:
                rect214.setFill("white")
                i = 1
        elif isClicked(rect215, mousePos):
            if i == 1:
                rect215.setFill("black")
                i = 2
            else:
                rect215.setFill("white")
                i = 1

        elif isClicked(rect31, mousePos):
            if i == 1:
                rect31.setFill("black")
                i = 2
            else:
                rect31.setFill("white")
                i = 1
        elif isClicked(rect32, mousePos):
            if i == 1:
                rect32.setFill("black")
                i = 2
            else:
                rect32.setFill("white")
                i = 1
        elif isClicked(rect33, mousePos):
            if i == 1:
                rect33.setFill("black")
                i = 2
            else:
                rect33.setFill("white")
                i = 1
        elif isClicked(rect34, mousePos):
            if i == 1:
                rect34.setFill("black")
                i = 2
            else:
                rect34.setFill("white")
                i = 1

        elif isClicked(rect35, mousePos):
            if i == 1:
                rect35.setFill("black")
                i = 2
            else:
                rect35.setFill("white")
                i = 1
        elif isClicked(rect36, mousePos):
            if i == 1:
                rect36.setFill("black")
                i = 2
            else:
                rect36.setFill("white")
                i = 1
        elif isClicked(rect37, mousePos):
            if i == 1:
                rect37.setFill("black")
                i = 2
            else:
                rect37.setFill("white")
                i = 1
        elif isClicked(rect38, mousePos):
            if i == 1:
                rect38.setFill("black")
                i = 2
            else:
                rect38.setFill("white")
                i = 1

        elif isClicked(rect39, mousePos):
            if i == 1:
                rect39.setFill("black")
                i = 2
            else:
                rect39.setFill("white")
                i = 1
        elif isClicked(rect310, mousePos):
            if i == 1:
                rect310.setFill("black")
                i = 2
            else:
                rect310.setFill("white")
                i = 1
        elif isClicked(rect311, mousePos):
            if i == 1:
                rect311.setFill("black")
                i = 2
            else:
                rect311.setFill("white")
                i = 1
        elif isClicked(rect312, mousePos):
            if i == 1:
                rect312.setFill("black")
                i = 2
            else:
                rect312.setFill("white")
                i = 1
        elif isClicked(rect313, mousePos):
            if i == 1:
                rect313.setFill("black")
                i = 2
            else:
                rect313.setFill("white")
                i = 1
        elif isClicked(rect314, mousePos):
            if i == 1:
                rect314.setFill("black")
                i = 2
            else:
                rect314.setFill("white")
                i = 1
        elif isClicked(rect315, mousePos):
            if i == 1:
                rect315.setFill("black")
                i = 2
            else:
                rect315.setFill("white")
                i = 1

        elif isClicked(rect41, mousePos):
            if i == 1:
                rect41.setFill("black")
                i = 2
            else:
                rect41.setFill("white")
                i = 1
        elif isClicked(rect42, mousePos):
            if i == 1:
                rect42.setFill("black")
                i = 2
            else:
                rect42.setFill("white")
                i = 1
        elif isClicked(rect43, mousePos):
            if i == 1:
                rect43.setFill("black")
                i = 2
            else:
                rect43.setFill("white")
                i = 1
        elif isClicked(rect44, mousePos):
            if i == 1:
                rect44.setFill("black")
                i = 2
            else:
                rect44.setFill("white")
                i = 1

        elif isClicked(rect45, mousePos):
            if i == 1:
                rect45.setFill("black")
                i = 2
            else:
                rect45.setFill("white")
                i = 1
        elif isClicked(rect46, mousePos):
            if i == 1:
                rect46.setFill("black")
                i = 2
            else:
                rect46.setFill("white")
                i = 1
        elif isClicked(rect47, mousePos):
            if i == 1:
                rect47.setFill("black")
                i = 2
            else:
                rect47.setFill("white")
                i = 1
        elif isClicked(rect48, mousePos):
            if i == 1:
                rect48.setFill("black")
                i = 2
            else:
                rect48.setFill("white")
                i = 1

        elif isClicked(rect49, mousePos):
            if i == 1:
                rect49.setFill("black")
                i = 2
            else:
                rect49.setFill("white")
                i = 1
        elif isClicked(rect410, mousePos):
            if i == 1:
                rect410.setFill("black")
                i = 2
            else:
                rect410.setFill("white")
                i = 1
        elif isClicked(rect411, mousePos):
            if i == 1:
                rect411.setFill("black")
                i = 2
            else:
                rect411.setFill("white")
                i = 1
        elif isClicked(rect412, mousePos):
            if i == 1:
                rect412.setFill("black")
                i = 2
            else:
                rect412.setFill("white")
                i = 1
        elif isClicked(rect413, mousePos):
            if i == 1:
                rect413.setFill("black")
                i = 2
            else:
                rect413.setFill("white")
                i = 1
        elif isClicked(rect414, mousePos):
            if i == 1:
                rect414.setFill("black")
                i = 2
            else:
                rect414.setFill("white")
                i = 1
        elif isClicked(rect415, mousePos):
            if i == 1:
                rect415.setFill("black")
                i = 2
            else:
                rect415.setFill("white")
                i = 1

        elif isClicked(rect51, mousePos):
            if i == 1:
                rect51.setFill("black")
                i = 2
            else:
                rect51.setFill("white")
                i = 1
        elif isClicked(rect52, mousePos):
            if i == 1:
                rect52.setFill("black")
                i = 2
            else:
                rect52.setFill("white")
                i = 1
        elif isClicked(rect53, mousePos):
            if i == 1:
                rect53.setFill("black")
                i = 2
            else:
                rect53.setFill("white")
                i = 1
        elif isClicked(rect54, mousePos):
            if i == 1:
                rect54.setFill("black")
                i = 2
            else:
                rect54.setFill("white")
                i = 1
        elif isClicked(rect55, mousePos):
            if i == 1:
                rect55.setFill("black")
                i = 2
            else:
                rect55.setFill("white")
                i = 1
        elif isClicked(rect56, mousePos):
            if i == 1:
                rect56.setFill("black")
                i = 2
            else:
                rect56.setFill("white")
                i = 1
        elif isClicked(rect57, mousePos):
            if i == 1:
                rect57.setFill("black")
                i = 2
            else:
                rect57.setFill("white")
                i = 1
        elif isClicked(rect58, mousePos):
            if i == 1:
                rect58.setFill("black")
                i = 2
            else:
                rect58.setFill("white")
                i = 1

        elif isClicked(rect59, mousePos):
            if i == 1:
                rect59.setFill("black")
                i = 2
            else:
                rect59.setFill("white")
                i = 1
        elif isClicked(rect510, mousePos):
            if i == 1:
                rect510.setFill("black")
                i = 2
            else:
                rect510.setFill("white")
                i = 1
        elif isClicked(rect511, mousePos):
            if i == 1:
                rect511.setFill("black")
                i = 2
            else:
                rect511.setFill("white")
                i = 1
        elif isClicked(rect512, mousePos):
            if i == 1:
                rect512.setFill("black")
                i = 2
            else:
                rect512.setFill("white")
                i = 1
        elif isClicked(rect513, mousePos):
            if i == 1:
                rect513.setFill("black")
                i = 2
            else:
                rect513.setFill("white")
                i = 1
        elif isClicked(rect514, mousePos):
            if i == 1:
                rect514.setFill("black")
                i = 2
            else:
                rect514.setFill("white")
                i = 1
        elif isClicked(rect515, mousePos):
            if i == 1:
                rect515.setFill("black")
                i = 2
            else:
                rect515.setFill("white")
                i = 1

        elif isClicked(rect61, mousePos):
            if i == 1:
                rect61.setFill("black")
                i = 2
            else:
                rect61.setFill("white")
                i = 1
        elif isClicked(rect62, mousePos):
            if i == 1:
                rect62.setFill("black")
                i = 2
            else:
                rect62.setFill("white")
                i = 1
        elif isClicked(rect63, mousePos):
            if i == 1:
                rect63.setFill("black")
                i = 2
            else:
                rect63.setFill("white")
                i = 1
        elif isClicked(rect64, mousePos):
            if i == 1:
                rect64.setFill("black")
                i = 2
            else:
                rect64.setFill("white")
                i = 1
        elif isClicked(rect65, mousePos):
            if i == 1:
                rect65.setFill("black")
                i = 2
            else:
                rect65.setFill("white")
                i = 1
        elif isClicked(rect66, mousePos):
            if i == 1:
                rect66.setFill("black")
                i = 2
            else:
                rect66.setFill("white")
                i = 1
        elif isClicked(rect67, mousePos):
            if i == 1:
                rect67.setFill("black")
                i = 2
            else:
                rect67.setFill("white")
                i = 1
        elif isClicked(rect68, mousePos):
            if i == 1:
                rect68.setFill("black")
                i = 2
            else:
                rect68.setFill("white")
                i = 1
        elif isClicked(rect69, mousePos):
            if i == 1:
                rect69.setFill("black")
                i = 2
            else:
                rect69.setFill("white")
                i = 1
        elif isClicked(rect610, mousePos):
            if i == 1:
                rect610.setFill("black")
                i = 2
            else:
                rect610.setFill("white")
                i = 1
        elif isClicked(rect611, mousePos):
            if i == 1:
                rect611.setFill("black")
                i = 2
            else:
                rect611.setFill("white")
                i = 1
        elif isClicked(rect612, mousePos):
            if i == 1:
                rect612.setFill("black")
                i = 2
            else:
                rect612.setFill("white")
                i = 1
        elif isClicked(rect613, mousePos):
            if i == 1:
                rect613.setFill("black")
                i = 2
            else:
                rect613.setFill("white")
                i = 1
        elif isClicked(rect614, mousePos):
            if i == 1:
                rect614.setFill("black")
                i = 2
            else:
                rect614.setFill("white")
                i = 1
        elif isClicked(rect615, mousePos):
            if i == 1:
                rect615.setFill("black")
                i = 2
            else:
                rect615.setFill("white")
                i = 1

        elif isClicked(rect71, mousePos):
            if i == 1:
                rect71.setFill("black")
                i = 2
            else:
                rect71.setFill("white")
                i = 1
        elif isClicked(rect72, mousePos):
            if i == 1:
                rect72.setFill("black")
                i = 2
            else:
                rect72.setFill("white")
                i = 1
        elif isClicked(rect73, mousePos):
            if i == 1:
                rect73.setFill("black")
                i = 2
            else:
                rect73.setFill("white")
                i = 1
        elif isClicked(rect74, mousePos):
            if i == 1:
                rect74.setFill("black")
                i = 2
            else:
                rect74.setFill("white")
                i = 1
        elif isClicked(rect75, mousePos):
            if i == 1:
                rect75.setFill("black")
                i = 2
            else:
                rect75.setFill("white")
                i = 1
        elif isClicked(rect76, mousePos):
            if i == 1:
                rect76.setFill("black")
                i = 2
            else:
                rect76.setFill("white")
                i = 1
        elif isClicked(rect77, mousePos):
            if i == 1:
                rect77.setFill("black")
                i = 2
            else:
                rect77.setFill("white")
                i = 1
        elif isClicked(rect78, mousePos):
            if i == 1:
                rect78.setFill("black")
                i = 2
            else:
                rect78.setFill("white")
                i = 1
        elif isClicked(rect79, mousePos):
            if i == 1:
                rect79.setFill("black")
                i = 2
            else:
                rect79.setFill("white")
                i = 1
        elif isClicked(rect710, mousePos):
            if i == 1:
                rect710.setFill("black")
                i = 2
            else:
                rect710.setFill("white")
                i = 1
        elif isClicked(rect711, mousePos):
            if i == 1:
                rect711.setFill("black")
                i = 2
            else:
                rect711.setFill("white")
                i = 1
        elif isClicked(rect712, mousePos):
            if i == 1:
                rect712.setFill("black")
                i = 2
            else:
                rect712.setFill("white")
                i = 1
        elif isClicked(rect713, mousePos):
            if i == 1:
                rect713.setFill("black")
                i = 2
            else:
                rect713.setFill("white")
                i = 1
        elif isClicked(rect714, mousePos):
            if i == 1:
                rect714.setFill("black")
                i = 2
            else:
                rect714.setFill("white")
                i = 1
        elif isClicked(rect715, mousePos):
            if i == 1:
                rect715.setFill("black")
                i = 2
            else:
                rect715.setFill("white")
                i = 1

        elif isClicked(rect81, mousePos):
            if i == 1:
                rect81.setFill("black")
                i = 2
            else:
                rect81.setFill("white")
                i = 1
        elif isClicked(rect82, mousePos):
            if i == 1:
                rect82.setFill("black")
                i = 2
            else:
                rect82.setFill("white")
                i = 1
        elif isClicked(rect83, mousePos):
            if i == 1:
                rect83.setFill("black")
                i = 2
            else:
                rect83.setFill("white")
                i = 1
        elif isClicked(rect84, mousePos):
            if i == 1:
                rect84.setFill("black")
                i = 2
            else:
                rect84.setFill("white")
                i = 1
        elif isClicked(rect85, mousePos):
            if i == 1:
                rect85.setFill("black")
                i = 2
            else:
                rect85.setFill("white")
                i = 1
        elif isClicked(rect86, mousePos):
            if i == 1:
                rect86.setFill("black")
                i = 2
            else:
                rect86.setFill("white")
                i = 1
        elif isClicked(rect87, mousePos):
            if i == 1:
                rect87.setFill("black")
                i = 2
            else:
                rect87.setFill("white")
                i = 1
        elif isClicked(rect88, mousePos):
            if i == 1:
                rect88.setFill("black")
                i = 2
            else:
                rect88.setFill("white")
                i = 1
        elif isClicked(rect89, mousePos):
            if i == 1:
                rect89.setFill("black")
                i = 2
            else:
                rect89.setFill("white")
                i = 1
        elif isClicked(rect810, mousePos):
            if i == 1:
                rect810.setFill("black")
                i = 2
            else:
                rect810.setFill("white")
                i = 1
        elif isClicked(rect811, mousePos):
            if i == 1:
                rect811.setFill("black")
                i = 2
            else:
                rect811.setFill("white")
                i = 1
        elif isClicked(rect812, mousePos):
            if i == 1:
                rect812.setFill("black")
                i = 2
            else:
                rect812.setFill("white")
                i = 1
        elif isClicked(rect813, mousePos):
            if i == 1:
                rect813.setFill("black")
                i = 2
            else:
                rect813.setFill("white")
                i = 1
        elif isClicked(rect814, mousePos):
            if i == 1:
                rect814.setFill("black")
                i = 2
            else:
                rect814.setFill("white")
                i = 1
        elif isClicked(rect815, mousePos):
            if i == 1:
                rect815.setFill("black")
                i = 2
            else:
                rect815.setFill("white")
                i = 1

        elif isClicked(rect91, mousePos):
            if i == 1:
                rect91.setFill("black")
                i = 2
            else:
                rect91.setFill("white")
                i = 1
        elif isClicked(rect92, mousePos):
            if i == 1:
                rect92.setFill("black")
                i = 2
            else:
                rect92.setFill("white")
                i = 1
        elif isClicked(rect93, mousePos):
            if i == 1:
                rect93.setFill("black")
                i = 2
            else:
                rect93.setFill("white")
                i = 1
        elif isClicked(rect94, mousePos):
            if i == 1:
                rect94.setFill("black")
                i = 2
            else:
                rect94.setFill("white")
                i = 1
        elif isClicked(rect95, mousePos):
            if i == 1:
                rect95.setFill("black")
                i = 2
            else:
                rect95.setFill("white")
                i = 1
        elif isClicked(rect96, mousePos):
            if i == 1:
                rect96.setFill("black")
                i = 2
            else:
                rect96.setFill("white")
                i = 1
        elif isClicked(rect97, mousePos):
            if i == 1:
                rect97.setFill("black")
                i = 2
            else:
                rect97.setFill("white")
                i = 1
        elif isClicked(rect98, mousePos):
            if i == 1:
                rect98.setFill("black")
                i = 2
            else:
                rect98.setFill("white")
                i = 1
        elif isClicked(rect99, mousePos):
            if i == 1:
                rect99.setFill("black")
                i = 2
            else:
                rect99.setFill("white")
                i = 1
        elif isClicked(rect910, mousePos):
            if i == 1:
                rect910.setFill("black")
                i = 2
            else:
                rect910.setFill("white")
                i = 1
        elif isClicked(rect911, mousePos):
            if i == 1:
                rect911.setFill("black")
                i = 2
            else:
                rect911.setFill("white")
                i = 1
        elif isClicked(rect912, mousePos):
            if i == 1:
                rect912.setFill("black")
                i = 2
            else:
                rect912.setFill("white")
                i = 1
        elif isClicked(rect913, mousePos):
            if i == 1:
                rect913.setFill("black")
                i = 2
            else:
                rect913.setFill("white")
                i = 1
        elif isClicked(rect914, mousePos):
            if i == 1:
                rect914.setFill("black")
                i = 2
            else:
                rect914.setFill("white")
                i = 1
        elif isClicked(rect915, mousePos):
            if i == 1:
                rect915.setFill("black")
                i = 2
            else:
                rect915.setFill("white")
                i = 1

        elif isClicked(rect101, mousePos):
            if i == 1:
                rect101.setFill("black")
                i = 2
            else:
                rect101.setFill("white")
                i = 1
        elif isClicked(rect102, mousePos):
            if i == 1:
                rect102.setFill("black")
                i = 2
            else:
                rect102.setFill("white")
                i = 1
        elif isClicked(rect103, mousePos):
            if i == 1:
                rect103.setFill("black")
                i = 2
            else:
                rect103.setFill("white")
                i = 1
        elif isClicked(rect104, mousePos):
            if i == 1:
                rect104.setFill("black")
                i = 2
            else:
                rect104.setFill("white")
                i = 1
        elif isClicked(rect105, mousePos):
            if i == 1:
                rect105.setFill("black")
                i = 2
            else:
                rect105.setFill("white")
                i = 1
        elif isClicked(rect106, mousePos):
            if i == 1:
                rect106.setFill("black")
                i = 2
            else:
                rect106.setFill("white")
                i = 1
        elif isClicked(rect107, mousePos):
            if i == 1:
                rect107.setFill("black")
                i = 2
            else:
                rect107.setFill("white")
                i = 1
        elif isClicked(rect108, mousePos):
            if i == 1:
                rect108.setFill("black")
                i = 2
            else:
                rect108.setFill("white")
                i = 1
        elif isClicked(rect109, mousePos):
            if i == 1:
                rect109.setFill("black")
                i = 2
            else:
                rect109.setFill("white")
                i = 1
        elif isClicked(rect1010, mousePos):
            if i == 1:
                rect1010.setFill("black")
                i = 2
            else:
                rect1010.setFill("white")
                i = 1
        elif isClicked(rect1011, mousePos):
            if i == 1:
                rect1011.setFill("black")
                i = 2
            else:
                rect1011.setFill("white")
                i = 1
        elif isClicked(rect1012, mousePos):
            if i == 1:
                rect1012.setFill("black")
                i = 2
            else:
                rect1012.setFill("white")
                i = 1
        elif isClicked(rect1013, mousePos):
            if i == 1:
                rect1013.setFill("black")
                i = 2
            else:
                rect1013.setFill("white")
                i = 1
        elif isClicked(rect1014, mousePos):
            if i == 1:
                rect1014.setFill("black")
                i = 2
            else:
                rect1014.setFill("white")
                i = 1
        elif isClicked(rect1015, mousePos):
            if i == 1:
                rect1015.setFill("black")
                i = 2
            else:
                rect1015.setFill("white")
                i = 1

        elif isClicked(rect111, mousePos):
            if i == 1:
                rect111.setFill("black")
                i = 2
            else:
                rect111.setFill("white")
                i = 1
        elif isClicked(rect112, mousePos):
            if i == 1:
                rect112.setFill("black")
                i = 2
            else:
                rect112.setFill("white")
                i = 1
        elif isClicked(rect113, mousePos):
            if i == 1:
                rect113.setFill("black")
                i = 2
            else:
                rect113.setFill("white")
                i = 1
        elif isClicked(rect114, mousePos):
            if i == 1:
                rect114.setFill("black")
                i = 2
            else:
                rect114.setFill("white")
                i = 1
        elif isClicked(rect115, mousePos):
            if i == 1:
                rect115.setFill("black")
                i = 2
            else:
                rect115.setFill("white")
                i = 1
        elif isClicked(rect116, mousePos):
            if i == 1:
                rect116.setFill("black")
                i = 2
            else:
                rect116.setFill("white")
                i = 1
        elif isClicked(rect117, mousePos):
            if i == 1:
                rect117.setFill("black")
                i = 2
            else:
                rect117.setFill("white")
                i = 1
        elif isClicked(rect118, mousePos):
            if i == 1:
                rect118.setFill("black")
                i = 2
            else:
                rect118.setFill("white")
                i = 1
        elif isClicked(rect119, mousePos):
            if i == 1:
                rect119.setFill("black")
                i = 2
            else:
                rect119.setFill("white")
                i = 1
        elif isClicked(rect1110, mousePos):
            if i == 1:
                rect1110.setFill("black")
                i = 2
            else:
                rect1110.setFill("white")
                i = 1
        elif isClicked(rect1111, mousePos):
            if i == 1:
                rect1111.setFill("black")
                i = 2
            else:
                rect1111.setFill("white")
                i = 1
        elif isClicked(rect1112, mousePos):
            if i == 1:
                rect1112.setFill("black")
                i = 2
            else:
                rect1112.setFill("white")
                i = 1
        elif isClicked(rect1113, mousePos):
            if i == 1:
                rect1113.setFill("black")
                i = 2
            else:
                rect1113.setFill("white")
                i = 1
        elif isClicked(rect1114, mousePos):
            if i == 1:
                rect1114.setFill("black")
                i = 2
            else:
                rect1114.setFill("white")
                i = 1
        elif isClicked(rect1115, mousePos):
            if i == 1:
                rect1115.setFill("black")
                i = 2
            else:
                rect1115.setFill("white")
                i = 1

        elif isClicked(rect121, mousePos):
            if i == 1:
                rect121.setFill("black")
                i = 2
            else:
                rect121.setFill("white")
                i = 1
        elif isClicked(rect122, mousePos):
            if i == 1:
                rect122.setFill("black")
                i = 2
            else:
                rect122.setFill("white")
                i = 1
        elif isClicked(rect123, mousePos):
            if i == 1:
                rect123.setFill("black")
                i = 2
            else:
                rect123.setFill("white")
                i = 1
        elif isClicked(rect124, mousePos):
            if i == 1:
                rect124.setFill("black")
                i = 2
            else:
                rect124.setFill("white")
                i = 1
        elif isClicked(rect125, mousePos):
            if i == 1:
                rect125.setFill("black")
                i = 2
            else:
                rect125.setFill("white")
                i = 1
        elif isClicked(rect126, mousePos):
            if i == 1:
                rect126.setFill("black")
                i = 2
            else:
                rect126.setFill("white")
                i = 1
        elif isClicked(rect127, mousePos):
            if i == 1:
                rect127.setFill("black")
                i = 2
            else:
                rect127.setFill("white")
                i = 1
        elif isClicked(rect128, mousePos):
            if i == 1:
                rect128.setFill("black")
                i = 2
            else:
                rect128.setFill("white")
                i = 1
        elif isClicked(rect129, mousePos):
            if i == 1:
                rect129.setFill("black")
                i = 2
            else:
                rect129.setFill("white")
                i = 1
        elif isClicked(rect1210, mousePos):
            if i == 1:
                rect1210.setFill("black")
                i = 2
            else:
                rect1210.setFill("white")
                i = 1
        elif isClicked(rect1211, mousePos):
            if i == 1:
                rect1211.setFill("black")
                i = 2
            else:
                rect1211.setFill("white")
                i = 1
        elif isClicked(rect1212, mousePos):
            if i == 1:
                rect1212.setFill("black")
                i = 2
            else:
                rect1212.setFill("white")
                i = 1
        elif isClicked(rect1213, mousePos):
            if i == 1:
                rect1213.setFill("black")
                i = 2
            else:
                rect1213.setFill("white")
                i = 1
        elif isClicked(rect1214, mousePos):
            if i == 1:
                rect1214.setFill("black")
                i = 2
            else:
                rect1214.setFill("white")
                i = 1
        elif isClicked(rect1215, mousePos):
            if i == 1:
                rect1215.setFill("black")
                i = 2
            else:
                rect1215.setFill("white")
                i = 1

        elif isClicked(rect131, mousePos):
            if i == 1:
                rect131.setFill("black")
                i = 2
            else:
                rect131.setFill("white")
                i = 1
        elif isClicked(rect132, mousePos):
            if i == 1:
                rect132.setFill("black")
                i = 2
            else:
                rect132.setFill("white")
                i = 1
        elif isClicked(rect133, mousePos):
            if i == 1:
                rect133.setFill("black")
                i = 2
            else:
                rect133.setFill("white")
                i = 1
        elif isClicked(rect134, mousePos):
            if i == 1:
                rect134.setFill("black")
                i = 2
            else:
                rect134.setFill("white")
                i = 1
        elif isClicked(rect135, mousePos):
            if i == 1:
                rect135.setFill("black")
                i = 2
            else:
                rect135.setFill("white")
                i = 1
        elif isClicked(rect136, mousePos):
            if i == 1:
                rect136.setFill("black")
                i = 2
            else:
                rect136.setFill("white")
                i = 1
        elif isClicked(rect137, mousePos):
            if i == 1:
                rect137.setFill("black")
                i = 2
            else:
                rect137.setFill("white")
                i = 1
        elif isClicked(rect138, mousePos):
            if i == 1:
                rect138.setFill("black")
                i = 2
            else:
                rect138.setFill("white")
                i = 1
        elif isClicked(rect139, mousePos):
            if i == 1:
                rect139.setFill("black")
                i = 2
            else:
                rect139.setFill("white")
                i = 1
        elif isClicked(rect1310, mousePos):
            if i == 1:
                rect1310.setFill("black")
                i = 2
            else:
                rect1310.setFill("white")
                i = 1
        elif isClicked(rect1311, mousePos):
            if i == 1:
                rect1311.setFill("black")
                i = 2
            else:
                rect1311.setFill("white")
                i = 1
        elif isClicked(rect1312, mousePos):
            if i == 1:
                rect1312.setFill("black")
                i = 2
            else:
                rect1312.setFill("white")
                i = 1
        elif isClicked(rect1313, mousePos):
            if i == 1:
                rect1313.setFill("black")
                i = 2
            else:
                rect1313.setFill("white")
                i = 1
        elif isClicked(rect1314, mousePos):
            if i == 1:
                rect1314.setFill("black")
                i = 2
            else:
                rect1314.setFill("white")
                i = 1
        elif isClicked(rect1315, mousePos):
            if i == 1:
                rect1315.setFill("black")
                i = 2
            else:
                rect1315.setFill("white")
                i = 1

        elif isClicked(rect141, mousePos):
            if i == 1:
                rect141.setFill("black")
                i = 2
            else:
                rect141.setFill("white")
                i = 1
        elif isClicked(rect142, mousePos):
            if i == 1:
                rect142.setFill("black")
                i = 2
            else:
                rect142.setFill("white")
                i = 1
        elif isClicked(rect143, mousePos):
            if i == 1:
                rect143.setFill("black")
                i = 2
            else:
                rect143.setFill("white")
                i = 1
        elif isClicked(rect144, mousePos):
            if i == 1:
                rect144.setFill("black")
                i = 2
            else:
                rect144.setFill("white")
                i = 1
        elif isClicked(rect145, mousePos):
            if i == 1:
                rect145.setFill("black")
                i = 2
            else:
                rect145.setFill("white")
                i = 1
        elif isClicked(rect146, mousePos):
            if i == 1:
                rect146.setFill("black")
                i = 2
            else:
                rect146.setFill("white")
                i = 1
        elif isClicked(rect147, mousePos):
            if i == 1:
                rect147.setFill("black")
                i = 2
            else:
                rect147.setFill("white")
                i = 1
        elif isClicked(rect148, mousePos):
            if i == 1:
                rect148.setFill("black")
                i = 2
            else:
                rect148.setFill("white")
                i = 1
        elif isClicked(rect149, mousePos):
            if i == 1:
                rect149.setFill("black")
                i = 2
            else:
                rect149.setFill("white")
                i = 1
        elif isClicked(rect1410, mousePos):
            if i == 1:
                rect1410.setFill("black")
                i = 2
            else:
                rect1410.setFill("white")
                i = 1
        elif isClicked(rect1411, mousePos):
            if i == 1:
                rect1411.setFill("black")
                i = 2
            else:
                rect1411.setFill("white")
                i = 1
        elif isClicked(rect1412, mousePos):
            if i == 1:
                rect1412.setFill("black")
                i = 2
            else:
                rect1412.setFill("white")
                i = 1
        elif isClicked(rect1413, mousePos):
            if i == 1:
                rect1413.setFill("black")
                i = 2
            else:
                rect1413.setFill("white")
                i = 1
        elif isClicked(rect1414, mousePos):
            if i == 1:
                rect1414.setFill("black")
                i = 2
            else:
                rect1414.setFill("white")
                i = 1
        elif isClicked(rect1415, mousePos):
            if i == 1:
                rect1415.setFill("black")
                i = 2
            else:
                rect1415.setFill("white")
                i = 1

        elif isClicked(rect151, mousePos):
            if i == 1:
                rect151.setFill("black")
                i = 2
            else:
                rect151.setFill("white")
                i = 1
        elif isClicked(rect152, mousePos):
            if i == 1:
                rect152.setFill("black")
                i = 2
            else:
                rect152.setFill("white")
                i = 1
        elif isClicked(rect153, mousePos):
            if i == 1:
                rect153.setFill("black")
                i = 2
            else:
                rect153.setFill("white")
                i = 1
        elif isClicked(rect154, mousePos):
            if i == 1:
                rect154.setFill("black")
                i = 2
            else:
                rect154.setFill("white")
                i = 1
        elif isClicked(rect155, mousePos):
            if i == 1:
                rect155.setFill("black")
                i = 2
            else:
                rect155.setFill("white")
                i = 1
        elif isClicked(rect156, mousePos):
            if i == 1:
                rect156.setFill("black")
                i = 2
            else:
                rect156.setFill("white")
                i = 1
        elif isClicked(rect157, mousePos):
            if i == 1:
                rect157.setFill("black")
                i = 2
            else:
                rect157.setFill("white")
                i = 1
        elif isClicked(rect158, mousePos):
            if i == 1:
                rect158.setFill("black")
                i = 2
            else:
                rect158.setFill("white")
                i = 1
        elif isClicked(rect159, mousePos):
            if i == 1:
                rect159.setFill("black")
                i = 2
            else:
                rect159.setFill("white")
                i = 1
        elif isClicked(rect1510, mousePos):
            if i == 1:
                rect1510.setFill("black")
                i = 2
            else:
                rect1510.setFill("white")
                i = 1
        elif isClicked(rect1511, mousePos):
            if i == 1:
                rect1511.setFill("black")
                i = 2
            else:
                rect1511.setFill("white")
                i = 1
        elif isClicked(rect1512, mousePos):
            if i == 1:
                rect1512.setFill("black")
                i = 2
            else:
                rect1512.setFill("white")
                i = 1
        elif isClicked(rect1513, mousePos):
            if i == 1:
                rect1513.setFill("black")
                i = 2
            else:
                rect1513.setFill("white")
                i = 1
        elif isClicked(rect1514, mousePos):
            if i == 1:
                rect1514.setFill("black")
                i = 2
            else:
                rect1514.setFill("white")
                i = 1
        elif isClicked(rect1515, mousePos):
            if i == 1:
                rect1515.setFill("black")
                i = 2
            else:
                rect1515.setFill("white")
                i = 1

    win.close()


if __name__ == '__main__':
    main()
