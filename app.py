from flask import Flask,request,render_template
from whois import whois

app = Flask(__name__)

def format_date(date_obj):
    if date_obj == None or isinstance(date_obj, str):
        return date_obj
    def get_ordinal(n):
        suffix = "th" if 11 <= n % 100 <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
        return f"{n}{suffix}"

    if isinstance(date_obj, list):
        formatted_dates = [f"{get_ordinal(date.day)} {date.strftime('%B %Y')}" for date in date_obj]
        return ', '.join(formatted_dates)
    else:
        return f"{get_ordinal(date_obj.day)} {date_obj.strftime('%B %Y')}"

@app.route("/",methods=["GET"]) #homepage
def home():
    r = render_template("index.html",title="whois",description="Lookup domains and IP Addresses.")
    return r

@app.route("/lookup",methods=["POST"]) # this end point is used by the form in the home page to post domain or IP-address
def lookup():
    query = request.form["query"]
    try:
        result = whois(query)
    except:
        return render_template("error.html",error=f"{query} doesn't exist.",title="Invalid Input")
    return render_template("details.html", exp=format_date(result["expiration_date"]), code=result.text)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
