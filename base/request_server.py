from base.authorization import authorization_admin

pb = authorization_admin()



class Full_list():
    def groups(self):
        return pb.collection("group").get_full_list()

    def words(self=''):
        return pb.collection("baseword").get_full_list()

class One_record:
    def base_word(self, id_word):
        return pb.collection("baseword").get_one(id_word)

    def group(self, id_group):
        return pb.collection("group").get_one(id_group)

full_list = Full_list()
one_record = One_record()

