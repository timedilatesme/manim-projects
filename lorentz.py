from manimlib.imports import *
import math as mt

# DRIVER CODE
# python manim.py my_projects\For_Videos\Special_Relativity\lorentz.py -pl

class TwoFriends(CustomScene):
	def construct(self):
		
		man2 = self.add_man(file_name = "running.svg").to_edge(LEFT + 0.5*UP).shift(1*RIGHT)
		man1 = self.add_man(velocity_label = "0",velocity_color = RED,frame_label = "S_{1}",add_vector = False).next_to(man2,DOWN,buff = 1)

		self.write_by_index(man1,time_gap = 1,single_anim_time = 1)

		self.write_by_index(man2,time_gap = 1,single_anim_time = 1)
		self.wait(2)

		self.play(man2.shift,4*RIGHT)
		self.wait()

		dot = Dot(radius = 0.5).to_edge(RIGHT).set_color(TEAL)

		line1 = self.horizontal_distance_measuring_line(man1.get_bottom(),(dot.get_x() - man1.get_x())*RIGHT,label = "x_{1}").shift(0.5*DOWN)
		line2 = self.horizontal_distance_measuring_line(man2.get_bottom(),(dot.get_x() - man2.get_x())*RIGHT,label = "x_{2}")

		line3 = self.horizontal_distance_measuring_line(man2.get_top(),man1.get_x()*RIGHT - man2.get_x()*RIGHT,label = "vt")

		self.play(ShowCreation(line3),run_time = 3)
		self.wait(2)

		self.play(FadeIn(dot))
		self.wait(2)

		self.play(ShowCreation(line1),run_time = 3)
		self.wait(2)

		self.play(ShowCreation(line2),run_time = 3)
		self.wait(2)

		galtran = TexMobject("x_{2}"," = ","x_{1}"," - ","vt").scale(2)
		for i,color in [(0,RED),(2,RED),(-1,RED)]:
			galtran[i].set_color(color)
		galtran1 = TexMobject("t_{2}"," = ","t_{1}"," = ","t").next_to(galtran,DOWN,buff = 0.5).scale(2)
		for i,color in [(0,RED),(-1,RED),(2,RED)]:
			galtran1[i].set_color(color)

		galtran_text = TextMobject("\"Galilean Transformation\"").scale(1.5).to_edge(UP).set_color_by_gradient(PINK,YELLOW,GREEN,RED)

		self.play(*[FadeOut(x) 
					for x in [man1,man2,dot,line1,line2,line3]],
					*[ReplacementTransform(x.copy(),galtran[j])
					for x,j in [(line1[-1],2),(line2[-1],0),(line3[-1],-1)]],
					Write(galtran[1]),Write(galtran[3]),
					run_time = 3)
		self.wait(2)

		box = SurroundingRectangle(galtran,buff = 0.5,color = GREEN)

		self.play(Write(box))
		self.wait(2)

		box_new = SurroundingRectangle(VGroup(galtran,galtran1),buff = 0.5,color = GREEN)

		self.play(Transform(box,box_new),Write(galtran1),run_time = 2)
		self.wait(2)

		self.play(Write(galtran_text),run_time = 2)
		self.wait(2)

		self.play(*[FadeOut(x)
					for x in [box,galtran,galtran1,galtran_text]])
		self.wait(2)

		self.play(*[FadeIn(x)
					for x in [man1,man2,dot,line1,line2,line3]])
		self.wait(2)

		man2_new = self.add_man(file_name = "running.svg",velocity_label = "v \\approx c").to_edge(LEFT + 0.5*UP).shift(5*RIGHT)

		self.play(Transform(man2[2],man2_new[2].shift(0.8*RIGHT)))
		self.wait(2)

		self.play(*[FadeOut(x)
					for x in [man1,man2,dot,line1,line2,line3]])
		self.wait()


		
	def add_man(self,file_name = "standing.svg",vector_side = RIGHT,velocity_label = "v",velocity_color = GREEN,frame_label = "S_{2}",add_vector = True,flip_vertical_image = False,scale = 1):
		man =  SVGMobject("./extmedia/svg_images/" + file_name).rotate(PI,RIGHT).scale(scale)
		if flip_vertical_image:
			man.rotate(PI,axis = UP)
		if add_vector:
			vector = Vector(vector_side).set_color(velocity_color)
			if (vector_side[0] == 1):
				vector.set_left(man.get_right())
			elif (vector_side[0] == -1):
				vector.set_right(man.get_left())
			else:
				raise Exception("Not Implemented")
			vector_label = TexMobject(velocity_label).move_to(vector.get_end() + 0.2*vector_side).set_color(velocity_color)
			

		frame_label = TexMobject(frame_label,color = YELLOW).next_to(man,UP + vector_side,buff = 0.3)

		if add_vector:
			return VGroup(man,vector,vector_label,frame_label)

		else:
			return VGroup(man,frame_label)

	def horizontal_distance_measuring_line(self,start,vector,label = None,label_direction = DOWN):
		line  =  Line(start,start + vector).set_color(GREY)
		tick_start = Line(-0.2*UP,0.2*UP).set_stroke(WHITE,5).move_to(start).set_color(GREY)
		tick_end = Line(-0.2*UP,0.2*UP).set_stroke(WHITE,5).move_to(start + vector).set_color(GREY)
		if label is not(None):
			label = TexMobject(label)
			label.next_to(line,label_direction,buff=0.2).set_color(RED)
		return VGroup(line,tick_start,tick_end,label)

