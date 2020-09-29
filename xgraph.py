from manimlib.imports import*

# python manim.py my_projects\For_Videos\xgraph.py -pl

class methods(CustomScene,ThreeDScene):
	def img(self,file_name):
		img = ImageMobject("./extmedia/raster_images/" + file_name)
		return img

	def addbackdrop(self,file_name = "wood.jpg",opacity = 0.5):
		backdrop = self.img(file_name)
		camera = self.camera
		backdrop.set_width(camera.frame_width)
		backdrop.set_height(camera.frame_height)
		backdrop.set_opacity(opacity)
		self.add(backdrop)

	def add_fixed_in_frame_backdrop(self,file_name = "wood.jpg",opacity = 0.5):
		backdrop = self.img(file_name)
		camera = self.camera
		backdrop.set_width(camera.frame_width)
		backdrop.set_height(camera.frame_height)
		backdrop.set_opacity(opacity)
		self.add_fixed_in_frame_mobjects(backdrop)


	def underlines(self,mob,buff = 0.2):
		line1 = Line(mob.get_left(),mob.get_right())
		line2 = line1.copy()
		line1.move_to(mob.get_bottom())
		line2.next_to(line1,DOWN,buff = 0.1)

		ul = VGroup(line1,line2)

		ul.next_to(mob,DOWN,buff = buff)

		return ul

class WhyNotDefined(methods):
	def construct(self):

		self.addbackdrop()

		eqn1 = TexMobject("x = e^{\\ln(x)}").scale(2)

		self.play(Write(eqn1),run_time = 2)
		self.wait(2)

		eqn2 = TexMobject("x^x"," = ","e^{x","\\ln(x)}").scale(2)

		self.play(eqn1.shift,2*UP)

		self.play(Write(eqn2),run_time = 2)
		self.wait(2)

		self.scale_and_wait(eqn2[-1])
		self.wait(2)

		eqn3 = TexMobject("\\ln(-ve)"," = ","\\ ???").scale(2)

		eqn3.shift(eqn2[1].get_x() - eqn3[1].get_x() )		
		self.play(Write(eqn3),run_time = 3)
		self.wait(2)

	
class negativeln(methods):
	def construct(self):
		self.addbackdrop()

		eqn1 = TexMobject("\\ln(-1) = \\ ?").scale(2).shift(1.5*UP + 3*LEFT)

		eqn2 = TexMobject("e^{?} = -1").scale(2).shift(1.5*UP - 3*LEFT).shift(0.2*UP)

		eqn3 = TexMobject("e^{i\\pi} = -1").scale(2).shift(-1.5*UP - 3*LEFT).shift(0.2*UP)

		eqn4 = TexMobject("\\ln(-1) = i\\pi").scale(2).shift(-1.5*UP + 3*LEFT)

		eqn5 = TexMobject("\\ln(-ve) = Complex").scale(2)

		for eqn in [eqn1,eqn2,eqn3,eqn4]:
			self.play(Write(eqn),run_time = 2)
			self.wait(2)

		self.play(ReplacementTransform(VGroup(eqn1,eqn2,eqn3,eqn4),eqn5))
		self.wait(2)

		box4 = SurroundingRectangle(eqn4)
		self.play(ShowCreation(box4))
		self.wait(2)


