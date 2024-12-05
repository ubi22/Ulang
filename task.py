import random

from base.authorization import authorization_admin

pb = authorization_admin()

def random_word():
    id_word = random.choice(pb.collection("baseword").get_full_list()).id # getting a random word id
    return pb.collection("baseword").get_one(id_word) # returning all the word data



random_word()
