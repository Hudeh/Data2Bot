import os
import unittest

from main import generate_schema, process_json_file

class TestSchemaGeneration(unittest.TestCase):
    def setUp(self):
        self.input_dir = "./data"
        self.output_dir = "./schema"

    def test_generate_schema_string(self):
        data = {
            "message": {
                "attribute_string": "Test String"
            }
        }
        schema = generate_schema(data)
        self.assertEqual(schema["attribute_string"]["type"], "string")

    def test_generate_schema_integer(self):
        data = {
            "message": {
                "attribute_integer": 123
            }
        }
        schema = generate_schema(data)
        self.assertEqual(schema["attribute_integer"]["type"], "integer")

    def test_generate_schema_enum(self):
        data = {
            "message": {
                "attribute_enum": ["Option1", "Option2"]
            }
        }
        schema = generate_schema(data)
        self.assertEqual(schema["attribute_enum"]["type"], "enum")

    def test_generate_schema_array(self):
        data = {
            "message": {
                "attribute_array": [{"sub_attr": "value"}]
            }
        }
        schema = generate_schema(data)
        self.assertEqual(schema["attribute_array"]["type"], "array")

    def test_process_json_file(self):
        input_file = os.path.join(self.input_dir, "test_data.json")
        output_file = os.path.join(self.output_dir, "test_data_schema.json")
        process_json_file(input_file, self.output_dir)
        self.assertTrue(os.path.exists(output_file))

    def tearDown(self):
        for filename in os.listdir(self.output_dir):
            if filename.endswith("_schema.json"):
                file_path = os.path.join(self.output_dir, filename)
                os.remove(file_path)

if __name__ == "__main__":
    unittest.main()
