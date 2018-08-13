# githubsearch

INSTALLATION 

In Debian9.2 (or Linux in general ) install the python-requests module:      

	*  sudo apt-get install python-requests
 

Run the script stand-alone ./githubsearch.py. Introduce the "topic" of the issues and the credentials of Github. 

	
OBSERVATIONS

About the list "owners" input : in this script, we obtain for evry topic ( e.g "tensorflow" of Google) just 30 results per page: this is a know limitation of Github API for not authorized users . We assume that 30 results in an input list is enough for our scope. 
From the online documentation of Github : "The Search API has a custom rate limit. For requests using Basic Authentication, OAuth, or client ID and secret, you can make up to 30 requests per minute. 
For unauthenticated requests, the rate limit allows you to make up to 10 requests per minute." 
This can be modified in the code using the following request 

 	r = requests.get('API_REQUEST' + topic_string, auth=('USER', 'PASSWD'));

 
