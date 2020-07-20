from manimlib.imports import*

# DRIVER CODE
# python manim.py my_projects\For_Videos\scattpart.py -pl 

class IntroScene(Scene):
	def construct(self):
		contents = BulletedList("","","")

		

#DONE
class reltnbw_kandE(Scene):
	#CONFIG = {"camera_config" : {"background_color" : GREEN_SCREEN}}
	#Extract it as a transparent Scene
	def construct(self):
		eq = TexMobject("E"," = ","{{{\\hbar}^2{k^2}}\\over{2m}}").set_color(PURPLE).scale(2)
		eq[0].set_color(TEAL_E),eq[1].set_color(WHITE)
		self.play(Write(eq),run_time = 3)
		self.wait(2)
#DONE
class IntroducingProton(Scene):
	def construct(self):

		def Highlight(object,half_angle = PI/24,scale_factor = 1.3,single_anim_time = 0.5):
			self.play(object.scale,scale_factor,run_time = single_anim_time)
			self.play(object.rotate,half_angle,run_time = single_anim_time)
			self.play(object.rotate,-2*half_angle,run_time = single_anim_time)
			self.play(object.rotate,half_angle,run_time = single_anim_time)
			self.play(object.scale,1/scale_factor,run_time = single_anim_time)

		protonA = Dot(color = RED).scale(3).shift(-3*RIGHT)
		protonB = Dot(color = BLUE).scale(3).shift(3*RIGHT)

		ArrowA = Vector(-2*LEFT).set_color(RED).shift(-3*RIGHT)
		ArrowB = Vector(2*LEFT).set_color(BLUE).shift(3*RIGHT)
		ArrowC = Vector(2.2*LEFT).set_color(BLUE).shift(3*RIGHT)

		grpA = VGroup(protonA,ArrowA)
		grpB = VGroup(protonB,ArrowB)

		speed = TextMobject("0.99999999 \\\\ Speed of Light").shift(2*UP).scale(2).set_color(GREEN)
		speed1 = TextMobject("0.99999999999999995 \\\\ Speed of Light").shift(2*UP).scale(2).set_color(GREEN)

		self.play(FadeInFrom(grpA,LEFT),FadeInFrom(grpB,RIGHT),run_time = 2)
		self.wait(2)

		self.play(Write(speed),run_time = 2)
		self.wait(2)

		Highlight(grpA)
		self.wait(2)

		self.play(FadeOut(speed),FadeOut(ArrowA))
		self.wait(2)

		self.play(Transform(ArrowB,ArrowC))
		self.wait(2)

		self.play(Write(speed1))
		self.wait(2)

		self.play(*[FadeOut(x)
					for x in [protonA,grpB,speed1]])


class DecaytoPhotons(Scene):
	def construct(self):
		
		hboson_symbol = TexMobject("H^0")
		photon_symbol = TexMobject("\\gamma")
		hb = Dot(color = GREEN).scale(7).shift(-3*RIGHT)
		hboson = VGroup(hb,hboson_symbol.copy().shift(-3*RIGHT) )
		photon1 = VGroup(Dot(color = BLUE).scale(3).shift(3*RIGHT + 1*UP),photon_symbol.copy().shift(3*RIGHT + 1*UP))
		photon2 = VGroup(Dot(color = BLUE).scale(3).shift(3*RIGHT+ 1*DOWN),photon_symbol.copy().shift(3*RIGHT - 1*UP))

		self.play(Write(hboson))
		self.wait(2)
		self.play(Write(TextMobject("Higgs \\\\ Boson",color = GREEN).next_to(hboson,DOWN,buff  =0.5)))

		self.play(ReplacementTransform(hboson.copy(),VGroup(photon1,photon2)),run_time = 3)
		self.wait(2)
		self.play(Write(TextMobject("Photons",color = BLUE).shift(5*RIGHT)))
		self.wait(2)

