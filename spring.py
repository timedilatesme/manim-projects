from manimlib.imports import*


# DRIVER CODE
# python manim.py my_projects\For_Videos\spring.py -pl

class SourceScene(CustomScene,ThreeDScene,Mobject):		

	def spring(self,t_min = 0,t_max = 1/3*PI,radius = 1,w = 90,pitch = lambda t:  t**2,include_gravity = True,**kwargs):
		if include_gravity :
			spring = ParametricFunction(lambda t : radius*((np.sin(w*t))*RIGHT + (0.05*t*w*pitch(t))*UP + (np.cos(w*t))*OUT),t_min = t_min,t_max = t_max,**kwargs)
		else:
			spring = ParametricFunction(lambda t : radius*((np.sin(w*t))*RIGHT + (0.05*t*w*1)*UP + (np.cos(w*t))*OUT),t_min = t_min,t_max = t_max,**kwargs)

		return spring
	def set_top(self,point):
		top    = self.get_top()
		change = point - top
		return self.shift(change)

	def set_bottom(self,point):
		bottom = self.get_bottom()
		change = point-bottom
		return self.shift(change)

	def set_left(self,point):
		left = self.get_left()
		change = point-left
		return self.shift(change)

	def set_right(self,point):
		right = self.get_right()
		change = point-right
		return self.shift(change)

	def vector_with_text(self,vector,text,tail_position):
		arrow = Arrow(tail_position,vector + tail_position)
		text  = text
		text.move_to(ArrowTip.get_tip_point(arrow) + vector)
		
		return VGroup(arrow,text)		


	def vector_with_tex(self,vector,tex,tail_position):
		arrow = Arrow(tail_position,vector + tail_position)
		tex = tex
		tex.move_to(ArrowTip.get_tip_point(arrow) + vector)

		return VGroup(arrow,tex)


