### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

Python syntax is simpler and has tons of libraries that are easy to use. Javascript runs on a browser.

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.

```python
test_dict = {'a': 1, "b": 2}
c = test_dict.get('c')
```

```python
test_dict = {'a': 1, "b": 2}
try:
  c = test_dict['c']
except KeyError:
  print("key not found")
```

- What is a unit test?

A test that only tests one apsect.

- What is an integration test?

A test that tests multiple working parts.

- What is the role of web application framework, like Flask?

Back-end server logic. Get and post requests.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

The route URL is more like the subject of a page while the URL query is more like extra info. Query usually comes from a form.

- How do you collect data from a URL placeholder parameter using Flask?

```python
@app.route('/post/<data>')
def show_page(data):
  # code
```

- How do you collect data from the query string using Flask?

```python
request.args['parameter']
request.args.get('parameter')
```

- How do you collect data from the body of the request using Flask?

```python
request.data
```

- What is a cookie and what kinds of things are they commonly used for?

cookies are key value pairs saved on a browser to keep track of things like logged in status and other information that websites use.

- What is the session object in Flask?

It is data saved on the server using cookies and is unreadable to humans.

- What does Flask's `jsonify()` do?

converts the request data into json for use with javascript.

```

```
