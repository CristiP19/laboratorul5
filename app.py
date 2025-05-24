from flask import Flask, render_template

app = Flask(__name__)

cars = [
    {
        'name': 'Dodge Charger R/T 1970',
        'engine': 'V8 7.2L Supercharged',
        'horsepower': '900+ HP',
        'image': 'https://cars.bonhams.com/_next/image.jpg?url=https%3A%2F%2Fimg2.bonhams.com%2Fimage%3Fsrc%3DImages%2Flive%2F2024-07%2F24%2F25547967-11-32.jpg&w=2400&q=75'  #
    },
    {
        'name': 'Toyota Supra MK IV 1995',
        'engine': '2JZ-GTE 3.0L Twin-Turbo',
        'horsepower': '1000+ HP',
        'image': 'https://media.carsandbids.com/cdn-cgi/image/width=2080,quality=70/f2acd32538fd950f45033f2020f43e44e93f4359/photos/3pX5wvRW-DQ8TF_nyLJ-(edit).jpg?t=169654044693'
    },
    {
        'name': 'Nissan Skyline GT-R R34',
        'engine': 'RB26DETT 2.6L Twin-Turbo',
        'horsepower': '800+ HP',
        'image': 'https://www.octane-magazine.com/app/uploads/2024/06/24_0325_bbl_34_37245_re_re_full.jpg-1160x500.jpg'
    }
]

@app.route('/')
def index():
    return render_template('index.html', cars=cars)

if __name__ == '__main__':
    app.run(debug=True)