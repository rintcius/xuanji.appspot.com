# Interactive SICP

[tree/master/isicp](https://github.com/zodiac/appspot-grading/tree/master/isicp)

![screenshot](https://raw.github.com/zodiac/appspot-grading/master/isicp/screenshot.png)

Structure and Interpretation of Computer Programs now in an interactive textbook form! 

Click on (almost) any code fragment to edit. Ctrl-Enter will re-run the script.

## Contributing

This project is a work-in-progress and we need your help! Help by 

- Report any bugs, typos etc that you find
- Adding more content by converting more of [SICP](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-4.html#%_toc_start) and writing more exercises
- Adding new features (for eg, perhaps you feel that a scheme cheatsheet should pop up when you click on a certain link)

## todo

- Display all code fragments that the currently focused code fragment depends on (and other [light table](http://www.chris-granger.com/2012/04/12/light-table---a-new-ide-concept/) features)
- Display hints as to why user did not pass an exercise

## Programming

Most of the magic happens in [coding.js](https://github.com/zodiac/appspot-grading/tree/master/isicp/coding.js). 

#### makeEditable

makeEditable(_editor) converts the div with the id string _editor into a CodeMirror editor

#### linkEditor
