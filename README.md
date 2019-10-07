# Grounding

A project to improve the grounding models on transmission lines and substations.

## Disclaimer

This project was developed during the second semester of 2018. After some time, i decided to make some tweaks and publish this on Github to give inspiration to fellow engineers who aspire to learn about software development.  

As i gained more experience, i started to realize i made some development mistakes on this project. I did some refactoring along the way, but there is still work to be done.  

If you catch some errors, i would be very happy to hear. Some are probably already mapped, but i am pretty sure i missed a lot.

## Motivation

This software is a joint effort between me and Braulio Chuco (my teacher) to design AC substation grounding systems.
It was developed as a part of my undergraduate thesis using Python, a language loved by engineers, statisticians and scientists all over the world.  

The main goal of this project is to inspire other fellow engineers and engineering students to delve into the world of software development,
and use this skillset as a innovative advantage and make the world a better place.  

In my point of view, one of the worse wastes of human time and work is doing something
that can be automated, which is the case of doing the procedural math for the grounding systems design.

## How to run

### Installing Dependencies

This project uses Python 3.7.3, but anything above 3.6 should work.  
To install the dependencies, you can use the requirements.txt file and install via pip:

```bash
pip install -r requirements.txt
```

### Running the Project

As this is a Django project, you need to first start the backend server. You can do so on the command line:

```bash
python manage.py runserver
```

Then all you have to do is open up your browser at <http://127.0.0.1:8000/> or whatever port Django is set up to.

### Running the test suite

Unfortunately i didn't develop the unit tests for this project yet. I have plans on implementing tests soon, but if you want to get ahead, feel free to open a PR and add those tests! =)

## How to contribute

On the close future i don't have any plans on adding new features to the project, but if you want to contribute and add, open an issue or a PR with your code/suggestions.

## Project Aftermath

This project as an undergraduate thesis was a success! I was able to get my bachelor's degree and it was an excellent experience to develop a web application end-to-end.
