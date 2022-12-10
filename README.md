# Capitals Quiz
## Description 
Capitals Quiz is an online Quiz designed to allow the user to test his knowledge about the capitals of the World. The Quiz is created in a very interactive and intuitive manner that would make it very accessible and entertaining. 
![Responsive](doc/screenshots/Responsive.png)

### User Stories
  * As a user, I would like to test my knowledge on the world's capitals 

## Features
### Existing Features
  * Capitals Quiz Heading 

As the page has been uploaded the user is presented with a large title area that is designed to caption his attention and interest.

![Title](doc/screenshots/title.png)

  * The Start Button

After getting intrigued by the title user should be already willing to play the game, and this can be easily done by pressing the start button. 

![Start](doc/screenshots/Start.png)

  * Question Section

Once the user has started the game, he will be presented with one question per page, which will have three answer options, from which he can choose and then submit his answer. 

![Question](doc/screenshots/question.png)

  * The Score Area

After submitting his answer a text will appear to say if the answer was correct and if contrary to say which was the correct answer. Also underneath this text, there is a section that will allow the user to see exactly how many correct and incorrect answers they have provided.

![Scores](doc/screenshots/scoresarea.png)

  * Next button

Aside from the submit button, there is a Next button, which can be pressed only after submitting an answer, and this will take the user to the next question or at the end of the game when questions have finished. 

![Buttons](doc/screenshots/buttons.png)

  * End of Game

When questions have ended user will be presented with his final score, and then have the option to play the quiz again by pressing the Restart button. 

![Final Score](doc/screenshots/finalscore.png)


### Features Left to Implement

In time the site should allow the user to create an account and play against time and other users.

## Technologies used 
* GitHub
* Gitpod
* HTML
* CSS
* JavaScript 
* Google Chrome developer tools
* FontAwesome

## Typography and colour scheme
The page has a fairly simple appearance. The background is created by an image with different flags, then the text area is fitted inside a white container. Text colours have been specified in CSS by RGB(red,  green, blue) values. 
 
## Testing
* Step I: pressing the Start button will show the first question and options.
* Step II: once an answer is selected by the user Submit button will appear.
* Step III: once Submit button is pressed, the answer selected gets checked - a message will appear for the user, the score will get incremented, and now Submit button will disappear and the Next button will show up.
* Step IV: once all questions are finished, the user will be shown the final score and a Restart button which if pressed, the page will be uploaded and the user can start playing the game again.

Capitals Quiz Project looks and works well on different browsers and screen sizes.

![Responsive:iPhoneSE](doc/screenshots/iPhoneSE.png)

![Responsive:iPadAir](doc/screenshots/iPadAir.png)


### Validator Testing
#### HTML

No errors were returned when passing through the official W3C validator.

#### CSS

No errors were returned when passing through the official W3C CSS validator.

#### JavaScript

No errors were found when passing through the official Jshint validator.
Metrics
* There are 5 functions in this file.

* Function with the largest signature take 1 argument, while the median is 0.

* Largest function has 13 statements in it, while the median is 4.

* The most complex function has a cyclomatic complexity value of 6 while the median is 1.

### Fixed Bugs 
* 
* 

## Deployment
### Heroku


### Gitpod
After opening the repository in GitHub, you can press on Gitpod button which will take you to Gitpod.



## Credits
### Content


### Media

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!