class visualexplaination(SourceScene):
	def construct(self):
		spring1 = self.spring(t_max = PI/4,color  = BLUE)
		spring2 = self.spring(t_min = PI/4,t_max = PI/3,color = BLUE)
		spring = VGroup(spring1,spring2)
		spring.shift(4*LEFT)

		dot0 = Dot(color = RED).shift(-3*RIGHT)
		dot1 = Dot(color = RED).shift(49/180*PI*UP - 3*RIGHT)
		dot2 = Dot(color = RED).shift(2.181659722222222*UP - 3*RIGHT)
		dot3 = Dot(color = RED).shift(4*UP - 3*RIGHT)

		grp = VGroup(spring,dot0,dot1,dot2).set_top(4*UP - 3*RIGHT)
		
		self.add(spring)

		self.play(spring.stretch_about_point,1.5,1,4*UP,rate_func = there_and_back,run_time = 2.5)
		self.wait(2)

		brace_l = Brace(spring,LEFT,buff  = 1,color  =YELLOW)
		brace_l_tex =  brace_l.get_tex("l").set_color(PURPLE)
		self.play(Write(brace_l))
		self.play(Write(brace_l_tex))
		self.wait(2)

		brace_x  = Brace(spring2,LEFT,buff = 0.2,color = YELLOW)
		brace_x_tex = brace_x.get_tex("x").set_color(PURPLE)
		self.play(Write(brace_x))
		self.play(Write(brace_x_tex))
		self.wait(2)


		spring.save_state()
		spring1.save_state()
		spring2.save_state()

		box_for_spring1 = SurroundingRectangle(spring1,buff = 0.05).set_stroke(YELLOW,0.75)
		box_for_spring1.shift(-box_for_spring1.get_top() + spring1.get_top())

		self.play(ShowCreation(box_for_spring1),
					spring.fade,(0.5),run_time = 2)
		self.wait(2)

		mass_vector = self.vector_with_tex(2*DOWN,TexMobject("mass(x)g"),spring1.get_top()).set_color(RED)
		mass_vector.shift(box_for_spring1.get_bottom() - mass_vector.get_top())

		self.play(Write(mass_vector[0]))
		self.write_by_index(mass_vector[1],time_gap = 1,single_anim_time = 1)
		self.wait(2)

		spring2_vector = self.vector_with_tex(2*UP,TexMobject("k","\\delta(x)"),spring1.get_top()).set_color(GREEN)
		spring2_vector.shift(box_for_spring1.get_top() - spring2_vector.get_bottom())

		spring2.restore()
		self.highlight(spring2)

		self.play(Write(spring2_vector[0]),spring2.fade,0.8)
		self.write_by_index(spring2_vector[1],time_gap = 1,single_anim_time = 1)
		self.wait(2)

		self.scale_and_wait(spring2_vector[1][1],wait_time = 2,single_anim_time = 1)
		self.wait()

		

		eqn1 = TexMobject("k","\\delta(x)"," = "," m(x) \\ g").next_to(spring,RIGHT,buff =  2)
		for i,color in [(0,GREEN),(1,GREEN),(3,RED)]:
			eqn1[i].set_color(color)

		eqn2 = TexMobject("k","\\delta(x)"," = ","{m ","\\over"," l} ","(","l"," - ","x",")","g").next_to(spring,RIGHT,buff =  2)
		for i,color in [(0,GREEN),(1,GREEN),(-1,RED),(3,RED),(5,GREEN),(7,GREEN),(9,GREEN)]:
			eqn2[i].set_color(color)

		eqn3 = TexMobject("\\delta(x)"," = ","{m ","\\over"," lk} ","(","l"," - ","x",")","g").next_to(spring,RIGHT,buff =  3).shift(1*DOWN).scale(1.5)
		for i,color in [(0,GREEN),(2,RED),(-1,RED),(-7,GREEN),(-5,GREEN),(-3,GREEN)]:
			eqn3[i].set_color(color)

		self.play(*[ReplacementTransform(spring2_vector[1][x].copy(),eqn1[i])
					for x,i in [(0,0),(1,1)]],run_time = 2)
		self.wait(2)

		self.play(Write(eqn1[2]))

		self.play(ReplacementTransform(mass_vector[1].copy(),eqn1[3]),run_time = 2)
		self.wait(2)

		brace_x_tex.save_state()

		#new_things = VGroup(spring2_vector,mass_vector,brace_x,brace_l,brace_l_tex,brace_x_tex)
		#self.play(new_things.fade,0.5)

		mass = TexMobject("m(x)"," = ","{m ","\\over"," l} ","(","l"," - ","x",")").next_to(eqn1,DOWN,buff = 1)
		for i,color in [(0,RED),(2,RED),(4,GREEN),(6,GREEN),(8,GREEN)]:
			mass[i].set_color(color)

		self.play(Write(mass))
		self.wait()

		self.play(Transform(eqn1[3],eqn2[3:]),run_time = 2)
		self.wait(2)

		self.play(FadeOut(mass),ReplacementTransform(eqn1,eqn3))
		self.wait(2)

		rect = SurroundingRectangle(eqn3,buff = 0.3)

		self.play(ShowCreation(rect),run_time  =2)
		self.wait(2)

		brace_x_tex.restore()

		self.highlight(brace_x_tex)

		width0 = eqn3[0].get_width()
		height0 = eqn3[0].get_height()
		width3 = eqn3[-3].get_width()
		height3 = eqn3[-3].get_height()

		scale_tracker  = ValueTracker(1)

		def eqn3_updater(m):
			m[0].set_width(width0/scale_tracker.get_value()).set_height(height0/scale_tracker.get_value())
			m[-3].set_width(width3*scale_tracker.get_value()).set_height(height3*scale_tracker.get_value())
			return m


		eqn3.add_updater(eqn3_updater)

		self.play(scale_tracker.set_value,2,run_time = 2)
		self.play(scale_tracker.set_value,0.5,run_time = 2)
		self.play(scale_tracker.set_value,1,run_time = 2)
		self.wait(2)


	
class hookes_law(SourceScene,Camera):
	def construct(self):
		x = ValueTracker(1)

		wall = Line(1*UP,1*DOWN).set_stroke(GREY,50).shift(LEFT*self.frame_width/2)

		spring = self.spring().rotate(PI/2).center().set_left(LEFT*self.frame_width/2).set_color(TEAL_E)
		def spring_updater(m):
			new = self.spring().rotate(PI/2).center().set_left(LEFT*self.frame_width/2).set_color(TEAL_E).stretch_about_point(x.get_value(),0,LEFT*self.frame_width/2)
			return m.become(new)
		spring.add_updater(spring_updater)

		force =  self.vector_with_tex(2*RIGHT,TexMobject("F"),spring.get_right() + 0.2*LEFT).set_color(RED)
		def force_updater(m):
			new = self.vector_with_tex(2*RIGHT,TexMobject("F"),spring.get_right() + 0.2*LEFT).set_color(RED)
			new[1].scale(1.5*x.get_value())
			return m.become(new)
		force.add_updater(force_updater)

		spring_force = self.vector_with_tex(2*LEFT,TexMobject("k\\delta"),spring.get_right() + 0.2*LEFT).set_color(GREEN)
		def spring_force_updater(m):
			new = self.vector_with_tex(2*LEFT,TexMobject("k\\delta"),spring.get_right() - 0.2*LEFT).set_color(GREEN)
			new[1].scale(1.5*x.get_value())
			return m.become(new)
		spring_force.add_updater(spring_force_updater)

		
		self.play(ShowCreation(spring),Write(wall),run_time  = 2)
		self.wait()

		self.play(Write(force),run_time = 2)
		self.wait(2)

		self.play(x.set_value,1.8,run_time = 2,rate_func  = there_and_back)
		self.wait(2)

		self.play(Write(spring_force))
		self.wait(2)

		delta = TextMobject("$\\delta$: spring stretch \\\\ or compression").set_color_by_gradient(RED,GREEN,BLUE)

		self.play(Write(delta.to_edge(RIGHT,buff = 0.5)),run_time = 3)
		self.wait(2)

		self.play(FadeOut(delta))
		self.wait(2)

		self.play(x.set_value,1.8,run_time = 2,rate_func  = there_and_back)
		self.wait(2)

		hooke = TexMobject("F"," = ","k \\delta").to_edge(DOWN,buff = 1.8).scale(2)
		for i,color in [(0,RED),(-1,GREEN)]:
			hooke[i].set_color(color)


		self.play(*[ReplacementTransform(x.copy(),hooke[j])
					for x,j in [(spring_force[1],2),(force[1],0)]],Write(hooke[1]),run_time = 2)
		self.wait(2)

		title = TextMobject("Hooke's Law").scale(2).to_edge(UP).set_color_by_gradient(PINK,BLUE,YELLOW)

		fb = SurroundingRectangle(hooke,buff = 0.3)

		self.play(ShowCreation(fb))
		self.wait(2)

		self.play(Write(title))
		self.wait(2)

		

