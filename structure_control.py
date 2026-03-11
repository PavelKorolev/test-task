import get_json

required_fields = { "name", "location", "year_founded", "country", "author", "condition", "type" }


def structure_control(input):
    for key in required_fields:
        if key not in input:
            print ("Invalid parameters in JSON")
            return None

    return input