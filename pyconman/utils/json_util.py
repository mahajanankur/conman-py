class JsonUtils:
    @staticmethod
    def merge_json(json1, json2):
        # Recursively merges two JSON objects
        if isinstance(json1, dict) and isinstance(json2, dict):
            merged = json1.copy()
            for key, value in json2.items():
                if key in merged:
                    merged[key] = JsonUtils.merge_json(merged[key], value)
                else:
                    merged[key] = value
            return merged
        else:
            return json2