class ReferenceFrames(TwoFriends):
	def construct(self):
		man2 = self.add_man(file_name = "running.svg").to_edge(LEFT + 0.5*UP).shift(1*RIGHT)
		man1 = self.add_man(velocity_label = "0",velocity_color = RED,frame_label = "S_{1}",add_vector = False).next_to(man2,DOWN,buff = 1)
		
		man1_new,man2_new = self.flipped_reference(man1,man2)

		graph0 = self.get_graphs([(lambda m:m/3,GREEN,-5,5)],x_label = "t_{1}",y_label ="x_{1}",scale = 0.5).shift(1.5*RIGHT)

		graph1 = self.get_graphs([((lambda m:3*m),GREEN,-5/3,5/3),(self.light_path1,WHITE,-5,5),(self.light_path2,WHITE,-5,5)],
					scale = 0.5).shift(1.5*RIGHT)
		graph2 = self.get_graphs([((lambda m:-3*m),RED,-5/3,5/3),(self.light_path1,WHITE,-5,5),(self.light_path2,WHITE,-5,5)],
					x_label = "x_{2}",y_label = "ct_{2}",frame_label = "S_{2}",scale=0.5).shift(1.5*RIGHT)

		
		l1 = self.get_light_beam(man1.get_right())
		l2 = self.get_light_beam(man2.get_right())

		self.play(*[FadeIn(x)
					for x in [man1,man2]])
		self.wait(2)

		self.scale_and_wait(man1,wait_time = 2)
		self.wait(2)

		self.play(Write(graph0[0][:3]),Write(graph0[-1]),run_time = 2)
		self.wait(2)

		self.highlight(man2[0])
		self.wait(2)

		self.play(Write(graph0[0][3]),run_time = 2)
		self.wait(2)

		self.play(*[ReplacementTransform(i,j)
					for i,j in [(graph0[0][0],graph1[0][0]),(graph0[0][1],graph1[0][2]),(graph0[0][2],graph1[0][1]),(graph0[-1],graph1[-1])]],
					FadeOut(graph0[0][-1]),
					run_time = 3)
		self.wait(2)

		self.highlight(graph1[0][2])
		self.wait(2)

		self.highlight(man1[0])
		self.wait(2)

		man1_line1 = Line(-5*UP,5*UP,color = RED).move_to(graph1[0][0].get_center()).scale(0.5).rotate(PI,axis = RIGHT)

		self.play(Write(man1_line1),run_time = 2)
		self.wait(2)

		self.highlight(man2[0])
		self.wait(2)

		self.play(Write(graph1[0][-1][0]),run_time = 2)
		self.wait(2)

		label_vect1 = Matrix(["v/c","1"]).set_color(GREEN).scale(0.5)
		self.play(Write(label_vect1.next_to(graph1[0][-1][0],2*RIGHT + 1*UP,buff = 0.2)),run_time = 2)
		self.wait(2)
		self.play(FadeOut(label_vect1))
		self.wait()

		for i in range(3):
			self.play(l1.copy().shift,20*RIGHT,run_time = 2)
			self.wait(1)

		self.play(Write(graph1[0][-1][1]))
		self.play(Write(graph1[0][-1][-1]))
		self.wait(2)

		self.scale_and_wait(man2,wait_time = 2)
		self.wait(2)

		man2_line2 = Line(-5*UP,5*UP,color = GREEN).move_to(graph1[0][0].get_center()).scale(0.5)

		self.play(*[ReplacementTransform(x,y)
					for x,y in [(man1,man1_new),(man2,man2_new),
					(graph1[0][0].copy(),graph2[0][0]),
					(graph1[0][1].copy(),graph2[0][1]),
					(graph1[0][2].copy(),graph2[0][2]),
					(graph1[-1].copy(),graph2[-1]),
					(graph1[0][-1][-1].copy(),graph2[0][-1][-1]),
					(graph1[0][-1][-2].copy(),graph2[0][-1][-2]),
					(graph1[0][-1][0].copy(),man2_line2),
					(man1_line1.copy(),graph2[0][-1][0])]],
					FadeOut(graph1),FadeOut(man1_line1)
					,run_time = 3)
		self.wait(2)


		self.highlight_two_at_a_time(man2_new[0],man2_line2)
		self.wait(2)

		self.highlight_two_at_a_time(man1_new[0],graph2[0][-1][0])
		self.wait(2)

		label_vect2 = Matrix(["-v/c","1"]).set_color(RED).scale(0.5)
		self.play(Write(label_vect2.next_to(graph2[0][-1][0],2*LEFT + 1*UP,buff = 0.2)),run_time = 2)
		self.wait(2)
		self.play(FadeOut(label_vect2))
		self.wait()

		self.highlight_two_at_a_time(graph2[0][-1][-1],graph2[0][-1][-2])
		self.wait(2)

		grp1 = VGroup(graph1.copy(),man1_line1.copy()).scale(0.5)
		grp2 = VGroup(graph2.copy(),man2_line2.copy()).scale(0.5)

		VGroup(grp2,grp1).arrange(DOWN,aligned_edge = RIGHT,buff = 0.5).to_edge(RIGHT,buff = 2)

		self.play(*[ReplacementTransform(x,y)
					for x,y in [(VGroup(graph1,man1_line1),grp1),
								(VGroup(graph2,man2_line2),grp2)]],run_time = 3)
		self.wait(2)

		box1 = SurroundingRectangle(grp1,buff = 0.2)
		box2 = SurroundingRectangle(grp2,buff = 0.2)

		self.play(Write(box1),Write(box2),run_time = 2)
		self.wait(2)

		s1 = VGroup(grp1,box1)
		s2 = VGroup(grp2,box2)

		s1_new = VGroup(grp1,box1).copy().center().to_edge(LEFT,buff = 1.5).scale(1.5)
		s2_new = VGroup(grp2,box2).copy().center().to_edge(RIGHT,buff = 1.5).scale(1.5)

		self.play(*[FadeOut(x) for x in [man1_new,man2_new]],
					*[Transform(x,y) for x,y in [(s1,s1_new),(s2,s2_new)]],
					run_time = 3
					)
		self.wait(2)

		arrow = Arrow(s1.get_right(),s2.get_left()).set_stroke(RED,5).set_color(RED)

		self.highlight(s1)
		self.wait(2)

		self.play(Write(arrow),run_time = 2)
		self.wait(2)

		self.highlight(s2)
		self.wait(2)

		self.play(arrow.rotate,PI,axis = UP,run_time = 2)
		self.wait(2)

		self.play(*[FadeOut(x) for x in [s1,s2,arrow]])
		self.wait(2)
		
	
	def get_graphs(self,funcol,x_min = -5,x_max = 5,y_min = -5,y_max = 5,x_label = "x_{1}",y_label = "ct_{1}",frame_label = "S_{1}",scale = 0.5):
		axes = Axes(x_min = x_min,x_max = x_max, y_min = y_min ,y_max = y_max,color = GREY,axis_config = {"include_tip":True})
		all_graphs = VGroup()
		x_label = TexMobject(x_label).scale(1/scale).shift((x_max + 0.3/scale)*RIGHT)
		y_label = TexMobject(y_label).scale(1/scale).shift((y_max + 0.3/scale)*UP)

		for function,color,x_min,x_max in funcol:
			all_graphs.add(FunctionGraph(function,x_min = x_min,x_max = x_max,color = color))		

		grp = VGroup(axes,x_label,y_label,all_graphs)

		frame_label = TexMobject(frame_label,color = YELLOW).next_to(grp,UR,buff = 0).scale(1/scale).set_stroke(YELLOW,3)

		return VGroup(grp,frame_label).scale(scale).center()

	def light_path1(self,x):
		return x
	def light_path2(self,x):
		return -x

	def get_light_beam(self,start_point):
		light1 = Line(-0.2*RIGHT,0.2*RIGHT).set_stroke(WHITE,6).move_to(start_point)
		light2 = Line(-0.2*RIGHT,0.2*RIGHT).set_stroke(WHITE,5).move_to(start_point - 0.1*UR)
		light3 = Line(-0.2*RIGHT,0.2*RIGHT).set_stroke(WHITE,5).move_to(start_point + 0.1*UL)
		light4 = Line(-0.2*RIGHT,0.2*RIGHT).set_stroke(WHITE,4).move_to(start_point - 0.2*UR)
		light5 = Line(-0.2*RIGHT,0.2*RIGHT).set_stroke(WHITE,4).move_to(start_point + 0.2*UL)
		light = VGroup(light1,light2,light3,light4,light5)
		
		return light

	def flipped_reference(self,man1,man2):
		man1_new = self.add_man(file_name = "running.svg",vector_side = LEFT,velocity_label = "v",velocity_color = RED,frame_label = "S_{1}",flip_vertical_image = True)
		man2_new = self.add_man(file_name = "standing.svg",add_vector = False,velocity_label = "0",vector_side = LEFT)
		man1_new.move_to(man1.get_center())
		man2_new.move_to(man2.get_center())
		return (man1_new,man2_new)

	def highlight_two_at_a_time(self,object1,object2,half_angle = PI/24,scale_factor = 1.3,single_anim_time = 0.5):
		self.play(object1.scale,scale_factor,
					object2.scale,scale_factor,
					run_time = single_anim_time)
		self.play(object1.rotate,half_angle,
					object2.rotate,half_angle,
					run_time = single_anim_time)
		self.play(object1.rotate,-2*half_angle,
					object2.rotate,-2*half_angle,
					run_time = single_anim_time)
		self.play(object1.rotate,half_angle,
					object2.rotate,half_angle,
					run_time = single_anim_time)
		self.play(object1.scale,1/scale_factor,
					object2.scale,1/scale_factor,
					run_time = single_anim_time)


