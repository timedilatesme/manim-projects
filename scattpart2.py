from manimlib.imports import*
from from_3b1b.active.diffyq.part3.temperature_graphs import TemperatureGraphScene

# DRIVER CODE
# python manim.py my_projects\For_Videos\scattpart2.py -pl

class CustomScene(Scene):
    
    def __init__(self, **kwargs):
        Scene.__init__(self, **kwargs)

    def scale_and_wait(self,object,scale_factor = 1.3,wait_time = 2,single_anim_time = 0.5):
        self.play(object.scale,scale_factor,run_time = single_anim_time)
        self.wait(wait_time)
        self.play(object.scale,1/scale_factor,run_time = single_anim_time)

    def highlight(self,object,half_angle = PI/24,scale_factor = 1.3,single_anim_time = 0.5):
        self.play(object.scale,scale_factor,run_time = single_anim_time)
        self.play(object.rotate,half_angle,run_time = single_anim_time)
        self.play(object.rotate,-2*half_angle,run_time = single_anim_time)
        self.play(object.rotate,half_angle,run_time = single_anim_time)
        self.play(object.scale,1/scale_factor,run_time = single_anim_time)

    def write_by_index(self,object,time_gap = 0.5,single_anim_time = 0.5):
        for i in object:
            self.play(Write(i),run_time = single_anim_time)
            self.wait(time_gap)


class IntroScene(Scene):
	def construct(self):
		pass

