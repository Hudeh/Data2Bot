import json
import os

def generate_schema(data):
  """generate the schema of the given JSON file.

  Args:
    json_data: A JSON data.

  Returns:
    A dictionary representing the JSON schema.
  """
  def sniff_data_type(value):
      if isinstance(value, str):
          return "string"
      elif isinstance(value, int):
          return "integer"
      elif isinstance(value, bool):
          return "boolean"
      elif isinstance(value, list):
          if all(isinstance(item, str) for item in value):
              return "enum"
          elif all(isinstance(item, dict) for item in value):
              return "array"
      return "unknown"

  def pad_attribute(attribute_name):
    """ return schem format """
    return {
        "tag": "",
        "description": "",
        "required": False,
        "type": attribute_type
    }

  schema = {}

  message_data = data.get("message", {})
  for attribute, value in message_data.items():
      attribute_type = sniff_data_type(value)
      schema[attribute] = pad_attribute(attribute)

  return schema

def process_json_file(input_path, output_dir):
  """ process the file for the input path and output directory """
  with open(input_path, "r") as file:
      input_data = json.load(file)

  schema = generate_schema(input_data)

  output_file = os.path.join(output_dir, os.path.basename(input_path).replace(".json", "_schema.json"))

  with open(output_file, "w") as file:
      json.dump(schema, file, indent=4)

# run code with give input
if __name__ == "__main__":
    input_dir = "./data"
    output_dir = "./schema"

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            input_path = os.path.join(input_dir, filename)
            process_json_file(input_path, output_dir)
