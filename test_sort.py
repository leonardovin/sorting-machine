import unittest
from sort import sort, is_bulky, is_heavy

class TestSortMethod(unittest.TestCase):
    
    def test_standard_packages(self):
        """Test packages that should be classified as STANDARD"""
        # Small, light package
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")
        # Medium package, still within limits
        self.assertEqual(sort(100, 100, 100, 15), "STANDARD")
        # Edge case: exactly at the limits but not exceeding
        self.assertEqual(sort(150, 150, 44, 20), "STANDARD")  # volume = 990,000 < 1,000,000 and dimensions ≤ 150
    
    def test_bulky_packages(self):
        """Test packages that are bulky but not heavy"""
        # Large dimension
        self.assertEqual(sort(200, 50, 50, 10), "SPECIAL")
        # Large volume
        self.assertEqual(sort(150, 150, 150, 15), "SPECIAL")  # volume > 1,000,000
        # Edge case: exactly 151 cm in one dimension
        self.assertEqual(sort(151, 50, 50, 10), "SPECIAL")
    
    def test_heavy_packages(self):
        """Test packages that are heavy but not bulky"""
        # Heavy but small
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")
        # Edge case: exactly 21 kg
        self.assertEqual(sort(100, 100, 50, 21), "SPECIAL")
    
    def test_rejected_packages(self):
        """Test packages that are both bulky and heavy"""
        # Large dimension and heavy
        self.assertEqual(sort(200, 100, 100, 25), "REJECTED")
        # Large volume and heavy
        self.assertEqual(sort(150, 150, 150, 30), "REJECTED")
        # Multiple violations
        self.assertEqual(sort(200, 200, 200, 50), "REJECTED")
    
    def test_edge_case_boundaries(self):
        """Test exact boundary conditions"""
        # Exactly at weight limit (20 kg) - should be STANDARD
        self.assertEqual(sort(100, 100, 50, 20), "STANDARD")
        # Just over weight limit (20.1 kg) - should be SPECIAL
        self.assertEqual(sort(100, 100, 50, 20.1), "SPECIAL")
        
        # Exactly at dimension limit (150 cm) - should be STANDARD
        self.assertEqual(sort(150, 100, 50, 15), "STANDARD")
        # Just over dimension limit (150.1 cm) - should be SPECIAL
        self.assertEqual(sort(150.1, 100, 50, 15), "SPECIAL")
        
        # Exactly at volume limit (1,000,000 cubic cm) - should be STANDARD
        self.assertEqual(sort(100, 100, 100, 15), "STANDARD")  # volume = 1,000,000
        # Just over volume limit - should be SPECIAL
        self.assertEqual(sort(100, 100, 100.1, 15), "SPECIAL")  # volume > 1,000,000
    
    def test_error_handling_negative_values(self):
        """Test error handling for negative values"""
        # Negative width
        result = sort(-10, 50, 50, 10)
        self.assertTrue(result.startswith("ERROR"))
        self.assertIn("Dimensions must be positive values", result)
        
        # Negative height
        result = sort(50, -10, 50, 10)
        self.assertTrue(result.startswith("ERROR"))
        
        # Negative length
        result = sort(50, 50, -10, 10)
        self.assertTrue(result.startswith("ERROR"))
        
        # Negative weight
        result = sort(50, 50, 50, -10)
        self.assertTrue(result.startswith("ERROR"))
        self.assertIn("Weight cannot be negative", result)
    
    def test_error_handling_zero_values(self):
        """Test error handling for zero values"""
        # Zero width
        result = sort(0, 50, 50, 10)
        self.assertTrue(result.startswith("ERROR"))
        self.assertIn("Dimensions must be positive values", result)
        
        # Zero height
        result = sort(50, 0, 50, 10)
        self.assertTrue(result.startswith("ERROR"))
        
        # Zero length
        result = sort(50, 50, 0, 10)
        self.assertTrue(result.startswith("ERROR"))
        
        # Zero weight should be allowed
        self.assertEqual(sort(50, 50, 50, 0), "STANDARD")
    
    def test_error_handling_extreme_values(self):
        """Test error handling for extremely large values"""
        # Extremely large dimension
        result = sort(20000, 50, 50, 10)
        self.assertTrue(result.startswith("ERROR"))
        self.assertIn("Dimensions too large", result)
        
        # Extremely large weight
        result = sort(50, 50, 50, 20000)
        self.assertTrue(result.startswith("ERROR"))
        self.assertIn("Weight too large", result)
    
    def test_decimal_values(self):
        """Test that decimal values work correctly"""
        # Decimal dimensions and weight
        self.assertEqual(sort(50.5, 50.5, 50.5, 10.5), "STANDARD")
        # Decimal that crosses boundary
        self.assertEqual(sort(150.5, 50, 50, 10), "SPECIAL")
        self.assertEqual(sort(50, 50, 50, 20.5), "SPECIAL")

class TestIsBulkyMethod(unittest.TestCase):
    
    def test_bulky_by_dimension(self):
        """Test bulky classification by dimension"""
        self.assertTrue(is_bulky(200, 50, 50))
        self.assertTrue(is_bulky(50, 200, 50))
        self.assertTrue(is_bulky(50, 50, 200))
        # Exactly 150 should NOT be bulky (since condition is > 150)
        self.assertFalse(is_bulky(150, 50, 50))
        self.assertFalse(is_bulky(50, 150, 50))
        self.assertFalse(is_bulky(50, 50, 150))
    
    def test_bulky_by_volume(self):
        """Test bulky classification by volume"""
        self.assertTrue(is_bulky(150, 150, 150))  # volume > 1,000,000
        self.assertFalse(is_bulky(100, 100, 100))  # volume = 1,000,000
    
    def test_is_bulky_error_handling(self):
        """Test error handling in is_bulky"""
        with self.assertRaises(ValueError):
            is_bulky(-10, 50, 50)
        with self.assertRaises(ValueError):
            is_bulky(50, 0, 50)
        with self.assertRaises(ValueError):
            is_bulky(20000, 50, 50)

class TestIsHeavyMethod(unittest.TestCase):
    
    def test_heavy_classification(self):
        """Test heavy classification"""
        self.assertTrue(is_heavy(25))
        self.assertTrue(is_heavy(21))
        self.assertFalse(is_heavy(20))
        self.assertFalse(is_heavy(15))
        self.assertFalse(is_heavy(0))
    
    def test_is_heavy_error_handling(self):
        """Test error handling in is_heavy"""
        with self.assertRaises(ValueError):
            is_heavy(-10)
        with self.assertRaises(ValueError):
            is_heavy(20000)

if __name__ == "__main__":
    # Run the tests
    unittest.main(verbosity=2)