from manimlib.imports import *

# DRIVER CODE
# python manim.py my_projects\For_Videos\Conservation_Principle\conservation_principle.py -pl 

consveqndiff = TexMobject("\\nabla \\cdot ",	#0
							"\\vec{J}" ,		#1
							"=",				#2
							"-{",				#3
							"\\partial",		#4
							" \\rho",			#5
							" \\over ",			#6
							"\\partial t",		#7	
							"}" ).scale(3)  	#8
for i,color in [(0,BLUE),(1,MAROON),(4,RED),(5,PURPLE),(6,RED),(7,RED)]:
	consveqndiff[i].set_color(color)

eqntext = TextMobject("\\textbf{THE CONTINUITY EQUATION}").set_color(TEAL_B)


st1 = TexMobject("\\textbf{Electromagnetism}")
st2 = TexMobject("\\textbf{Fluid\\enspace Dynamics}")
st3 = TexMobject("\\textbf{Thermodynamics}")
st4 = TexMobject("\\textbf{Quantum\\enspace Mechanics}")
st5 = TexMobject("\\textbf{Relativity}")
st6 = TexMobject("\\textbf{Particle\\enspace Physics}")
st7 = TexMobject("\\textbf{Noether's\\enspace Theorem}")

group = VGroup(st1,st4,st3,st2,st5,st6,st7).set_color(TEAL_A)
group.arrange(DOWN,aligned_edge = LEFT,buff = 0.6).shift(4*LEFT)


fb1 = SurroundingRectangle(st1,buff = 0.2,color = YELLOW)
fb2 = SurroundingRectangle(st2,buff = 0.2,color = YELLOW)
fb3 = SurroundingRectangle(st3,buff = 0.2,color = YELLOW)
fb4 = SurroundingRectangle(st4,buff = 0.2,color = YELLOW)

brace = Brace(group,RIGHT,buff = 0.1).set_color(GREEN).shift(0.5*RIGHT).set_height(7)

eqn = consveqndiff.copy().next_to(brace,RIGHT,buff = 0).scale(2/3).shift(0.5*LEFT)

fb5 = SurroundingRectangle(eqn,buff = 0.2,color = GREEN)

generalsurface = Sphere(radius = 1,resolution = (24,24)) 

def Jfield_func(a):
    [x,y,z] = a[0:3]
    mag = (x**2 + y**2 + z**2)**0.5
    if (abs(x)<=1 and abs(y)<=1 and abs(z)<= 1):
        return np.array([(x/mag**3),(y/mag**3),(z/mag**3)])
    else:
        return np.array([0,0,0])


class IntroScene(Scene):
	def construct(self):
			
		self.play(Write(consveqndiff) , run_time = 2)

		self.wait(2)

		self.play(Transform(consveqndiff,eqntext))

		self.wait(2)

		self.play(ReplacementTransform(consveqndiff,eqn),run_time = 2)

		self.play(FadeInFrom(brace,LEFT),ShowCreation(fb5),run_time = 2)

		self.play(Write(group))

		self.wait(2)

		self.play(*[
						ShowCreation(i)
						for i in [fb1,fb4]
			])

		self.wait(5)

class Generalization_Visual(ThreeDScene):
	def construct(self):
		surface = Sphere(radius = 1,resolution = (24,24))
		
		Jfield = VectorField(Jfield_func,
							length_func = linear,
                            delta_x = 1,
                            delta_y = 1,
                            delta_z = 1,
                            x_min = -2.5,
                            x_max = 2.5,
                            y_min = -2.5,
                            y_max = 2.5,
                            z_min = -2.5,
                            z_max = 2.5
							)

		dot1  = Sphere(radius = 0.1).set_color(RED)
		dot2  = Sphere(radius = 0.1).set_color(RED)
		dot3  = Sphere(radius = 0.1).set_color(RED)
		dot4  = Sphere(radius = 0.1).set_color(RED)
		dot5  = Sphere(radius = 0.1).set_color(RED)
		dot6  = Sphere(radius = 0.1).set_color(RED)
		dot7  = Sphere(radius = 0.1).set_color(RED) 
		dot8  = Sphere(radius = 0.1).set_color(RED)
		dot9  = Sphere(radius = 0.1).set_color(RED)
		dot10 = Sphere(radius = 0.1).set_color(RED)
		dot11 = Sphere(radius = 0.1).set_color(RED)
		dot12 = Sphere(radius = 0.1).set_color(RED)
		dot13 = Sphere(radius = 0.1).set_color(RED)
		dot14 = Sphere(radius = 0.1).set_color(RED)

		dots = [dot1,dot2,dot3,dot4,dot5,dot6,dot7,dot8,dot9,dot10,dot11,dot12,dot13,dot14]

		

		dots_points = [(dot1,[5,1.5,0]),(dot2,[0,-10,0]),(dot3,[0,0,2.0]),(dot4,[-4.5,2.0,0]),(dot5,[0,2.1,4.9]),(dot6,[2.0,0,-2.0]),(dot7,[-2.0,2.0,0]),(dot8,[-2.0,1.0,0]),
						(dot9,[0,-2,0]),(dot10,[0,1,3.5]),(dot11,[-2,2.1,0]),(dot12,[0,-2.0,2.0]),(dot13,[-0.20,1,-2.0]),(dot14,[2.000,2.0,-1.0])]
		
		dots_group = VGroup()
		for dot in dots:
			dots_group = dots_group.add(dot)

		self.set_camera_orientation(phi=30*DEGREES)
		self.add(surface)
		self.begin_ambient_camera_rotation(rate = 0.5)
		self.add_fixed_in_frame_mobjects(TextMobject("\\textbf{V}").shift(UP+RIGHT))
		self.wait(5)

		self.bring_to_back(dots_group)
		

		self.play(*[
				Transform(dot,dot.copy().shift(np.array(point)))
				for dot,point in dots_points
			]
			,run_time = 4

			)	
		self.wait(4)

		self.remove(dots_group)

		self.play(ShowCreation(Jfield),run_time = 3)

		self.wait(4)