class Mass_Explaination(Scene):
	def construct(self):
		title = TextMobject("Units?").set_color(ORANGE).to_edge(UP).scale(2)

		energy0 = TexMobject("E"," = ","m","c^2").set_color_by_gradient(GREEN,WHITE,GREEN,RED,RED)
		energy1 = TexMobject("E_{\\alpha}"," = ","m","c^2").set_color_by_gradient(GREEN,WHITE,GREEN,RED,RED)
		energy2 = TexMobject("m"," = ","{E_{\\alpha}","\\over c^2}").shift(1.5*DOWN).set_color_by_gradient(GREEN,WHITE,GREEN,WHITE,WHITE,RED,RED)

		units =  TexMobject("{eV"," \\over ","c^2}").set_color_by_gradient(GREEN,GREEN,WHITE,RED,RED)

		speed_arrow = Vector(2*RIGHT).set_color(RED)
		particle  = Dot(color = GREEN).scale(7)		
		speed = TextMobject("speed $\\approx$ c",color = BLUE).next_to(speed_arrow,RIGHT,buff = 0.1)

		grp = VGroup(speed_arrow,particle,speed).center().shift(1*UP)

		self.play(Write(title))
		self.wait(2)

		self.play(Write(particle))
		self.wait()

		self.play(Write(speed_arrow))
		self.wait()

		self.play(Write(speed))
		self.wait(2)

		self.play(ReplacementTransform(particle.copy(),VGroup(energy0[0],energy0[2])),Write(energy0))
		self.wait(2)

		self.play(Transform(energy0[0],energy1[0]))
		self.wait(2)

		self.play(*[ReplacementTransform(energy1[i].copy(),energy2[j])
					for i,j in [(0,2),(1,1),(2,0),(3,3)]])
		self.wait(2)

		units.next_to(energy2,RIGHT,buff = 1)

		self.play(Write(units[0]))
		self.wait()

		self.play(Write(units[1:]))
		self.wait(2)


class SeeingInsideLHC(Scene):
	def construct(self):

		def Highlight(object,half_angle = PI/24,scale_factor = 1.3,single_anim_time = 0.5):
			self.play(object.scale,scale_factor,run_time = single_anim_time)
			self.play(object.rotate,half_angle,run_time = single_anim_time)
			self.play(object.rotate,-2*half_angle,run_time = single_anim_time)
			self.play(object.rotate,half_angle,run_time = single_anim_time)
			self.play(object.scale,1/scale_factor,run_time = single_anim_time)
		
		#Variables Definition

		title = TextMobject("What Happens Inside \\\\ Particle Accelerator?")

		protonA = Dot(color = RED).scale(3)
		protonB = Dot(color = BLUE).scale(3)

		potential = FunctionGraph(lambda x : x**(-1), x_min = 1/5,x_max = 10 , color = RED)
		

		axes = Axes(x_min = 0,x_max = 10, y_min = 0 ,y_max = 5,color = RED,axis_config = {"include_tip":False})
		x_lbl = TextMobject("Distance").shift(5*RIGHT + 0.5*DOWN).set_color(TEAL_D)
		y_lbl = TextMobject("Potential Energy").rotate(PI/2).shift(3*UP + 0.5*LEFT).set_color(MAROON)

		grp = VGroup(axes,potential,protonA,x_lbl,y_lbl).shift(2*DOWN + 3*LEFT)
		
		potential_with_Range = FunctionGraph(self.potential_with_Range, x_min = 1/(5+1/5),x_max = 10 , color = RED).shift(2*DOWN + 3*LEFT)
		potential_with_Range2 = FunctionGraph(self.potential_with_Range2, x_min = 1/(5+1/5),x_max = 10 , color = RED).shift(2*DOWN + 3*LEFT)
		potential_with_Range3 = FunctionGraph(self.potential_with_Range3, x_min = 1/(5+1/5),x_max = 10 , color = RED).shift(2*DOWN + 3*LEFT)

		protonB.shift(11*RIGHT).shift(2*DOWN + 3*LEFT)

		range_tick = Line(-0.2*UP,0.2*UP).set_stroke(WHITE,5).shift(5*RIGHT).shift(2*DOWN + 3*LEFT)
		range_text = TextMobject("R").set_stroke(WHITE,2).next_to(range_tick,UP,buff = 0.1)
		range_mark = VGroup(range_tick,range_text).set_color(GREEN)

		Group = VGroup(protonA,protonB,axes,x_lbl,y_lbl,potential,potential_with_Range,potential_with_Range2,potential_with_Range3,range_mark).shift(2*LEFT)

		#Animations

		self.play(Write(title.to_edge(UP)))
		self.wait(2)

		self.play(FadeIn(protonA),run_time = 1)
		self.wait(2)

		self.play(Write(VGroup(axes,potential,x_lbl,y_lbl)),run_time = 2)
		self.wait(2)

		self.play(Transform(potential,potential_with_Range))
		self.wait(2)

		self.play(Write(range_mark))
		self.wait(2)

		for i in [potential_with_Range2,potential_with_Range3,potential_with_Range]:
			self.play(Transform(potential,i))
			self.wait(2)

		self.play(range_mark.scale,(1.3),run_time = 0.5)
		self.play(range_mark.scale,(1/1.3),run_time = 0.5)
		self.wait(2)

		self.play(FadeIn(protonB))
		self.wait(2)

		self.play(protonB.shift,10*LEFT,run_time = 3)
		self.play(protonB.shift,10*RIGHT,run_time = 3)
		self.wait(2)

		self.play(FadeOut(protonA))
		self.wait(2)

		self.play(protonB.shift,10*LEFT,run_time = 3)
		self.play(protonB.shift,10*RIGHT,run_time = 3)
		self.wait(2)

	@staticmethod
	def potential_with_Range(x):
		if (x <= 5):
			return (x**(-1) - 1/5)
		else:
			return 0

	@staticmethod
	def potential_with_Range2(x):
		if (x <=5):
			return np.sin(2*PI*x/5)
		else:
			return 0

	@staticmethod
	def potential_with_Range3(x):
		if (x <=5):
			if x == 0 :
				return 0
			if (x <= 2.5):
				return 1
			else:
				return -1
		else:
			return 0


