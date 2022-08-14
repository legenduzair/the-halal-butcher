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

Each Epic has individual potential User Stories that have been created and followed when developing the code of the web application. From the 13 Epics, 42 User Stories were created. Each one was assigned story points based on the estimation of difficulty & time taken to create the feature and a category of either 'Must Have', 'Should Have', 'Could Have', 'Won't Have'. There were a total of 180 story points from all of the User Stories from which 168 story points were completed and 12 were incompleted. Due to personal reasons & time restraints, these unfinished story points will be completed and added into the project as future implementations, improving the web application for users. All of the User Stories along with their categories can be found [here](https://github.com/legenduzair/the-halal-butcher/projects/2).

Below are the User Stories that were completed within the project's first release:

1. Initial Django Setup:
    - [#14](https://github.com/legenduzair/the-halal-butcher/issues/14) - As a **Developer**, I can **setup Django by installing the appropriate libraries, creating the admin superuser and create my first app** so that **I can initiate development**.
    - [#15](https://github.com/legenduzair/the-halal-butcher/issues/15) - As a **developer**, I want **to setup the Django environment secret keys in an env.py file/Gitpod settings** so that **I do not expose the keys in an insecure fashion**.

2. Creating Base Template & Configuring Home App:
    - [#20](https://github.com/legenduzair/the-halal-butcher/issues/20) - As a **developer**, I want **to create base & home templates and stylesheets** so that **the user audience can navigate around the website intuitively on all viewport sizes**.
    - [#21](https://github.com/legenduzair/the-halal-butcher/issues/21) - As a **user**, I can **navigate around the main home page of the site** so that **I can begin my online shopping with happiness and ease**.
    
3. Allauth Setup:
    - [#16](https://github.com/legenduzair/the-halal-butcher/issues/16) - As a **developer**, I want **to setup the Allauth Django library** so that **the target audience can access authentication capabilities of the project**.
    - [#17](https://github.com/legenduzair/the-halal-butcher/issues/17) - As a **user**, I can **create an account on the website** so that **I can access features that require authenticated permissions such as posting a product review, ordering & paying for a product and more**.
    - [#18](https://github.com/legenduzair/the-halal-butcher/issues/18) - As a **user**, I can **sign in to my registered account** so that **I can access the advanced permissions required of some features on the website**.
    - [#19](https://github.com/legenduzair/the-halal-butcher/issues/19) - As a **user**, I can **sign out of my registered account** so that **I can keep my account safe and secure**.

4. Configuring Products App:
    - [#22](https://github.com/legenduzair/the-halal-butcher/issues/22) - As a **user**, I can **view the list of products that available on the website** so that **I am aware of what products are for sale, so I can potentially click into them for more detailed information**.
    - [#23](https://github.com/legenduzair/the-halal-butcher/issues/23) - As a **user**, I can **view each product from the product list in details** so that **I can view more information about the specific product which may potentially lead to a purchase**.
    - [#24](https://github.com/legenduzair/the-halal-butcher/issues/24) - As a **user**, I can **search for a product of my liking** so that **I can easily find the product I am looking for**.
    - [#25](https://github.com/legenduzair/the-halal-butcher/issues/25) - As a **user**, I can **filter the products list I want by price/category** so that **I can compare the products easily with other products**.

5. Configure Wishlist App:
    - [#26](https://github.com/legenduzair/the-halal-butcher/issues/26) - As a **user**, I can **add products to a wishlist** so that **I can quickly access the products at a later date**.
    - [#27](https://github.com/legenduzair/the-halal-butcher/issues/27) - As a **user**, I can **able to view products from my wishlist** so that **purchase them when required**.
    - [#28](https://github.com/legenduzair/the-halal-butcher/issues/28) - As a **user**, I can **remove products from my wishlist** so that **I can remove products that I no longer require for the future**.

6. Configure Shopping Bag App:
    - [#29](https://github.com/legenduzair/the-halal-butcher/issues/29) - As a **user**, I can **add products to my shopping cart** so that **proceed to purchase them**.
    - [#30](https://github.com/legenduzair/the-halal-butcher/issues/30) - As a **user**, I can **view the products I have added to the cart** so that **I can confirm before proceeding to checkout**.
    - [#31](https://github.com/legenduzair/the-halal-butcher/issues/31) - As a **user**, I can **edit products in my shopping cart** so that **I can proceed with the correct products to checkout**.
    - [#32](https://github.com/legenduzair/the-halal-butcher/issues/32) - As a **user**, I can **remove a product from the shopping cart** so that **I can proceed with checkout or if I no longer need the item**.
    - [#33](https://github.com/legenduzair/the-halal-butcher/issues/33) - As a **user**, I can **proceed to checkout with the added items from the shopping cart** so that **I can quickly purchase the items added**.

7. Configure Checkout App:
    - [#34](https://github.com/legenduzair/the-halal-butcher/issues/34) - As a **user**, I can **add my delivery and billing details when processing an order** so that **I can complete my order**.
    - [#35](https://github.com/legenduzair/the-halal-butcher/issues/35) - As a **user**, I can **add my payment details during checkout** so that **I can pay for the purchase**.
    - [#36](https://github.com/legenduzair/the-halal-butcher/issues/36) - As a **user**, I can **view the order confirmation page after it has been processed** so that **I am aware that my order and payment have gone through**.

8. Configure Profile App:
    - [#37](https://github.com/legenduzair/the-halal-butcher/issues/37) - As a **user**, I can **create my user profile** so that **I can view my order details of processed orders and input saved delivery information so I can process future orders easily**.
    - [#38](https://github.com/legenduzair/the-halal-butcher/issues/38) - As a **user**, I can **edit personal information on my user profile** so that **I can use the correct details when processing future potential orders**.

9. Product Management:
    - [#39](https://github.com/legenduzair/the-halal-butcher/issues/39) - As a **store owner**, I can **add any new products to the store product list** so that **the site can be up to date with new products**.
    - [#40](https://github.com/legenduzair/the-halal-butcher/issues/40) - As a **store owner**, I can **edit products through product management** so that **I can keep the existing products up to date on the website**.
    - [#41](https://github.com/legenduzair/the-halal-butcher/issues/41) - As a **store owner**, I can **delete products via product management** so that **I can remove any unwanted products from the site**.

10. Final Deployment:
    - [#42](https://github.com/legenduzair/the-halal-butcher/issues/42) - As a **developer**, I want to **create and deploy my project on Heroku** so that **my project is deployed properly live**.
    - [#43](https://github.com/legenduzair/the-halal-butcher/issues/43) - As a **developer**, I want to **setup AWS including access to S3 buckets** so that **my media and static files are stored and have loaded up properly**.
    - [#44](https://github.com/legenduzair/the-halal-butcher/issues/44) - As a **developer**, I want to **input any final code and cache changes** so that **my project is deployed with all of the correct code and variables**.

11. Product Reviews:
    - [#45](https://github.com/legenduzair/the-halal-butcher/issues/45) - As a **user**, I can **add a product review** so that **I can share my review with other users who are also interested in purchasing the products**.
    - [#46](https://github.com/legenduzair/the-halal-butcher/issues/46) - As a **user**, I can **read other people's reviews** so that **I can view other people's opinions of the product I wish to purchase**.
    - [#47](https://github.com/legenduzair/the-halal-butcher/issues/47) - As a **user**, I can **edit product reviews** so that **I am able to make corrections to the review and update it**.
    - [#48](https://github.com/legenduzair/the-halal-butcher/issues/48) - As a **user**, I can **delete product reviews** that **I have written so that it is no longer on the website for others to view**.

12. Web Marketing:
    - [#49](https://github.com/legenduzair/the-halal-butcher/issues/49) - As a **store owner**, I want **to add the option for users to sign up to an email newsletter** so that **I can use it for marketing new products**.
    - [#50](https://github.com/legenduzair/the-halal-butcher/issues/50) - As a **store owner**, I want **to create a Facebook page for the company** so that **I can promote marketing of new products and advertise the company to Facebook users**.

13. Configure Blog App:
    - [#52](https://github.com/legenduzair/the-halal-butcher/issues/52) - As a **user**, I can **view a chosen blog entry in detail** so that **I can read the full content of the blog**.
    - [#53](https://github.com/legenduzair/the-halal-butcher/issues/53) - As a **user**, I can **view a chosen blog entry in detail** so that **I can read the full content of the blog**.
    - [#54](https://github.com/legenduzair/the-halal-butcher/issues/54) - As a **store owner**, I can **add a blog to the list of blog entries** so that **the site can be setup with blog entries for users to read**.
    - [#55](https://github.com/legenduzair/the-halal-butcher/issues/55) - As a **store owner**, I can **update a blog entry** so that **the site can be updated with the correct & latest information**.
    - [#56](https://github.com/legenduzair/the-halal-butcher/issues/56) - As a **store owner**, I can **delete any blog entries from the website** so that **I can remove any unwanted blogs on the site**.

### The Structure Plane

#### Entity Relationship Diagram

As this project utilises Django which is a MVT(Model, View & Template) framework, a connection to database tables or 'Models' is required. An entity relationship diagram was created to visually map out the structure of the databases & models. The entity relationship diagram was creating using [DrawSQL](https://drawsql.app/) and is shown below:

![screenshot of ERD on DrawSQL](/readme/screenshots/Screenshot%202022-08-14%20at%2017.57.09.png)

#### User Stories - Acceptance Criterias'

As part of the Strategy Plane, I also incorporated Acceptance Criterias' within each User Story, to help plan and structure the development of my project and be more organised about the whole workflow & process.

<details>
    <summary></summary>      
        
</details>

### The Skeleton Plane

### The Surface Plane

## Features

## Future Improvements

## Web Marketing

## Testing

## Technologies Used

## Deployment

## Credits
