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

The expected output for the program is to be able to create a pizza order and have it displayed. 
The acutal output was a bunch of errors and bugs discussed below:

I noticed that the naming of variable were not the same when using in PizzaTopping. Inorder to use a property the naming must be the same

I noticed a routing error when saving it was about routing.
The redirect url_for route uses redirect(url_for('/')) instead of redirect(url_for('home'))

Since testing out the program it looked like none of the form data was saved I noticed
that the form.get() naming does not match those assigned within the template so 
I had to change the form.get() names because didn't match with the form in template

I noticed that the pattern to save things to the db we needed db.session.commit(),
it was missing and which is why nothing was saved so I just add that.

The bug now is it is not showing the specific pizza toppings that I picked and 
just shows all of the toppings I went online to find of a way to get multiple parameters
within a form. I found that I need to change get to getList when want multiple items from form for the toppings_list

I also noticed that the loop to add the toppings is not to the toppings the user has
chosen but to all of them, so I hange the loop to toppings_list instead of PizzaTopping.


## Exercise 2

The expected ouput for this program is to enter in a city name and get its weather 
information. The actual output is getting an internal system error and lots of other bugs
discussed and sloved below:

I noticed that the request.args.get() naming is not the same as on the names on the 
templates so I change the request.args.get to match the template's names. 

While looking at the OpenMapweatherAPI documentation on how to perform API calls 
I noticed that our base URL was mising a "?" so I change the url route to ave an added "?"

Again while looking at the documentation I noticed that the parameter naming for the 
city is "q" instead of city name so I changed that to "q"

The error I got was when parsing throught the JSON I got from making the API call
and noticed that in the JSON the format for the temperature is labeled as "temp"
and not as "temperature"

## Exercise 3

The expect output for this program is to return a sorted array using merge sort
to sort an array or using binary search to search for a number but the actual output
is an error about index, and the other error is the binary search mid is needing an
integer instead of a float. Actual bug below


The bug was that the index was out of range so after looking at the code I noticed
that I am not assgining it to the correct index. 
To fix I change the merge sort function while loop of `while j < len(right_side):` to 
`arr[k] = right_side[j]` instead of `i`

For the second bug I found that mid was expecting an integer instead of a float 
so I just added a floor `//` divisor to get the mid.


## GitHub Link To Exercises With All Bugs Fixed
https://github.com/caocmai/SPD-2.31-Testing-and-Architecture/tree/main/Homework/SPD-2.3-Debugging-Techniques-Lab