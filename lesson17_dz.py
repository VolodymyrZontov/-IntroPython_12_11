def sort_by_text(item):
    return len(item["text"].split())

def sort_by_years(item):
    return len(item["text"].split())

def write_json(data, filename, param):
    keys_params = {"text": sort_by_text,
                   "years": sort_by_years}
    sorted_data = sorted(data, key=keys_params[param])

data = []

write_json(data, "test.json", "text")