class cutting_spring(SourceScene):
	def construct(self):
		spring1 = self.spring(include_gravity = False,t_max = PI/6,color = TEAL_E)
		spring1.center()
		spring2 = spring1.copy().shift(-spring1.get_top() + spring1.get_center())
		spring1.shift(spring1.get_top() - spring1.get_center()).rotate(PI,axis = UP)

		spring = VGroup(spring1,spring2)		

		self.play(spring.shift,4*LEFT,run_time = 2)
		self.wait(2)

		brace_l = Brace(spring,LEFT,buff = 0.2).set_color(YELLOW)
		brace_l_tex = brace_l.get_tex("l").set_color(PURPLE) 
		brace_x = Brace(spring1,RIGHT,buff = 0.2).set_color(YELLOW)
		brace_x_tex = brace_x.get_tex("x").set_color(PURPLE)
		brace_lx = Brace(spring2,RIGHT,buff = 0.2).set_color(YELLOW)
		brace_lx_tex = brace_lx.get_tex("l-x").set_color(PURPLE)

		self.play(Write(brace_l))
		self.wait()

		self.play(Write(brace_l_tex))
		self.wait()		

		cut_line = DashedLine(0.3*LEFT + spring.get_left(),0.3*RIGHT + spring.get_right(),color = RED)

		self.play(Write(cut_line))
		self.wait(2)

		self.play(Write(brace_x))
		self.wait()

		self.play(Write(brace_x_tex))
		self.wait()

		self.play(Write(brace_lx))
		self.wait()

		self.play(Write(brace_lx_tex))
		self.wait()

		daughter_spring1 = self.spring(include_gravity = False,t_max = PI/6,color = MAROON).center().rotate(PI,axis = UP)
		daughter_spring2 = self.spring(include_gravity = False,t_max = PI/6,color = MAROON).center()

		daughters = VGroup(daughter_spring1,daughter_spring2).arrange(DOWN,aligned_edge = ORIGIN,buff = 2).shift(3*RIGHT)

		d_brace_x = Brace(daughter_spring1,RIGHT,buff = 0.2).set_color(YELLOW)
		d_brace_x_tex = d_brace_x.get_tex("x").set_color(PURPLE)
		d_brace_lx = Brace(daughter_spring2,RIGHT,buff = 0.2).set_color(YELLOW)
		d_brace_lx_tex = d_brace_lx.get_tex("l-x").set_color(PURPLE)

		self.play(*[ReplacementTransform(s.copy(),d)
					for s,d in [(spring1,daughter_spring1),(spring2,daughter_spring2)]],run_time = 2)
		self.wait(2)

		self.play(Write(d_brace_x))
		self.wait()

		self.play(Write(d_brace_x_tex))
		self.wait()

		self.play(Write(d_brace_lx))
		self.wait()

		self.play(Write(d_brace_lx_tex))
		self.wait()

		k  = TexMobject("k").next_to(spring,UP,buff = 0.3).set_color(RED)
		k1 = TexMobject("k_{1}").next_to(daughter_spring1,LEFT,buff = 0.3).set_color(RED)
		k2 = TexMobject("k_{2}").next_to(daughter_spring2,LEFT,buff = 0.3).set_color(RED)

		self.play(Write(k))
		self.wait()

		self.play(Write(k1),Write(k2))
		self.wait()

		self.highlight(k1),self.highlight(k2)
		self.wait(2)

		self.highlight(k1,scale_factor = 1.5),self.highlight(k2,scale_factor = 1.5)
		self.wait(2)

		eqn = TexMobject("k","l"," = ","k_{1}","x"," = ","k_{2}","(l-x)").scale(2)
		for i,color in [(0,RED),(1,PURPLE),(3,RED),(4,PURPLE),(6,RED),(7,PURPLE)]:
			eqn[i].set_color(color)
		
		all_things = VGroup(k,k1,k2,brace_l_tex,d_brace_lx_tex,d_brace_x_tex,brace_l,spring,daughter_spring1,daughter_spring2,cut_line,brace_x,brace_lx,brace_x_tex,brace_lx_tex,d_brace_lx,d_brace_x)

		self.play(all_things.fade)

		text = TextMobject("(spring constant)","(length of spring)","\\\\ = constant").set_color_by_gradient(PURPLE,GREEN).scale(1.5)
		self.write_by_index(text,time_gap = 1,single_anim_time = 1)
		self.wait(2)

		self.play(FadeOut(text))
		self.wait(2)

		self.play(*[ReplacementTransform(x.copy(),eqn[y])
					for x,y in [(k,0),(brace_l_tex,1)]],run_time = 2)
		self.wait(2)

		self.play(Write(eqn[2]))
		self.wait()

		self.play(*[ReplacementTransform(x.copy(),eqn[y])
					for x,y in [(k1,3),(d_brace_x_tex,4)]],run_time = 2)

		self.play(Write(eqn[5]))
		self.wait()

		self.play(*[ReplacementTransform(x.copy(),eqn[y])
					for x,y in [(k2,-2),(d_brace_lx_tex,-1)]],run_time = 2)

		self.wait(2)

		frame = SurroundingRectangle(eqn,buff = 0.5)

		self.play(ShowCreation(frame),
					all_things.set_opacity,0)
		self.wait(2)