class Postulates(CustomScene):
	def construct(self):
		title = TextMobject("Postulates of \\\\ Special Relativity").scale(1.5).to_edge(UP).set_color(GREEN)

		l = BulletedList("Laws of physics are same in any Inertial Frame.","Speed of Light is constant in any Inertial Frame.").set_color(TEAL_E)

		self.play(Write(title))
		self.wait()

		self.write_by_index(l,time_gap = 1,single_anim_time = 2)
		self.wait(4)

		cons = TextMobject("\"Constant Velocity\"").to_edge(DOWN).shift(1*UP).scale(2).set_color(BLUE)
		self.play(Write(cons),run_time = 2)
		self.wait()
		self.play(FadeOut(cons))
		self.wait(2)

class ShowTransformation1to2(LinearTransformationScene):
	CONFIG = {"lorentz_matrix" : [[3/(2*mt.sqrt(2)),1/(2*mt.sqrt(2))],[1/(2*mt.sqrt(2)),3/(2*mt.sqrt(2))]],
				"show_basis_vectors" : False,
			}
	def construct(self):
		self.setup()

		s1 = TexMobject("S_{1}",color = YELLOW).set_stroke(YELLOW,5).scale(3).to_corner(UR)
		s2 = TexMobject("S_{2}",color = YELLOW).set_stroke(YELLOW,5).scale(3).to_corner(UR)

		for s in [s1,s2]:
			s.add_to_back(BackgroundRectangle(s))


		light1 = FunctionGraph(lambda x : x,x_min = -10,x_max = 10,color = WHITE)
		light2 = FunctionGraph(lambda x : -x,x_min = -10,x_max = 10,color = WHITE)

		line1 = Line(-20*UP,20*UP,color = RED)
		line2 = FunctionGraph(lambda x : 3*x,x_min = -10,x_max = 10,color = GREEN)
		self.add_transformable_mobject(line1,line2,light1,light2)
		self.remove(line1,line2,light1,light2)
		

		x_label,y_label = self.get_reference_labels("x_{1}","c t_{1}")
				

		self.play(ShowCreation(self.plane),run_time = 2)
		self.wait(2)

		self.play(Write(x_label),Write(y_label),run_time = 2)
		self.wait(2)

		self.play(Write(s1))
		self.wait(2)

		self.play(Write(line1),run_time =2)
		self.bring_to_front(x_label,y_label)
		self.wait(2)

		self.play(Write(line2),run_time =2)
		self.wait(2)

		x_label_new,y_label_new = self.get_reference_labels("x_{2}","c t_{2}")
		self.bring_to_front(x_label,y_label)

		self.apply_inverse_transpose(self.lorentz_matrix,
			added_anims = [ReplacementTransform(x_label,x_label_new),Transform(y_label,y_label_new),ReplacementTransform(s1.copy(),s2),FadeOut(s1)])
		self.bring_to_front(x_label_new,y_label_new)
		self.wait(2) 
		

		x_label,y_label = self.get_reference_labels("x_{1}","c t_{1}")

		self.wait(2)

		self.apply_transposed_matrix(self.lorentz_matrix,
			added_anims = [ReplacementTransform(x_label_new,x_label),ReplacementTransform(y_label_new,y_label),ReplacementTransform(s2.copy(),s1),FadeOut(s2)]
			)
		self.bring_to_front(x_label,y_label)

		v1 = self.add_vectors_along(UR,BLUE,GOLD_E,ORANGE)
		v2 = self.add_vectors_along(DR,BLUE,GOLD_E,ORANGE)

		self.play(Write(v1),run_time = 2)
		self.wait(2)

		self.play(Write(v2),run_time = 2)
		self.wait(2)

		x_label_new,y_label_new = self.get_reference_labels("x_{2}","c t_{2}")
		self.apply_inverse_transpose(self.lorentz_matrix,
			added_anims = [ReplacementTransform(x_label,x_label_new),Transform(y_label,y_label_new),ReplacementTransform(s1.copy(),s2),FadeOut(s1)])
		self.bring_to_front(x_label_new,y_label_new)
		self.wait(2)

		self.highlight(VGroup(light1,v1,))
		self.wait(2) 

		self.highlight(VGroup(light2,v2))
		self.wait(2)

		matrix_mob = Matrix([["?","?"],["?","?"]],include_background_rectangle = True).shift(3*LEFT + 1*UP)
		self.play(Write(matrix_mob))
		self.wait(2)
		


	def add_vectors_along(self,direction,*colors):
		unit_vector = (direction[0]*RIGHT + direction[1]*UP + direction[2]*OUT)/self.magnitude(direction)
		vectors = VGroup()
		for i in range(-5,6,1):
			if (i == 0):
				vectors.add(self.get_vector(unit_vector))
				vectors.add(self.get_vector(-1*unit_vector))
			else:
				vectors.add(self.get_vector(np.sign(i)*unit_vector).shift(i*unit_vector))
		self.add_transformable_mobject(vectors.set_color_by_gradient(*colors))
		self.remove(vectors)
		return vectors

	def magnitude(self,vector):
		return (vector[0]**2 + vector[1]**2 + vector[2]**2)**0.5

	def get_reference_labels(self,x_label,y_label,buff = 0.1):
		x_label = TexMobject(x_label).to_edge(RIGHT,buff = buff)
		y_label = TexMobject(y_label).to_edge(UP,buff = buff)
		for lbl in [x_label,y_label]:
			lbl.add_to_back(BackgroundRectangle(lbl))
		return (x_label,y_label)

	def get_special_mobjects(self, mob_list, *mobs_to_add):
		for mobject in mobs_to_add:
			if mobject not in mob_list:
				mob_list.append(mobject)
		return mob_list

	def get_transformable_mobject(self,*mobjects):
		self.get_special_mobjects(self.transformable_mobjects, *mobjects)

	def add_to_moving_vectors(self, *mobjects):
		for mobject in mobjects:
			self.moving_vectors.append(mobject)

	def remove_from_moving_vectors(self, *mobjects):
		for mobject in mobjects:
			self.moving_vectors.remove(mobject)

	def remove_from_moving_mobjects(self, *mobjects):
		for mobject in mobjects:
			self.moving_mobjects.remove(mobject)

	def add_moving_mobjects(self, *mobjects):
		for mobject in mobjects:
			self.add_moving_mobject(mobject)

