import unittest
import numpy as np
from matplotlib import pyplot as plt
from ass4 import VoltageData


class Test(unittest.TestCase):
    
    # Test len
    def test_len(self):
        self.assertAlmostEqual(len(val), len(t), places = 1)
        
    # Test attributes
    def test_attr(self):
        self.assertEqual(list(val.times), list(t))
        self.assertEqual(list(val.voltages), list(v))
        self.assertEqual(list(val.errors), list(e))
        
    # Test square parenthesis
    def test_sq_par(self):
        self.assertAlmostEqual(val[3, 0], t[3])
        self.assertAlmostEqual(val[3, 1], v[3])
        self.assertAlmostEqual(val[3, 2], e[3])
         
    # Test slicing
    def test_slicing(self):
        self.assertEqual(list(val[2 : 5, 1]), list(v[2 : 5]))
         
    # Test constructor from data file
    def test_file(self):
        val_2 = VoltageData.parse_line('sample_data_file_with_errs.txt')
        self.assertEqual(list(val_2[:, 0]), list(val[:, 0]))
        self.assertEqual(list(val_2[:, 1]), list(val[:, 1]))
        self.assertEqual(list(val_2[:, 2]), list(val[:, 2]))
         
    # Test iteration
    def test_iter(self):
        for i, entry in enumerate(val):
            self.assertAlmostEqual(entry[0], t[i])
            self.assertAlmostEqual(entry[1], v[i])
            self.assertAlmostEqual(entry[2], e[i])
    
    # Test representation
    def test_repr(self):
        self.assertEqual(print(val), val.debug_repr())
        
    # Test interpolation
    def test_interp(self):
        v5 = val(val.times[5], 3)
        self.assertAlmostEqual(v5, val.voltages[5])
        
    # Test plotting
    def test_plot(self):
        vec = np.linspace(min(t), max(t), 200)
        val.plot(lab = 'Data', tit = 'Test', plot_style = '-')
        plt.plot(vec, val(vec, 3), 'r-', label = 'spline')
        plt.legend()
        plt.show()
        

if __name__ == '__main__':
    t, v, e = np.loadtxt('sample_data_file_with_errs.txt', unpack = True)
    val = VoltageData(t, v, e)
    unittest.main()