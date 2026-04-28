# README

Individual Flask project. This Flask app provides routes to explore global literacy rate and education.

## How to Run

From the top level of the repository, run:

```bash
python3 app.py 
```

## Routes
For any thing it looks like this:

http://127.0.0.1:PORT/literacy-growth/<country>

### 1. Literacy Growth by Country

Note, use hyphens instead of spaces for country names. Such as for US:
http://127.0.0.1:5000/literacy-growth/France
http://127.0.0.1:5000/literacy-growth/United-States

### 2. Average Years of Schooling by Country and Year Range

Also use hyphens if needed:
http://127.0.0.1:5000/schooling/France/2000/2020
http://127.0.0.1:5000/schooling/United-States/2010/2020


## Command to run the tests
python3 -m unittest Tests/test_routes.py