class Generalization_Scene(Scene):
	def construct(self):
		g1 = TexMobject("\\vec{J} = \\rho\\vec{v}")
		g2 = TextMobject("Rate of flow of q through \\\\ closed surface ","$ = \\oiint\\limits_{\\partial V}{\\vec{J}\\cdot d\\vec{A}}$")
		g2[1].set_color(ORANGE)
		g2[0].set_color(BLUE_D)
		g3_1 = TextMobject("Rate of Change of q").shift(3.5*LEFT + UP)
		g3_2 = TextMobject("Rate of Production of q").shift(3.5*LEFT + UP)
		g3_3 = TextMobject("Rate of flow of q \\\\ through closed surface").shift(3.5*LEFT + UP)

		g4 = TexMobject("\\frac{dq}{dt}"," = ","\\Sigma "," - ","\\oiint\\limits_{\\partial V}{\\vec{J}\\cdot d\\vec{A}}")
		g4.shift(1*DOWN + 3.5*LEFT)
		
		g5 = TexMobject("\\frac{d}{dt}{\\int_{V}{\\rho dV}}"," = ","\\int_{V}{\\sigma dV} "," - ","\\int_{V}{\\nabla \\cdot \\vec{J} dV}")
		
		for i,color,word in [(0,RED,g3_1),(2,GREEN,g3_2),(4,ORANGE,g3_3)] :
			g4[i].set_color(color)
			g5[i].set_color(color)
			word.set_color(color)
		
		g6 = TexMobject("\\int_{V}{\\frac{\\partial \\rho}{\\partial t} dV}"," + ","\\int_{V}{\\nabla\\cdot\\vec{J} dV}"," = ","\\int_{V}{\\sigma dV}")
		g7 = TexMobject("\\frac{\\partial \\rho}{\\partial t}"," + ","\\nabla\\cdot\\vec{J}"," = ","\\sigma")
		for i,color in [(0,RED),(4,GREEN),(2,ORANGE)]:
			g6[i].set_color(color)
			g7[i].set_color(color)
		
		g8 = consveqndiff.scale(1/3)

		self.play(Write(TextMobject("\\textbf{THE CONTINUITY EQUATION}").set_color(GREEN).move_to(3*UP)),
				ShowCreation(Line(3*UP + 5.5*LEFT,3*UP + 5.5*RIGHT).next_to(TextMobject("\\textbf{THE CONTINUITY EQUATION}").set_color(GREEN).move_to(3*UP),DOWN,buff = 0.3).set_color(YELLOW)),
				run_time = 3
			)
		self.wait(2)

		self.play(Write(g1.shift(3.5*LEFT + 1.5*UP).set_color(YELLOW)),run_time = 2)
		self.wait(2)


		self.play(Write(g2.shift(3.5*LEFT))
				,run_time = 4)
		self.wait(2)

		self.play(FadeOut(g2),FadeOut(g1),run_time = 3)
		self.wait(2)

		for word,i in [(g3_1,0),(g3_2,2),(g3_3,4)]:
			self.play(Write(word),run_time = 2)
			self.wait(2)
			self.play(ReplacementTransform(word,g4[i]),run_time = 2)
			self.wait(2)
		
		self.play(Write(g4[1]),Write(g4[3]),
			g4.shift,UP,
			run_time = 2)
		self.wait(3)

		self.play(	
					Write(g5[:4]),
					ReplacementTransform(g4[4].copy(),g5.shift(1.5*DOWN + 2.5*LEFT)[4]),
					run_time = 3
			)	
		self.wait(2)

		self.play(	
					Write(g6.shift(3*DOWN + 2.5*LEFT)[1:]),
					ReplacementTransform(g5[0].copy(),g6[0]),
					run_time = 3
			)
		self.wait(2)

		self.play(
					*[FadeOut(x)
						for x in [g4,g5]
					],
					g6.shift,3*UP,
					run_time = 3
			)
		self.wait(2)

		self.play(
					ReplacementTransform(g6.copy(),g7.shift(1.5*DOWN + 3.5*LEFT)),
					run_time = 2
			)
		self.wait(3)

		self.play(g7.shift,2.5*UP,FadeOut(g6),run_time = 2)
		self.wait(2)


		brace_sig = Brace(g7[4],UP).set_color(RED)
		text_sig = brace_sig.get_text("0").set_color(GREEN)

		self.play(
					ShowCreation(brace_sig),
					Write(text_sig),
					run_time = 2
			)
		self.wait(2) 

		self.play(
					FadeOut(brace_sig),FadeOut(text_sig),
					ReplacementTransform(g7,g8.scale(2).shift(3.5*LEFT)),
					run_time = 2
			)
		self.wait(2)






