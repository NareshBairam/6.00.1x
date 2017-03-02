class Message(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        lower_keys = list(string.ascii_lowercase)
        lower_values = list(string.ascii_lowercase)
        shift_lower_values = lower_values[shift:] + lower_values[:shift]
        
        upper_keys = list(string.ascii_uppercase)                 
        upper_values = list(string.ascii_uppercase)
        upper_shift_values = upper_values[shift:] + upper_values[:shift]

        full_keys = lower_keys + upper_keys
        full_values = shift_lower_values + upper_shift_values

        self.shift_dict = dict(zip(full_keys, full_values))
        return self.shift_dict        

    def apply_shift(self, shift):
        new_msg = []
        for i in self.message_text:
            if i not in self.build_shift_dict(shift).keys():
                new_msg.append(i)
                continue
            else:
                new_msg.append(self.build_shift_dict(shift)[i])
        return ''.join(new_msg)