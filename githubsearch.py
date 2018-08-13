#!/usr/bin/env python2.7
import os
import json
import requests


def main():
        print("++++++   github issues retrieval  ++++++ ")
        print("++++++   print the first 30 issues in Github for a certain topic  ++++++ ")

        topic_string = raw_input("Please,insert the topic that you want to explore in github\t");
        print("++++++   credentials   ++++++ ")
        account_name= raw_input("Please, insert your user name in Github\t");
        password = raw_input("Please, insert your password in Github\t");

        r = requests.get('https://api.github.com/search/repositories?q=topic:' + topic_string);
        
        data = r.json();
        repos = data["items"];
        logins =  [x["owner"]["login"] for x in repos];
        repo_names = [x["name"]  for x in repos];

        owners = []

        for i in range(len(repos)):
                owners.append(str(logins[i] + "/" + repo_names[i]));

 
        print("produced and input of " + str(len(owners)) + " pairs of author/owner using the topic " + topic_string);
       
        ''' skeleton of the json document ''' 
        JSON_DATA = """ {
        "issues" : {
        },
        "top_day": {
                "day": "value",
                "occurences" : {

                }
        }
        }"""


        data_vault=[];
        data_vault2 = {};
        items =[]
        ids = []
        state = []
        titles = []
        created_at = []
        repositories = [];
        for x in owners[0:10:1]:
                r = requests.get('https://api.github.com/search/issues?q=repo:' + x,auth=(account_name,password));
                data = r.json();
                items = items + data["items"]
                ids = ids + [ x["id"] for x in items ];
                state = state + [ x["state"] for x in items ];
                titles = titles + [ x["title"] for x in items ];
                repositories = repositories + [ x["repository_url"] for x in items ];
                created_at = created_at + [ x["created_at"] for x in items ];

        elements = [];


        for i in range(0,len(ids)):
                my_elem = dict();
                my_elem["created_at"] = created_at[i];
                my_elem["state"] = state[i];
                my_elem["title"] = titles[i];
                my_elem["repository"] = repositories[i];          
                my_elem["id"] = ids[i];
                elements.append(my_elem);

        elements.sort(reverse=False);


        handle_data = json.loads(JSON_DATA);
        my_dict = dict(handle_data);
        my_dict["issues"] = elements;
        days = [elements[i]["created_at"] for i in range(0,len(elements))];
        days= [ x[0:10:1] for x in created_at];
        occurences = [x for x in days if days.count(x) > 1]
        my_dict["top_day"]["day"]= max(occurences);
       
        counter = days.count(max(occurences));
        owner = {};
        print(counter);
        for i in range(0,len(elements)):
                if days[i] == max(occurences):
                        repo_name = repositories[i].split('https://api.github.com/repos/')[1];
                        repo_name = repo_name.encode('ascii','ignore');
                        print("printout repository");
                        owner[repo_name] = counter;
                        print(owner); 
                        my_dict["top_day"]["occurences"]= owner;
                        break;
 
     
        print(json.dumps(my_dict, sort_keys=True, indent=4));

       

if __name__ == "__main__":
        main();