class QM_Formalism(Scene):
	def construct(self):

		def Highlight(object,half_angle = PI/24,scale_factor = 1.3,single_anim_time = 0.5):
			self.play(object.scale,scale_factor,run_time = single_anim_time)
			self.play(object.rotate,half_angle,run_time = single_anim_time)
			self.play(object.rotate,-2*half_angle,run_time = single_anim_time)
			self.play(object.rotate,half_angle,run_time = single_anim_time)
			self.play(object.scale,1/scale_factor,run_time = single_anim_time)


		#Variables Definition
		a1 = Vector(np.array([-1,0,0])).set_stroke(YELLOW,3)
		f1 = FunctionGraph(self.plain_wave,x_min = 0,x_max = PI)
		t1 = TexMobject("{{-e^{-i(","k","x + {{Et}\\over{\\hbar}})}}\\over{2i}}").scale(2)
		incident_wave_symbol = VGroup(a1,f1)
		incident_wave = VGroup(incident_wave_symbol,t1.next_to(incident_wave_symbol,UP,buff= 0.35)).scale(0.3).set_color(YELLOW).center()

		a2 = Vector(np.array([1,0,0])).set_stroke(GREEN,3).shift(PI*RIGHT)
		f2 = FunctionGraph(self.plain_wave,x_min = 0,x_max = PI)
		t2 = TexMobject("{e^{i(kx - {Et\\over{\\hbar}})}\\over{2i}}","{e^{2i","\\delta(E)}}").scale(2)
		t2[0].set_color(GREEN),t2[1:].set_color(PURPLE)
		reflected_wave_symbol = VGroup(a2,f2).set_color(GREEN)
		reflected_wave = VGroup(reflected_wave_symbol,t2.next_to(reflected_wave_symbol,DOWN,buff= 0.35)).scale(0.3).center()

		protonB = Dot(color = BLUE).scale(3).shift(11*RIGHT).shift(2*DOWN + 5*LEFT)

		Energy_line = DashedLine(-1*DOWN + 5*LEFT,-1*DOWN + 5*RIGHT).set_color(TEAL_E)
		Energy_lbl = TextMobject("E").next_to(Energy_line,RIGHT,buff = 0.1).set_color(TEAL_E)
		Energy_lbl0 = TextMobject("E").shift(protonB.get_center()).set_color(TEAL_E)

		#From SeeingInsideLHC
		
		potential_with_Range = FunctionGraph(self.potential_with_Range, x_min = 1/(5+1/5),x_max = 10 , color = RED)
		
		axes = Axes(x_min = 0,x_max = 10, y_min = 0 ,y_max = 5,color = RED,axis_config = {"include_tip":False})
		x_lbl = TextMobject("Distance(x)").shift(5*RIGHT + 0.5*DOWN).set_color(TEAL_D)
		y_lbl = TextMobject("Potential Energy (V)").rotate(PI/2).shift(3*UP + 0.5*LEFT).set_color(MAROON)

		range_tick = Line(-0.2*UP,0.2*UP).set_stroke(WHITE,5).shift(5*RIGHT)
		range_text = TextMobject("R").set_stroke(WHITE,2).next_to(range_tick,UP,buff = 0.1)
		range_mark = VGroup(range_tick,range_text).set_color(GREEN)

		grp = VGroup(axes,potential_with_Range,x_lbl,y_lbl,range_mark).shift(2*DOWN + 5*LEFT)
	

		#Animations

		incident_wave.next_to(protonB,UP,buff = 0.1)
		reflected_wave.next_to(protonB,DOWN,buff = 0.1)

		self.play(ShowCreation(grp),FadeIn(protonB),run_time = 3)
		self.wait(2)

		self.play(protonB.scale,1.4,run_time = 0.5)
		self.play(protonB.scale,1/1.4,run_time = 0.5)
		self.wait(2)

		self.play(potential_with_Range.scale,1.2,run_time = 0.5)
		self.play(potential_with_Range.scale,1/1.2,run_time = 0.5)
		self.wait(2)

		self.play(Write(Energy_line))
		self.wait(2)

		self.play(ReplacementTransform(Energy_lbl0,Energy_lbl))
		self.wait(2)


		self.play(FadeInFrom(incident_wave_symbol,RIGHT),run_time = 1.5)
		self.wait(2)
		self.play(Write(t1))
		self.wait(2)

		self.play(t1[1].scale,1.5,run_time = 0.5)
		self.wait(2)
		self.play(t1[1].scale,1/1.5,run_time = 0.5)
		self.wait(2)

		self.play(FadeOut(x_lbl),FadeOut(y_lbl))
		self.wait(2)

		self.play(incident_wave.shift,6*LEFT,run_time = 2)
		self.play(FadeOutAndShift(incident_wave,LEFT))
		self.play(FadeInFrom(reflected_wave_symbol.move_to(incident_wave.get_center()),LEFT))
		self.play(Write(t2.next_to(reflected_wave_symbol,UP,buff = 0.1)))
		self.wait(2)

		Highlight(t2[1:],half_angle = 0,)
		self.wait(2)

		Highlight(t2[2])
		self.wait(2)

		self.play(reflected_wave.shift,6*RIGHT,run_time = 2)
		self.wait(2)

		self.play(Write(incident_wave.shift(6*RIGHT).next_to(reflected_wave,LEFT,buff = 0.5)))
		self.wait(2)

		self.play(*[FadeOut(x)
					for x in [axes,potential_with_Range,Energy_line,Energy_lbl,range_mark,protonB]
					],
					incident_wave.move_to,(-3.5*RIGHT + 2*UP),
					reflected_wave.move_to,(3.5*RIGHT + 2*UP)
					)
		self.wait(2)

		brace_inc = Brace(incident_wave,UP).set_color(TEAL_A)
		text_inc = brace_inc.get_text("Incident Wave").set_color(TEAL_A)

		brace_ref = Brace(reflected_wave,UP).set_color(TEAL_A)
		text_ref = brace_ref.get_text("Reflected Wave").set_color(TEAL_A)

		self.play(FadeInFrom(brace_inc,UP),FadeInFrom(brace_ref,UP))
		self.wait(2)
		self.play(FadeInFrom(text_inc,UP),FadeInFrom(text_ref,UP))
		self.wait(2)

		wavefun_text = TexMobject("\\Psi(x>R,t) = ",
									"\\frac{-e^{-i(kx + {{Et}\\over{\\hbar}})}}{2i}",
									"+",
									"{e^{i(kx - {Et\\over{\\hbar}})}\\over{2i}}",
									"{e^{2i\\delta(E)}}")

		self.play(Write(wavefun_text[0].set_color(RED)))
		self.wait(2)

		self.play(ReplacementTransform(t1.copy(),wavefun_text[1].set_color(YELLOW)))
		self.play(Write(wavefun_text[2].set_color(RED)))
		self.wait(2)

		wavefun_text[3].set_color(GREEN),wavefun_text[4].set_color(PURPLE)
		self.play(ReplacementTransform(t2.copy(),wavefun_text[3:5]))
		self.wait(2)

		wavefun_text1 = TexMobject("\\Psi(x>R,t) = ",
									"e^{i\\delta(E)}",
									"{\\left(-\\frac{e^{-i(kx + \\delta(E))}}{2i}",
									" + ",
									"\\frac{e^{i(kx + \\delta(E))}}{2i}\\right)}",
									"{e^{-iEt/{\\hbar}}}")

		for i,color in [(0,RED),(1,PURPLE),(2,YELLOW),(3,RED),(4,GREEN),(5,MAROON)]:
			wavefun_text1[i].set_color(color)

		self.play(Write(wavefun_text1.shift(1.5*DOWN)))
		self.wait(2)

		wavefun_text2 = TexMobject("\\Psi(x>R,t) = ",
									"e^{i\\delta(E)}",
									"\\sin(kx + \\delta(E))",
									"{e^{-iEt/{\\hbar}}}").shift(1.5*DOWN)

		for i,color in [(0,RED),(1,PURPLE),(2,BLUE),(3,MAROON)]:
			wavefun_text2[i].set_color(color)

		self.play(wavefun_text1[2:5].scale,1.2,run_time = 0.5)
		self.play(wavefun_text1[2:5].scale,1/1.2,run_time = 0.5)
		self.wait(2)

		self.play(*[ReplacementTransform(wavefun_text1[i],wavefun_text2[j])
					for i,j in [(0,0),(1,1),(5,3)]],ReplacementTransform(wavefun_text1[2:5],wavefun_text2[2])
			)
		self.wait(2)

		box = SurroundingRectangle(VGroup(brace_ref,text_ref,reflected_wave),buff = 0.1).set_color(BLUE)
		self.play(ShowCreation(box))
		self.wait(2)	

		

	@staticmethod
	def plain_wave(x):
		return np.sin(5*x)

	@staticmethod
	def potential_with_Range(x):
		if (x <= 5):
			return (x**(-1) - 1/5)
		else:
			return 0

