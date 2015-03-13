import urllib2
import json
import time

from webapp import app
@app.route('/search/<string:keyword>')
@app.route('/search/<string:keyword>/<int:maxcount>')
def search(keyword,maxcount=10):
  url = ""
  param_start = ""
  betterResults = {}

  for i in range(0, maxcount+1, 10):
    if i > 0:
      param_start = "&start=%d" % (i)
    query = 'q=' + keyword
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s%s'  % (query, param_start)
    results = urllib2.urlopen(url)
    resultsjson = json.loads(results.read())
    betterResults.update({url: str(resultsjson["responseData"])})
    time.sleep(2)

  return json.dumps(betterResults, indent=2,
          sort_keys=True)


