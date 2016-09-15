from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
    


@app.route('/summary')
def view_summary():
    
    title_list = [{"name":"IBM","price":15.43,"sentiment_twitter":-0.41},
                {"name":"Apple","price":5.21,"sentiment_twitter":-0.13},
                {"name":"Facebook","price":102.01,"sentiment_twitter":0.62},
                    ]
    #~ title_list = ["IBM", "Apple","Google","Facebook"]
    
    
    return render_template('template_summary.html', title_list=title_list)


    
@app.route('/detail/<title>')
def show_title_detail(title):
    # deatails for a given title
    return 'Title %s' % title


#~ @app.route('/post/<int:post_id>')
#~ def show_post(post_id):
    #~ # show the post with the given id, the id is an integer
    #~ return 'Post %d' % post_id
    
    
if __name__ == "__main__":
    app.run()
    
