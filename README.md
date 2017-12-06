# Fresh Tomatoes Movie Trailer Website

The Fresh Tomatoes Movie Trailer Website contains the movie posters of some of my favorite movies.
If the user clicks on one of those posters, a link to the movie trailer will open on the page. 

## Source code for a Movie Trailer website.

The source code for this site can be found on my [github](https://github.com/sjcorreia/ud036_StarterCode) page.

The module `media.py` contains a class `Movie` where we have created a data structure to store information about a particular film. The contents of this file are adapted for this project after following the Python Foundation course on Udacity.

The file `entertainment_center.py` will read from the JSON file _movies.json_, which acts as a simplified database, and create a list of `Movie` objects which will be passed to the `open_movies_page` function contained in the  `fresh_tomatoes` module.

The module file `fresh_tomatoes.py` has been provided by Udacity. I made a few modifications to this file in order to personailze the site a little bit.

## Running the code

The user will need to download and install [Python](https://www.python.org/downloads/), if it is not already installed.

Executing the code is as simple as typing the command 

	python entertainment_center.py

into the terminal.

This program will then open a window (or a new tab) in the default web browser with the newly created HTML site containing my favorite movies.

The code was written keeping in mind that the user will most likely be using Python 3.6, but it is compatible and will run if the user is still using Python 2.7. I recommend using **Python 3** for future projects.

## Resources

While creating this project, it was important that it have some sort of simulated real world behavior. The idea to use a JSON file to store the information about each film was added as a way to accomplish this simulation.

* The [json](https://docs.python.org/3/library/json.html) module for Python.
* [JSON](https://www.json.org/) format.
* The `gitignore` file was copied from [gitignore.io](https://www.gitignore.io/api/python)
* Font Family Oswald taken from [Google Fonts](https://fonts.google.com/?selection.family=Oswald)
* HMTL color pallette from [w3schools](https://www.w3schools.com/colors/colors_palettes.asp)
* Favicon taken from [freefavicon.com](https://www.freefavicon.com/freefavicons/icons/iconinfo/movie-icon-152-174286.html)
* How to add a favicon from [stackoverflow](https://stackoverflow.com/questions/9943771/adding-a-favicon-to-a-static-html-page)


## Known Issues

If the title of the movie contain more than 25 characters, the `fresh_tomatoes` module will create an undesired layout for the HTML.
This is the reason why I changed the name of the movie to simply "Star Wars: The Last Jedi" when I had originally used "Star Wars: Episode VIII The Last Jedi".

## License

The contents of this repository are covered under the [MIT License](LICENSE).