class FindingTheMatrix(CustomScene):
	def construct(self):
		matrix = Matrix([["a","b"],["c","d"]]).set_color(BLUE)
		vect1 = Matrix(["x_{1}","ct_{1}"]).set_color(RED)
		vect2 = Matrix(["x_{2}","ct_{2}"]).set_color(GREEN)

		eqn = self.get_matrix_equation(matrix,vect1,vect2)

		brace_1 = Brace(eqn[1],UP,buff = 0.1)
		brace_2 = Brace(eqn[-1],UP,buff = 0.1)
		brace_1_tex = brace_1.get_tex("S_{1}")
		brace_2_tex = brace_2.get_tex("S_{2}")

		brace1 = VGroup(brace_1,brace_1_tex).set_color(YELLOW)
		brace2 = VGroup(brace_2,brace_2_tex).set_color(YELLOW)

		self.play(Write(eqn[1]))
		self.wait(2)

		self.play(FadeInFrom(brace1,UP))
		self.wait(2)

		self.play(Write(eqn[-1]))
		self.wait(2)

		self.play(FadeInFrom(brace2,UP))
		self.wait(2)

		self.play(Write(matrix),Write(eqn[-2]))
		self.wait(2)

		self.scale_and_wait(matrix,scale_factor = 1.1,wait_time = 2)
		self.wait(2)

		matrix_asign_eqn = self.get_matrix_assignment(matrix.copy(),"M")

		self.play(*[FadeOut(x) for x in [brace1,brace2,eqn[1],eqn[-1]]],
					*[ReplacementTransform(x,y) for x,y in [(eqn[2],matrix_asign_eqn[1]),(eqn[0],matrix_asign_eqn[-1])]],
					Write(matrix_asign_eqn[0]),
					run_time = 3
					)
		self.wait(2)
		

	def get_matrix_equation(self,matrix,input_vect,output_vect,gap = 0.2):
		input_vect.next_to(matrix,RIGHT,buff = gap)
		eql = TexMobject(" = ").next_to(input_vect,RIGHT,buff = gap)
		output_vect.next_to(eql,RIGHT,buff = gap)
		VGroup(matrix,input_vect,eql,output_vect).center()
		return VGroup(matrix,input_vect,eql,output_vect)

	def get_matrix_equation_with_factor(self,matrix,input_vect,output_vect,factor = "\\lambda_{1}",gap = 0.2):
		input_vect.next_to(matrix,RIGHT,buff = gap)
		eql = TexMobject(" = ").next_to(input_vect,RIGHT,buff = gap)
		factor = TexMobject(factor).next_to(eql,RIGHT,buff = gap).set_color(BLUE)
		output_vect.next_to(factor,RIGHT,buff = gap)
		VGroup(matrix,input_vect,eql,factor,output_vect).center()
		return VGroup(matrix,input_vect,eql,factor,output_vect)

	def get_matrix_assignment(self,matrix,assignment,gap = 0.2):
		assignment = TexMobject(assignment).set_color(matrix.get_color())
		eql = TexMobject(" = ").next_to(assignment,RIGHT,buff = gap)
		matrix.next_to(eql,RIGHT,buff = gap)
		VGroup(assignment,eql,matrix).center()
		return VGroup(assignment,eql,matrix)

	def get_vector_eqn_with_factor(self,vect1,vect2,factor = "\\lambda_{1}",gap = 0.2):
		eql = TexMobject(" = ").next_to(vect1,RIGHT,buff = gap)
		factor = TexMobject(factor).next_to(eql,RIGHT,buff = gap).set_color(BLUE)
		vect2.next_to(factor,RIGHT,buff = gap)
		VGroup(vect1,eql,factor,vect2).center()
		return VGroup(vect1,eql,factor,vect2)

	def get_vector_eqn(self,vect1,vect2,gap = 0.2):
		eql = TexMobject(" = ").next_to(vect1,RIGHT,buff = gap)
		vect2.next_to(eql,RIGHT,buff = gap)
		VGroup(vect1,eql,vect2).center()
		return VGroup(vect1,eql,vect2)

