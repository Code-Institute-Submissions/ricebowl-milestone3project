# Data Centric Development Milestone Project Testing - Rice Bowl

*Developer: Anthony Guillermo*

## Tests and Fixes

[HTML Validator Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fabg-ricebowl.herokuapp.com%2F)

[CSS Validator Results](http://www.css-validator.org/validator?uri=https%3A%2F%2Fabg-ricebowl.herokuapp.com%2F&profile=css21&usermedium=all&warning=1&lang=en)
 
**Desktop/Tablet/Mobile** 
Tested on Chrome Desktop/Tablet/Mobile simulator

***Desktop/Tablet/Mobile Issue***
Position of banners on homepage were not visually pleasing on all screens not being the same width as the image above it when in a container class.

***Desktop/Tablet/Mobile Fix***
Override the Materialize default margins to align the banner with the image above.

>.container  .row {
margin-left: 0px;
margin-right: 0px;
}

***Desktop/Tablet/Mobile Issue***
The site wasn't running when deployed to Heroku.

***Desktop/Tablet/Mobile Fix***
The requirements.txt file was updated so the correct python packages were loaded in order for the app to run.

>click=7.1.2
Flask=1.1.2
itsdangerous=1.1.0
Werkzeug=1.0.1
Flask-PyMongo=2.3.0
dnspython=2.0.0
Jinja2=2.10.1
MarkupSafe=1.1.0
pymongo=3.7.2

***Desktop/Tablet/Mobile Issue***
The app was running in Heroku but the MongoDB database wasn't loading in the app.

***Desktop/Tablet/Mobile Fix***
Heroku 'configvars' were edited to include the connection to MongoDB server under 'MONGO_URI'.

***Desktop/Tablet/Mobile Issue***
In the accordion title there was no space after the '-' between the recipe name and cuisine

***Desktop/Tablet/Mobile Fix***
Space was forced using 'nbsp;' to create the space and be more pleasing to the eye.

***Desktop/Tablet/Mobile Issue***
Position of banners on homepage were not visually pleasing on all screens not being the same width as the image above it when in a container class.

***Desktop/Tablet/Mobile Fix***
Override the Materialize default margins to align the banner with the image above.

>.container  .row {
margin-left: 0px;
margin-right: 0px;
}

***Tablet/Mobile Issue***
Navigation bar wasn't expanding in mobile view when the css code from Materialize was used.

***Tablet/Mobile Fix***
Changed the class of the navbar to 'button-collapse' and changed the javascript in the footer to target this class.

>a  href="#"  data-activates="mobile-demo"  class="button-collapse"

>$(".button-collapse").sideNav();

***Mobile Issue***
The taglines under the title were to long on mobile view.

***Mobile Fix***
There were two taglines set for desktop and tablet and a shorter tagline for mobile screens.

>h4  class="hide-on-small-only">Search our database for Asian recipes. Got a new recipe or cuisine for us? You can add it to the database too./h4
h4  class="hide-on-med-and-up">View and add Recipes./h4

***Mobile Issue***
In Recipes page 'add a recipe button' and 'view/add cuisines' buttons were on top of other but had no spacing in mobile view.

***Mobile Fix***
The buttons were hidden in mobile view. Then two new buttons each within their own row and column class would be shown in mobile view.

>div  class="row hide-on-small-only">
div  class="col s12">
a  href="{{ url_for('add_recipe')}}"  class="waves-effect waves-light btn-large amber accent-4">i  class="material-icons right">history_edu/i>Add a Recipe/a>
a  href="{{ url_for('get_cuisines')}}"  class="waves-effect waves-light btn-large amber accent-4">i  class="material-icons right">outlined_flag/i>View/Add Cuisines/a>

>div  class="row hide-on-med-and-up">
div  class="col s12">
a  href="{{ url_for('add_recipe')}}"  class="waves-effect waves-light btn-large amber accent-4">i  class="material-icons right">history_edu/i>Add a Recipe/a>
div  class="row hide-on-med-and-up">
div  class="col s12">
a  href="{{ url_for('get_cuisines')}}"  class="waves-effect waves-light btn-large amber accent-4">i  class="material-icons right">outlined_flag/i>View/Add Cuisines/a>


***Desktop/Tablet/Mobile Issue***
In the Recipe page there was too much information in the accordion when in mobile view. Recipe name, Cuisine and Course info looked jumbled on mobile. This was made worse if the recipe name was long. 

***Desktop Fix***
 Course name was moved from the accordion title to the collapsable body. So it would appear when clicked. The Recipe names were amended in MongoDB if they were too long. So the titles wouldn't look jumbled on mobile.

>h5  class="recipe-title">{{recipe.recipe_name}}/h5>  h5>&nbsp;- {{recipe.cuisine_name}}/h5>
/div>
div  class="collapsible-body">
span>
h5  class="recipe-title">Course:/h5>h5>{{recipe.course_name}}/h5>
h5  class="recipe-title">Servings:/h5>h5>{{recipe.servings}}/h5> 

**Issues not Addressed**
***Mobile Issue***
In the Travel Blog page the two images of dishes do not correctly resize in order to view the images of the dishes correctly.

## Manual Testing

**Desktop/Tablet/Mobile** 
Tested on Chrome Desktop/Tablet/Mobile simulator

**Exploratory Testing**

***Page Links - Desktop***
The app was navigated through the different pages on both Desktop/Tablet & Mobile. In order to check if the user was able to navigate to and from each of the pages; Homepage, Recipes, Spotlight and Travel Blog. 

The buttons in Recipes were checked to see if it lead to the Add a Recipe form, Cuisine database and the Add a Cuisine form.

The navigation was also checked to so that the user would  be able to navigate the site without having to use the back button.

***Page Links - Tablet/Mobile***
In the tablet and mobile views there is a burger bar menu. This was tested to see if the menu would slide from the left when clicked.

As similar with the Desktop test, all pages were navigated to and from each other to test the links. The button navigation was tested as well.

**Device View - Desktop/Tablet/Mobile**
The rows and columns were checked to different devices to make sure the they were applied to correct screen size.

Also the text and buttons designed to appear on specific views were also checked to ensure there was no repeat or overlap.

 ***Social Links - Desktop/Tablet/Mobile***
All social links were checked at the footer of each page to make sure Facebook, Pinterest, Twitter, Instagram and Youtube all opened in a new tab.

**Base.html - Desktop/Tablet/Mobile**
All pages were checked to ensure the basic structure from the site extended to all pages.

**MongoDB - Desktop/Tablet/Mobile**
The app was checked to see if the MongoDB database was loading correctly on the site. After this was checked the two forms were tested Add a Recipe and Add a Cuisine. Test Recipes and cuisines were inputted into the forms and checked in the Recipes and Cuisines pages along with checking the database correctly. Both tests were successful both test recipes and cuisines appeared in both the site and the MongoDB database.

> Written with [StackEdit](https://stackedit.io/).