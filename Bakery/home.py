from flask import Flask,render_template,redirect,url_for,request,session
app = Flask(__name__)
app.secret_key="administrator"
c=False
@app.route("/")
def home():
	b=["Cookies","Cakes","Desserts"]
	cookies=[["Chocolate Chip","Oatmeal Raisin","Shortbread","Peanut Butte"],["Butter Cake","Pound Cake","Sponge Cake","Genoise Cake"],["Frozen desserts","Pastries","Custards","Puddings"]]
	img1=[[url_for('static',filename="img/imgc1.jpg"),url_for('static',filename="img/imgc2.jpg"),url_for('static',filename="img/imgc3.jpg"),url_for('static',filename="img/imgc4.jpg")],[url_for('static',filename="img/imgca1.jpg"),url_for('static',filename="img/imgca2.jpg"),url_for('static',filename="img/imgca3.jpg"),url_for('static',filename="img/imgca4.jpg")],[url_for('static',filename="img/imgd1.jpg"),url_for('static',filename="img/imgd2.jpg"),url_for('static',filename="img/imgd3.jpg"),url_for('static',filename="img/imgd4.jpg")]]

	#cakes=["Butter Cake","Pound Cake","Sponge Cake","Genoise Cake"]
	#img2=[url_for('static',filename="img/imgca1.jpg"),url_for('static',filename="img/imgca2.jpg"),url_for('static',filename="img/imgca3.jpg"),url_for('static',filename="img/imgca4.jpg")]

	#desserts=["Frozen desserts","Pastries","Custards","Puddings"]
	#img3=[url_for('static',filename="img/imgd1.jpg"),url_for('static',filename="img/imgd2.jpg"),url_for('static',filename="img/imgd3.jpg"),url_for('static',filename="img/imgde4.jpg")]

	return render_template("index.html",cook=cookies,img=img1,l=b)
@app.route("/userup")
def signup():
	return render_template("signup.html")
	


@app.route("/userin")
def login():

	return render_template("login.html")
	


if __name__=="__main__":
	app.run(debug=True)