class UsingTheEigenVectors(FindingTheMatrix,ReferenceFrames):
	def construct(self):
		matrix = Matrix([["a","b"],["c","d"]]).set_color(BLUE)
		matrix_new = Matrix([["a","b"],["b","a"]]).set_color(BLUE)
		input_vect = Matrix(["x_{1}","ct_{1}"]).set_color(RED)
		output_vect = Matrix(["x_{2}","ct_{2}"]).set_color(GREEN)
		
		eigen_vect1 = Matrix([1,1]).set_color(RED)
		eigen_vect2 = Matrix([1,-1]).set_color(RED)

		eigen_vect1_new = Matrix(["a + b","c + d"]).set_color(PURPLE)
		eigen_vect2_new = Matrix(["a - b","c - d"]).set_color(PURPLE)

		matrix_asign_eqn = self.get_matrix_assignment(matrix_new.copy(),"M")

		eqn = self.get_matrix_equation(matrix.copy(),input_vect.copy(),output_vect.copy())

		eigen_eqn1 = self.get_matrix_equation_with_factor(matrix.copy(),eigen_vect1.copy(),eigen_vect1.copy().set_color(GREEN))
		eigen_eqn2 = self.get_matrix_equation_with_factor(matrix.copy(),eigen_vect2.copy(),eigen_vect2.copy().set_color(GREEN),factor = "\\lambda_{2}")

		eigen_eqn1_new = self.get_vector_eqn_with_factor(eigen_vect1_new.copy(),eigen_vect1.copy().set_color(GREEN))
		eigen_eqn2_new = self.get_vector_eqn_with_factor(eigen_vect2_new.copy(),eigen_vect2.copy().set_color(GREEN),factor = "\\lambda_{2}")

		#################################################################

		self.play(Write(eqn.to_edge(UP,buff = 0.3)),run_time = 2)
		self.wait(2)

		eigen_eqn1.to_edge(LEFT,buff = 0.3).scale(0.8)
		eigen_eqn2.to_edge(RIGHT,buff = 0.3).scale(0.8)		

		self.play(*[ReplacementTransform(eqn[i].copy(),eigen_eqn1[i])
					for i in range(3)],ReplacementTransform(eqn[-1].copy(),eigen_eqn1[3:]),
					run_time = 2)
		self.wait(2)

		self.play(*[ReplacementTransform(eqn[i].copy(),eigen_eqn2[i])
					for i in range(3)],ReplacementTransform(eqn[-1].copy(),eigen_eqn2[3:]),
					run_time = 2)
		self.wait(2)

		self.highlight_two_at_a_time(eigen_eqn1[-2],eigen_eqn2[-2])
		self.wait(2)

		self.highlight(eqn[0],scale_factor = 1.1)
		self.wait(2)

		eigen_eqn1_new.to_edge(LEFT,buff = 0.8).scale(0.8)
		eigen_eqn2_new.to_edge(RIGHT,buff = 0.8).scale(0.8)

		self.play(*[Transform(x,y) for x,y in [(eigen_eqn1,eigen_eqn1_new),(eigen_eqn2,eigen_eqn2_new)]],run_time = 3)
		self.wait(2)

		final = self.solving_eigen_equations(eigen_eqn1,eigen_eqn2)

		self.play(Transform(eqn[0],matrix_new.move_to(eqn[0].get_center())),
					run_time = 2)
		self.wait(2)

		self.play(*[FadeOut(x) for x in [final,eigen_eqn1,eigen_eqn2]])
		self.wait(2)

		self.play(Write(matrix_asign_eqn[:2]))
		self.play(ReplacementTransform(eqn[0].copy(),matrix_asign_eqn[2]),run_time = 2)
		self.wait(2)

		sym = TextMobject("\"Symmetric Matrix\"").to_edge(DOWN,buff = 1.5).set_color(GREEN).scale(2)

		self.play(Write(sym),run_time = 2)
		self.wait(2) 


	def eigen_value_eqn_scene(self,m):
		eigen_val_eqn1 = TexMobject("det\\left(M - \\lambda I \\right) = 0").set_color(BLUE).to_edge(DOWN,buff = 1)
		eigen_val_matrix = Matrix([["a-\\lambda","b"],["c","d-\\lambda"]],h_buff = 1.8).set_color(BLUE)
		eigen_val_eqn2 = VGroup(eigen_val_matrix,get_det_text(eigen_val_matrix,determinant = 0)).move_to(eigen_val_eqn1.get_center())
		eigen_val_eqn3 = TexMobject("1","\\lambda^2 ","- (d + a)","\\lambda + (ad - bc) = 0").set_color(BLUE).move_to(eigen_val_eqn1.get_center())

		sumof_roots = TexMobject("\\lambda_{1}"," + ","\\lambda_{2}"," = ","-","{\\left(","-(d+a)","\\over","1","\\right)}")
		sumof_roots1 = TexMobject("\\lambda_{1}"," + ","\\lambda_{2}"," = ","(d+a)")

		for i in [0,2,6,8]:
			sumof_roots[i].set_color(BLUE)
		for i in [0,2,4]:
			sumof_roots1[i].set_color(BLUE)

		self.play(Write(eigen_val_eqn1),run_time = 2)
		self.wait(2)

		self.play(Transform(eigen_val_eqn1,eigen_val_eqn2),run_time = 2)
		self.wait(2)

		self.play(Transform(eigen_val_eqn1,eigen_val_eqn3[1:]),run_time = 2)
		self.wait(2)

		sumof_roots.next_to(eigen_val_eqn1,UP,buff = 0.3)
		sumof_roots1.move_to(m.get_bottom() + 0.8*DOWN)

		self.write_by_index(sumof_roots[:4],time_gap = 0.5,single_anim_time = 0.5)

		self.play(Write(sumof_roots[4:6]),
					ReplacementTransform(eigen_val_eqn3[2].copy(),sumof_roots[6]),
					ReplacementTransform(eigen_val_eqn3[0],sumof_roots[-2]),
					Write(sumof_roots[-3]),
					Write(sumof_roots[-1]),
					run_time = 4
					)
		self.wait(2)

		self.play(Transform(sumof_roots,sumof_roots1),
				FadeOut(eigen_val_eqn1),run_time = 2)
		self.wait(2)

		return sumof_roots

	def solving_eigen_equations(self,ee1n,ee2n):
		plus = TexMobject("+").scale(2)
		sub = TexMobject("-").scale(2)

		v1 = Matrix(["2a","2c"]).set_color(PURPLE)
		v2 = Matrix(["\\lambda_{1} + \\lambda_{2}","\\lambda_{1} - \\lambda_{2}"]).set_color(BLUE)
		
		v3 = Matrix(["2b","2d"]).set_color(PURPLE)
		v4 = Matrix(["\\lambda_{1} - \\lambda_{2}","\\lambda_{1} + \\lambda_{2}"]).set_color(BLUE)

		v5 = Matrix(["2d","2b"]).set_color(PURPLE)
		v6 = Matrix(["\\lambda_{1} + \\lambda_{2}","\\lambda_{1} - \\lambda_{2}"]).set_color(BLUE)
		

		add_eigen_eqn = self.get_vector_eqn(v1,v2).next_to(ee1n,DOWN,buff = 0.8).scale(0.8)
		sub_eigen_eqn = self.get_vector_eqn(v3,v4).next_to(ee2n,DOWN,buff = 0.8).scale(0.8)
		sub_eigen_eqn_flipped = self.get_vector_eqn(v5,v6).next_to(ee2n,DOWN,buff = 0.8).scale(0.8)


		self.play(Write(plus))
		self.wait(2)

		self.play(ReplacementTransform(VGroup(ee1n.copy(),ee2n.copy()),add_eigen_eqn),run_time = 2)
		self.wait(2)

		self.play(FadeOut(plus))
		self.wait(2)

		self.play(Write(sub))
		self.wait(2)

		self.play(ReplacementTransform(VGroup(ee1n.copy(),ee2n.copy()),sub_eigen_eqn),run_time = 2)
		self.wait(2)

		self.play(FadeOut(sub))
		self.wait(2)

		self.play(Transform(sub_eigen_eqn,sub_eigen_eqn_flipped),run_time = 2)
		self.wait(2)

		sfinal = self.get_vector_eqn(Matrix(["a","c"]).set_color(PURPLE),Matrix(["d","b"]).set_color(PURPLE)).move_to(2.5*DOWN)
		final = TexMobject("a"," = ","d","\\\\ ","b"," = ","c").move_to(sfinal.get_center())
		for i in [0,2,4,6]:
			final.set_color(PURPLE)

		self.play(ReplacementTransform(VGroup(add_eigen_eqn,sub_eigen_eqn),sfinal),run_time = 2)
		self.wait(2)

		self.play(ReplacementTransform(sfinal,final),run_time = 2)
		self.wait(2)

		return final

