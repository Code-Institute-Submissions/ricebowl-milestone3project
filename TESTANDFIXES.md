# Data Centric Development Milestone Project - Rice Bowl

*Developer: Anthony Guillermo*

## Tests and Fixes

[HTML Validator Results](/)

[CSS Validator Results](/)

**Desktop/Tablet/Mobile** 
Tested on Chrome desktop/tablet/mobile simulator

***Mobile Issue***
Navigation bar wasn't expanding in mobile view when the css code from Materialize was used.

***Mobile Fix***
Changed the class of the navbar to 'button-collapse' and changed the javascript in the footer to target this class.

>a  href="#"  data-activates="mobile-demo"  class="button-collapse"

>$(".button-collapse").sideNav();

***Desktop/Tablet/Mobile Issue***
Position of banners on homepage were not visually pleasing on all screens not being the same width as the image above it when in a container class.

***Desktop/Tablet/Mobile Fix***
Override the Materialize default margins to align the banner with the image above.

>.container  .row {
margin-left: 0px;
margin-right: 0px;
}

***Desktop/Tablet/Mobile Issue***
In the accordion title there was no space after the '-' between the recipe name and cuisine

***Desktop/Tablet/Mobile Fix***
Space was forced using 'nbsp;' to create the space and be more pleasing to the eye.

***Mobile Issue***
The taglines under the title were to long on mobile view 

***Mobile Fix***
There were two taglines set for desktop and tablet and a shorter tagline for mobile screens 

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


***Mobile Issue***
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
