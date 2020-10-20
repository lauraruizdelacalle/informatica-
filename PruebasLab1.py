from unittest import TestCase, main

class Test(TestCase):
    
    def test_ninguna_libra_a_gramos(self):
        self.assertAlmostEqual(libras_a_gramos(0.), 0.)

    def test_media_libra_a_gramos(self):
        self.assertAlmostEqual(libras_a_gramos(0.5), 226.796185)

    def test_una_libra_a_gramos(self):
        self.assertAlmostEqual(libras_a_gramos(1.), 453.59237)
        
    def test_billon_libras_a_gramos(self):
        self.assertAlmostEqual(libras_a_gramos(1e12), 453592370000000.0)
    
    def test_declinacion_21_dic(self):
        self.assertGreater(declinacion(355), -23.45)
        self.assertLess(declinacion(355), -23.44)
        
    def test_declinacion_22_mar(self):
        self.assertAlmostEqual(declinacion(81), .0)
        
    def test_declinacion_1_ene(self):
        self.assertGreater(declinacion(1), -23.0117)
        self.assertLess(declinacion(1), -23.0116)

    def test_declinacion_dia_100(self):
        self.assertAlmostEqual(declinacion(100), 7.533773566685933)
        
    def test_area_jardin_0(self):
        self.assertEqual(area_jardin(0.), 0.)

    def test_area_jardin_1(self):
        from math import pi
        self.assertAlmostEqual(area_jardin(1.), pi - 2.)
        
    def test_area_jardin_2(self):
        from math import pi
        self.assertAlmostEqual(area_jardin(2.)/4., pi - 2.)
        
    def test_area_jardin_medio(self):
        self.assertAlmostEqual(area_jardin(.5)*4., area_jardin(1.))

    def test_momento_inercia_tubo_m0(self):
        self.assertEqual(momento_inercia_tubo(0.,2,3), 0.)

    def test_momento_inercia_tubo_m1(self):
        self.assertAlmostEqual(momento_inercia_tubo(1.,1.,1.5), 1.625)

    def test_momento_inercia_tubo_m2(self):
        self.assertAlmostEqual(momento_inercia_tubo(2.,1.,1.5), 3.25)

    def test_momento_inercia_tubo_m1r2(self):
        self.assertAlmostEqual(momento_inercia_tubo(1.,2.,2.5), 5.125)
        
    def test_cardioide_a1_0(self):
        from math import pi
        self.assertAlmostEqual(cardioide(1.,0), 2.0)

    def test_cardioide_a1_pi3(self):
        from math import pi
        self.assertAlmostEqual(cardioide(1.,pi/3), 1.5)

    def test_cardioide_a1_2pi3(self):
        from math import pi
        self.assertAlmostEqual(cardioide(1.,2*pi/3), 0.5)

    def test_cardioide_a1_pi(self):
        from math import pi
        self.assertAlmostEqual(cardioide(1.,pi), 0.)

    def test_empuje_cohete_1_0_10_2_1(self):
        self.assertAlmostEqual(empuje_cohete(1,0,10,2,1), 10.)
    
    def test_empuje_cohete_1_1_1_2_1(self):
        self.assertAlmostEqual(empuje_cohete(1,1,1,2,1), 2.)
    
    def test_empuje_cohete_1_2_1_2_1(self):
        self.assertAlmostEqual(empuje_cohete(1,2,1,2,1), 3.)
    
    def test_empuje_cohete_2_1_2_2_1(self):
        self.assertAlmostEqual(empuje_cohete(2,1,2,2,1), 4.)
    
    def test_angulos_equi(self):
        from math import pi
        A,B,C = angulos_triangulo(1,1,1)
        self.assertAlmostEqual(A,B)
        self.assertAlmostEqual(A,C)
        self.assertAlmostEqual(A,pi/3.)

    def test_angulos_iso(self):
        from math import pi
        A,B,C = sorted(angulos_triangulo(2,2,1))
        self.assertAlmostEqual(sum((A,B,C)), pi)
        self.assertAlmostEqual(B,C)
        
    def test_angulos_rec(self):
        from math import pi
        A,B,C = sorted(angulos_triangulo(3,4,5))
        self.assertAlmostEqual(sum((A,B,C)), pi)
        self.assertAlmostEqual(C, pi/2)

    def test_angulos_iso_ob(self):
        from math import pi, sqrt, atan
        A,B,C = sorted(angulos_triangulo(4, sqrt(5), sqrt(5)))
        self.assertAlmostEqual(sum((A,B,C)), pi)
        self.assertAlmostEqual(A, B)
        self.assertAlmostEqual(A, atan(.5))

    def test_velocidad_escape_0_1(self):
        self.assertAlmostEqual(velocidad_escape(0,1), 0.)

    def test_velocidad_escape_1_0(self):
        self.assertAlmostEqual(velocidad_escape(1,0), 0.)
    
    def test_velocidad_escape_1_2(self):
        self.assertAlmostEqual(velocidad_escape(1,2), 2.)
    
    def test_velocidad_escape_2_4(self):
        self.assertAlmostEqual(velocidad_escape(2,4), 4.)

    def test_velocidad_orbital_h_h_h(self):
        G = 6.674e-11
        self.assertAlmostEqual(velocidad_orbital(.5/G,.5,.5), 1.)

    def test_velocidad_orbital_h_1_1h(self):
        from math import sqrt
        G = 6.674e-11
        self.assertAlmostEqual(velocidad_orbital(.5/G,1,1.5), sqrt(2./3.))
        
    def test_velocidad_orbital_1_1_1(self):
        G = 6.674e-11
        self.assertAlmostEqual(velocidad_orbital(1./G,1,1), 1.)
    
    def test_velocidad_orbital_1_h_1(self):
        from math import sqrt
        G = 6.674e-11
        self.assertAlmostEqual(velocidad_orbital(.5/G,.5,1.5), sqrt(5./3.))
        
    def test_catenaria_15_1(self):
        self.assertAlmostEqual(catenaria(1.5,1.), 2.352409615243247)

    def test_catenaria_0_1(self):
        self.assertAlmostEqual(catenaria(0.,1.), 1.)

    def test_catenaria_0_2(self):
        self.assertAlmostEqual(catenaria(0.,2.), 2.)

    def test_catenaria_m1_1(self):
        self.assertAlmostEqual(catenaria(-1.,1.), 1.5430806348152437)

# Si usas Jupyter descomenta la segunda línea y comenta la siguiente
main() # IDLE, Python, PyCharm
# main(argv=['first-arg-is-ignored'], exit=False) # Jupyter
