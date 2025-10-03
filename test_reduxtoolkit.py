# test_reduxtoolkit.py
"""
Tests for ReduxToolkit module.
"""

import unittest
from reduxtoolkit import ReduxToolkit

class TestReduxToolkit(unittest.TestCase):
    """Test cases for ReduxToolkit class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ReduxToolkit()
        self.assertIsInstance(instance, ReduxToolkit)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ReduxToolkit()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