class Time_Delay(Scene):
	#CONFIG = {"camera_config" : {"background_color" : GREEN_SCREEN}}
	def construct(self):
		def Highlight(object,half_angle = PI/24,scale_factor = 1.3,single_anim_time = 0.5):
			self.play(object.scale,scale_factor,run_time = single_anim_time)
			self.play(object.rotate,half_angle,run_time = single_anim_time)
			self.play(object.rotate,-2*half_angle,run_time = single_anim_time)
			self.play(object.rotate,half_angle,run_time = single_anim_time)
			self.play(object.scale,1/scale_factor,run_time = single_anim_time)

		title = TextMobject("Time Delay").set_color(RED).scale(2)
		text = TextMobject("It's the time that the incident \\\\ wavefunction takes to return back.").set_color(MAROON)
		eqn = TexMobject("\\tau",
							" = ",
							" 2{\\hbar}",
							"{{d",
							"\\delta}",
							"\\over{d",
							"E}}").scale(2)

		for i,color in [(0,RED),(2,GREEN),(4,PURPLE),(6,TEAL_A)]:
			eqn[i].set_color(color)

		self.play(Write(title.to_edge(UP)))
		self.wait(2)

		self.play(Write(text.shift(1*UP)),run_time = 2)
		self.wait(2)

		self.play(Write(eqn.shift(1.5*DOWN)),run_time = 2)
		self.wait(2)

		Highlight(eqn[3:])
		self.wait(2)


