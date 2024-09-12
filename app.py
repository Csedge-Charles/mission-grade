from flask import Flask, render_template, request, url_for, redirect
import func

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def homepage():
    if request.method == 'POST':    
        if request.form['gradegpa'] == 'Chemistry':
            return redirect('/chemistry', code=302)
        if request.form['gradegpa'] == 'PreCalculus':
            return redirect('/precalculus', code=302)

    return render_template('index.html', sign=True)



@app.route('/chemistry', methods=['POST', 'GET'])

def hello():
    if request.method == 'POST':
        if request.form['submit'] == 'Back':
            return redirect('/', code=302)
        if request.form['submit'] == 'PreCalculus':
            return redirect('/precalculus', code=302)
        if request.form['submit'] == 'Chemistry':
            return render_template('gradecalc.html')
        grade1 = request.form['firstrow']
        grade2 = request.form['secondrow']
        grade3 = request.form['thirdrow']

        
        value1 = grade1
        value3 = grade2
        value5 = grade3
        
        weight1 = 55
        weight2 = 35
        weight3 = 10
        
        if grade1 == '':
            grade1 = 2
            weight1 = 0
        if grade2 == '':
            grade2 = 2
            weight2 = 0
        if grade3 == '':
            grade3 = 2
            weight3 = 0


        
        grade1 = float(grade1)
        grade2 = float(grade2)
        grade3 = float(grade3)



        
        final_grade = float(func.grade_calculator(grade1, weight1, grade2, weight2, grade3, weight3, 0, 0, 0, 0, 0, 0, 0, 0))
        letter = '&'
        if final_grade >= 89:
            letter = 'A'
        if final_grade >= 79 and final_grade < 89:
            letter = 'B'
        
        if final_grade >= 69 and final_grade < 79:
            letter = 'C'
        if final_grade >= 59 and final_grade < 69:
            letter = 'D'
        if final_grade < 59:
            letter = 'F'
        
            
        
    
        
        return render_template('gradecalc.html', result=str(final_grade) + '%', letter=letter, 
                               value1=value1, value3=value3,  value5=value5)
    return render_template('gradecalc.html')

@app.route('/precalculus', methods=['POST', 'GET'])
def gpa():
    if request.method == 'POST':
        if request.form['submit'] == 'Back':
            return redirect('/', code=302)
        if request.form['submit'] == 'Chemistry':
            return redirect('/chemistry', code=302)
        if request.form['submit'] == 'PreCalculus':
            return render_template('precalc.html')
        
        weight = 25
        grade1 = request.form['firstrow']
        grade2 = request.form['secondrow']
        grade3 = request.form['thirdrow']

        
        value1 = grade1
        value3 = grade2
        value5 = grade3
        
        weight1 = 60
        weight2 = 15
        weight3 = 25
        
        if grade1 == '':
            grade1 = 2
            weight1 = 0
        if grade2 == '':
            grade2 = 2
            weight2 = 0
        if grade3 == '':
            grade3 = 2
            weight3 = 0


        
        grade1 = float(grade1)
        grade2 = float(grade2)
        grade3 = float(grade3)



        
        final_grade = float(func.grade_calculator(grade1, weight1, grade2, weight2, grade3, weight3, 0, 0, 0, 0, 0, 0, 0, 0))
        letter = ''
        if final_grade == 100:
            letter = 'A+'
        if final_grade >= 93 and final_grade < 100:
            letter = 'A'
        
        if final_grade >= 90 and final_grade < 93:
            letter = 'A-'
        if final_grade >= 87 and final_grade < 90:
            letter = 'B+'
        if final_grade >= 83 and final_grade < 87:
            letter = 'B'
        if final_grade >= 80 and final_grade < 83:
            letter = 'B-'
            
        if final_grade >= 77 and final_grade < 80:
            letter = 'C+'
        if final_grade >= 73 and final_grade < 77:
            letter = 'C'
        if final_grade >= 70 and final_grade < 73:
            letter = 'C-'

        if final_grade >= 67 and final_grade < 70:
            letter = 'D+'
        if final_grade >= 63 and final_grade < 67:
            letter = 'D'
        if final_grade >= 60 and final_grade < 63:
            letter = 'D-'
            
        if final_grade < 60:
            letter = 'F'
        
        
            
        
    
        
        return render_template('precalc.html', result=str(final_grade) + '%', letter=letter, 
                               value1=value1, value3=value3,  value5=value5)
    return render_template('precalc.html')
    
    








if __name__ == '__main__':
    app.run(host='0.0.0.0', port=82, debug=True)