class Interesting_Fact_About_Symmetric_Matrices(ShowTransformation1to2):
	CONFIG  = {
				"symm_matrix" : [[3,1],[1,3]]
	}
	def construct(self):
		self.setup()
		self.play(ShowCreation(self.plane))
		self.wait(2)

		i_vector = self.get_vector(1*RIGHT).set_color(GREEN)

		self.add_to_moving_vectors(i_vector)

		self.play(Write(i_vector))
		self.wait(2)

		matrix_mob = Matrix(self.symm_matrix,include_background_rectangle = True).shift(3*LEFT + 1*UP)

		self.play(Write(matrix_mob))
		self.wait(2)

		self.play(FadeOut(matrix_mob))
		self.wait(2)

		self.apply_transposed_matrix(self.symm_matrix)
		self.wait(2)

		self.apply_inverse_transpose(self.symm_matrix)
		self.wait(2)

		j_vector = self.get_vector(1*UP).set_color(RED)
		self.add_to_moving_vectors(j_vector)

		self.play(Write(j_vector))
		self.wait(2)

		self.apply_transposed_matrix(self.symm_matrix)
		self.wait(2)

		light1 = FunctionGraph(lambda x:x,x_min = -10,x_max = 10,color = PINK)
		light2 = FunctionGraph(lambda x:-x,x_min = -10,x_max = 10,color = PINK)

		self.play(Write(light1))
		self.wait(2)

		self.apply_inverse_transpose(self.symm_matrix,run_time = 2)
		self.wait(2)

		self.play(FadeOut(i_vector),FadeOut(j_vector))
		self.wait(2)

		self.remove_from_moving_vectors(i_vector,j_vector)

		v1 = self.add_vectors_along(RIGHT,BLUE,GREEN,PURPLE)
		v2 = self.add_vectors_along(UP,BLUE,GREEN,PURPLE)

		self.play(Write(v1),Write(v2),run_time = 2)
		self.wait(2)

		self.apply_transposed_matrix(self.symm_matrix)
		self.wait(2)

		self.play(Write(light2))
		self.wait(2)

class SymmetricMatrixInOurCase(ShowTransformation1to2,FindingTheMatrix):
	def construct(self):
		self.setup()

		s1 = TexMobject("S_{1}",color = YELLOW).set_stroke(YELLOW,5).scale(3).to_corner(DL)
		s2 = TexMobject("S_{2}",color = YELLOW).set_stroke(YELLOW,5).scale(3).to_corner(DL)

		for s in [s1,s2]:
			s.add_to_back(BackgroundRectangle(s))

		x1_label,ct1_label = self.get_reference_labels("x_{1}","c t_{1}",buff = 0.5)
		
		x1_line = Line(-20*RIGHT,20*RIGHT,color = RED)
		ct1_line = Line(-20*UP,20*UP,color = RED)
		self.add_transformable_mobject(x1_line,ct1_line)

		self.play(ShowCreation(self.plane),ShowCreation(x1_line),ShowCreation(ct1_line),run_time  =2)
		self.wait(2)

		self.play(Write(s1))
		self.wait(2)

		self.add_moving_mobjects(x1_label,ct1_label)
		self.play(Write(x1_label),Write(ct1_label),run_time = 2)
		self.wait(2)

		self.apply_inverse_transpose(self.lorentz_matrix,added_anims = [FadeOut(s1),ReplacementTransform(s1.copy(),s2)],run_time = 2)
		self.wait(2)

		light1 = DashedLine(20*DL,-20*DL,color = PINK)
		self.play(Write(light1),run_time = 2)
		self.wait(2)

		x2_label,ct2_label = self.get_reference_labels("x_{2}","c t_{2}",buff = 0.5)

		x2_line = Line(-20*RIGHT,20*RIGHT,color = GREEN)
		ct2_line = Line(-20*UP,20*UP,color = GREEN)
		self.add_transformable_mobject(x2_line,ct2_line)

		self.play(ShowCreation(x2_line),ShowCreation(ct2_line),run_time  =2)
		self.wait(2)

		self.add_moving_mobjects(x2_label,ct2_label)
		self.play(Write(x2_label),Write(ct2_label),run_time = 2)
		self.wait(2)

		self.apply_transposed_matrix(self.lorentz_matrix,added_anims = [FadeOut(s2),ReplacementTransform(s2.copy(),s1)],run_time = 2)
		self.wait(2)

		light2 = DashedLine(20*DR,-20*DR,color = PINK)
		self.play(Write(light2),run_time = 2)
		self.wait(2)

		vect1 = self.get_vector(1*UP).set_color(PURPLE)
		self.add_to_moving_vectors(vect1)

		sym_matrix = Matrix([["a","b"],["b","a"]]).set_color(BLUE)
		vect_ip = Matrix(["0","1"]).set_color(PURPLE)
		vect_op = Matrix(["-v/c","1"]).set_color(PURPLE)

		eqn1 = self.get_matrix_equation_with_factor(sym_matrix.copy(),vect_ip.copy(),vect_op.copy(),factor = "k")
		eqn1.to_edge(DOWN)

		br_eqn1 = BackgroundRectangle(eqn1)
		self.add(br_eqn1)

		self.play(Write(vect1),Write(eqn1[1]),run_time = 2)
		self.wait(2)

		self.apply_inverse_transpose(self.lorentz_matrix,added_anims = [Write(eqn1[0])],run_time = 2)
		self.wait(2)

		self.write_by_index(eqn1[2:],time_gap = 0.5,single_anim_time = 1)
		self.wait(2)

		eqn2 = self.get_vector_eqn(Matrix(["b","a"]).set_color(PURPLE),Matrix(["-kv/c","k"]).set_color(PURPLE))
		eqn2.move_to(eqn1.get_center())

		br_eqn2 = BackgroundRectangle(eqn2)
		
		self.play(*[ReplacementTransform(x,y) 
					for x,y in [(br_eqn1,br_eqn2),(eqn1,eqn2)]],run_time = 2)
		self.wait(2)

		eqn3 = TexMobject("b "," = ","-{av \\over c}").move_to(eqn2.get_center())
		for i in [0,2]:
			eqn3[i].set_color(BLUE)

		br_eqn3 = BackgroundRectangle(eqn3)

		self.play(*[ReplacementTransform(x,y) 
					for x,y in [(br_eqn2,br_eqn3),(eqn2,eqn3)]],run_time = 2)
		self.wait(2)

		matrix_asign_eqn1 = self.get_matrix_assignment(sym_matrix,"M").shift(3*LEFT + 1*UP)
		br1 = BackgroundRectangle(matrix_asign_eqn1)

		matrix_sf = TexMobject("\\begin{bmatrix} a & {-a{v \\over c}} \\\\ {-a{v \\over c}} & a \\end{bmatrix}").set_color(BLUE)

		matrix_asign_eqn2 = self.get_matrix_assignment(matrix_sf.copy(),"M").shift(3*LEFT + 1*UP)
		br2 = BackgroundRectangle(matrix_asign_eqn2)

		self.add(br1)
		self.play(Write(matrix_asign_eqn1),run_time = 2)

		self.play(ReplacementTransform(br1,br2),ReplacementTransform(matrix_asign_eqn1,matrix_asign_eqn2),run_time = 2)
		self.wait(2)

		self.play(FadeOut(VGroup(br_eqn3,eqn3)))
		self.wait(2)

		
		