class Generalization_Visual_With_Field_And_Dots(ThreeDScene):
	def construct(self):
		#self.add(text,brace,fb4,fb3,fb2,fb1,fb5,group)
		Jfield = VectorField(Jfield_func,
                            delta_x = 0.4,
                            delta_y = 0.4,
                            delta_z = 0.4,
                            x_min = -1.5,
                            x_max = 1.5,
                            y_min = -1.5,
                            y_max = 1.5,
                            z_min = -1.5,
                            z_max = 1.5
							)
		self.add(Jfield,generalsurface)
		self.set_camera_orientation(phi = 45*DEGREES)
		self.begin_ambient_camera_rotation(rate = 1)
		self.wait(2)

		
		

		dot1  = Sphere(radius = 0.1).set_color(RED)
		dot2  = Sphere(radius = 0.1).set_color(RED)
		dot3  = Sphere(radius = 0.1).set_color(RED)
		dot4  = Sphere(radius = 0.1).set_color(RED)
		dot5  = Sphere(radius = 0.1).set_color(RED)
		dot6  = Sphere(radius = 0.1).set_color(RED)
		dot7  = Sphere(radius = 0.1).set_color(RED) 
		dot8  = Sphere(radius = 0.1).set_color(RED)
		dot9  = Sphere(radius = 0.1).set_color(RED)
		dot10 = Sphere(radius = 0.1).set_color(RED)
		dot11 = Sphere(radius = 0.1).set_color(RED)
		dot12 = Sphere(radius = 0.1).set_color(RED)
		dot13 = Sphere(radius = 0.1).set_color(RED)
		dot14 = Sphere(radius = 0.1).set_color(RED)

		dots = [dot1,dot2,dot3,dot4,dot5,dot6,dot7,dot8,dot9,dot10,dot11,dot12,dot13,dot14]

		

		dots_points = [(dot1,[5,1.5,0]),(dot2,[0,-10,0]),(dot3,[0,0,2.0]),(dot4,[-4.5,2.0,0]),(dot5,[0,2.1,4.9]),(dot6,[2.0,0,-2.0]),(dot7,[-2.0,2.0,0]),(dot8,[-2.0,1.0,0]),
						(dot9,[0,-2,0]),(dot10,[0,1,3.5]),(dot11,[-2,2.1,0]),(dot12,[0,-2.0,2.0]),(dot13,[-0.20,1,-2.0]),(dot14,[2.000,2.0,-1.0])]
		
		dots_group = VGroup()
		for dot in dots:
			dots_group = dots_group.add(dot)
		self.bring_to_back(dots_group)
		
		self.play(*[
				Transform(dot,dot.copy().shift(np.array(point)))
				for dot,point in dots_points
			]
			,run_time = 4

			)			
		#self.add_fixed_in_frame_mobjects(consveqndiff)
		self.wait(2)
	
