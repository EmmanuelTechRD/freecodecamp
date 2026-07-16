import unittest
from migrate_record import migrate_record

class TestMigrateRecord(unittest.TestCase):
    
    def test_fill_missing_properties(self):
        obj1 = {"id": 1, "role": "admin", "status": "active"}
        obj2 = {"id": 1, "status": "pending"}

        expected = {"id": 1, "role": "admin", "status": "pending"}
        self.assertEqual(migrate_record(obj1, obj2), expected)

if __name__ == '__main__':
    unittest.main()