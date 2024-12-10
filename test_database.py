import unittest
from database import add_vehicle_to_db, delete_vehicle_from_db, empty_database, get_database 
from database import view_vehicle_from_db

class MyTestCase(unittest.TestCase):
   
    def test_add_vehicle(self):
        self.assertEqual(get_database(), [])
        add_vehicle_to_db("BMW", "320", 1996, "blue", 300_000)
        self.assertEqual(get_database(), [("BMW", "320", 1996, "blue", 300_000)])
    
    def test_delete_vehicle(self):
        empty_database()
        add_vehicle_to_db("BMW","320", 1996, "blue", 300_000)
        delete_vehicle_from_db(0)
        self.assertEqual(get_database(), [])
    
    def test_view_vehicle(self):
        empty_database()
        add_vehicle_to_db("BMW", "320", 1996, "blue", 300_000)
        vehicle_data = view_vehicle_from_db(0)
        self.assertEqual(vehicle_data[0],"BMW")
        self.assertEqual(vehicle_data[1], "320")
        self.assertEqual(vehicle_data[2], 1996)
        self.assertEqual(vehicle_data[3], "blue")
        self.assertEqual(vehicle_data[4], 300_000) 
        

if __name__ == '__main__':
    unittest.main()

