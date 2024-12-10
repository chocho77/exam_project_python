import unittest
from database import add_vehicle_to_db, delete_vehicle_from_db, db

class MyTestCase(unittest.TestCase):
    def test_add_vehicle(self):
        self.assertEqual(db, [])
        add_vehicle_to_db("BMW", "320", 1996, "blue", 300_000)
        self.assertEqual(db, [("BMW", "320", 1996, "blue", 300_000)])
    
    def test_delete_vehicle(self):
        add_vehicle_to_db("BMW","320", 1996, "blue", 300_000)
        delete_vehicle_from_db(0)
        delete_vehicle_from_db(0)
        self.assertEqual(db, [])

        

if __name__ == '__main__':
    unittest.main()