class EndScene(SourceScene):
	def construct(self):
		spring1 = self.spring()
		spring2 = self.spring()
		spring3 = self.spring()
		spring4 = self.spring()
		spring5 = self.spring()
		spring6 = self.spring()
		spring7 = self.spring()
		spring8 = self.spring()
		spring9 = self.spring()
		spring10 = self.spring()
		spring11 = self.spring()
		spring12 = self.spring()

		grp = VGroup(spring1,spring2,spring3,spring4,spring5,spring6,spring7,spring8,spring9,spring10,spring11,spring12).arrange(RIGHT,aligned_edge = UP,buff = 0.8).shift(6*UP).set_color_by_gradient(PURPLE,BLUE,GREEN,YELLOW,ORANGE,RED)

		self.add(grp)

		self.camera.frame_center.shift(27*OUT)

		for i in range(5):			
			self.play(spring1.stretch_about_point,2.5 + (np.sin(2*spring1.get_x()))**1,1,spring1.get_top(),
						spring2.stretch_about_point,2.5 + (np.sin(2*spring2.get_x()))**1,1,spring2.get_top(),
						spring3.stretch_about_point,2.5 + (np.sin(2*spring3.get_x()))**1,1,spring3.get_top(),
						spring4.stretch_about_point,2.5 + (np.sin(2*spring4.get_x()))**1,1,spring4.get_top(),
						spring5.stretch_about_point,2.5 + (np.sin(2*spring5.get_x()))**1,1,spring5.get_top(),
						spring6.stretch_about_point,2.5 + (np.sin(2*spring6.get_x()))**1,1,spring6.get_top(),
						spring7.stretch_about_point,2.5 + (np.sin(2*spring7.get_x()))**1,1,spring6.get_top(),
						spring8.stretch_about_point,2.5 + (np.sin(2*spring8.get_x()))**1,1,spring8.get_top(),
						spring9.stretch_about_point,2.5 + (np.sin(2*spring9.get_x()))**1,1,spring9.get_top(),
						spring10.stretch_about_point,2.5 + (np.sin(2*spring10.get_x()))**1,1,spring10.get_top(),
						spring11.stretch_about_point,2.5 + (np.sin(2*spring11.get_x()))**1,1,spring11.get_top(),
						spring12.stretch_about_point,2.5 + (np.sin(2*spring12.get_x()))**1,1,spring12.get_top(),
						rate_func = there_and_back,run_time = 3)
		self.wait(2)

class thumb(Scene):
	def construct(self):
		text = TextMobject("Why is this \\\\ Seperation \\\\ Decreasing?").set_color_by_gradient(PINK,BLUE,YELLOW,RED)
		text.scale(3)

		self.add(text)

