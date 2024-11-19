import unittest
from app import mongo

class MongoDBTests(unittest.TestCase):

    def test_mongodb_connection(self):
        try:
            result = mongo.cx.admin.command('ping')
            self.assertEqual(result["ok"], 1.0)
        except Exception as e:
            self.fail(f"MongoDB connection failed: {e}")

    def test_mongodb_insert(self):
        test_collection = mongo.db.test_collection
        test_document = {"name": "Test", "value": 123}

        # Insert and verify
        insert_result = test_collection.insert_one(test_document)
        self.assertTrue(insert_result.acknowledged)
        queried_document = test_collection.find_one({"_id": insert_result.inserted_id})
        self.assertIsNotNone(queried_document)

        # Cleanup
        test_collection.delete_one({"_id": insert_result.inserted_id})
