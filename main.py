from flask import render_template
from flask import Flask
from task import word
from base.request_server import full_list, one_record

app = Flask(__name__)

list_word = []

@app.route('/name_group/<id_group>')
def name_group(id_group):
    group = word.is_group(id_group)
    word_remember = one_record.group(id_group)
    for i in group: list_word.append(i)
    return render_template('index.html',
                            link = "/group_word/-1",
                            en_word = word_remember.name_english,
                            ru_word = word_remember.name_russian)

@app.route('/group_word/<index>') # I've been very clever with this function, it's better to rewrite it
def group_word(index):
    index = int(index)
    print(list_word)
    if index+1 == len(list_word):
        groups = full_list.groups()
        list_word.clear()
        return render_template("groups.html", group=groups)
    else:
        words = one_record.base_word(list_word[index+1])
        print(list_word[index+1])
        return render_template('index.html',
                                link = f"/group_word/{index+1}",
                                en_word = words.english_word,
                                ru_word = words.russian_word)

# @app.route('/submit', methods=['POST'])
# def submit():
#
#     return render_template('index.html', en_word=words.english_word, ru_word=words.russian_word)

@app.route('/')
def main():
    groups = full_list.groups()
    # data = []
    # for i in groups:
    #     data.append(one_record.group(i.id))
    return render_template("groups.html", group = groups)

app.run(debug=True)
# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)