#DONE
class Scattered_Wavefunction(Scene):
	def construct(self):
		###############################
		###############################

		a1 = Vector(np.array([1,0,0])).set_stroke(GREEN,3).shift(PI*RIGHT)
		f1 = FunctionGraph(self.plain_wave,x_min = 0,x_max = PI)

		a2 = Vector(np.array([1,0,0])).set_stroke(GREEN,3).shift(PI*RIGHT)
		f2 = FunctionGraph(self.plain_wave,x_min = 0,x_max = PI)
		
		t2 = TexMobject("{e^{i(kx - {Et\\over{\\hbar}})}\\over{2i}}","{e^{2i","\\delta(E)}}").scale(3)
		
		t3 = TexMobject("{e^{i(kx - {Et\\over{\\hbar}})}\\over{2i}}","{e^{2i","0}}").scale(3)
		
		t4 = TexMobject("{e^{i(kx - {Et\\over{\\hbar}})}\\over{2i}}").scale(3).scale(0.4)
		
		t2[0].set_color(GREEN),t2[1:].set_color(PURPLE)
		t3[0].set_color(GREEN),t3[1:].set_color(PURPLE)
		t4[0].set_color(GREEN)
		
		reflected_wave_symbol1 = VGroup(a1,f1).set_color(GREEN)
		reflected_wave_symbol2 = VGroup(a2,f2).set_color(GREEN)
		
		reflected_wave_with_delta = VGroup(reflected_wave_symbol1,t2.next_to(reflected_wave_symbol1,DOWN,buff= 0.35)).scale(0.3).center()

		reflected_wave_without_delta = VGroup(reflected_wave_symbol2,t3.next_to(reflected_wave_symbol2,DOWN,buff= 0.35)).scale(0.3).center()

		##############################
		##############################
		
		title = TextMobject("\\textbf{Scattered Wavefunction}").set_color(MAROON).scale(2)
		
		scatt_wave_text = TextMobject("Something that vanishes for a Free Particle.").set_color(GOLD_E)
		
		deltaforfp = TextMobject("For a Free Particle","$ \\ \\delta(E) = 0 $")
		deltaforfp[0].set_color(TEAL_A),deltaforfp[1].set_color(PURPLE)

		scatt_wave = TexMobject("\\Psi_{s}(x,t)","=").set_color(BLUE).scale(1.8)

		minus = TexMobject("-").set_color(BLUE).scale(1.8)

		#ANIMATIONS

		self.play(Write(title.to_edge(UP)))
		self.wait(2)

		self.play(Write(scatt_wave_text.shift(1.5*UP)),run_time = 2)
		self.wait(2)

		self.play(Write(deltaforfp.shift(0.5*UP)),run_time = 2)
		self.wait(2)

		self.play(Write(scatt_wave.shift(1.5*DOWN + 4*LEFT)))
		self.wait(2)

		self.play(FadeIn(reflected_wave_with_delta.scale(1.2).next_to(scatt_wave,RIGHT,buff = 5*SMALL_BUFF)),run_time = 2)
		self.wait(2)

		self.play(Write(minus.next_to(reflected_wave_with_delta,RIGHT,buff = 5*SMALL_BUFF)))
		self.wait(2)

		self.play(ReplacementTransform(reflected_wave_with_delta.copy(),reflected_wave_without_delta.scale(1.2).next_to(minus,RIGHT,buff = 5*SMALL_BUFF)),run_time = 2)
		self.wait(2)

		t4.move_to(t3.get_center())
		self.play(Transform(t3,t4))
		self.wait(2)

		scatt_wave_final = TexMobject("\\Psi_{s}(x,t)","=","e^{i\\delta}\\sin(\\delta)","e^{i(kx - {{Et}\\over{\\hbar}})}").scale(1.5)
		scatt_wave_final[0:2].set_color(BLUE),scatt_wave_final[2].set_color(MAROON),scatt_wave_final[3].set_color(GOLD_E)

		self.play(*[FadeOut(x)
					for x in [scatt_wave_text,deltaforfp]],
					*[ReplacementTransform(scatt_wave[i],scatt_wave_final[j])
						for i,j in [(0,0),(1,1)]],
					ReplacementTransform(VGroup(reflected_wave_with_delta,reflected_wave_without_delta,minus),scatt_wave_final[2:]),
					run_time  = 3
					)
		self.wait(2)

		brace_amp = Brace(scatt_wave_final[2],DOWN).set_color(MAROON)
		text1 = brace_amp.get_tex("A_{s}",buff = 0.2).set_color(MAROON).scale(1.5)
		text2 = brace_amp.get_text("\"Scattering \\\\ Amplitude\"" , buff = 0.2).set_color(MAROON)

		self.play(FadeInFrom(brace_amp,DOWN))
		self.wait(2)

		self.play(Write(text2))
		self.wait(2)

		self.play(ReplacementTransform(text2,text1))
		self.wait(2)

		scatt_amp = TexMobject("A_{s}","=","e^{i\\delta}\\sin(\\delta)").set_color(MAROON).shift(2*DOWN).scale(2)

		self.play(*[ReplacementTransform(x,scatt_amp[y])
					for x,y in [(text1,0),(brace_amp,1),(scatt_wave_final[2].copy(),2)]],run_time = 2)
		self.wait(2)

		amp_sqr  = TexMobject("|A_{s}|^2","=","\\sin^2{(\\delta)}").move_to(scatt_amp.get_center()).set_color(MAROON).scale(2)

		self.play(*[ReplacementTransform(scatt_amp[i],amp_sqr[j])
					for i,j in [(0,0),(1,1),(2,2)]],run_time = 2)
		self.wait(2)

		self.play(*[FadeOut(x)
					for x in [amp_sqr,title,scatt_wave_final]])

	@staticmethod
	def plain_wave(x):
		return np.sin(5*x)

