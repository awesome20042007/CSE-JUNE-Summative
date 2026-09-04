Frontend (what the user sees/interacts with)          Backend (what processes and stores data)
─────────────────────────────────────────            ──────────────────────────────────────────
landing.html    →  the welcomescreen                  
models.py    →  database structure
register.html   →  the form itself                    
forms.py     →  validation rules
style.css       →  colors, layoutfonts                views.py     →  logic that connects everything
                                                     urls.py      →  which web address triggers what

                                                     `


`fca holds settings that apply everywhere`   
`i told django about my app`
`i told it where to locate my templates`
`i told it where to locate my css`
NOTE `it automatically cant just locate them  so you have to tell it within settings`


MODELS.PY
3---`went to models and designed our data base structure with fields like first_name, date_of_birth, gender,etc`
NOTE `a model is djangos way of taking note of what a record in your database looks like`


FORMS.PY
4---`went into forms.py and this is the core file or heart of my validations to start working on the validations in my form`
By default, Django would render gender as a dropdown, since it has choices. forms.RadioSelect overrides that, forcing it to render as radio buttons instead — matching the design exactly. Similarly, type: 'date' tells the browser to show its own native calendar date-picker instead of a plain text box


5---VIEWS.py 
`then i went to views and worked on the logic that ties everything together`



6----URLS.PY 
`then went to  the URLS to organise my routing`
"If FCA later asked me to change the URL from /register/ to /apply/, I'd only change one line in urls.py. Every {% url 'register' %} reference across every template automatically updates itself — I don't have to hunt through every file."

7----TEMPLATES
then went to 
`the forst ine was simple because it was just a link within a button`


8----THE CSS 
`turned the style guide into code `