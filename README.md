# <div align="center">The Halal Butcher</div>

## Project Overview

The Halal Butcher is a full-stack Django website built using Python, JavaScript, HTML and CSS. This web application is a full B2C e-commerce website for a fictional online Halal meat supplier based in the North West of England. The Halal Butcher specialises in selling and delivering the finest quality of meats such as beef, chicken, lamb, sheep & more to users who want to enjoy these cuts with their family and friends. The site provides users with different functionalities that eases the process of purchasing a product. Users of the site can browse all products, filter products by diverse categories and also search for specific products by keyword search. From the list of products, users can select them to display each product in detail, giving users the option to add the product to their basket or return to the product list page to browse other meats. Users are also able to view the website blog to view all the latest & updated information on on The Halal Butcher. Registered users can add the product to their wishlist or a leave a review for other users to view. Authenticated users can also checkout securely inputting their personal & payment details to purchase the product and also store these details on their profile for easier future purchases. On the other hand, The Halal Butcher provides the store owner with functionalities such as product management (add, edit & delete products) without accessing the admin interface and blog post management (add, edit & delete blogs).

This website application includes CRUD functionality, user authentication (using Django's allauth library), email validation and database interaction.

[View the live website on Heroku](https://halal-butcher.herokuapp.com/)

## Table of Contents

## UX & Planning

### The Strategy Plane

#### Overall Project Goals
    - To provide a B2C e-commerce platform, selling meat products to consumers.
    - To provide users different functionalities such as user authentication, product purchase, reviewing products and wishlist/basket management. 
    - To provide the store owner the ability to manage the site to update products and information via the blog feature.

#### Target Audience
    - Users who love enjoy consuming diverse meat products.
    - An audience that consume Halal meats.
    - Users that prefer to purchase their meats online rather than visiting the butchers shop.

#### Site Owner Goals
    - Build a platform that has an intuitive user interface to provide users to easily navigate the website.
    - To promote products that are listed on the e-commerce website.
    - To provide users with a platform to purchase quality Halal meats.
    - To provide competition in the meat supplier market.

### The Scope Plane

#### Entity Relationship Diagram

As this project utilises Django which is a MVT(Model, View & Template) framework, a connection to database tables or 'Models' is required. An entity relationship diagram was created to visually map out the structure of the databases & models. The entity relationship diagram was creating using [DrawSQL](https://drawsql.app/) and is shown below:

![screenshot of ERD on DrawSQL](/readme/screenshots/Screenshot%202022-08-14%20at%2017.57.09.png)

#### Agile Methodology

#### Epics

13 Epics were created as basis to further make 42 User Stories. The project kanban board that was created to list these Epics & User Stories can be visited on this link [here](https://github.com/legenduzair/the-halal-butcher/projects/2). These Epics are detailed below:

1. Initial Django Setup [#1](https://github.com/legenduzair/the-halal-butcher/issues/1) - As a **developer**, I can **setup the Django environment** so that **I can begin development of my Django project**.
    
    **Potential User Stories Included:**
    - Create Django Project
    - Install Django Libraries required
    - Create admin superuser
    - Create first app
    - Initial Deployment

2. Creating Base Template & Configuring Home App [#2](https://github.com/legenduzair/the-halal-butcher/issues/2) - As a **developer**, I can **create templates & stylesheets for the base and configure the home app** so that **the user can navigate around the website with ease**.

    **Potential User Stories Included:**
    - Creating base template and stylesheets
    - Configuring the Home app
    - Creating the navigation templates

3. Allauth setup [#3](https://github.com/legenduzair/the-halal-butcher/issues/3) - As a **developer**, I would **like to setup the Django authentication library - allauth** so that **my user audience has the option to register, sign in and sign out of their accounts for advanced permissions**.

    **Potential User Stories Included:**
    - Register a user account
    - Sign in to user account
    - Sign out from user account

4. Configuring Products App [#4](https://github.com/legenduzair/the-halal-butcher/issues/4) - As a **developer**, I would **like to create and configure the products app** so that **the user audience can view, search for and click on**.

    **Potential User Stories Included:**
    - View product list
    - View products in detail with summary information
    - Search for a specific product
    - Filter through to acquire a specific product

5. Configure Wishlist App [#5](https://github.com/legenduzair/the-halal-butcher/issues/5) - As a **developer**, I would **like to incorporate a wishlist app** so that **the user audience can add & remove products to & from their wishlist**.

    **Potential User Stories Included:**
    - Add product to wishlist
    - View product detail from wishlist
    - Remove product from wishlist

6. Configure Shopping Bag App [#6](https://github.com/legenduzair/the-halal-butcher/issues/6) - As a **developer**, I would **like to create a shopping bag app** so that **the user audience can control the products that they want to purchase**.

    **Potential User Stories Included:**
    - Add product to cart
    - View product in cart
    - Edit product in cart
    - Remove product from cart
    - Proceed to checkout

7. Configure Checkout App [#8](https://github.com/legenduzair/the-halal-butcher/issues/8) - As a **developer**, I would **like to create and configure a checkout app** so that **the user audience can place their order and successfully pay with their payment details**.

    **Potential User Stories Included:**
    - Add delivery & billing details
    - Save details to profile
    - Add payment details when going through checkout
    - Authorise payment details
    - Order confirmation with order details

8. Configure Profile App [#9](https://github.com/legenduzair/the-halal-butcher/issues/9) - As a **developer**, I would like **to create a profile app** so that **the user audience can view their order history and have saved delivery & personal details so that they can order quickly again**.

    **Potential User Stories Included:**
    - Create user profile
    - Edit and save personal information on user profile
    - View order history

9. Product Management [#10](https://github.com/legenduzair/the-halal-butcher/issues/10) - As a **developer**, I would **like to integrate product management to my project** so that **as a site owner, I am able to manage the products on the site easily and keeping the site up to date**.

    **Potential User Stories Included:**
    - Add products
    - Edit products
    - Delete products

10. Final Deployment [#11](https://github.com/legenduzair/the-halal-butcher/issues/11) - As a **developer**, I can **setup the final deployment** so that **my project is deployed properly**.

    **Potential User Stories Included:**
    - Creating and Configuring Heroku App
    - AWS setup
    - Final caching or code refactoring

11. Product Reviews - [#12](https://github.com/legenduzair/the-halal-butcher/issues/12) - As a **developer**, I would **like to incorporate product reviews** so that **the user audience can post reviews of products on the website which will be detailed on product detail page**.

    **Potential User Stories Included:**
    - Add product review
    - Read product review
    - Edit product review
    - Delete product review

12. Web Marketing - [#13](https://github.com/legenduzair/the-halal-butcher/issues/13) - As a **developer**, I would **like to incorporate web marketing to my project** so that **I stay up to date with the company easily**.

    **Potential User Stories Included:**
    - Create an email newsletter signup using Mail Chimp
    - Create a Facebook page for the company

13. Configure Blog App - [#51](https://github.com/legenduzair/the-halal-butcher/issues/51) - As a **developer**, I would **like to create & configure a blog app** so that **the user audience can browse through the latest information & news supplied by the company**.

    **Potential User Stories Included:**
    - View blog entries list
    - View blog entries in detail
    - Add blog entry
    - Update blog entry
    - Delete blog entry

#### User Stories



### The Structure Plane

### The Skeleton Plane

### The Surface Plane

## Features

## Future Improvements

## Web Marketing

## Testing

## Technologies Used

## Deployment

## Credits
