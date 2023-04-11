import json
import re


class JsonProcessor:
    def remove_html_tags(self, data):
        regex = re.compile(r'<.*?>')
        return regex.sub(' ', data)

    def process_json(self, json_string):
        dictionary = json.loads(json_string)
        assert len(dictionary) == 6     # make sure we haven't skipped anything

        title = dictionary['title']
        description = self.remove_html_tags(dictionary['description'])
        attributes = '. '.join(dictionary['attributes'])
        
        characteristics = ''
        for key in ['defined_characteristics', 'custom_characteristics', 'filters']:
            for char_key, char_val in dictionary[key].items():
                characteristics += f'{char_key}: ' + ', '.join(char_val) + '. '

        return title, description, attributes, characteristics