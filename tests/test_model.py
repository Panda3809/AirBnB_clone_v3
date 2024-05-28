import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.model = BaseModel()

    def test_model_creation(self):
        """Test if model is created correctly"""
        self.assertIsNotNone(self.model.id)
        self.assertIsNotNone(self.model.created_at)
        self.assertIsNotNone(self.model.updated_at)

    def test_model_str(self):
        """Test the string representation of the model"""
        self.assertEqual(str(self.model), f"[BaseModel] ({self.model.id}) {self.model.__dict__}")

if __name__ == "__main__":
    unittest.main()
