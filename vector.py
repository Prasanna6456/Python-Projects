from manim import *

class DrawVectors(Scene):
    def construct(self):
        num = NumberPlane()
        self.play(Create(num),run_time =2)

        arrowAB = Arrow(ORIGIN,[2,2,0],buff=0)
        AB_pos = np.array([0.5,1,0])
        vec_nm_AB = TextMobject("$\\vec{AB}$")
        vec_nm_AB.move_to(AB_pos)
        vec_nm_AB.rotate(45*DEGREES)
        self.play(Create(Dot(ORIGIN)))
        self.play(Create(arrowAB))
        self.play(Write(vec_nm_AB))

        self.wait(0.5)

        arrowCD = Arrow(np.array([3.,-3.,0.]),[2,-1,0],buff = 0)
        CD_pos = np.array([(3.,-2.,0.)])
        vec_nm_CD = TextMobject("$\\vec{CD}$")
        vec_nm_CD.rotate(315*DEGREES)
        vec_nm_CD.move_to(CD_pos)
        self.play(Create(Dot(np.array([3.,-3.,0.]))))
        self.play(Create(arrowCD))
        self.play(Write(vec_nm_CD))

        valAB = TextMobject("$\\vec{AB} = 2i+2j$").move_to(5*LEFT+2*DOWN)
        valCD = TextMobject("$\\vec{DC} = -i+2j$").move_to(5*LEFT+3*DOWN)

        self.play(Write(valAB),run_time=2)
        self.play(Write(valCD),run_time=2)


        self.wait()
