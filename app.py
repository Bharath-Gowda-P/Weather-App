from flask import Flask, render_template, request
import requests 


app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def search():
    url = 'http://api.openweathermap.org/data/2.5//weather?q={}&units=metric&appid=a1aa59589cbd9247c0f8c239c8e758bd'
    city = request.form.get('city')
    r = requests.get(url.format(city)).json()

    weather = {
        'city': city,
        'description': r['weather'][0]['description'],
        'temp': r['main']['temp'],
        'humidity': r['main']['humidity'],
        'country': r['sys']['country']
    }



    return render_template('search.html', weather=weather)




if __name__ == '__main__':
    app.run(debug=False)











































"""
This is a comment
written in
a
a
a

a
a
a

a
a

aaa

aa
a
This comment is used to ignore the html file for github tags
so yeah 
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

a
a
a
aa
a

a

a
a
more than just one line
"""