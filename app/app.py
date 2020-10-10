from flask import Flask, render_template, request, redirect, jsonify
import json
import requests
app = Flask(__name__)
s = ""
j = {"data": ""}


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":

        return render_template("index.html")
    else:

        x = request.form.get("creditscore")
        s = str(x)
        x = request.form.get("geography")
        s = s+","+str(x)
        x = request.form.get("gender")
        s = s+","+str(x)
        x = request.form.get("age")
        s = s+","+str(x)
        x = request.form.get("tenure")
        s = s+","+str(x)
        x = request.form.get("balance")
        s = s+","+str(x)
        x = request.form.get("products")
        s = s+","+str(x)
        x = request.form.get("hascredit")
        s = s+","+str(x)
        x = request.form.get("activemember")
        s = s+","+str(x)
        x = request.form.get("salary")
        s = s+","+str(x)

        print(s)
        j = {"data": s}
        print(type(j))
        print(j)

        j = json.dumps(j, indent=4)
        headers = {
            'Content-Type': 'application/json',
            'X-Amz-Content-Sha256': '043e156820c0122ed0469c8aa6b997f36722dd56aecb29c788a6fa673ed10f6f',
            'X-Amz-Security-Token': 'FwoGZXIvYXdzEDkaDLRl1csLGAfylY4umiLLAVrOx7HVPITEeaxF551hXadtzwH35l9eQNdhOyhkfRKuReRJbcmWSmV8tLiYpiPW6WP1yWOnC87NcBG0MbZQPTU7GmVKG8iHf6a0HhpIpCgxH39d+rUUqBbKqujVMVspgqN1sKl/Wu2kt+rjva33qJNJXiGfhocsqvMh0zyRFWesfT8iceCCOWcGnK20j/oMmx3VeOZSyfBfk31s16qWGlBS21b+KyLcvkoz0obodDtYYta3zXLiI2Pzf5Ojfsg2Kq77cccv2w7eA61FKMWth/wFMi1sYoj+eVWJDmrP/AOMEOaQtWYPkWp7zsAkgW6be4jVpYOlAaKBRwM1u6fBECg =',
            'X-Amz-Date': '20201010T203801Z',
            'Authorization': 'AWS4-HMAC-SHA256 Credential=ASIAXFLZARECKCGOG4CG/20201010/us-east-1/execute-api/aws4_request, SignedHeaders=content-type;host;x-amz-content-sha256;x-amz-date;x-amz-security-token, Signature=55394f11ce71cbf7f9c01420bb45b100717523cdb4b3582a09df133ea84f9c6b'
        }
        r = requests.post(
            'https://i21uuqbl2i.execute-api.us-east-1.amazonaws.com/test/predict', headers=headers, data=j)
        print(r)
        if r.text == '1':
            res = "Yes, the customer is likely to leave"
        else:
            res = "No, the customer is unlikely to leave"
        print(r.text)
        return render_template("predict.html", res=res)


if __name__ == '__main__':
    app.run(debug=True)
