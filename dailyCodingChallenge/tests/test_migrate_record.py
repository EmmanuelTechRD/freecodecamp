import unittest
from migrate_record import migrate_record

class TestMigrateRecord(unittest.TestCase):
    
    def test_fill_missing_properties(self):
        obj1 = {"id": 1, "role": "admin", "status": "active"}
        obj2 = {"id": 1, "status": "pending"}

        expected = {"id": 1, "role": "admin", "status": "pending"}
        self.assertEqual(migrate_record(obj1, obj2), expected)

    def test_no_missing_properties(self):
        obj1 = {"theme": "dark"}
        obj2 = {"theme": "light", "notifications": False}

        expected = {"theme": "light", "notifications": False}
        self.assertEqual(migrate_record(obj1, obj2), expected)

    def test_completely_empty_target(self):
        obj1 = {"name": "Emmanuel", "age": 21}
        obj2 = {}

        expected = {"name": "Emmanuel", "age": 21}
        self.assertEqual(migrate_record(obj1, obj2), expected)

    def test_preserve_none_values(self):
        obj1 = {"bio": "Software Engineer"}
        obj2 = {"bio": None}

        expected = {"bio": None}
        self.assertEqual(migrate_record(obj1, obj2), expected)

if __name__ == '__main__':
    unittest.main()