# test_zookeepersync.py
"""
Tests for ZookeeperSync module.
"""

import unittest
from zookeepersync import ZookeeperSync

class TestZookeeperSync(unittest.TestCase):
    """Test cases for ZookeeperSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZookeeperSync()
        self.assertIsInstance(instance, ZookeeperSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZookeeperSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