#DONE
class Resonance(Scene):
	def construct(self):
		def Highlight(object1,object2,half_angle = PI/24,scale_factor = 1.3,single_anim_time = 0.5):
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

		title = TextMobject("\\textbf{Resonance}").set_color(GREEN).to_edge(UP).scale(2)
		
		eqn1 = TexMobject("tan(",
							"\\delta(k)",
							") = \\frac{\\beta}{\\alpha - k}",
							"\\ \\ \\ \\alpha",
							",",
							"\\beta",
							" > 0")
		eqn1[0].set_color(BLUE),eqn1[1].set_color(PURPLE),eqn1[2:].set_color(BLUE)

		

		# delta vs k Plot
		######################################################
		d_axes = Axes(x_min = 0,x_max = 5, y_min = 0 ,y_max = 4,color = GREEN,axis_config = {"include_tip":False})
		d_x_lbl1 = TextMobject("Angular Wavenumber").shift(2.5*RIGHT + 0.6*DOWN).set_color(BLUE)
		d_x_lbl2 = TexMobject("k").shift(4*RIGHT + 2.6*DOWN).set_color(BLUE)
		d_y_lbl = TexMobject("\\delta(k)").shift((PI/2 + 0.25)*UP + 0.7*LEFT).set_color(PURPLE)
		delta_plot = FunctionGraph(lambda x: self.deltaplot(x),x_min = 0,x_max=5,color = MAROON)

		graph1 = VGroup(d_axes,d_x_lbl1,d_y_lbl,delta_plot).shift(2*DOWN + 1.5*RIGHT)

		#alpha tick
		alpha = TexMobject("\\alpha").set_color(GREEN)
		alpha_tick = Line(-0.2*UP,0.2*UP).set_stroke(WHITE,5)
		alpha_mark = VGroup(alpha_tick,alpha.next_to(alpha_tick,UR,buff = 0.2)).shift(2*DOWN + 4.5*RIGHT)

		#pi/2 tick
		p = TexMobject("{\\pi \\over 2}").set_color(PURPLE)
		p_tick  = Line(-0.2*RIGHT,0.2*RIGHT).set_stroke(WHITE,5)
		p_mark = VGroup(p.next_to(p_tick,RIGHT,buff = 0.1),p_tick).shift(2*DOWN + UP*PI/2 + 1.5*RIGHT)

		######################################################
	
		#ANIMATIONS

		self.play(Write(title))
		self.wait(2)

		self.play(Write(eqn1))
		self.wait(2)

		Highlight(eqn1[3],eqn1[5],scale_factor = 1.5)

		self.play(eqn1.shift,2.5*LEFT
				,run_time = 2)
		self.wait(2)

		self.play(FadeOut(eqn1[3:]))
		self.wait(2)

		self.play(Write(d_axes))
		self.wait(2)

		self.play(Write(d_y_lbl),Write(d_x_lbl1))
		self.wait(2)

		self.play(Transform(d_x_lbl1,d_x_lbl2))
		self.wait(2)

		self.play(Write(delta_plot),run_time = 2.5)
		self.wait(2)

		self.play(Write(alpha_mark))
		self.wait(2)

		Highlight(alpha,alpha)
		self.wait(2)

		sq1 = Square().shift(3*RIGHT + UP*PI/2).shift(2*DOWN + 1.5*RIGHT).set_color(GOLD_E)#.scale(0.3)

		self.play(ShowCreation(sq1))
		self.play(sq1.scale,0.3)
		self.wait(2)

		self.play(Write(p_mark))
		self.wait(2)

		Highlight(d_y_lbl,p)
		self.wait(2)

		Highlight(alpha,p)
		self.wait(2)

		self.play(eqn1[:3].shift,1.5*UP)
		self.wait(2)

		l1 = TexMobject("|A_{s}|^2"," = ","\\sin^2{(\\delta)}"," = 1").set_color(MAROON)
		l2 = TexMobject("\\tau"," = ","2{\\hbar}{{d\\delta}\\over{dE}}"," = {1\\over{","\\beta}}","\\to \\infty").set_color(MAROON)
		l = VGroup(l1,l2).arrange(DOWN,aligned_edge = LEFT,buff = 0.5).next_to(eqn1[:3],DOWN,buff = 1)
		sq2 = SurroundingRectangle(l,buff = 0.5).set_color(GOLD_E)
		l_list = VGroup(sq2,l)
		self.play(ReplacementTransform(sq1.copy(),sq2))
		self.wait(2)

		for i in range(4):	
			self.play(Write(l1[i]))
			self.wait()
		for i in range(5):
			self.play(Write(l2[i]))
			self.wait()

		Highlight(l2[4],l2[4],half_angle = 0)
		self.wait(2)

		self.play(Write(l2[5]))
		self.wait()

		######################################################
		##What is resonance
		meaning = BulletedList("Maximum Scattering Amplitude.","Very Large or Infinite Time \\\\ Delay.","Particle Should never return \\\\ back.").set_color_by_gradient(TEAL_E,BLUE,TEAL_A)
		######################################################
		self.play(*[FadeOut(x)
					for x in [p_mark,alpha_mark,sq1,graph1,eqn1[:3]]],
					l_list.shift,1*UP
					)
		self.wait(2)

		meaning.next_to(l_list,RIGHT,buff = 0.5)

		for i in [0,1,2]:
			self.play(Write(meaning[i]))
			self.wait()

		self.play(*[FadeOut(x)
					for x in [meaning,l_list]])
		self.wait(2)

		############################################################

		eqn2 = TexMobject("|A_{s}|^2 = {{\\beta^2}\\over{\\beta^2 + (\\alpha - k)^2}}").set_color(MAROON).shift(1.5*UP)

		eqn3 = TexMobject("|A_{s}|^2 = {{{(\\Gamma/2)}^2}\\over{{(\\Gamma/2)}^2 + (E - E_{\\alpha})^2}}").set_color(MAROON)

		eqn4 = TexMobject("\\Gamma = {{2{\\hbar^2}\\alpha\\beta}\\over{m}}").set_color(BLUE)

		eqn5 = TexMobject("E - E_{\\alpha} = {{{\\hbar}^2}\\over{2m}}{(k^2 - {\\alpha}^2)}")
		eqn6 = TexMobject("E - E_{\\alpha} = {{{\\hbar}^2}\\over{2m}}{(k - {\\alpha})(k + {\\alpha})}")
		eqn7 = TexMobject("k \\approx \\alpha").set_color(BLUE)
		eqn8 = TexMobject("E - E_{\\alpha} = {{{\\hbar}^2}\\over{2m}}{(k - {\\alpha})(2{\\alpha})}")
		eqn8 = TexMobject("E - E_{\\alpha} = {{{\\hbar}^2{\\alpha}}\\over{m}}{(k - {\\alpha})}")

		eqn9 = TexMobject("|A_{s}|^2"," = ","\\sin^2{(\\delta)}").set_color(MAROON)

		name = TextMobject("\"Breit–Wigner \\\\ Distribution\"")
		############################################################

		# Distribution Plot
		######################################################
		axes = Axes(x_min = -2,x_max = 5, y_min = 0 ,y_max = 2,color = GREEN,axis_config = {"include_tip":False})
		x_lbl = TextMobject("Energy of Particle (E)").shift(1.5*RIGHT + 0.5*DOWN).set_color(BLUE)
		y_lbl = TexMobject("|A_{s}|^2").shift(2.5*UP + 0.1*RIGHT).set_color(MAROON)
		one = TexMobject("1").shift(1*UP + 0.3*UR - 0.1*RIGHT).set_color(GOLD_E)

		max_line = DashedLine(2*LEFT + 1*UP , 5*RIGHT + 1*UP).set_color(GOLD_E)

		distribution_plot = FunctionGraph(lambda x:self.breit_wigner_distribution(x),x_min = -2,x_max = 5,color = RED)

		#Energy_alpha tick
		energy_alpha = TexMobject("E_{\\alpha}").set_color(BLUE)
		energy_tick = Line(-0.2*UP,0.2*UP).set_stroke(WHITE,5).shift(2*RIGHT)
		energy_mark = VGroup(energy_tick,energy_alpha.next_to(energy_tick,UR,buff = 0.1))


		graph2 = VGroup(axes,x_lbl,y_lbl,distribution_plot,max_line,one,energy_mark)
		######################################################

		self.play(Write(eqn1[:3]))
		self.wait()
		self.play(Write(eqn9.next_to(eqn1[:3],RIGHT,buff = 4)))
		self.wait()

		self.play(ReplacementTransform(VGroup(eqn1[:3],eqn9),eqn2),run_time = 3)
		self.wait(2)

		self.play(Write(eqn7.next_to(eqn2,RIGHT,buff = 2)))
		self.wait(2)
		self.play(ReplacementTransform(eqn2,eqn3))
		self.wait(2)

		self.play(Write(eqn4.next_to(eqn3,RIGHT,buff = 1.5)),FadeOut(eqn7))
		self.wait(2)

		self.play(FadeOut(eqn4),
					eqn3.shift,1.5*UP)
		self.wait(2)

		graph2.next_to(eqn3,DOWN,buff = 0.2)


		self.play(Write(axes))
		self.wait()

		self.play(Write(y_lbl),Write(x_lbl))
		self.wait()

		self.play(ShowCreation(distribution_plot))
		self.wait(2)

		self.play(Write(name.set_color(YELLOW).next_to(distribution_plot,UR,buff = 0.4)))
		self.wait(2)

		self.play(Write(energy_mark),run_time = 2)
		self.wait(2)

		self.play(Write(max_line))
		self.wait(2)

		self.play(Write(one))
		self.wait(2)

		self.play(*[FadeOut(x)
					for x in [graph2,name,eqn3,title]])


	@staticmethod
	def breit_wigner_distribution(E,E0 = 2,g = 2):
		return ((g/2.0)**2)/((g/2.0)**2 + (E-E0)**2)
	@staticmethod
	def deltaplot(k,alpha = 3,beta = 0.1):
		if (k <= alpha):
			return np.arctan(beta/(alpha - k))
		else:
			return PI + np.arctan(beta/(alpha - k))



class I1(Scene):
	def construct(self):
		kg = TextMobject("Kilograms (kg)").set_color(PURPLE)
		g = TextMobject("Grams (g)").set_color(RED)

		self.play(Write(kg))
		self.wait(1)

		self.play(kg.shift,1*UP,
					Write(g.shift(1*DOWN)))
		self.wait(1)
		

class I2(Scene):
	def construct(self):
		text  = TextMobject("Measure of \\\\ \"attractiveness\" \\\\ of the Potential").set_color_by_gradient(RED,GREEN,BLUE)

		self.play(Write(text),run_time = 3)
		self.wait(2)


			