class Electromagnetism_Scene(Scene):
	def construct(self):
		
		lorentz_force = TexMobject("\\vec{F}"," = ","q\\vec{E} + q\\vec{v}\\times\\vec{B}")

		t1  = TextMobject("What would the expression for infinitesimal \\\\ work would look like ?")
		t2  = TexMobject("dW = ","\\vec{F}","\\cdot d\\vec{l}")
		t3  = TextMobject("If you remember the WORK-ENERGY Theorem ")
		t4  = TextMobject("It tells you that the work done by all the forces \\\\ is the same as change in kinetic energy.")
		t5  = TexMobject("dW = ","dU_{kinetic}")
		t6  = TexMobject("dU_{kinetic} = dW = \\vec{F}\\cdot d\\vec{l}")
		t7  = TexMobject("d\\vec{l} = \\vec{v}dt")
		t8  = TexMobject("dU_{kinetic}"," = (q\\vec{E} + q\\vec{v}\\times\\vec{B}) \\cdot d\\vec{l}")
		t9  = TexMobject("dU_{kinetic} = (q\\vec{E} + q\\vec{v}\\times\\vec{B}) \\cdot \\vec{v}dt")
		t10 = TexMobject("dU_{kinetic} = q\\vec{E}\\cdot \\vec{v}dt + ","q(\\vec{v}\\times\\vec{B})\\cdot \\vec{v}dt")
		t11 = TexMobject("dU_{kinetic} = q\\vec{E}\\cdot \\vec{v}dt")
		t12 = TexMobject("\\frac{dU_{kinetic}}{dt} = q\\vec{E}\\cdot\\vec{v}")
		t13 = TexMobject("\\frac{dU_{kinetic}}{dt} = \\int_{V}{ ","\\rho \\vec{v}","\\cdot\\vec{E} \\ dV}")
		t131= TexMobject("\\frac{dU_{kinetic}}{dt} = ","\\int_{V}{ ","\\vec{J}","\\cdot\\vec{E} \\ dV}")
		t14 = TexMobject("\\frac{dU_{kinetic}}{dt} = ","\\int_{V}{{\\partial u_{kinetic} \\over \\partial t} \\ dV}")
		t141= TexMobject("\\int_{V}{{\\partial u_{kinetic} \\over \\partial t} \\ dV}","= \\int_{V}{\\vec{J}\\cdot\\vec{E} \\ dV}")
		t15 = TexMobject("{\\partial u_{kinetic} \\over \\partial t} = \\vec{J}\\cdot\\vec{E}")
		t16 = TexMobject("\\nabla\\times\\vec{B} = \\mu_{0}\\vec{J} + \\mu_{0}\\varepsilon_{0}\\frac{\\partial\\vec{E}}{\\partial t}") # Ampere's Law
		t17 = TexMobject("\\vec{J} = {(\\nabla\\times\\vec{B}) \\over \\mu_{0}} - \\varepsilon_{0}\\frac{\\partial\\vec{E}}{\\partial t}")
		t18 = TexMobject("{\\partial u_{kinetic} \\over \\partial t} = {\\vec{E}\\cdot(\\nabla\\times\\vec{B}) \\over \\mu_{0}} - \\varepsilon_{0}\\vec{E}\\cdot\\frac{\\partial\\vec{E}}{\\partial t}")
		t19 = TexMobject("\\nabla\\cdot(\\vec{E}\\times\\vec{B}) = \\vec{B}\\cdot(\\nabla\\times\\vec{E}) - \\vec{E}\\cdot(\\nabla\\times\\vec{B}) ") # Vector Calculus Identity
		t20 = TexMobject("\\vec{E}\\cdot(\\nabla\\times\\vec{B}) = \\vec{B}\\cdot(\\nabla\\times\\vec{E}) - \\nabla\\cdot(\\vec{E}\\times\\vec{B}) ")
		t21 = TexMobject("{\\partial u_{kinetic} \\over \\partial t} = { (\\vec{B}\\cdot(\\nabla\\times\\vec{E}) - \\nabla\\cdot(\\vec{E}\\times\\vec{B})) \\over \\mu_{0}} - \\varepsilon_{0}\\vec{E}\\cdot\\frac{\\partial\\vec{E}}{\\partial t}")
		t22 = TexMobject("\\nabla\\times\\vec{E} = -{{\\partial\\vec{B}} \\over {\\partial t}}") #Faraday's Law
		t23 = TexMobject("{\\partial u_{kinetic} \\over \\partial t} = { (\\vec{B}\\cdot(-{{\\partial\\vec{B}} \\over {\\partial t}}) - \\nabla\\cdot(\\vec{E}\\times\\vec{B})) \\over \\mu_{0}} - \\varepsilon_{0}\\vec{E}\\cdot\\frac{\\partial\\vec{E}}{\\partial t}")
		t24 = TexMobject("{\\partial u_{kinetic} \\over \\partial t} = { (\\vec{B}\\cdot(-{{\\partial\\vec{B}} \\over {\\partial t}}) - \\nabla\\cdot(\\vec{E}\\times\\vec{B})) \\over \\mu_{0}} - \\varepsilon_{0}\\vec{E}\\cdot\\frac{\\partial\\vec{E}}{\\partial t}")
		t25 = TexMobject("{\\partial u_{kinetic} \\over \\partial t} = -\\frac{1}{\\mu_{0}}{\\vec{B}\\cdot({{\\partial\\vec{B}} \\over {\\partial t}})} - \\varepsilon_{0}\\vec{E}\\cdot\\frac{\\partial\\vec{E}}{\\partial t} - \\nabla\\cdot({\\vec{E}\\times\\vec{B} \\over \\mu_{0}}) ")
		t26 = TexMobject("\\vec{B}\\cdot{\\partial \\vec{B} \\over \\partial t} = \\frac{1}{2}\\frac{\\partial}{\\partial t}{(\\vec{B}\\cdot\\vec{B})}")
		t27 = TexMobject("{\\partial u_{kinetic} \\over \\partial t} = -\\frac{1}{2}\\left(\\varepsilon_{0}\\frac{\\partial}{\\partial t}{(\\vec{E}\\cdot\\vec{E})} +\\frac{1}{\\mu_{0}}\\frac{\\partial}{\\partial t}{(\\vec{B}\\cdot\\vec{B})}\\right) - \\nabla\\cdot\\left({\\vec{E}\\times\\vec{B} \\over \\mu_{0}}\\right) ")
		t28 = TexMobject("{\\partial u_{kinetic} \\over \\partial t} = -\\frac{\\partial}{\\partial t}\\left(\\frac{\\varepsilon_{0}}{2}\\vec{E}\\cdot\\vec{E} + \\frac{1}{2\\mu_{0}}{\\vec{B}\\cdot\\vec{B}}\\right) - \\nabla\\cdot\\left({\\vec{E}\\times\\vec{B} \\over \\mu_{0}}\\right)")
		t29 = TexMobject("{\\partial u_{kinetic} \\over \\partial t} = -\\frac{\\partial u_{field}}{\\partial t} - \\nabla\\cdot\\left({\\vec{E}\\times\\vec{B} \\over \\mu_{0}}\\right)")
		t30 = TexMobject("{\\partial  \\over \\partial t}{\\left(","u_{kinetic} + u_{field}","\\right)} = - \\nabla\\cdot\\left({\\vec{E}\\times\\vec{B} \\over \\mu_{0}}\\right)")
		t31 = TexMobject("{\\partial  \\over \\partial t}{(","u_{total}",")} = - \\nabla\\cdot\\vec{S}")
		t311 = TexMobject("\\vec{S} = {\\vec{E}\\times\\vec{B} \\over \\mu_{0}}")
		t312 = TexMobject("\\nabla\\cdot\\vec{S} = -{\\partial  \\over \\partial t}{(","u_{total}",")}")

		t32 = TexMobject("I = -\\frac{d}{dt}\\int_{V}{\\rho \\ dV}")
		t33 = TexMobject("I \\ = ","\\oiint_{\\partial V}{\\vec{J}\\cdot d\\vec{A}}")
		t34 = TexMobject("I = ","\\int_{V}{-\\frac{\\partial \\rho}{\\partial t} dV}")
		t35 = TexMobject("\\int_{V}{-\\frac{\\partial \\rho}{\\partial t} dV} = ","\\oiint_{\\partial V}{\\vec{J}\\cdot d\\vec{A}}")
		t351 = TexMobject("\\int_{V}{-\\frac{\\partial \\rho}{\\partial t} dV} = ","\\int_{V}{\\nabla\\cdot\\vec{J} dV}")
		t352 = consveqndiff.copy().shift(0.5*DOWN + 3.5*LEFT).scale(0.5)
		t36 = TexMobject("dW = ","(q\\vec{E} + q\\vec{v}\\times\\vec{B})","\\cdot d\\vec{l}").shift(3*DOWN)
		
		# Animation to move from contents to title Electromagnetism
		self.add(eqn,fb5,group,brace,fb1,fb4)
		self.wait(2)

		emtitle = st1.copy().move_to(3*UP)

		self.play(ReplacementTransform(st1,emtitle),
					ShowCreation(Line(3*UP + 5.5*LEFT,3*UP + 5.5*RIGHT).next_to(emtitle,DOWN,buff = 0.5).set_color(YELLOW)),
					*[FadeOut(x)
						for x in [group.remove(st1),eqn,fb5,brace,fb1,fb4]
					],
					run_time = 2
			)
		self.wait(2)
		
		titleCC = TextMobject("\\textbf{Charge Conservation}").set_color(RED)
		titleEC = TextMobject("\\textbf{Energy Conservation}").set_color(RED)
		VGroup(titleCC,titleEC).arrange(DOWN,aligned_edge = LEFT,buff = 1)
		
		self.play(Write(titleEC),Write(titleCC),run_time = 3)
		self.wait(2)
		
		# Charge Conservation Starts
		
		self.play(
					FadeOut(emtitle),FadeOut(titleEC),
					titleCC.shift,(emtitle.get_center() - titleCC.get_center()),
					run_time = 3
			)
		self.wait(2)

		self.play(Write(t32.set_color(MAROON).shift(3.5*LEFT)),run_time = 2)
		self.wait(3)

		self.play(Write(t33.set_color(BLUE).shift(2*DOWN + 3.8*LEFT)),run_time = 2)
		self.wait(3)

		self.play(ReplacementTransform(t32,t34.set_color(MAROON).shift(3.5*LEFT)),run_time = 2)
		self.wait(3)

		t35.set_color(TEAL_E).shift(3.5*LEFT+0.5*DOWN)

		self.play(
						ReplacementTransform(VGroup(t34,t33),t35),
						run_time = 2)
		self.wait(3)

		self.play(ReplacementTransform(t35,t351.set_color(TEAL_D).shift(0.5*DOWN+3.5*LEFT)))
		self.wait(3)

		self.play(ReplacementTransform(t351,t352),run_time = 2)
		self.wait(3)
		
		# Charge Conservation Ends

		# Energy Conservation Starts
		
		self.play(
					FadeOut(emtitle),FadeOut(titleCC),
					titleEC.shift,(emtitle.get_center() - titleEC.get_center()),
					run_time = 3
			)
		self.wait(2)

		self.play(Write(lorentz_force.set_color(BLUE).shift(1.5*UP)),run_time = 2)
		self.wait(2)

		self.play(Write(t1.set_color(RED)),run_time = 3.5)
		self.wait(2)

		self.play(Write(t2.set_color(MAROON).shift(1.5*DOWN)),run_time = 2)
		self.wait(2)

		self.play(ReplacementTransform(t2.copy().set_color(MAROON).shift(1.5*DOWN)[1],t36[1].set_color(BLUE)),
					ReplacementTransform(t2.copy().set_color(MAROON).shift(1.5*DOWN)[0],t36[0].set_color(MAROON)),
					ReplacementTransform(t2.copy().set_color(MAROON).shift(1.5*DOWN)[2],t36[2].set_color(MAROON))
					,run_time = 2)

		
		self.wait(2)

		self.play(*[FadeOut(x)
					for x in [t36,t2,lorentz_force,t1]
			])
		self.wait()

		self.play(Write(t3.set_color(BLUE).shift(1.5*UP)),run_time = 4)
		self.wait(2)

		self.play(Write(t4.set_color(RED)),run_time = 3.5)
		self.wait(2)

		self.play(Write(t5.set_color(MAROON).shift(1.5*DOWN)),run_time = 2)
		self.wait(2)

		self.play(
					ReplacementTransform(t5[1].copy(),t8.shift(1.5*DOWN)[0].set_color(MAROON)),
					ReplacementTransform(t5[0].copy(),t8.shift(1.5*DOWN)[1].set_color(MAROON)),
					run_time = 2
			)
		self.wait(2)

		self.play(
					*[FadeOut(x)
					for x in [t3,t4,t5]
					],
					t8.shift,4.5*UP,
					run_time = 2
			)
		self.wait(2)

		self.play(
					ReplacementTransform(t8.copy(),t9.set_color(BLUE)),
					run_time = 2
			)
		self.wait(2)
		self.play(
					ReplacementTransform(t9.copy(),t10.set_color(PINK).shift(1.5*DOWN)),
					run_time = 2
			)
		self.wait(2)

		brace_magterm = Brace(t10[1],DOWN,buff = 0.1).set_color(GREEN)
		brace_magterm_text = brace_magterm.get_text("0").set_color(GREEN)
		self.play(ShowCreation(brace_magterm),
			Write(brace_magterm_text),
			run_time = 2)

		self.wait(2)

		self.play(
					ReplacementTransform(t10[0].copy(),t11.shift(3*DOWN).set_color(BLUE_B)),
					run_time = 2
			)
		self.wait(2)

		self.play(
					*[FadeOut(x)
					for x in [t8,t9,t10,brace_magterm_text,brace_magterm]
					],
					t11.shift,4.5*UP,
					run_time = 2
			)
		self.wait(2)

		self.play(
					ReplacementTransform(t11.copy(),t12.set_color(PINK)),
					run_time = 2
			)
		self.wait(2)

		self.play(
					ReplacementTransform(t12.copy(),t13.set_color(RED).shift(1.5*DOWN)),
					run_time = 2
			)
		self.wait(2)

		brace_pv = Brace(t13[1],UP,buff = 0)
		text_brace_pv = brace_pv.get_text("$\\vec{J}$").scale(1)

		self.play(ShowCreation(brace_pv),
			ShowCreation(text_brace_pv))
		self.wait(2)

		self.play(ReplacementTransform(t13.copy(),t131.shift(3*DOWN).set_color(MAROON)),
			run_time = 2)
		self.wait(2)

		self.play(
					*[FadeOut(x)
					for x in [t11,t12,t13,brace_pv,text_brace_pv]
					],
					t131.shift,4.5*UP,
					run_time = 2
			)
		self.wait(2)

		self.play(t131.shift,3.5*RIGHT,
			Write(t14.set_color(MAROON).shift(3.5*LEFT+1.5*UP)),
			run_time = 2)
		self.wait(2)

		self.play(
			ReplacementTransform(t131[1:4].copy(),t141.set_color(BLUE)[1]),
			ReplacementTransform(t14[1].copy(),t141.set_color(BLUE)[0]),
			run_time = 2)
		self.wait(2)

		self.play(
			ReplacementTransform(t141.copy(),t15.shift(1.5*DOWN).set_color(TEAL_E))
			,run_time = 2
			)
		self.wait(2)

		self.play(
			Write(t16.shift(3*DOWN).set_color(PINK)),
			run_time = 2
			)
		self.wait(2)

		self.play(
					*[FadeOut(x)
					for x in [t131,t14,t141]
					],
					t15.shift,(3.5*LEFT+3*UP),
					t16.shift,4.5*UP+3.5*RIGHT,
					run_time = 3
			)
		self.wait(2)

		self.play(
					ReplacementTransform(t16.copy(),t17.set_color(BLUE)),
					run_time = 2
			)
		self.wait(2)

		self.play(
					ReplacementTransform(VGroup(t15.copy(),t17.copy()),t18.shift(1.5*DOWN).set_color(PINK)),
					run_time = 2
			)
		self.wait(2)

		self.play(
					Write(t20.shift(3*DOWN).set_color(BLUE_D)),
					run_time = 2
					)
		self.wait(2)

		self.play(
					*[FadeOut(x)
					for x in [t15,t16,t17]
					],
					ReplacementTransform(VGroup(t18,t20),t21.shift(1.5*UP).set_color(BLUE)),
					run_time = 3
			)
		self.wait(2)

		self.play(Write(t22.set_color(MAROON)),run_time = 2)
		self.wait(2)

		self.play(
					ReplacementTransform(VGroup(t21.copy(),t22.copy()),t23.shift(1.5*DOWN).set_color(RED)),
					run_time = 2
			)
		self.wait(2)

		self.play(
					*[FadeOut(x)
					for x in [t21,t22]
					],
					t23.shift,3*UP
			)
		self.wait(2)

		self.play(
					ReplacementTransform(t23.copy(),t25.set_color(BLUE_D)),
					run_time = 2
			)
		self.wait(2)

		self.play(
					Write(t26.shift(1.5*DOWN).set_color(MAROON)),
					run_time = 2
			)
		self.wait(2)

		self.play(
					ReplacementTransform(VGroup(t26.copy(),t25.copy()),t27.shift(3*DOWN).set_color(TEAL_E)),
					run_time = 2
			)
		self.wait(2)

		

		self.play(
					*[FadeOut(x)
					for x in [t23,t25,t26]
					],
					t27.shift,4.5*UP,
					run_time = 2
			)
		self.wait(3)

		self.play(
					ReplacementTransform(t27.copy(),t28.set_color(PINK)),
					run_time = 2
			)
		self.wait(2)

		self.play(
					ReplacementTransform(t28.copy(),t29.shift(1.5*DOWN).set_color(BLUE_D)),
					run_time = 2
			)
		self.wait(2)

		self.play(
					ReplacementTransform(t29.copy(),t30.shift(3*DOWN).set_color(MAROON))
					,run_time = 2	
			)
		self.wait(2)

		self.play(
					*[FadeOut(x)
					for x in [t27,t28,t29]
					],
					*[ReplacementTransform(t30[i],t31.set_color(TEAL_E)[i])
						for i in [0,1,2]
					],
					run_time = 4
			)
		self.wait(2)

		self.play(
					t31.shift,3.5*LEFT,
					Write(consveqndiff.shift(3.5*RIGHT).scale(1/3)),
					run_time = 2
			)
		self.wait(2)

		self.play(
					ReplacementTransform(t31,t312.set_color(TEAL_E).shift(3.5*LEFT))
					,run_time = 2
				)
		self.wait(2)

		self.play(
					Write(t311.shift(1.5*DOWN+3.8*LEFT).set_color(YELLOW)),
					run_time = 2
			)
		self.wait(2)

		#Energy Conservation Ends 


