# Interactive SICP

[tree/master/isicp](https://github.com/zodiac/appspot-grading/tree/master/isicp)

![screenshot](https://raw.github.com/zodiac/appspot-grading/master/isicp/images/screenshot.png)

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
- Make scheme evaluation asynchronous

## API

Most of the prompts in the book are defined by

```html
<div id="scheme-divide">
(/ 10 5)
</div>
<script> prompt("scheme-divide"); </script>
```

the div contains the initial text. Autograded input is written as such

```html
<div class='exercise'>

<p> <b> Exercise 1.2. </b>  Translate the following expression into prefix form.

<p> <img src='http://upload.wikimedia.org/math/4/3/e/43e4ba3449a3038629dca7de56757cae.png'>
<div id="scheme-ex-12-input" class='input'></div>

<script> 
makePromptingInput("scheme-ex-12-input");
addOutput("scheme-ex-12-input");
linkEditor("scheme-ex-12-input", "scheme-ex-12-input-output", function(x, y) {

  var code = "(equal? (quote " + y + ") " + 
      "'(/ (+ 5 4 (- 2 (- 3 (+ 6 (/ 4 5))))) (* 3 (- 6 2) (- 2 7))))";

  if (biwascheme.evaluate(code) == true) {
    return "<div class='right-answer'> \u2713 </div>";
  } else {
    return "<div class='wrong-answer'> \u2717 </div>";
  }
});
</script>
</div>
```

## Internals

Most of the magic happens in [coding.js](https://github.com/zodiac/appspot-grading/tree/master/isicp/coding.js). We use the [CodeMirror](http://codemirror.net/) editor and the [BiwaScheme](http://www.biwascheme.org/) scheme interpreter.

#### makeEditable

makeEditable(_editor) converts the div with id _editor into a CodeMirror editor. CodeMirror emits a blur event when the editor is unfocused; we additionally emit this event when ctrl-enter is pressed.

#### makeStatic

same as makeEditable, except editing is disabled. Used for exercises and the like where user should not be able to cheat in that way.

#### linkEditor

linkEditor(_editor, _output, func) links the CodeMirror editor associated with _editor to a div with id _output. When CodeMirror throws blur, func is called on its contents and the result printed in the output div.

#### Example

```html
<div id="scheme-number">
(+ 485 1)
</div>
<div id="scheme-number-output" class="output"> </div>

<script>
makeEditable("scheme-number");
linkEditor("scheme-number", "scheme-number-output", function(x, y) {return evaluate(x);});
</script>
```

in this case, func calls the evaluate function (also defined in coding.js) which uses the biwascheme interpreter to evaluate the user's input.