class equations(CustomScene):
	def construct(self):

		scatt_amp1 = TexMobject("{A_{s}}","=","e^{i\\delta}","\\sin(\\delta)")
		for i,color in [(0,MAROON),(2,PURPLE),(3,PURPLE)]:
			scatt_amp1[i].set_color(color)

		scatt_amp2 = TexMobject("A_{s}","=","{\\sin(\\delta)"," \\over ","e^{-i\\delta}}")
		for i,color in [(0,MAROON),(2,PURPLE),(4,PURPLE)]:
			scatt_amp2[i].set_color(color)

		scatt_amp3 = TexMobject("A_{s}","=","{\\sin(\\delta)"," \\over ","{\\cos(\\delta)"," - ","i\\sin(\\delta)}}")
		for i,color in [(0,MAROON),(2,PURPLE),(4,PURPLE),(6,PURPLE)]:
			scatt_amp3[i].set_color(color)

		scatt_amp4 = TexMobject("A_{s}",           	 	#00    
								"=",			   	 	#01
								"{1",              	 	#02
								" \\over ",        	 	#03
								"{{\\cos(\\delta)", 	#04
								"\\over ",		   	 	#05
								"\\sin(\\delta)}", 	 	#06 
								" - ",             	 	#07
								"i{\\sin(\\delta)",	 	#08 
								" \\over ",        	 	#09
								"\\sin(\\delta)}}}") 	#10
		for i,color in [(0,MAROON),(2,PURPLE),(4,PURPLE),(6,PURPLE),(8,PURPLE),(10,PURPLE)]:
			scatt_amp4[i].set_color(color)

		scatt_amp5 = TexMobject("A_{s}","=","{1"," \\over ","{\\cot(\\delta)"," - ","i}}")
		for i,color in [(0,MAROON),(2,PURPLE),(4,PURPLE),(6,PURPLE)]:
			scatt_amp5[i].set_color(color)

		scatt_amp6 = TexMobject("A_{s}","=","{1"," \\over ","{{{\\alpha - k}\\over{\\beta}}","-","i}}")
		for i,color in [(0,MAROON),(2,PURPLE),(4,PURPLE),(6,PURPLE)]:
			scatt_amp6[i].set_color(color)

		scatt_amp7 = TexMobject("A_{s}","=","{\\beta ","\\over"," {\\alpha"," - ","\\beta"," i"," - ","k}}")
		for i,color in [(0,MAROON),(2,YELLOW),(4,YELLOW),(6,YELLOW),(7,RED),(9,PURPLE)]:
			scatt_amp7[i].set_color(color)

		eqn0 = TexMobject("\\tan(\\delta)"," = ","{{\\beta}\\over{\\alpha - k}}")
		for i,color in [(0,PURPLE),(2,PURPLE)]:
			eqn0[i].set_color(color)

		eqn1 = TexMobject("\\cot(\\delta)"," = ","{{\\alpha - k}\\over{\\beta}}")
		for i,color in [(0,PURPLE),(2,PURPLE)]:
			eqn1[i].set_color(color)


		eqn2 = TexMobject("{\\cot(\\delta)"," = ","i}")
		for i,color in [(0,PURPLE),(2,PURPLE)]:
			eqn2[i].set_color(color)

		eqn3 = TexMobject("\\Rightarrow","A_{s}","\\to"," \\infty")
		for i,color in [(1,MAROON),(3,MAROON)]:
			eqn3[i].set_color(color)

		eqn4 = TexMobject("{\\tan(\\delta)"," = - ","i}")
		for i,color in [(0,PURPLE),(2,PURPLE)]:
			eqn4[i].set_color(color)

		for eqn in [scatt_amp1,scatt_amp2,scatt_amp3,scatt_amp4,scatt_amp5,scatt_amp6,scatt_amp7,eqn0,eqn1,eqn2,eqn3,eqn4]:
			eqn.scale(2)


		#ANIMATIONS

		self.write_by_index(scatt_amp1,time_gap = 1,single_anim_time = 1)

		self.scale_and_wait(scatt_amp1[0],wait_time = 2)
		self.wait(2)

		self.play(*[ReplacementTransform(scatt_amp1[i],scatt_amp2[j])
					for i,j in [(0,0),(1,1),(2,4),(3,2)]],run_time = 3)
		self.play(Write(scatt_amp2[3]))
		self.wait(2)

		self.scale_and_wait(scatt_amp2[4],wait_time = 2)
		self.wait(2)

		self.play(*[ReplacementTransform(scatt_amp2[i],scatt_amp3[j])
					for i,j in [(0,0),(1,1),(2,2),(3,3)]],ReplacementTransform(scatt_amp2[4],scatt_amp3[4:]),run_time = 3)
		self.wait(2)

		self.play(*[ReplacementTransform(scatt_amp3[i],scatt_amp4[j])
					for i,j in [(0,0),(2,2),(1,1),(3,3),(4,4),(5,7),(6,8)]],
					*[ReplacementTransform(scatt_amp3[2].copy(),scatt_amp4[j])
					for j in [6,10]],run_time = 3)
		self.play(*[Write(scatt_amp4[i])
					for i in [5,9]])
		self.wait(2)

		self.play(*[ReplacementTransform(scatt_amp4[i],scatt_amp5[j])
					for i,j in [(0,0),(1,1),(2,2),(3,3),(7,5)]],
					ReplacementTransform(scatt_amp4[4:7],scatt_amp5[4]),
					ReplacementTransform(scatt_amp4[8:],scatt_amp5[-1]),run_time = 3)
		self.wait(2)

		fb_scatt_amp5 = SurroundingRectangle(scatt_amp5,buff = 0.4,color = RED)

		imp0 = VGroup(scatt_amp5,fb_scatt_amp5)

		self.play(ShowCreation(fb_scatt_amp5))
		self.wait()
		self.play(imp0.scale,0.5,
				imp0.to_corner,UL,
				run_time = 2)
		self.wait(2)

		eqn3.next_to(eqn2,DOWN,buff = 0.2)
		VGroup(eqn2,eqn3).center()

		self.play(*[ReplacementTransform(scatt_amp5[i].copy(),eqn2[j])
					for i,j in [(4,0),(5,1),(6,2)]],run_time = 2)
		self.wait()

		self.write_by_index(eqn3,time_gap = 1,single_anim_time = 1)
		self.wait(2)



		eqn4.move_to(eqn2.get_center())

		self.play(*[Transform(eqn2[i],eqn4[j])
					for i,j in [(0,0),(1,1),(2,2)]],run_time = 2)
		self.wait()

		fb_eqn2and3 = SurroundingRectangle(VGroup(eqn2,eqn3),buff = 0.5,color = RED)

		imp1 = VGroup(fb_eqn2and3,eqn2,eqn3)

		self.play(ShowCreation(fb_eqn2and3))
		self.wait()
		self.play(imp1.scale,0.5,
				imp1.to_edge,UP,
				run_time = 2)
		self.wait(2)

		self.scale_and_wait(imp1,wait_time = 3)
		self.wait(2)

		textforresonance = TextMobject("If you want to find \\\\ the Resonance for \\\\ a given potential.").set_color_by_gradient(RED,GREEN,BLUE)
		delta = TexMobject("\\delta(k)")

		self.write_by_index(eqn0,time_gap = 1,single_anim_time = 1)
		self.wait(2)

		self.play(*[ReplacementTransform(eqn0[i],eqn1[j])
					for i,j in [(0,0),(1,1),(2,2)]],run_time = 2)
		self.wait(2)

		self.play(Transform(scatt_amp5[4],scatt_amp6[4].scale(0.5).move_to(scatt_amp5[4].get_center())),run_time = 2)
		self.wait(2)

		self.play(Transform(scatt_amp5,scatt_amp7.move_to(scatt_amp5.get_center()).scale(0.5)),run_time = 2)
		self.wait(2)

		self.play(FadeOut(eqn1))
		self.wait(2)

		self.play(Write(textforresonance.to_edge(LEFT)),run_time = 3)
		self.wait(2)

		rightarr = TexMobject("\\Rightarrow",color = YELLOW).next_to(textforresonance,RIGHT,buff = 0.3)

		self.play(Write(rightarr))
		self.wait(2)

		eqn0 = TexMobject("\\tan(\\delta)"," = ","{{\\beta}","\\over","{\\alpha"," - ","k}}"," = ","-","i").next_to(rightarr,RIGHT,buff = 0.3)
		for i,color in [(0,PURPLE),(2,PURPLE),(4,PURPLE),(6,PURPLE),(-1,PURPLE)]:
			eqn0[i].set_color(color)

		self.play(Write(eqn0[:7]))
		self.wait(2)

		self.play(Write(eqn0[7:]))
		self.wait(2)

		rightarr2 = TexMobject("\\Rightarrow",color = YELLOW).next_to(eqn0,DOWN,buff = 0.3).rotate(-PI/2)

		self.play(Write(rightarr2))
		self.wait(2)

		eqn5 = TexMobject(" k "," = "," \\alpha"," - "," \\beta"," i").next_to(rightarr2,DOWN,buff= 0.3)
		for i,color in [(0,PURPLE),(2,YELLOW),(4,YELLOW),(5,RED)]:
			eqn5[i].set_color(color)

		self.play(*[ReplacementTransform(eqn0[i].copy(),eqn5[j])
					for i,j in [(2,4),(4,2),(6,0),(7,1),(8,3),(-1,-1)]],run_time = 2)

		self.wait(2)

		frame = SurroundingRectangle(eqn5,buff = 0.25,color = TEAL_E)

		self.play(ShowCreation(frame))
		self.wait(2)





