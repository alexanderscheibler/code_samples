# Cheapest Options

Coding challenge for a job opening. Given a list of dates, provide the cheapest option according to the client type.

Challenge: 
- Full description of [the problem here](#problem) 
- Full description of [the solution here](#solution) 

- Code originally written in 2019. 
- Test cases added in 2019.

## Test Execution
```
[user@user cheapest_options]$ python3 -m unittest discover -s tests
..........................................
----------------------------------------------------------------------
Ran 43 tests in 0.002s

OK
```

## Coverage report

```
[user@user cheapest_options]$ coverage report

Name                             Stmts   Miss  Cover
----------------------------------------------------
constants.py                         1      0   100%
enums/__init__.py                    0      0   100%
enums/client.py                      4      0   100%
enums/stars.py                       5      0   100%
helpers/helpers.py                  40      0   100%
main.py                             29     15    48%
models/__init__.py                   0      0   100%
models/establishment.py             25      1    96%
models/input_processor.py           16      1    94%
models/price.py                     36      0   100%
models/reservation_date.py          13      0   100%
tests/__init__.py                    0      0   100%
tests/test_establishment.py         41      1    98%
tests/test_helpers.py               70      1    99%
tests/test_input_processor.py       40      1    98%
tests/test_main.py                  14      1    93%
tests/test_price.py                 25      1    96%
tests/test_reservation_date.py      22      1    95%
----------------------------------------------------
TOTAL                              381     23    94%
```


## Problem

------

A hotel chain wants to offer an online booking service. 
The chain is made up of establishments in three categories: Economy, Medium, and Luxury. 
Each establishment has different rates for weekdays and weekends, including specific 
rates for loyalty program participants. 
Additionally, each establishment has a rating indicating the quality of service.


* Economy has a rating of 3 and its weekday rates are R$ 110 for regular customers and R$ 80 for loyalty program participants. Weekend rates are respectively R$ 90 and R$ 80 for regular customers and loyalty program participants.
* Medium has a rating of 4 and its weekday rates are R$ 160 for regular customers and R$ 110 for loyalty program participants. Weekend rates are respectively R$ 60 and R$ 50 for regular customers and loyalty program participants.
* Luxury has a rating of 5 and its weekday rates are R$ 220 for regular customers and R$ 100 for loyalty program participants. Weekend rates are respectively R$ 150 and R$ 40 for regular customers and loyalty program participants.

Write a program to find the cheapest hotel. 
The program input will be a sequence of dates for regular customers or loyalty program participants. 
Use "Regular" to denote a regular customer and "Reward" to denote a customer participating in the loyalty program. 
The output should be the cheapest available hotel and, in case of a tie, the hotel with the highest rating should be returned.

#### Format of input:

<type_of_customer>: <date1>, <date2>, <date3>, ...

 
#### Format of output:

<name_of_cheapest_hotel>

---
#### Samples:

###### Input 1:
Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)

###### Output 1:
Economy

---

###### Input 2:
Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)

###### Output 2:
Medium

---

###### Input 3:
Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)

###### Output 3:
Luxury

---

## Solution

------
### Running the Application

Requirements:
- Python 3.6+

Run from the "cheapest_options" directory:
```
$ python3 main.py ${INPUT_FILE}
```
Example:
```
$ python3 main.py "samples/sample_data.txt"
```

To run the tests, from the "cheapest_options" directory:
```
$ python3 -m unittest discover -s tests
```

### Assumptions:

- The customer type (Regular or Rewards) will not be blank;
- The list of dates does not necessarily have a limit (past or future), nor do they need to be in chronological order, as long as they are valid dates;
- The weekend is considered to be Saturday and Sunday only; the total price should aggregate values for different types of days, as applicable (it doesn’t assume the highest or lowest value);
- The input file will have a limited size, and the program will run on a computer with sufficient resources to process it adequately. Continuous input, such as a log file being written to while processing, was not considered.

### Application Design:

The entry point is created in the `main.py` module, which sets up and handles file input. From this point, the `run()` function is called for each line of input, executing the following application flow:
- `InputProcessor` parses the line, separating the string with the customer type from the list of date strings for the reservation;
- `ReservationDate` converts date strings into datetime objects and calculates information about the dates, such as the number of weekdays, weekends, and the length of stay;
- It records whether the customer is Rewards or Regular;
- `Price` organizes prices, instantiating categories of establishments according to the dates and customer type for the reservation;
- The `Establishment` class provides information on which rate should be considered based on the type of date, customer, and establishment category.
- Based on the processed information, the output is returned as the name of the cheapest establishment.

Additionally:
- **_Helpers_**: module with support functions, more generic and reusable in the future;
- **_Enums_**: used for values that don’t change necessarily and don’t need extensive logic;
- **_Constants_**: module with application constants, including the price table formatted as a dictionary—although it’s mutable, the intent is to abstract these details from the application and emulate a non-relational database.

### Application Execution:
```
[user@user cheapest_options]$ python3 main.py "samples/sample_data.txt"
Economy
Medium
Luxury
```

