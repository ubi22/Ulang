from authorization import authorization_admin

pb = authorization_admin()
def delete_base(name_base):
    for i in pb.collection(name_base).get_full_list():
        pb.collection(name_base).delete(i.id)
    print("Succses")

delete_base("baseword")