class ComplexGraphScene(TemperatureGraphScene):
    CONFIG = {
        "axes_config": {
            "x_min": 0,
            "x_max": 4,
            "y_min": -2,
            "y_max": 2,
            "z_min": 0,
            "z_max": 3,
            "x_axis_config": {
                "tick_frequency": 1,
                "include_tip": False,},
			"y_axis_config": {
            	"tick_frequency": 1,
            }

            },

        "y_label"  : "Im(k)",
        "x_label"  : "Re(k)",
        "z_label"  : "|A_{s}|^2",


    }

    def add_axes_labels(self, axes,labels_to_add = [1,1,1]):
        x_label = TexMobject(self.x_label)
        x_label.next_to(axes.x_axis.get_end(), RIGHT)
        axes.x_axis.label = x_label.set_color(BLUE)

        y_label = TexMobject(self.y_label)
        y_label.rotate(90 * DEGREES, OUT)
        y_label.next_to(axes.y_axis.get_end(), UP)
        axes.y_axis.label = y_label.set_color(BLUE)

        z_label = TexMobject(self.z_label)
        z_label.rotate(90 * DEGREES, RIGHT)
        z_label.next_to(axes.z_axis.get_zenith(), RIGHT)
        axes.z_axis.label = z_label.set_color(BLUE)
        
        if (labels_to_add == [1,1,1]):
        	for axis in axes:
        		axis.add(axis.label)
        if (labels_to_add == [0,1,1]):
        	for axis in [axes.y_axis,axes.z_axis]:
        		axis.add(axis.label)
        if (labels_to_add == [1,0,1]):
        	for axis in [axes.x_axis,axes.z_axis]:
        		axis.add(axis.label)
        if (labels_to_add == [1,1,0]):
        	for axis in [axes.x_axis,axes.y_axis]:
        		axis.add(axis.label)
        if (labels_to_add == [1,0,0]):
        	for axis in [axes.x_axis]:
        		axis.add(axis.label)
        if (labels_to_add == [0,1,0]):
        	for axis in [axes.y_axis]:
        		axis.add(axis.label)
        if (labels_to_add == [0,0,1]):
        	for axis in [axes.z_axis]:
        		axis.add(axis.label)
        else:
        	pass


        return axes

