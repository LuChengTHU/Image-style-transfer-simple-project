from flask import Flask, request, render_template
from PIL import Image
import os
import evaluate

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))


@app.route('/kalawaqiao', methods=['GET', 'POST'])
def hello_world():
    inputdir = os.path.join(os.path.join(os.path.join(basedir, 'static'),'kalawaqiao'), 'input')
    outputdir = os.path.join(os.path.join(os.path.join(basedir, 'static'), 'kalawaqiao'), 'output')

    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            file = request.files['pic']
            im = Image.open(file)
            print(file.filename)
            (w, h) = im.size
            scale = max(w // 800, h // 760)
            if scale == 0:
                scale = 1
            im = im.resize((w//scale, h//scale), Image.ANTIALIAS)
            filedir = os.path.join(inputdir, file.filename.split('.')[0])
            if not os.path.exists(filedir):
                os.makedirs(filedir)
                filepath = os.path.join(filedir, file.filename)
                im.save(filepath)

            filepath = os.path.join(os.path.join(inputdir, file.filename.split('.')[0]), file.filename)

            resultdir = os.path.join(outputdir, file.filename.split('.')[0])
            if not os.path.exists(resultdir):
                os.makedirs(resultdir)

            evaluate.evaluate(os.path.join(basedir, 'model_kalawaqiao'), filepath, resultdir)

            resultpath = os.path.join(os.path.join(os.path.join(os.path.join('static','kalawaqiao'), 'output'), file.filename.split('.')[0]), file.filename)
            srcpath = os.path.join(os.path.join(os.path.join(os.path.join('static','kalawaqiao'), 'input'), file.filename.split('.')[0]),
                                      file.filename)
            return render_template('result.html', image_result=resultpath)
        except ValueError:
            return 'ValueError', 400

@app.route('/weimier', methods=['GET', 'POST'])
def hello_world2():
    inputdir = os.path.join(os.path.join(os.path.join(basedir, 'static'),'weimier'), 'input')
    outputdir = os.path.join(os.path.join(os.path.join(basedir, 'static'), 'weimier'), 'output')

    if request.method == 'GET':
        return render_template('index2.html')
    else:
        try:
            file = request.files['pic']
            im = Image.open(file)
            (w, h) = im.size
            scale = max(w // 800, h // 760)
            if scale == 0:
                scale = 1
            im = im.resize((w//scale, h//scale), Image.ANTIALIAS)
            filedir = os.path.join(inputdir, file.filename.split('.')[0])
            if not os.path.exists(filedir):
                os.makedirs(filedir)
                filepath = os.path.join(filedir, file.filename)
                im.save(filepath)

            filepath = os.path.join(os.path.join(inputdir, file.filename.split('.')[0]), file.filename)

            resultdir = os.path.join(outputdir, file.filename.split('.')[0])
            if not os.path.exists(resultdir):
                os.makedirs(resultdir)

            evaluate.evaluate(os.path.join(basedir, 'model_weimier'), filepath, resultdir)

            resultpath = os.path.join(os.path.join(os.path.join(os.path.join('static','weimier'), 'output'), file.filename.split('.')[0]), file.filename)
            srcpath = os.path.join(os.path.join(os.path.join(os.path.join('static','weimier'), 'input'), file.filename.split('.')[0]),
                                      file.filename)
            return render_template('result2.html', image_result=resultpath)
        except ValueError:
            return 'ValueError', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
