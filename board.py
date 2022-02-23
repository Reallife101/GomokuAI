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
    win = GraphWin('ExampleWindow', 1000, 1000)
    rect = Rectangle(Point(66, 1), Point(1, 66))
    rect.setFill('purple')
    rect2 = Rectangle(Point(132, 1), Point(66, 66))
    rect2.setFill('purple')
    rect3 = Rectangle(Point(198, 1), Point(132, 66))
    rect3.setFill('purple')
    rect4 = Rectangle(Point(264, 1), Point(198, 66))
    rect4.setFill('purple')
    rect5 = Rectangle(Point(330, 1), Point(264, 66))
    rect5.setFill('purple')
    rect6 = Rectangle(Point(396, 1), Point(330, 66))
    rect6.setFill('purple')
    rect7 = Rectangle(Point(462, 1), Point(396, 66))
    rect7.setFill('purple')
    rect8 = Rectangle(Point(528, 1), Point(462, 66))
    rect8.setFill('purple')
    rect9 = Rectangle(Point(594, 1), Point(528, 66))
    rect9.setFill('purple')
    rect10 = Rectangle(Point(660, 1), Point(594, 66))
    rect10.setFill('purple')
    rect11 = Rectangle(Point(726, 1), Point(660, 66))
    rect11.setFill('purple')
    rect12 = Rectangle(Point(792, 1), Point(726, 66))
    rect12.setFill('purple')
    rect13 = Rectangle(Point(858, 1), Point(792, 66))
    rect13.setFill('purple')
    rect14 = Rectangle(Point(924, 1), Point(858, 66))
    rect14.setFill('purple')
    rect15 = Rectangle(Point(990, 1), Point(924, 66))
    rect15.setFill('purple')

    rect21 = Rectangle(Point(66, 66), Point(1, 132))
    rect21.setFill('purple')
    rect22 = Rectangle(Point(132, 66), Point(66, 132))
    rect22.setFill('purple')
    rect23 = Rectangle(Point(198, 66), Point(132, 132))
    rect23.setFill('purple')
    rect24 = Rectangle(Point(264, 66), Point(198, 132))
    rect24.setFill('purple')
    rect25 = Rectangle(Point(330, 66), Point(264, 132))
    rect25.setFill('purple')
    rect26 = Rectangle(Point(396, 66), Point(330, 132))
    rect26.setFill('purple')
    rect27 = Rectangle(Point(462, 66), Point(396, 132))
    rect27.setFill('purple')
    rect28 = Rectangle(Point(528, 66), Point(462, 132))
    rect28.setFill('purple')
    rect29 = Rectangle(Point(594, 66), Point(528, 132))
    rect29.setFill('purple')
    rect210 = Rectangle(Point(660, 66), Point(594, 132))
    rect210.setFill('purple')
    rect211 = Rectangle(Point(726, 66), Point(660, 132))
    rect211.setFill('purple')
    rect212 = Rectangle(Point(792, 66), Point(726, 132))
    rect212.setFill('purple')
    rect213 = Rectangle(Point(858, 66), Point(792, 132))
    rect213.setFill('purple')
    rect214 = Rectangle(Point(924, 66), Point(858, 132))
    rect214.setFill('purple')
    rect215 = Rectangle(Point(990, 66), Point(924, 132))
    rect215.setFill('purple')

    rect31 = Rectangle(Point(66, 132), Point(1, 198))
    rect31.setFill('purple')
    rect32 = Rectangle(Point(132, 132), Point(66, 198))
    rect32.setFill('purple')
    rect33 = Rectangle(Point(198, 132), Point(132, 198))
    rect33.setFill('purple')
    rect34 = Rectangle(Point(264, 132), Point(198, 198))
    rect34.setFill('purple')
    rect35 = Rectangle(Point(330, 132), Point(264, 198))
    rect35.setFill('purple')
    rect36 = Rectangle(Point(396, 132), Point(330, 198))
    rect36.setFill('purple')
    rect37 = Rectangle(Point(462, 132), Point(396, 198))
    rect37.setFill('purple')
    rect38 = Rectangle(Point(528, 132), Point(462, 198))
    rect38.setFill('purple')
    rect39 = Rectangle(Point(594, 132), Point(528, 198))
    rect39.setFill('purple')
    rect310 = Rectangle(Point(660, 132), Point(594, 198))
    rect310.setFill('purple')
    rect311 = Rectangle(Point(726, 132), Point(660, 198))
    rect311.setFill('purple')
    rect312 = Rectangle(Point(792, 132), Point(726, 198))
    rect312.setFill('purple')
    rect313 = Rectangle(Point(858, 132), Point(792, 198))
    rect313.setFill('purple')
    rect314 = Rectangle(Point(924, 132), Point(858, 198))
    rect314.setFill('purple')
    rect315 = Rectangle(Point(990, 132), Point(924, 198))
    rect315.setFill('purple')

    rect41 = Rectangle(Point(66, 198), Point(1, 264))
    rect41.setFill('purple')
    rect42 = Rectangle(Point(132, 198), Point(66, 264))
    rect42.setFill('purple')
    rect43 = Rectangle(Point(198, 198), Point(132, 264))
    rect43.setFill('purple')
    rect44 = Rectangle(Point(264, 198), Point(198, 264))
    rect44.setFill('purple')
    rect45 = Rectangle(Point(330, 198), Point(264, 264))
    rect45.setFill('purple')
    rect46 = Rectangle(Point(396, 198), Point(330, 264))
    rect46.setFill('purple')
    rect47 = Rectangle(Point(462, 198), Point(396, 264))
    rect47.setFill('purple')
    rect48 = Rectangle(Point(528, 198), Point(462, 264))
    rect48.setFill('purple')
    rect49 = Rectangle(Point(594, 198), Point(528, 264))
    rect49.setFill('purple')
    rect410 = Rectangle(Point(660, 198), Point(594, 264))
    rect410.setFill('purple')
    rect411 = Rectangle(Point(726, 198), Point(660, 264))
    rect411.setFill('purple')
    rect412 = Rectangle(Point(792, 198), Point(726, 264))
    rect412.setFill('purple')
    rect413 = Rectangle(Point(858, 198), Point(792, 264))
    rect413.setFill('purple')
    rect414 = Rectangle(Point(924, 198), Point(858, 264))
    rect414.setFill('purple')
    rect415 = Rectangle(Point(990, 198), Point(924, 264))
    rect415.setFill('purple')

    rect51 = Rectangle(Point(66, 264), Point(1, 330))
    rect51.setFill('purple')
    rect52 = Rectangle(Point(132, 264), Point(66, 330))
    rect52.setFill('purple')
    rect53 = Rectangle(Point(198, 264), Point(132, 330))
    rect53.setFill('purple')
    rect54 = Rectangle(Point(264, 264), Point(198, 330))
    rect54.setFill('purple')
    rect55 = Rectangle(Point(330, 264), Point(264, 330))
    rect55.setFill('purple')
    rect56 = Rectangle(Point(396, 264), Point(330, 330))
    rect56.setFill('purple')
    rect57 = Rectangle(Point(462, 264), Point(396, 330))
    rect57.setFill('purple')
    rect58 = Rectangle(Point(528, 264), Point(462, 330))
    rect58.setFill('purple')
    rect59 = Rectangle(Point(594, 264), Point(528, 330))
    rect59.setFill('purple')
    rect510 = Rectangle(Point(660, 264), Point(594, 330))
    rect510.setFill('purple')
    rect511 = Rectangle(Point(726, 264), Point(660, 330))
    rect511.setFill('purple')
    rect512 = Rectangle(Point(792, 264), Point(726, 330))
    rect512.setFill('purple')
    rect513 = Rectangle(Point(858, 264), Point(792, 330))
    rect513.setFill('purple')
    rect514 = Rectangle(Point(924, 264), Point(858, 330))
    rect514.setFill('purple')
    rect515 = Rectangle(Point(990, 264), Point(924, 330))
    rect515.setFill('purple')

    rect61 = Rectangle(Point(66, 330), Point(1, 396))
    rect61.setFill('purple')
    rect62 = Rectangle(Point(132, 330), Point(66, 396))
    rect62.setFill('purple')
    rect63 = Rectangle(Point(198, 330), Point(132, 396))
    rect63.setFill('purple')
    rect64 = Rectangle(Point(264, 330), Point(198, 396))
    rect64.setFill('purple')
    rect65 = Rectangle(Point(330, 330), Point(264, 396))
    rect65.setFill('purple')
    rect66 = Rectangle(Point(396, 330), Point(330, 396))
    rect66.setFill('purple')
    rect67 = Rectangle(Point(462, 330), Point(396, 396))
    rect67.setFill('purple')
    rect68 = Rectangle(Point(528, 330), Point(462, 396))
    rect68.setFill('purple')
    rect69 = Rectangle(Point(594, 330), Point(528, 396))
    rect69.setFill('purple')
    rect610 = Rectangle(Point(660, 330), Point(594, 396))
    rect610.setFill('purple')
    rect611 = Rectangle(Point(726, 330), Point(660, 396))
    rect611.setFill('purple')
    rect612 = Rectangle(Point(792, 330), Point(726, 396))
    rect612.setFill('purple')
    rect613 = Rectangle(Point(858, 330), Point(792, 396))
    rect613.setFill('purple')
    rect614 = Rectangle(Point(924, 330), Point(858, 396))
    rect614.setFill('purple')
    rect615 = Rectangle(Point(990, 330), Point(924, 396))
    rect615.setFill('purple')

    rect71 = Rectangle(Point(66, 396), Point(1, 462))
    rect71.setFill('purple')
    rect72 = Rectangle(Point(132, 396), Point(66, 462))
    rect72.setFill('purple')
    rect73 = Rectangle(Point(198, 396), Point(132, 462))
    rect73.setFill('purple')
    rect74 = Rectangle(Point(264, 396), Point(198, 462))
    rect74.setFill('purple')
    rect75 = Rectangle(Point(330, 396), Point(264, 462))
    rect75.setFill('purple')
    rect76 = Rectangle(Point(396, 396), Point(330, 462))
    rect76.setFill('purple')
    rect77 = Rectangle(Point(462, 396), Point(396, 462))
    rect77.setFill('purple')
    rect78 = Rectangle(Point(528, 396), Point(462, 462))
    rect78.setFill('purple')
    rect79 = Rectangle(Point(594, 396), Point(528, 462))
    rect79.setFill('purple')
    rect710 = Rectangle(Point(660, 396), Point(594, 462))
    rect710.setFill('purple')
    rect711 = Rectangle(Point(726, 396), Point(660, 462))
    rect711.setFill('purple')
    rect712 = Rectangle(Point(792, 396), Point(726, 462))
    rect712.setFill('purple')
    rect713 = Rectangle(Point(858, 396), Point(792, 462))
    rect713.setFill('purple')
    rect714 = Rectangle(Point(924, 396), Point(858, 462))
    rect714.setFill('purple')
    rect715 = Rectangle(Point(990, 396), Point(924, 462))
    rect715.setFill('purple')

    rect81 = Rectangle(Point(66, 462), Point(1, 528))
    rect81.setFill('purple')
    rect82 = Rectangle(Point(132, 462), Point(66, 528))
    rect82.setFill('purple')
    rect83 = Rectangle(Point(198, 462), Point(132, 528))
    rect83.setFill('purple')
    rect84 = Rectangle(Point(264, 462), Point(198, 528))
    rect84.setFill('purple')
    rect85 = Rectangle(Point(330, 462), Point(264, 528))
    rect85.setFill('purple')
    rect86 = Rectangle(Point(396, 462), Point(330, 528))
    rect86.setFill('purple')
    rect87 = Rectangle(Point(462, 462), Point(396, 528))
    rect87.setFill('purple')
    rect88 = Rectangle(Point(528, 462), Point(462, 528))
    rect88.setFill('purple')
    rect89 = Rectangle(Point(594, 462), Point(528, 528))
    rect89.setFill('purple')
    rect810 = Rectangle(Point(660, 462), Point(594, 528))
    rect810.setFill('purple')
    rect811 = Rectangle(Point(726, 462), Point(660, 528))
    rect811.setFill('purple')
    rect812 = Rectangle(Point(792, 462), Point(726, 528))
    rect812.setFill('purple')
    rect813 = Rectangle(Point(858, 462), Point(792, 528))
    rect813.setFill('purple')
    rect814 = Rectangle(Point(924, 462), Point(858, 528))
    rect814.setFill('purple')
    rect815 = Rectangle(Point(990, 462), Point(924, 528))
    rect815.setFill('purple')

    rect91 = Rectangle(Point(66, 528), Point(1, 594))
    rect91.setFill('purple')
    rect92 = Rectangle(Point(132, 528), Point(66, 594))
    rect92.setFill('purple')
    rect93 = Rectangle(Point(198, 528), Point(132, 594))
    rect93.setFill('purple')
    rect94 = Rectangle(Point(264, 528), Point(198, 594))
    rect94.setFill('purple')
    rect95 = Rectangle(Point(330, 528), Point(264, 594))
    rect95.setFill('purple')
    rect96 = Rectangle(Point(396, 528), Point(330, 594))
    rect96.setFill('purple')
    rect97 = Rectangle(Point(462, 528), Point(396, 594))
    rect97.setFill('purple')
    rect98 = Rectangle(Point(528, 528), Point(462, 594))
    rect98.setFill('purple')
    rect99 = Rectangle(Point(594, 528), Point(528, 594))
    rect99.setFill('purple')
    rect910 = Rectangle(Point(660, 528), Point(594, 594))
    rect910.setFill('purple')
    rect911 = Rectangle(Point(726, 528), Point(660, 594))
    rect911.setFill('purple')
    rect912 = Rectangle(Point(792, 528), Point(726, 594))
    rect912.setFill('purple')
    rect913 = Rectangle(Point(858, 528), Point(792, 594))
    rect913.setFill('purple')
    rect914 = Rectangle(Point(924, 528), Point(858, 594))
    rect914.setFill('purple')
    rect915 = Rectangle(Point(990, 528), Point(924, 594))
    rect915.setFill('purple')

    rect101 = Rectangle(Point(66, 594), Point(1, 660))
    rect101.setFill('purple')
    rect102 = Rectangle(Point(132, 594), Point(66, 660))
    rect102.setFill('purple')
    rect103 = Rectangle(Point(198, 594), Point(132, 660))
    rect103.setFill('purple')
    rect104 = Rectangle(Point(264, 594), Point(198, 660))
    rect104.setFill('purple')
    rect105 = Rectangle(Point(330, 594), Point(264, 660))
    rect105.setFill('purple')
    rect106 = Rectangle(Point(396, 594), Point(330, 660))
    rect106.setFill('purple')
    rect107 = Rectangle(Point(462, 594), Point(396, 660))
    rect107.setFill('purple')
    rect108 = Rectangle(Point(528, 594), Point(462, 660))
    rect108.setFill('purple')
    rect109 = Rectangle(Point(594, 594), Point(528, 660))
    rect109.setFill('purple')
    rect1010 = Rectangle(Point(660, 594), Point(594, 660))
    rect1010.setFill('purple')
    rect1011 = Rectangle(Point(726, 594), Point(660, 660))
    rect1011.setFill('purple')
    rect1012 = Rectangle(Point(792, 594), Point(726, 660))
    rect1012.setFill('purple')
    rect1013 = Rectangle(Point(858, 594), Point(792, 660))
    rect1013.setFill('purple')
    rect1014 = Rectangle(Point(924, 594), Point(858, 660))
    rect1014.setFill('purple')
    rect1015 = Rectangle(Point(990, 594), Point(924, 660))
    rect1015.setFill('purple')

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


    win.close()


if __name__ == '__main__':
    main()