class Finding_Gamma_Rigorous(FindingTheMatrix,ReferenceFrames):
	def construct(self):

		matrix_1 = TexMobject("a","\\begin{bmatrix} 1 & {-{v \\over c}} \\\\ {-{v \\over c}} & 1 \\end{bmatrix}").set_color(BLUE)
		matrix_2 = TexMobject("a","\\begin{bmatrix} 1 & {{v \\over c}} \\\\ {{v \\over c}} & 1 \\end{bmatrix}").set_color(BLUE)
		matrix_3 = TexMobject("{a \\over det([M(-v)]_{S_{1}}^{S_{2}})}","\\begin{bmatrix} 1 & {-{v \\over c}} \\\\ {-{v \\over c}} & 1 \\end{bmatrix}").set_color(BLUE)

		eqn_1 = self.get_matrix_assignment(matrix_1.copy(),TexMobject("\\left[","M(v)","\\right]_{S_{1}}^{S_{2}}"))
		eqn_2 = self.get_matrix_assignment(matrix_2.copy(),TexMobject("\\left[","M(-v)","\\right]_{S_{1}}^{S_{2}}"))
		eqn_3 = self.get_matrix_assignment(matrix_2.copy(),TexMobject("\\left[","M(-v)","\\right]_{S_{1}}^{S_{2}}"))
		eqn_4 = self.get_matrix_assignment(matrix_3.copy(),TexMobject("\\left[","M(-v)","\\right]_{S_{2}}^{S_{1}}"))

		box1 = self.box1()
		box2 = self.box2(box1)
		box3 = self.box3()
		box4 = self.box4()

		m1 = eqn_1[0].copy().next_to(box1,DOWN,buff= 0.8)
		m2 = eqn_2[0].copy().next_to(box2,DOWN,buff= 0.8)
		m3 = eqn_3[0].copy().next_to(box3,DOWN,buff= 0.8)
		m4 = eqn_4[0].copy().next_to(box4,DOWN,buff= 0.8)

		self.play(ShowCreation(box1),run_time = 4)
		self.wait(2)

		eqn_1.next_to(box1,RIGHT,buff = 1)

		self.play(Write(eqn_1[0][1]),Write(eqn_1[1:]),run_time = 2)
		self.wait(2)

		self.play(Write(eqn_1[0][0]),Write(eqn_1[0][2:]),run_time = 2)
		self.wait(2)

		self.play(ReplacementTransform(eqn_1[0].copy(),m1),FadeOut(eqn_1),run_time = 2)
		self.wait(2)

		self.play(ReplacementTransform(box1.copy(),box2),ReplacementTransform(m1.copy(),m2),run_time = 3)
		self.wait(2)

		self.play(ReplacementTransform(box2.copy(),box3),ReplacementTransform(m2.copy(),m3),run_time = 3)
		self.wait(2)

		self.highlight_two_at_a_time(box1,box3,scale_factor = 1.1)

		self.play(box3.scale,1.1)
		self.wait(2)
		self.play(ReplacementTransform(box3,box4.scale(1.1)),ReplacementTransform(m3,m4),run_time = 3)
		self.wait(2)
		self.play(box4.scale,1/1.1)
		self.wait(2)

		self.scale_and_wait2(box1,box4)
		self.wait(2)

		feqn = TexMobject("\\left[M(v)\\right]_{S_{1}}^{S_{2}}"," = ","\\left[M(-v)\\right]_{S_{2}}^{S_{1}}")
		feqn.set_color(BLUE)
		feqn[1].set_color(WHITE)

		self.play(*[FadeOut(x) for x in [box1,box2,box4,m2]],ReplacementTransform(m1,feqn[0]),ReplacementTransform(m4,feqn[2]),Write(feqn[1]),run_time = 3)
		self.wait(2)

		feqn1 = TexMobject("\\left[M(v)\\right]_{S_{1}}^{S_{2}}"," = ","\\left(","\\left[M(-v)\\right]_{S_{1}}^{S_{2}}","\\right)^{-1}")
		for i in [0,3]:
			feqn1[i].set_color(BLUE)

		self.play(*[ReplacementTransform(feqn[i],feqn1[j])
					for i,j in [(0,0),(1,1),(2,3)]],Write(feqn1[2]),Write(feqn1[-1]),
					run_time = 2)
		self.wait(2)

		feqn2 = TexMobject("a \\begin{bmatrix} 1 & {-{v \\over c}} \\\\ {-{v \\over c}} & 1 \\end{bmatrix}",
							" = ",
							"{a \\over det([M(-v)]_{S_{1}}^{S_{2}})}\\begin{bmatrix} 1 & {-{v \\over c}} \\\\ {-{v \\over c}} & 1 \\end{bmatrix}")
		for i in [0,2]:
			feqn2[i].set_color(BLUE)

		self.play(ReplacementTransform(feqn1[0],feqn2[0]),run_time = 2)
		self.wait(2)

		self.play(ReplacementTransform(feqn1[2:],feqn2[-1]),ReplacementTransform(feqn1[1],feqn2[1]),run_time = 2)
		self.wait(2)

		feqn3 = TexMobject("{det([M(v)]_{S_{1}}^{S_{2}})"," = ","1")
		feqn3[0].set_color(BLUE),feqn3[-1].set_color(BLUE)
		feqn4 = TexMobject("det \\left( \\begin{bmatrix} a & {-a{v \\over c}} \\\\ {-a{v \\over c}} & a \\end{bmatrix} \\right)"," = ","1")
		feqn4[0].set_color(BLUE),feqn4[-1].set_color(BLUE)
		feqn5 = TexMobject("a"," = ","{1 \\over {\\sqrt{1-{v^2 \\over c^2}}}}"," = ","\\gamma")
		feqn5[0].set_color(RED),feqn5[-1].set_color(RED),feqn5[-3].set_color(RED)
		feqn6 = TexMobject("\\gamma"," = ","{1 \\over {\\sqrt{1-{v^2 \\over c^2}}}}")
		feqn6[0].set_color(RED),feqn6[-1].set_color(RED)

		self.play(ReplacementTransform(feqn2,feqn3),run_time = 2)
		self.wait(2)

		self.play(ReplacementTransform(feqn3,feqn4),run_time = 2)
		self.wait(2)

		self.play(ReplacementTransform(feqn4,feqn5[:3]),run_time = 2)
		self.wait(2)

		self.play(Write(feqn5[-2:]),run_time = 2)
		self.wait(2)

		lorentfactor  = TextMobject("\" Lorentz Factor \"").set_color(GREEN).scale(2)
		self.highlight(feqn5[-1])
		self.play(Write(lorentfactor.to_edge(DOWN,buff = 0.5)))
		self.wait(2)

		self.play(FadeOut(lorentfactor))

		matrix_4 = TexMobject("\\gamma","\\begin{bmatrix} 1 & {-{v \\over c}} \\\\ {-{v \\over c}} & 1 \\end{bmatrix}").set_color(BLUE)
		matrix_4[0].set_color(RED) 

		ffeqn = self.get_matrix_assignment(matrix_4.copy(),TexMobject("M")).scale(2)

		self.play(FadeOut(feqn5))
		self.wait(2)

		self.play(Write(ffeqn),run_time = 2)
		self.wait(2)

		self.play(Write(feqn6.to_edge(DOWN,buff = 0.5)),run_time = 2)
		self.wait(2)

		input_vect = Matrix(["x_{1}","ct_{1}"]).set_color(RED)
		output_vect = Matrix(["x_{2}","ct_{2}"]).set_color(GREEN)

		ffeqn1 = self.get_matrix_equation(matrix_4.copy(),input_vect.copy(),output_vect.copy()).scale(1.5)

		self.play(ReplacementTransform(ffeqn,ffeqn1),run_time = 2)
		self.wait(2)

		frame_box = SurroundingRectangle(ffeqn1,buff = 0.3)
		self.play(Write(frame_box))
		self.wait(2)


	def get_matrix_assignment(self,matrix,assignment,gap = 0.2):
		assignment.set_color(matrix.get_color())
		eql = TexMobject(" = ").next_to(assignment,RIGHT,buff = gap)
		matrix.next_to(eql,RIGHT,buff = gap)
		VGroup(assignment,eql,matrix).center()
		return VGroup(assignment,eql,matrix)

	def box1(self):
		man2 = self.add_man(file_name = "running.svg",scale = 0.5).to_edge(LEFT + 0.5*UP).shift(1*RIGHT + 1*DOWN)
		man1 = self.add_man(velocity_label = "0",velocity_color = RED,frame_label = "S_{1}",add_vector = False,scale = 0.5).next_to(man2,DOWN,buff = 0.7)

		fb = SurroundingRectangle(VGroup(man1,man2),buff = 0.1).set_color(PURPLE)

		return VGroup(man1,man2,fb)

	def box2(self,prev_box):
		man2 = self.add_man(file_name = "running.svg",scale = 0.5,flip_vertical_image = True,vector_side = LEFT)
		man1 = self.add_man(velocity_label = "0",velocity_color = RED,frame_label = "S_{1}",add_vector = False,scale = 0.5).next_to(man2,DOWN,buff = 0.7)

		fb = SurroundingRectangle(VGroup(man1,man2),buff = 0.1).set_color(PURPLE)

		grp = VGroup(man1,man2,fb).center().move_to(prev_box.get_center()[1])
		grp.shift(grp.get_x()*LEFT)
		return VGroup(man1,man2,fb)

	def box3(self):
		man2 = self.add_man(add_vector = False,scale = 0.5).to_edge(RIGHT + 0.5*UP).shift(1*LEFT + 1*DOWN)
		man1 = self.add_man(file_name = "running.svg",velocity_color = RED,frame_label = "S_{1}",scale = 0.5).next_to(man2,DOWN,buff = 0.7)

		fb = SurroundingRectangle(VGroup(man1,man2),buff = 0.1).set_color(PURPLE)

		return VGroup(man1,man2,fb)

	def box4(self):
		man2 = self.add_man(add_vector = False,frame_label = "S_{1}",scale = 0.5).to_edge(RIGHT + 0.5*UP).shift(1*LEFT + 1*DOWN)
		man1 = self.add_man(file_name = "running.svg",velocity_color = RED,scale = 0.5).next_to(man2,DOWN,buff = 0.7)

		fb = SurroundingRectangle(VGroup(man1,man2),buff = 0.1).set_color(PURPLE)

		return VGroup(man1,man2,fb)

	def scale_and_wait2(self,obj1,obj2,scale_factor = 1.3,wait_time = 2,single_anim_time = 0.5):
		self.play(obj1.scale,scale_factor,
					obj2.scale,scale_factor,
					run_time = single_anim_time)
		self.wait(wait_time)
		self.play(obj1.scale,1/scale_factor,
					obj2.scale,1/scale_factor,
					run_time = single_anim_time)

