# THE COACH

[Live live website -->](https://romanscoach.herokuapp.com/)

![Mockup image](docs/)

## About

The Coach is a command-line small Python program that can be considered a type of simulation or game. Project will put user in a position of a Coach for
a team of 5 Basketball players that will be created based on user input. Input has to be inside Realistic parameters determined by the developer.Program will output the percentage of possible team performance so that user will have a Idea of how good final result Is.Program was developed as a 3rd portfolio project in acquiring the "Diploma In Software Development" with Code institute.
The requirements of this project were use of Python programming language and it's libraries to develop a program in a mock terminal in the browser. 

## Table of Contents
  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Manual](#user-manual)
  - [User Stories](#user-stories)
    - [Users](#users)
    - [Site Owner](#site-owner)
  - [Technical Design](#technical-design)
    - [Flowchart](#flowchart)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks & Tools](#frameworks--tools)
    - [Libraries](#libraries)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Automated Testing](#automated-testing)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Project Goals
- The Coach program is intended to be the beginning of possible
real-world application used in sports by coaches, mentors and even
athletes themself.With certain upgrades and some more real-world based 
calculations in regard of caloric values and influences of certain training routines to athlete's bodies this program could provide value and assist
in optimizing the team and individual performance of an athlete.

### User Goals
- Interact with program that is fun and easy to understand
- Use a program that has real-life potential
- Be able to Log in and come back to the existing account
- Create something fun and unique 
- See the result of input choices




### Site Owner Goals



## User Experience

### Target Audience



### User Requirements and Expectations


### User Manual

<details><summary>Click here to view instructions</summary>

#### Main Menu




#### Program instructions

#### Play


#### Log-in

1. Try another email
2. Create a new player


Same option follow for Player2.

#### New players registration (sign-up)


#### Users greeting

Once both users have been logged in, the program will display a greeting message with both names and start the game.

#### Program


Operation: Input a numeric value and press enter key.

#### Go again
By selecting this option a new game starts for the same players.

#### Go to main menu




#### Exit program


</details>

[Back to Table Of Contents](#table-of-contents)

## User Stories

### Users

1. 
2.
3. 
4. 
5. 
6. 
7. 
8. 
9. 

### Site Owner

10. 
11. 
12. 
13. 
14. 
[Back to Table Of Contents](#table-of-contents)

## Technical Design

### Flowchart

The following flowchart summarises the structure and logic of the application.

<details><summary>Flowchart</summary>
<img >
</details>

## Technologies Used

### Languages

- [Python](https://www.python.org/) programming language for the logic of the program

### Frameworks & Tools

- [Diagrams.net](https://app.diagrams.net/) was used to draw program flowchart
- [Font Awesome](https://fontawesome.com/) - icons from Font Awesome were used in the footer below the program terminal
- [Git](https://git-scm.com/) was used for version control within VSCode to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Google Cloud Platform](https://cloud.google.com/cloud-console/) was used to manage access and permissions to the Google Services such as Google auth, sheets etc.
- [Google Sheets](https://www.google.co.uk/sheets/about/) were used to store players details
- [Heroku Platform](https://dashboard.heroku.com/) was used to deploy the project into live environment

- [Visual Studio Code (VSCode)](https://code.visualstudio.com/)
VSCode was used to write the project code using Code Institute template

### Libraries

#### Python Libraries
- os - used to clear terminal
- random - used to alternate first player to start the game
- sys & sleep - used to create a typing effect within the games rules
- time - used to displayed delayed messages in the terminal
- [unittest](https://docs.python.org/3/library/unittest.html) - used to carry out testing on single units in validation.py file

#### Third Party Libraries
- [colorama](https://pypi.org/project/colorama/) - JUSTIFICATION: I used this library to add color to the terminal and enhance user experience. I marked warning/error information with color red and user feedback with blue and green
- [email_validator](https://pypi.org/project/email-validator/) - JUSTIFICATION: I used this library to validate if user email input is of the form name@</span>example.com
- [gspread](https://docs.gspread.org/en/latest/) - JUSTIFICATION: I used gspread to add and manipulate data in my Google spreadsheet and to interact with Google APIs
- [google.oauth2.service_account](https://google-auth.readthedocs.io/en/master/) - JUSTIFICATION: module used to set up the authentification needed to access the Google API and connect my Service Account with the Credentials function. A creds.json file is created with all details the API needs to access the google account. In deployment to heroku this information is stored in the config var section.

[Back to Table Of Contents](#table-of-contents)

## Features

### Main menu


 
<details>
    <summary>Main Menu Screenshot</summary>

![Main menu](docs/features/main-menu.JPG)
</details>

### Game rules

  
<details>
    <summary>Game rules Screenshot</summary>

![Game rules](docs/features/game-rules.JPG)
</details>

### Play options


<details>
    <summary>Play options Screenshot</summary>

![Play options](docs/features/play-options.JPG)
</details>

### Log-in


<details>
    <summary>Log-in Screenshot</summary>

![Log-in](docs/features/log-in.JPG)
</details>

<details>
    <summary>Alternative options Screenshot</summary>

![Log-in wrong email](docs/features/log-in-wrong-email.JPG)
</details>

### Sign-up

<details>
    <summary>Sign-up Screenshot</summary>

![Sign-up](docs/features/sign-up.JPG)
</details>

<details>
    <summary>Sign-up email verification Screenshot</summary>

![Sign-up wrong email](docs/features/sign-up-wrong-email.JPG)
</details>

### Users greeting


<details>
    <summary>Greeting Screenshot</summary>

![User greeting](docs/features/user-greeting.JPG)
</details>

### Game


<details>
    <summary>Game Screenshot</summary>

![Game screen](docs/features/game-screen.JPG)
</details>

<details>
    <summary>Incorrect Move in Game Screenshot</summary>

![Move validation in Game screen](docs/features/game-screen-move-validation.JPG)
</details>

<details>
    <summary>Winner Message Screenshot</summary>

![Winner Message](docs/features/game-screen-winner-message.JPG)
</details>

### Finished Game options

<details>
    <summary>Finished Game options Screenshot</summary>

![Finished Game options](docs/features/finished-game-options.JPG)
</details>

#### Play 


<details>
    <summary>Restart game Screenshot</summary>

![Restart Game](docs/features/restart-game.JPG)
</details>

#### Go to main menu


#### See your statistics


<details>
    <summary>See your statistics Screenshot</summary>

![Statistics](docs/features/statistics.jpg)
</details>

#### Quit game
- Exits the program with a goodbye message

<details>
    <summary>Quit game Screenshot</summary>

![Quit Game](docs/features/quit-game.JPG)
</details>

### User Input Validation
- Displays an error message if user input is not in a form that was expected
- Asks for a new input and provides guidance to user on how to correctly format the input
- User stories covered: 5, 13, 14

<details>
    <summary>Username validation Screenshot</summary>

![Username validation](docs/features/validation-username.JPG)
</details>

<details>
    <summary>Email validation Screenshot</summary>

![Email validation](docs/features/validation-email.JPG)
</details>

<details>
    <summary>Validation of input during the game Screenshot</summary>

![Moves validation](docs/features/game-screen-move-validation.JPG)
</details>

[Back to Table Of Contents](#table-of-contents)

## Validation



## Testing

The testing approach is as follows:
1. Manual testing of user stories
2. Automated unit testing using the Python unittest library

### Manual Testing
<details><summary>See user stories testing</summary>

1.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |

<details><summary>Screenshot</summary>
<img src="docs/testing/user-story-1.jpg">
</details>

2.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Main menu | Select option 1 | Users are presented with game rules | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/user-story-2.jpg">
</details>

3. 

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |


<details><summary>Screenshot</summary>
<img src="docs/testing/user-story-3-a.jpg">
</details>
<details><summary>Screenshot</summary>
<img src="docs/testing/user-story-3-b.jpg">
</details>

4.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |


<details><summary>Screenshot</summary>
<img src="docs/testing/user-story-4.jpg">
</details>

5. 

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |


<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-5-a.JPG">
<img src="docs/testing/user-story-5-b.JPG">
<img src="docs/testing/user-story-5-c.JPG">
<img src="docs/testing/user-story-5-d.JPG">
</details>

6.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |


<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-6-a.JPG">
<img src="docs/testing/user-story-6-b.JPG">
</details>

7.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |


<details><summary>Screenshot</summary>
<img src="docs/testing/user-story-7.jpg">
</details>

8. 

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |


<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-8-a.JPG">
<img src="docs/testing/user-story-8-b.JPG">
</details>

9. 

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |


<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-9.jpg">
</details>

10. 

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |


<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-10-a.jpg">
<img src="docs/testing/user-story-10-b.jpg">
<img src="docs/testing/user-story-10-c.jpg">
</details>

11.  

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |


<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-11-a.jpg">
<img src="docs/testing/user-story-11-b.jpg">
<img src="docs/testing/user-story-11-c.jpg">
</details>

12. 

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |


<details><summary>Screenshot</summary>
<img src="docs/testing/user-story-12.jpg">
</details>

13.  

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |


<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-13-a.jpg">
<img src="docs/testing/user-story-13-b.jpg">
</details>

14.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |


<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-14-a.jpg">
<img src="docs/testing/user-story-14-b.jpg">
</details>

</details>

### Automated Testing
<details><summary>See unit testing</summary>

- I wrote unit tests using Python unittest library
- I tested separate functions to verify correct user input:
  - validation of user email and user name input

I needed to amend the function and add 'Try Except' blocks to handle TypeError.
Initial error called - 'TypeError: object of type 'int' has no len()'



</details>

[Back to Table Of Contents](#table-of-contents)
## Bugs

| **Bug** | **Fix** |
| ------- | ------- |


## Deployment

### Heroku
This application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
2. Create a new app, add a unique app name (this project is named "ci-pp3-connect4") and choose your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars store any sensitive data you saved in .json file. Name 'Key' field, copy the .json file and paste it to 'Value' field. Also add a key 'PORT' and value '8000'.
6. Add required buildpacks (further dependencies). For this project, I set up 'Python' and 'node.js' in that order.
7. Go to "Deploy" and select "GitHub" in "Deployment method"
8. To link up our Heroku app to our Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below
9.  Choose the branch you want to buid your app from
10. If prefered, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

### Forking the GitHub Repository
1. Go to the GitHub repository
2. Click on Fork button in top right corner
3. You will then have a copy of the repository in your own GitHub account.
   
### Making a Local Clone
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone <span>https://</span>github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone

[Back to Table Of Contents](#table-of-contents)

## Credits

### Images
- [Flaticon](https://www.flaticon.com/free-icon/connect_1707222) was used for the website favicon

### Code
- [ASCII Art Generator](http://patorjk.com/software/taag/) was used to create game title
- Code Institute - for git template IDE and "Love Sandwiches - Essentials Project" which helped me with connecting the Google Spreadsheet to my project.

- How to install a Python module, eg. [email validation](https://pypi.org/project/email-validator/Installing)
- [gspread documentation](https://docs.gspread.org/en/latest/user-guide.html) explained how to obtain a specific value from the google spreadsheet
- Instructions how to print colored text from [this](https://ozzmaker.com/add-colour-to-text-in-python/) and [this](https://stackabuse.com/how-to-print-colored-text-in-python/) sources
- 
- [Stack overflow]code used to clear the terminal console
- Youtube video on [Unit Test in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8) made by Socratica was very helpful to understand the concept of unit tesing

<details><summary>See winning move schemat</summary>
<img src="docs/winning-move- logic-schemat.jpg">
</details>

## Acknowledgements
