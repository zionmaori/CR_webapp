import json

try:
    p = ""
    tbl = "<tr><th>First Name</th><th>Last Name</th><th>UserName</th><th>Password</th></tr>"
    p+=(tbl)

    with open('users.json') as f:
            data = [json.loads(line) for line in f]
    sorted_data = sorted(data, key=lambda d: d['firstname'])
    print(sorted_data)
  
    for records in data[0:]:
        firstname = (records['firstname'].capitalize())
        lastname = (records['lastname'].capitalize())
        usrname = (records['username'])
        password = '*' * len((records['password']))
        
        p+="<tr>"
        p+="<td>" + firstname + "</td> \n" + "<td>" + lastname + "</td>" +"<td>" + usrname + "</td>" +"<td>" + password + "</td>" 
        p+="</tr>"


    contents = '''
        <html>
        <head>
        <style>
        table
        </style>
        <title>CR records</title>
        </head>
        <body>
        <table border='1' style="border-collapse:collapse;">
        {}
        </table>
        </body>
        </html>
        '''.format(p)
    
    

except Exception as e:
    print("Error reading data from MySQL table", e)
    import traceback ; traceback.print_exc()

finally:
    webfile='index.html'
    with open(webfile, "w") as weboutput:
        weboutput.write(contents)