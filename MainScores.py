print("@@@@\nimporting flask\n@@@@")
from flask import Flask, render_template
from Utils import SCORES_FILE_NAME

print("@@@@\napp = Flask\n@@@@")
app = Flask(__name__)
print("@@@@\nopening score file\n@@@@")
score_file = open(SCORES_FILE_NAME, 'r')
score = score_file.read()


@app.route('/')
def index():
    print("@@@@\nstarting main method\n@@@")
    try:
        print("@@@@\ntrying\n@@@@")
        # return 'hello world'
        return render_template('Score_Show.html', SCORE=int(score))
    except:
        print("@@@@\nexcept\n@@@@")
        return render_template('Score_Error.html')


if __name__ == '__main__':
    print("@@@@\nname = main\n@@@@")
    app.run(host='0.0.0.0', debug=True)
