class Anagram:
    def __init__(self, word):
        self.word = word
        
    # def match(self, anagram_list):
    #     match_list = []
    #     for item in anagram_list:
    #         is_anagram = True
    #         for char in item:
    #             if char not in self.word:
    #                 is_anagram = False
    #                 break
    #         if is_anagram:
    #             match_list.append(item)
    #     return match_list
    
    # def match(self, anagram_list):
    #     match_list = []
    #     for item in anagram_list:
    #         is_anagram = set(item) == set(self.word)
    #         if is_anagram:
    #             match_list.append(item)
    #     return match_list
    
    def match(self, anagram_list):
        return [item for item in anagram_list if set(item) == set(self.word)]