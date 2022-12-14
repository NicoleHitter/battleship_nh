# Battleship NH
Battleship NH is a Python terminal game, which can be played in the Code Institute mock terminal on Heroku. User can try to play against the computer, by guessing the correct location of computer's ship. 

## How to Play
Battleship NH is a game inspired by the classic pen-and-paper Battleships game, except that in this game is only the player that will guess the location of the ship, that has randomly been located by computer. 
Once the game starts, player will be asked to enter a number between 4-9, which will dictate the size of the square game board. For example if 5 is given then board will have 5 rows and 5 columns. After this board will be shown, and user will be asked to enter two numbers that will be the position of where his missile will land, and will need to corespond to where the ship is located. The board will appear again with the place chosen. 
In the end user will be shown if they have missed or hit the ship. 


### User Stories
  * As a user, I would like to play an interactive and fun game 

## Features
### Existing Features
  * Accepting user's input
  * Input Validation and Error Checking 
    * User cannot enter coordinates outside the size of the board 
    * Coordinates need to be numbers 
  * Board generation depending on user's input 
  * Play against the computer 

### Features Left to Implement
  * To allow player to throw more than one missile and computer to have more than one ship
  * To retain player's name and scores and be able to save this data on an external spreadsheet

## Technologies used 
* GitHub
* Gitpod
* Heroku

## Testing


### Validator Testing


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