class complexplanegraph(ComplexGraphScene):
	def construct(self):


		distribution_surface = ParametricSurface(self.distributionsurface,u_min = 0,u_max = 4,v_min = -2,v_max = 2)

		v_value = ValueTracker(0)
		
		moving_curve = ParametricFunction(lambda t : self.distributionsurface(t,v_value.get_value()),t_min = 0,t_max = 4,).set_color(RED)

		def updater(m):
			m.become(ParametricFunction(lambda t : self.distributionsurface(t,v_value.get_value()),t_min = 0,t_max = 4).set_color(RED))
		
		moving_curve.add_updater(updater)

		
		self.set_camera_orientation(
			phi=90 * DEGREES,
			theta=-90 * DEGREES,
        )
				
		

		#ANIMATIONS
		axes = self.get_three_d_axes(labels_to_add = [1,1,1])

		self.play(Write(axes))
		self.wait(2)

		self.play(ShowCreation(moving_curve),run_time = 2)
		self.wait(2)

		name =  TextMobject("\"Breit-Wigner \\\\ Distribution\"")
		self.camera.add_fixed_in_frame_mobjects(name)
		name.to_corner(UR).set_color(YELLOW)
		

		self.play(Write(name))
		self.wait(2)

		self.play(FadeOut(name))
		self.wait(2)
	
		self.move_camera(phi = 80*DEGREES,theta = -60*DEGREES,run_time = 3)
		
		self.begin_ambient_camera_rotation(rate = 0.05)

		number = self.add_valuetracker_for_position_of_peak(v_value)

		self.play(v_value.set_value,(-2)
			,run_time = 3,rate_func = there_and_back)
		self.play(v_value.set_value,2,
			run_time = 3,rate_func = there_and_back)
		self.wait(2)

		self.play(ShowCreation(distribution_surface))
		self.wait(2)

		self.move_camera(phi = 80*DEGREES,theta = -60*DEGREES,run_time = 2)

		self.play(v_value.set_value,-0.3,
			run_time = 4, rate_func = linear)
		self.wait(2)

		

		respo = TexMobject("\\alpha"," - ","\\beta"," i"," =")
		self.camera.add_fixed_in_frame_mobjects(respo)
		for i,color in [(0,YELLOW),(2,YELLOW),(3,RED)]:
			respo[i].set_color(color)

		respo.next_to(number,LEFT,buff = 0.2)

		self.play(Write(respo))
		self.wait(2)

	def add_valuetracker_for_position_of_peak(self,v_value):
		text = TextMobject("Peak Position :").set_color(TEAL_E)
		self.camera.add_fixed_in_frame_mobjects(text)
		text.to_corner(DR).shift(1.5*UP)
		
		number_value =  (v_value.get_value())
		if (number_value < 0):
			number = TexMobject("k"," = ","2.0",str(number_value)[0],"0."+str(number_value)[3],"i")
		else:
			number = TexMobject("k"," = ","2.0","+",str(number_value)[:3],"i")
		self.camera.add_fixed_in_frame_mobjects(number)
		for i,color in [(0,PURPLE),(2,YELLOW),(4,YELLOW),(5,RED)]:
			number[i].set_color(color)
		number.next_to(text,DOWN,buff = 0.5)

		full_tex = VGroup(text,number)

		self.play(Write(full_tex))
		self.wait()

		def update_full_tex(m):
			text = TextMobject("Peak Position :").set_color(TEAL_E)
			self.camera.add_fixed_in_frame_mobjects(text)
			text.to_corner(DR).shift(1.5*UP)
			
			number_value = (v_value.get_value())

			if (number_value < 0):
				number = TexMobject("k"," = ","2.0",str(number_value)[0],"0."+str(number_value)[3],"i")
			else:
				number = TexMobject("k"," = ","2.0","+",str(number_value)[:3],"i")
			self.camera.add_fixed_in_frame_mobjects(number)
			for i,color in [(0,PURPLE),(2,YELLOW),(4,YELLOW),(5,RED)]:
				number[i].set_color(color)
			number.next_to(text,DOWN,buff = 0.5)

			full_tex = VGroup(text,number)

			m.become(full_tex)

		full_tex.add_updater(update_full_tex)

		return number


	def distributionsurface(self,u,v,alpha = 2,beta = 0.3):
		return np.array([(u),
						(v),
						(beta**2/(0.01 + (alpha-u)**2 + (beta + v)**2))])
	
	def distributioncurve(self,t,alpha = 2,beta = 0.3):
		return self.distributionsurface(t,0)

class Thumbtext(Scene):
	def construct(self):
		text = TextMobject("How to \\\\ Find \\\\ Resonances?").set_color_by_gradient(RED,BLUE,GREEN)

		self.add(text.scale(3))

class Writepole(CustomScene):
	def construct(self):
		pole = TextMobject("P","O","L","E").set_color_by_gradient(PURPLE,GREEN,RED).scale(3)
		self.write_by_index(pole,time_gap = 1,single_anim_time = 1)
		self.wait(2)
