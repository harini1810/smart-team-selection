from flask import Flask, render_template,request,session,url_for,redirect
import chat
import sqlite3
from genetic import genetic_algo
from graph_gen import graph

app = Flask(__name__)

app.secret_key='abc@123'

@app.route('/')
def home():
    try:
        if session['loggedin']==True:
            return render_template('logout.html')
        else:
            return render_template('index.html')
    except:
        return render_template('index.html') 

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/service')
def service():
    return render_template("service.html")


@app.route('/login', methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'pass' in request.form:
        mail=str(request.form['username'])
        pasw=str(request.form['pass'])
        connection=sqlite3.connect('Customers.db')
        cursor=connection.cursor()
        cursor.execute("SELECT NAME,MAIL,PWD FROM CUSTOMER WHERE MAIL = ? and PWD = ?;",(mail,pasw))
        row=cursor.fetchall()
        if len(row)==1:
            session['loggedin'] = True
            session['name']=row[0][0]
            session['mail']=row[0][1]
            return render_template('proj.html')
        else:
            msg='incorrect login credentials! please recheck'
    return render_template('login.html')

@app.route("/signup", methods=["GET","POST"])
def signup():
    msg=''
    if request.method == 'POST':
        name=str(request.form['name'])
        mail=str(request.form['mail'])
        ph=int(request.form['phone'])
        pasw=str(request.form['pass'])
        if len(name)<15:
            if len(mail)<25:
                if '@gmail.com'in mail:
                    if len(str(ph))==10:
                        if len(pasw)<15:
                            connection=sqlite3.connect('Customers.db')
                            cursor=connection.cursor()
                            cursor.execute("SELECT NAME,MAIL,PwD FROM CUSTOMER WHERE MAIL = ?;",(mail,))
                            row=cursor.fetchall()
                            connection.commit()
                            if len(row)==0:
                                cursor.execute('''INSERT INTO CUSTOMER VALUES(?,?,?,?);''',(name,mail,ph,pasw))
                                connection.commit()
                                msg='registered successfully!'
                                session['loggedin'] = True
                                session['name']=name
                                session['mail']=mail
                                return render_template('proj.html')
                            else:
                                msg='          user already found,please sign in!'
                        else:
                            msg='         password length should be within 8 characters!'
                    else:
                        msg='          enter a valid phone number!'
                else:
                    msg='         email id should contain @gmail.com!'
            else:
                msg='          email-id too long!'
        else:
            msg='         name is more than the limit of 14 letters!'
    return render_template('signup.html')

@app.route("/proj1", methods=["GET","POST"])
def proj1():
    return render_template('proj1.html')

@app.route('/chat', methods = ['GET', 'POST'])
def chat_route():

    
    
    
            if request.method == 'POST':
                query = request.form.get('query')  # Get the search query from the form
                print(f"User Query: {query}")
                result = chat.chat(query)  # Pass the query to the chat function
                return render_template('chat.html', value=result)
            else:
                
                pass
            return render_template('chat.html') 

@app.route("/remove", methods=["GET","POST"])
def remove():
    msg=''
    if request.method=="POST":
        empname=request.form['empname']
        empid=request.form['empid']
        connection=sqlite3.connect('Customers.db')
        cursor=connection.cursor()
        cursor.execute("DELETE from EMPLOYEE where Name=? and ID=?;",(empname,empid,))
        return render_template('proj.html')
    return render_template('remove.html')

@app.route('/logout')
def logout():
    session['loggedin']=False
    return render_template('index.html')

@app.route('/result', methods=["GET","POST"])
def result():
    if request.method == 'POST':
        skills = request.form.getlist('skills')
        total=['JAVA','PYTHON','JAVASCRIPT','HTML','CSS','DJANGO','CPP','MONGODB','PHP','NODEJS','REACT','ANGULARJS','DSA','FLASK','MYSQL']
        skills_dict = {skill: 1 for skill in total if skill in skills}
        for skill in total:
            if skill not in skills:
                skills_dict[skill]=0
        print(skills_dict)
        connection=sqlite3.connect('Customers.db')
        cursor=connection.cursor()
        cursor.execute("SELECT NAME,JAVA,PYTHON,JAVASCRIPT,HTML,CSS,DJANGO,CPP,MONGODB,PHP,NODEJS,REACT,ANGULARJS,DSA,FLASK,MYSQL,ID FROM EMPLOYEE WHERE COMPANY = ?;",(session['name'],))
        row=cursor.fetchall()
        connection.commit()
        teamsize=int(request.form['teamsize'])
        employees={}
        for i in range (len(row)):
            employees[(row[i][0],row[i][16])]={'JAVA':row[i][1],'PYTHON':row[i][2],'JAVASCRIPT':row[i][3],'HTML':row[i][4],'CSS':row[i][5],'DJANGO':row[i][6],'CPP':row[i][7],'MONGODB':row[i][8],'PHP':row[i][9],'NODEJS':row[i][10],'REACT':row[i][11],'ANGULARJS':row[i][12],'DSA':row[i][13],'FLASK':row[i][14],'MYSQL':row[i][15]}
        solution=genetic_algo(skills_dict,employees,teamsize)
        skilltotal=['JAVA','PYTHON','JAVASCRIPT','HTML','CSS','DJANGO','CPP','MONGODB','PHP','NODEJS','REACT','ANGULARJS','DSA','FLASK','MYSQL']
        selected_skill=[]
        corresponding_skill=[]

        list1=[i for i in skills_dict if skills_dict[i]==1]


        for emp in solution:
            cursor.execute("SELECT JAVA,PYTHON,JAVASCRIPT,HTML,CSS,DJANGO,CPP,MONGODB,PHP,NODEJS,REACT,ANGULARJS,DSA,FLASK,MYSQL,ID FROM EMPLOYEE WHERE ID= ?;",(emp[1],))
            rows=cursor.fetchall()
            skillset=[skilltotal[i] for i in range(len(rows[0])) if rows[0][i]==1]
            matched_skill=[i for i in skillset if i in list1]
            corresponding_skill.append(len(matched_skill))
            selected_skill.extend(skillset)
            
        connection.commit()
        
        employees_list=[i[0] for i in solution]

        graph(list1,selected_skill,corresponding_skill,employees_list)
        return render_template('result.html', solution=solution)
    return render_template('proj1.html')

@app.route('/empadd', methods=["GET","POST"])
def empadd():
    if request.method == 'POST':
        empname=request.form['empname']
        empid=request.form['empid']
        company=session['name']
        empmail=request.form['mail']
        skills = request.form.getlist('skills')
        total=['JAVA','PYTHON','JAVASCRIPT','HTML','CSS','DJANGO','CPP','MONGODB','PHP','NODEJS','REACT','ANGULARJS','DSA','FLASK','MYSQL']
        skills_dict = {skill: 1 for skill in total if skill in skills}
        for skill in total:
            if skill not in skills:
                skills_dict[skill]=0        
        print(skills_dict)
        if len(empname)<15:
            if len(empmail)<25:
                if '@gmail.com'in empmail:
 
                            connection=sqlite3.connect('Customers.db')
                            cursor=connection.cursor()
                            cursor.execute("SELECT NAME,MAIL,COMPANY FROM EMPLOYEE WHERE ID = ?;",(empid,))
                            row=cursor.fetchall()
                            connection.commit()
                            if len(row)==0:
                                cursor.execute('''INSERT INTO EMPLOYEE VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);''',(empname,empmail,company,empid,skills_dict['JAVA'],skills_dict['PYTHON'],skills_dict['JAVASCRIPT'],skills_dict['HTML'],skills_dict['CSS'],skills_dict['DJANGO'],skills_dict['CPP'],skills_dict['MONGODB'],skills_dict['PHP'],skills_dict['NODEJS'],skills_dict['REACT'],skills_dict['ANGULARJS'],skills_dict['DSA'],skills_dict['FLASK'],skills_dict['MYSQL']))
                                connection.commit()
                                msg='registered successfully!'
                                
                                return render_template('proj.html')
                            else:
                                msg='          user already found,please sign in!'
                else:
                    msg='         email id should contain @gmail.com!'
            else:
                msg='          email-id too long!'
        else:
            msg='         name is more than the limit of 14 letters!'
    return render_template('empadd.html')

if __name__=="__main__":
    app.run(debug=True)