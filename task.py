import random
from base.request_server import full_list, one_record


class Word:
    # id_word = random.choice(full_list.groups()).id  # getting a random word id
    def is_group(self, id_group:str):
        return one_record.group(id_group).field
    # return pb.collection("baseword").get_one(id_word) # returning all the word data

word = Word()

# print(word.is_group("b5f3k3f0u325cs3"))