class Quantum_Mechanics_Scene(Scene):
	def construct(self):

		# Animation to move from contents to title Quantum Mechanics

		self.add(eqn,fb5,group,brace,fb1,fb4)
		self.wait(2)

		qmtitle = st4.copy().move_to(3*UP)

		self.play(ReplacementTransform(st4,qmtitle),
					ShowCreation(Line(3*UP + 5.5*LEFT,3*UP + 5.5*RIGHT).next_to(qmtitle,DOWN,buff = 0.4).set_color(YELLOW)),
					*[FadeOut(x)
						for x in [group.remove(st4),eqn,fb5,brace,fb1,fb4]
					],
					run_time = 2
			)
		self.wait(2)

		qm1 = TexMobject("\\int\\limits_{all \\ space}{|\\Psi(\\vec{x},0) |^2 \\ dV} = 1")
		qm2 = TexMobject("\\int\\limits_{all \\ space}{","|\\Psi(\\vec{x},t) |^2"," \\ dV} = 1")
		qmarrow1 = Arrow( qm2.get_top()*0.8 ,qm1.get_bottom()*1.2 ).set_color(RED).scale(2)
		qm3 = TexMobject("N(t) = \\int\\limits_{all \\ space}{\\rho \\ dV}")
		qm4 = TexMobject("\\frac{dN}{dt} = 0")	
		
		
		questmark = TexMobject("?").scale(2)

		# equation Writing Starts
		self.play(Write(qm1.set_color(BLUE_D).shift(1*UP)),run_time = 2)
		self.wait(2)

		self.play(ShowCreation(qmarrow1),run_time = 1)
		self.wait(2)

		self.play(Write(qm2.set_color(BLUE_D).shift(-2*UP)),run_time = 2)
		self.wait(2)

		self.play(ShowCreation(questmark.set_color(GREEN).next_to(qmarrow1,RIGHT,buff = 1)),run_time = 2)
		self.wait(2)

		self.play(
					*[FadeOut(x)
					for x in [qm1,qmarrow1,questmark]
					],
			qm2.shift,3*UP,run_time = 3)
		self.wait(2)

		brace_psi = Brace(qm2[1],DOWN).set_color(GREEN)
		rho_text = brace_psi.get_text("$\\rho$").set_color(GREEN)

		self.play(ShowCreation(brace_psi),ShowCreation(rho_text),run_time = 2)
		self.wait(2)

		self.play(Write(qm3.shift(1*DOWN + 3.5*LEFT).set_color(MAROON)),run_time = 2)
		self.wait(2)

		

		qm4.shift(1*DOWN + 3.5*RIGHT).set_color(MAROON)
		qmarrow2 = Arrow(qm3.get_right(),qm4.get_left()).set_color(RED)

		self.play(ShowCreation(qmarrow2),run_time = 2)
		self.wait(2)

		self.play(Write(qm4),run_time = 2)
		self.wait(2)

		qm5 = TexMobject("\\vec{J}(\\vec{x},t) = \\frac{\\hbar}{m}Im(\\Psi^* \\nabla \\Psi)").shift(3*DOWN + 3.5*RIGHT).set_color(TEAL_E)
		qm6 = consveqndiff.scale(1/3).shift(3*DOWN + 3.5*LEFT).set_color(TEAL_E)
		qmarrow3 = Arrow(qmarrow2.get_center(),qm6.get_top()).set_color(TEAL_E)
		qmarrow4 = Arrow(qmarrow2.get_center(),qm5.get_top()).set_color(TEAL_E)
		questmark2 = TexMobject("?").next_to(qmarrow2,UP,buff = 0.2).scale(2).set_color(RED)


		self.play(
					ShowCreation(qmarrow3),
					ShowCreation(qmarrow4),
					run_time = 2
			)
		self.wait(2)

		self.play(
					Write(qm5),
					Write(qm6),
					run_time = 2
			)
		self.wait(2)

		self.play(Write(questmark2),run_time = 2)
		self.wait(3)