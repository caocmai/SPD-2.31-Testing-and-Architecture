# Debug Log

**Explain how you used the the techniques covered (Trace Forward, Trace Backward, Divide & Conquer) to uncover the bugs in each exercise. Be specific!**

In your explanations, you may want to answer:

- What is the expected vs. actual output?
- If there is a stack trace, what useful information does it contain?
- Which technique did you use, on which line numbers?
- What assumptions did you have about each line of code, and which ones were proven to be wrong?

_Example: I noticed that the program should show pizza orders once a new order is made, and that it wasn't showing any. So, I used the trace forward technique starting on line 13. I discovered the bug on line 27 was caused by a typo of 'pzza' instead of 'pizza'._

_Then I noticed another bug ..._

## Exercise 1

Bugs:

Naming of varible not the same when using in PizzaTopping. Inorder to use a property
the naming must be the same

The rerfriect url_for route uses redirect(url_for('/')) instead of redirect(url_for('home'))

Had to change the form.get() names because didn't match with the form in template

Had to had the db.session.commit(), missing to save to db

Change get to getList when want multiple items from form for the toppings_list

Change the loop to toppings_list instead of PizzaTopping.


## Exercise 2

Change the request.args.get to match the template's names. 

Change the url route to ave an added "?"

Change the parameter naming to "q" instead of city name

Change context dictionary temp to be "temp" instead of "temperature"

## Exercise 3

[[Your answer goes here!]]
