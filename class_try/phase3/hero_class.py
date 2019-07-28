# -*- coding: UTF-8 -*-
# author by : Steven Lu
import random

class Hero():

    def __init__(self,s,n,p):
        if len(s)>0 and len(n)>0and len(p)>0:
            self.skin=s
            self.name=n
            self.position=p
            self.ab_viability=random.randint(1,100)
            self.ab_damage=random.randint(1,100)
            self.ab_effect=random.randint(1,100)
            self.ab_difficulty=random.randint(1,100)
        else:
           self.skin='英雄的原始皮肤'
           self.name='英雄的姓名'
           self.position='英雄的定位'

           self.ab_viability=0
           self.ab_damage=0
           self.ab_effect=0
           self.ab_difficulty=0
        return
    def show_presentation(self):
        print('\n英雄的介绍：xxxxxxx')
        print('\n生存能力=[%d], 攻击伤害=[%d], 技能效果=[%d], 上手难度=[%d]' % (
            self.ab_viability, self.ab_damage, self.ab_effect, self.ab_difficulty))
        return

    def show_story(self):
        print('\n英雄的故事: xxxxxxxxxxx')
        return

    def show_history(self):
        print('\n史实中的英雄: 其实他没那么厉害。。。。。。。')
        return