class converting_to_negative_domain(methods):
	def construct(self):
		self.addbackdrop()

		title = TextMobject("For x<0").scale(2).to_edge(UP).set_color(TEAL)
		ul = self.underlines(title)
		self.play(FadeInFrom(title,UP))
		self.play(ShowCreation(ul))
		self.wait(2)

		eqn1 = TexMobject("x"," = ","-|x|").scale(1.5)
		eqn2 = TexMobject("\\ln(x)"," = ","\\ln(-|x|)").scale(1.5)
		eqn3 = TexMobject("\\ln(x)"," = ","\\ln(-1) + \\ln(|x|)").scale(1.5)
		eqn4 = TexMobject("\\ln(x)"," = ","i\\pi"," + ","\\ln(|x|)").scale(1.5)
		eqn5 = TexMobject("x\\ln(x)"," = ","i{\\pi}x"," + ","x\\ln(|x|)").scale(1.5)

		self.play(Write(eqn1))
		self.wait(2)

		self.play(*[
					Transform(eqn1[i],eqn2[i])
					for i in range(3)],run_time = 2)
		self.wait(2)

		self.play(*[
					Transform(eqn1[i],eqn3[i])
					for i in range(3)],run_time = 2)
		self.wait(2)		

		self.play(*[
					Transform(eqn1[i],eqn4[i])
					for i in range(2)],
					Transform(eqn1[2],eqn4[2:]),run_time = 2)
		self.wait(2)

		box4 = SurroundingRectangle(eqn4[-1])
		self.play(ShowCreation(box4))
		self.wait(2)

		self.play(FadeOut(box4))
		self.wait(2)

		self.play(Transform(eqn1,eqn5),run_time = 2)
		self.wait(2)

		eqn6 = TexMobject("x^x"," = ","e^{x\\ln(x)}").scale(1.5).shift(1.5*DOWN)

		self.play(eqn1.shift,(0.5*UP))
		self.wait(2)
		self.play(Write(eqn6),run_time = 2)
		self.wait(2)

		eqn7 = TexMobject("x^x"," = ","e^{{({x\\ln(|x|)}} + {i{\\pi}x)}}").scale(1.5).shift(1.5*DOWN)

		self.play(*[
					Transform(eqn6[i],eqn7[i])
					for i in range(3)
			],run_time = 2)
		self.wait(2)

		eqn8 = TexMobject("x^x"," = ","e^{x\\ln(|x|)}","e^{i{\\pi}x}").scale(1.5)

		self.play(FadeOut(eqn1),
					eqn6.shift,1.5*UP,
					run_time = 2)
		self.wait(2)

		self.play(*[
					ReplacementTransform(eqn6[i],eqn8[i])
					for i in [0,1]
			],
					ReplacementTransform(eqn6[2],eqn8[2:]),
					run_time = 2)
		self.wait(2)

		eqn9 = TexMobject("x^x"," = ","{|x|^x}","e^{i{\\pi}x}").scale(1.5)

		self.play(*[
						Transform(eqn8[i],eqn9[i])
						for i in [0,1,2,3]],run_time = 2)
		self.wait(2)

		eqn10 = TexMobject("x^x"," = ","{\\frac{1}{|x|^{|x|}}}","e^{i{\\pi}x}").scale(1.5)

		self.play(*[
						Transform(eqn8[i],eqn10[i])
						for i in [0,1,2,3]],run_time = 2)
		self.wait(2)

		eqn11 = TexMobject("x^x"," = ","{\\frac{1}{|x|^{|x|}}}","{(\\cos({\\pi}x) + i \\sin({\\pi}x))}").scale(1.5)

		self.play(*[
						Transform(eqn8[i],eqn11[i])
						for i in [0,1,2,3]],run_time = 2)
		self.wait(2)

		self.play(eqn8.shift,0.5*UP)
		self.wait(2)

		re = TexMobject("\\Re(x^x)"," = ","\\frac{\\cos({\\pi}x)}{{|x|^{|x|}}}").to_edge(LEFT,buff  = 1.5).scale(1.5).shift(2*DOWN).set_color(PURPLE)
		im = TexMobject("\\Im(x^x)"," = ","\\frac{\\sin({\\pi}x)}{{|x|^{|x|}}}").to_edge(RIGHT,buff = 1.5).scale(1.5).shift(2*DOWN).set_color(PURPLE)

		self.play(ReplacementTransform(eqn8.copy(),re),run_time = 2)
		self.wait(2)

		self.play(ReplacementTransform(eqn8.copy(),im),run_time = 2)
		self.wait(2)



