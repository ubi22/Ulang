from authorization import authorization_admin

pb = authorization_admin()

def create_couple(text):
    text = text.split(") (")
    for i in text: #(a,один) (able,способный) (about,о)
        data = i.split(",")
        print(pb.collection("baseword").create(
            {
                "english_word": data[0],
                "russian_word": data[1]
            }
        ))


create_couple(input())