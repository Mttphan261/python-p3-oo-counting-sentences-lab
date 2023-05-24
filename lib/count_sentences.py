#!/usr/bin/env python3


class MyString:

    def __init__(self, value=''):
        self.value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        if type(value) is str:
            self._value = value
        else:
            print('The value must be a string.')

    value = property(get_value, set_value)

    def is_sentence(self):
        if self.value.endswith('.'):
            return True
        else:
            return False

    def is_question(self):
        if self.value.endswith('?'):
            return True
        else:
            return False

    def is_exclamation(self):
        if self.value.endswith('!'):
            return True
        else:
            return False

    def count_sentences(self):
        
        sentence_count = 0
        for each in self.value.split():
            if each.endswith('.') or each.endswith('!') or each.endswith('?'):
                sentence_count += 1

        return sentence_count






# test_string = MyString(
#     "This, well, is a sentence. This is too!! And so is this, I think? Woo..")

# test_string.count_sentences()