class Plotting(methods):
	def construct(self):

		self.add_fixed_in_frame_backdrop()

		title = TextMobject("Plotting").scale(2).to_edge(UP).set_color(TEAL)
		ul = self.underlines(title)
		self.play(FadeInFrom(title,UP))
		self.play(ShowCreation(ul))
		self.wait(2)

		self.play(FadeOut(title),FadeOut(ul))
		self.wait(2)

		axes = ThreeDAxes(y_min = -3,y_max = 3)

		labels = self.get_fixed_in_frame_labels(axes,y_label = "x^x")

		self.play(ShowCreation(axes))
		self.wait(2)

		self.play(Write(labels[0]))
		self.wait()
		self.play(Write(labels[1]))
		self.wait(2)

		initial_plot = ParametricFunction(self.curve,t_min = 0,t_max = 2.13).set_color(MAROON)
		negative_integers_points = self.negative_integers_points()

		self.play(Write(initial_plot),run_time = 2)
		self.wait()
		self.play(Write(negative_integers_points))
		self.wait(2)

		labels_new = self.get_fixed_in_frame_labels(axes)

		new_plot = ParametricFunction(self.curve,t_min = 0,t_max = -5.5).set_color(MAROON)

		self.move_camera(theta = -30*DEGREES,phi = 75*DEGREES,run_time = 2)
		self.wait(2)



		self.play(ReplacementTransform(labels[1],labels_new[1]),
					Transform(axes.y_axis,ThreeDAxes().get_y_axis()),
					Write(labels_new[2]),
					ReplacementTransform(labels[0],labels_new[0]),run_time = 2)
		self.wait(2)

		self.begin_ambient_camera_rotation(rate = -0.1)

		xyplane = self.get_xy_plane()
		yzplane = self.get_yz_plane()

		self.play(Write(xyplane))
		self.wait(2)
		self.play(FadeOut(xyplane))
		self.wait(2)

		self.play(Write(yzplane))
		self.wait(2)
		self.play(FadeOut(yzplane))
		self.wait(2)

		self.play(Write(new_plot),run_time = 2)
		self.wait(6)

		self.play(Write(xyplane))
		self.scale_and_wait(VGroup(initial_plot,new_plot),wait_time = 0.5)
		self.wait(2)
		self.scale_and_wait(negative_integers_points,wait_time = 0.5)
		self.wait(2)


		self.play(FadeOut(xyplane))

		self.wait(5)

		


	def curve(self,t):
		if t == 0:
			return np.array([0,1,0])
		if t > 0:
			return np.array([t,t**t,0])
		if t < 0:
			return np.array([
							t,
							(np.cos(np.pi*t)/((-t)**(-t))),
							(np.sin(np.pi*t)/((-t)**(-t)))
							])

	def get_xy_plane(self,opacity = 0.3):
		xyplane  = Polygon(5*DL,5*UL,5*UR,5*DR)
		xyplane.set_opacity(opacity)

		return xyplane

	def get_yz_plane(self,opacity = 0.3):
		yzplane  = Polygon(3*OUT + 5*DOWN,3*OUT+ 5*UP,3*IN + 5*UP,3*IN + 5*DOWN)
		yzplane.set_opacity(opacity).set_color(GREEN)

		return yzplane

	def get_fixed_in_frame_labels(self,axes,x_label = "x",y_label = "\\Re(x^x)",z_label = "\\Im(x^x)"):
		x_axis = axes.get_x_axis()
		y_axis = axes.get_y_axis()
		z_axis = axes.get_z_axis()

		x_lbl = TexMobject(x_label).next_to(x_axis.get_end(),RIGHT)
		y_lbl = TexMobject(y_label).next_to(y_axis.get_end(),RIGHT)
		z_lbl = TexMobject(z_label).next_to(z_axis.get_end(),RIGHT)

		def x_updater(m):
			new_x_lbl = TexMobject(x_label)
			new_x_lbl.next_to(x_axis.get_end(),RIGHT)
			phi = self.camera.get_phi()
			theta = self.camera.get_theta()
			new_x_lbl.rotate(np.pi/2 + theta,OUT)
			vect1 = np.array([
								np.sin(phi)*np.cos(theta),
								np.sin(phi)*np.sin(theta),
								np.cos(phi)])
			vect2 = OUT
			axis = np.cross(vect1,vect2)
			new_x_lbl.rotate(-phi,axis)

			m.become(new_x_lbl)

		def y_updater(m):
			new_y_lbl = TexMobject(y_label)
			new_y_lbl.next_to(y_axis.get_end(),UP)
			phi = self.camera.get_phi()
			theta = self.camera.get_theta()
			new_y_lbl.rotate(np.pi/2 + theta,OUT)
			vect1 = np.array([
								np.sin(phi)*np.cos(theta),
								np.sin(phi)*np.sin(theta),
								np.cos(phi)])
			vect2 = OUT
			axis = np.cross(vect1,vect2)
			new_y_lbl.rotate(-phi,axis)


			m.become(new_y_lbl)

		def z_updater(m):
			new_z_lbl = TexMobject(z_label)
			new_z_lbl.next_to(z_axis.get_end(),ORIGIN)
			phi = self.camera.get_phi()
			theta = self.camera.get_theta()
			new_z_lbl.rotate(np.pi/2 + theta,OUT)
			vect1 = np.array([
								np.sin(phi)*np.cos(theta),
								np.sin(phi)*np.sin(theta),
								np.cos(phi)])
			vect2 = OUT
			axis = np.cross(vect1,vect2)
			new_z_lbl.rotate(-phi,axis)

			m.become(new_z_lbl)		

		x_lbl.add_updater(x_updater)
		y_lbl.add_updater(y_updater)
		z_lbl.add_updater(z_updater)

		labels = VGroup(x_lbl,y_lbl,z_lbl)

		return labels

	def negative_integers_points(self):
		sphere = Sphere(radius = 0.05).set_color(MAROON)

		grp = VGroup()

		for i in [-1,-2,-3,-4,-5]:
			new = sphere.copy()

			new.shift(self.curve(i))

			grp.add(new)

		return grp