class crossgalilean(Scene):
	def construct(self):
		text = TextMobject("\"Galilean Transformation\"").scale(2).set_color_by_gradient(PINK,YELLOW,GREEN,RED)
		cross  = Cross(text)
		self.play(Write(text),run_time = 2)
		self.wait()
		self.play(Write(cross))
		self.wait(2)

class det1(Scene):
	def construct(self):
		feqn3 = TexMobject("{det([M(v)]_{S_{1}}^{S_{2}})"," = ","1").scale(2)
		feqn3[0].set_color(BLUE),feqn3[-1].set_color(BLUE)
		br = BackgroundRectangle(feqn3)
		self.play(Write(br),Write(feqn3),run_time = 2)
		self.wait(2)

class usuallorentz(Scene):
	def construct(self):
		eqn1 = TexMobject("x_{2} = \\gamma(x_{1} - vt_{1})").scale(1.5).set_color(BLUE)
		eqn2 = TexMobject("ct_{2} = \\gamma(ct_{1} - {v \\over c}x_{1})").scale(1.5).set_color(BLUE)
		grp = VGroup(eqn1,eqn2).arrange(DOWN,aligned_edge = LEFT,buff = 0.3)

		self.play(Write(grp),run_time = 2)
		self.wait(2)

		fb = SurroundingRectangle(grp,buff = 0.3)

		self.play(Write(fb),run_time = 2)
		self.wait(2)
class IntroduceFriends(TwoFriends):
	def construct(self):

		man1 = self.add_man(velocity_label = "0",velocity_color = RED,frame_label = "",add_vector = False,scale = 1.5).to_edge(LEFT,buff = 2)
		man2 = self.add_man(file_name = "running.svg",velocity_label = "0",velocity_color = RED,frame_label = "",add_vector = False,scale = 1.5).to_edge(RIGHT,buff = 2)

		self.play(FadeIn(man1),FadeIn(man2),run_time = 2)
		self.wait(5)

class thumbmain(TwoFriends):
	def construct(self):
		matrix_4 = TexMobject("\\gamma","\\begin{bmatrix} 1 & {-{v \\over c}} \\\\ {-{v \\over c}} & 1 \\end{bmatrix}").set_color_by_gradient("#43cea2","#185a9d").scale(2).shift(1*RIGHT + 2*DOWN)
		man2 = self.add_man(file_name = "running.svg",scale = 1.5,frame_label = "")
		man1 = self.add_man(velocity_label = "0",velocity_color = RED,frame_label = "",add_vector = False,scale = 1.5)
		text = TextMobject("Lorentz \\\\ Transformation").scale(2).set_color_by_gradient("#ffd89b","#19547b")
		br = BackgroundRectangle(text)
		text2 = TextMobject("What is This?").scale(2).set_color_by_gradient("#d76d77","#ffaf7b")
		text2.shift(1*UP + 2*LEFT)
		arrow = Arrow(text2.get_bottom(),matrix_4[0].get_top()).set_color(GREY)
