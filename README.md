# Data Centric Development Milestone Project - Rice Bowl

*Developer: Anthony Guillermo*

 - Project Brief 
 - Technologies
 - UXD
 - Deployment
 - Tests and Fixes
 - Media
 - Acknowledgements
 

## Project Brief

In this project I was tasked with building a data centric development site allowing users to manage a dataset about a particular domain, using all the technologies I learnt so far in this course.

The dataset should allow users to share their data with a community and have easy access to the data provided by all users. The site owner might also benefit from the collection of the dataset as a whole.

Build a website for users to find and share recipes (Rice Bowl) mainly using technologies such as HTML, CSS, JavaScript, Python+Flask and MongoDB. As an option additional libraries or external APIs. The project may be started using wireframes, as taught in the UX lesson.

Rice Bowl is an experienced website who have been around for 5 years. Since the sites's first inception they had been mostly doing food trip blogs in Asia, wanting to share Asian recipes with their online community. However since they have a number to recipes, they wish do share their recipes online and want to allow users to view and add recipes as well. Their main aim is to focus and give more exposure to Asian food. They currently have about 40 recipes but is looking to increase that number in the future. The following requirements were given by the food blogging site after meeting with the client;

 - Create a web application to allow users to store and easily access cooking recipes. With fields such as ingredients, steps etc.
 - Create backend code to allow users to add cuisines and recipes.
 - Provide users with a directory of recipes/cuisines
 - Present results that are visually appealing and user friendly.

## Technologies

 - HTML5
 - CSS3
 - JavaScript
 - Python
 - Flask
 - [jQuery](https://jquery.com)
 - [MongoDB](https://mongodb.com)
 - [Materialize v1.0.0](https://materializecss.com/)
 - [Font Awesome v4.7.0](https://fontawesome.com/v4.7.0/)
 - [Google Fonts](https://fonts.google.com)

## UXD

**Strategy**

|Focus	|User Needs	|Business Objectives	|
|:------------:|:------------:|:------------:|
|Aims	|Find and share recipes	|Increase site views/users	|
|	|Look at recipe details	|Retain users	|
|Clients|Follow recipes while cooking themselves| Increase community interaction|
|User objectives|View and learn new recipes|Gain more exposure for Asian cuisines
|	|Search database for recipes|	Grow recipe database	|
|	|Read monthly travel food blog|		|
|	|Add new recipe/cuisine to database| 		|
|	|View social media sites|	|
|	|Interact with website community|	|
|	|View photos of recipes|	|

**Scope**

|Focus	|Functional Specification	|Content Requirements	|
|:------------:|:------------:|:------------:|
|Features	|Home	|Information about site/features	|
|Future Features|Recipes	|Search and add recipes/cuisines|
|	|Spotlight	|Read and view photos of four monthly Spotlight recipes|
|	|Travel Blog|Read monthly Travel Food Blog|
|	|Social Media|Access social media links|
|	|~~Search~~|~~Search specific recipes~~|
|	|~~Comment~~|~~Leave and reply to comments on recipes~~|
|	|~~Message Board~~|~~Post and interact with posted topics~~|
|	|~~Recipe Filter~~|~~Filter recipe database with criteria~~|
|	|~~Recipe Images~~|~~Each recipe in database has an image~~|


**Structure**

|Focus	|Interaction Design	|Information Architecture	|
|:------------:|:------------:|:------------:|
|Information Structure	|How to navigate the site	|Navigational Structure (Tree/Dashboard)	|
|Groupings|Mobile- hamburger navigation|Home/Recipes/Spotlight/Travel Blog|
|	|Desktop/Tablet - navbar|Home - Site features and info	|	
|	|Links in Footer Section	|Recipes - View or add recipes and cuisines|
|	|	|Spotlight - View monthly four top picks of dishes|
|	|	|Travel Blog - Read monthly Travel Food Blog |
|	|	|Footer links - Social media sites|

**Skeleton**

|Focus	|Interaction Design	|Navigational Design|		|		|	|
|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|Presentation of information|[See Wireframe](https://github.com/anthonybguillermo/ricebowl-milestone3project/blob/master/wireframe/ricebowl-wireframe.pdf)|Home |	| | |
|User Navigation|Desktop/Tablet/Mobile - social links in footer|Recipes >|Recipes collection dataset| |	|
|	|	|	|Add Recipe Button >|Add Recipe	|	|
|	|	|	|View/Add Cuisine Button >	|Cuisine collection dataset||
|	|	| 	|	|Add Cuisine Button >|Add Cuisine	|
|	|	|Spotlight |	|	|	|
|	|	|Travel Blog|	|	|	|

**Surface**

|Focus	|Visual Design	|
|:------------:|:------------:|
|Look of finished product|	|
|Colors and typography used|[Roboto](https://fonts.google.com/specimen/Roboto)	|
|	|[Permanent Marker](https://fonts.google.com/specimen/Permanent+Marker)		|
|	|#3e2723|
|	|#ffab00|
|	|#8d6e63|
|	|#4e342e|
|	|#616161|

## Deployment

- In Github create a requirements file by typing 'sudo pip3 freeze --local > requirements.txt'.
- Create a Procfile by typing 'echo web: python app.py > Procfile'.
- In Heroku create a new app and input a unique app name 'abg-ricebowl'. Choose 'Europe' as the region. Click "Create App".
- In Github terminal type 'heroku login' and log into Heroku.
- Type 'heroku apps' to check if the created app 'abg-ricebowl' appears.
- Create a new repository by typing 'git init'
- Type 'git add .' then 'git commit -m "(commit message)"' to add files to repository.
- From deployment tab in Heroku copy 'heroku git:remote -a abg-ricebowl' and paste into Github to set the remote to Heroku.
- Push code to Heroku by typing 'git push heroku master'
- Tell Heroku to run the app by typing 'heroku ps:scale web=1'
- In Heroku go to settings tab and under config vars set the type 'IP' in key and '0.0.0.0' in value to set the IP address. Then type 'PORT' in key and '5000' in value to set the port.
- Click open app to check the app has been deployed.
- Project link: [Rice Bowl](/)

The code for this project was pushed to Github.
- Github link: [Rice Bowl Github](https://github.com/anthonybguillermo/ricebowl-milestone3project)

## Tests and Fixes

Test and Fixes link: [Rice Bowl Testing](https://github.com/anthonybguillermo/ricebowl-milestone3project/blob/master/TESTANDFIXES.md)

## Media
The photos used in this project were taken from:
- [Unsplash](https://unsplash.com/)
- [Pexels](https://www.pexels.com/)
- [Pixabay](https://pixabay.com/)

The text in this project was taken from:
- [Panlasang Pinoy](https://panlasangpinoy.com/)
- [Delish](https://www.delish.com/)
- [BBC Good Food](https://www.bbcgoodfood.com/)
- [Delicious](https://www.deliciousmagazine.co.uk/)
- [Google](https://www.google.com/)

## Acknowledgements
Inspiration for this project was taken from:
- [Panlasang Pinoy](https://panlasangpinoy.com/)
- [Delish](https://www.delish.com/)
- [The Ringer](https://www.theringer.com/) 

Previous Code Institute Projects were also an inspiration for this project (Love Running, Resume, Whiskey Drop, Thorin & Company and Task Manager Application).


> Written with [StackEdit](https://stackedit.io/).