class eitheta(methods):
	def construct(self):
		self.addbackdrop()

		title = TextMobject("For x<0").scale(2).to_corner(UL).set_color(TEAL)
		ul = self.underlines(title)

		self.add(title,ul)

		e1  = TexMobject("e^{ i\\pi} = -1").scale(1.5)
		e2 = TexMobject("e^{2i\\pi} = 1").scale(1.5)
		e3 = TexMobject("e^{3i\\pi} = -1").scale(1.5)
		e4 = TexMobject("e^{4i\\pi} = 1").scale(1.5)
		e5 = TexMobject(".").scale(1.5)
		e6 = TexMobject(".").scale(1.5)
		e7 = TexMobject(".").scale(1.5)

		eqn = TexMobject("x^x"," = ","{\\frac{1}{|x|^{|x|}}}","e^{i{\\pi}x}").set_color(MAROON).to_edge(LEFT,buff = 3).scale(2.5)

		a = VGroup(e1,e2,e3,e4,e5,e6,e7).arrange(DOWN,aligned_edge = ORIGIN,buff = 0.75).set_color(PURPLE).to_edge(RIGHT,buff = 1)

		self.play(Write(a),Write(eqn),run_time = 2)

		self.wait(4)

class thumbnail(Plotting):
	def construct(self):
		axes = ThreeDAxes()
		self.add(axes)
		self.set_camera_orientation(phi = 75*DEGREES,theta = 105*DEGREES)
		self.curvewithglow()
		text =  TexMobject("x^x").scale(6.5).to_corner(UR).set_color(BLUE)
		t2 = TexMobject("x^x").scale(6.55).to_corner(UR).set_color(TEAL).set_opacity(0.5)
		self.add_fixed_in_frame_mobjects(text,t2)
	def curvewithglow(self):
		c1 = ParametricFunction(self.curve,t_min = -5,t_max = 2.13).set_stroke(YELLOW,4.5)
		c2 = ParametricFunction(self.curve,t_min = -5,t_max = 2.13).set_stroke(ORANGE,6)

		self.add(c1,c2)
