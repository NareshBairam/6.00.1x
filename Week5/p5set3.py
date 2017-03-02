class CiphertextMessage(Message):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        word_counter = 0
        max_count = 0
        for i in range(26):
            for j in list(super(CiphertextMessage, self).apply_shift(i).split(' ')):
                if is_word(self.valid_words, j):
                    word_counter += 1
                if word_counter > max_count:
                    max_count = word_counter
                    shift_value = i
                    decrypted_msg = super(CiphertextMessage, self).apply_shift(i)
                        
        return (shift_value, decrypted_msg)