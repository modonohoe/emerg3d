# EMERG3D Props

![EMERG3D website preview](documentation/readme/am-i-responsive.png)

EMERG3D Props is a 3D printing business. This is their website (1st itertion made for my Portfolio Project 4 for Code Institute)

---

## Contents

* [User Experience](#user-experience) 🪄
  * [Strategy Plane](#strategy-plane)
    * [Project Goals](#project-goals)
  * [Scope Plane](#scope-plane)
    * [Feature Identification](#feature-identification)
  * [Structure Plane](#structure-plane)
    * [User Stories](#user-stories)
    * [Database Schema](#database-schema)
  * [Skeleton Plane](#skeleton-plane)
    * [Wireframes](#wireframes)
  * [Surface Plane](#surface-plane)
    * [Color Scheme](#color-scheme)
    * [Fonts](#fonts)
    * [Photography](#photography)
* [Agile Methodology](#agile-methodology) 🗃️
  * [Sprints](#sprints)
* [Features](#features) ✨
  * [Current Features](#current-features)
  * [Future Features](#future-features)
* [Technologies](#technologies) 🌐
  * [Languages](#languages)
  * [Database](#database)
  * [Frameworks](#frameworks)
  * [Libraries & Packages](#libraries--packages)
  * [Programs](#programs)
* [Testing](#testing) 📝
* [Bugs and Fixes](#bugs-and-fixes) 🛠️
* [Deployment](#deployment) 🖥️
* [Credits](#credits) 💐
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

## User Experience 🪄

### Strategy Plane

#### Project Goals

Emerg3D Props is primarily a Business to Consumer (B2C) website. Following on from a successful social media presence of Emerg3D (INSTAGRAM), the site owner would like a platform to engage in longer form communication with followers in the form of blog posts. The site owner would also like to provide an official way for customers to request collaboration and commission projects (currently this is only possible through direct messages on social media) as well as an online store for pre-printed products (divided into the categories of homeware and cosplay items). Another goal for the website is to showcase links to social media pages.

3D printing is a rapidly expanding industry and Emerg3D Prop’s goal is to establish a presence online in Ireland and worldwide.

### Scope Plane

#### Feature Identification

Planning for the website was undertaken in stages. The first step was meeting with the site owner to find out what they hoped to have delivered and then ranking these requests in order of importance, viability and deciding on the Minimum Viable Product (MVP) they would be happy with.

Although originally, it was hoped that Stripe payment system would be implemented, it was ultimately decided that the solution Shopify would be adopted in the next iteration of the website to handle the site's e-commerce.

The following features were identified:

| -- | -- | -- | -- | -- | -- |
| User Type | Feature | Importance | Viability | MVP | Achieved |
| Admin | Blog | 5 | 5 | YES  | ✅ |
| Admin* | View authored blogposts on profile | 5 | 5 |  | ✅ |
| Admin | Online store | 5 | 5 | YES | ✅ |
| Admin | Edit/delete shop items | 5 | 5 | YES | ✅ |
| Admin | Feature best sellers on homepage | 4 | 3 |  |  |
| Admin | Gallery | 3 | 4 |  |  |
| Admin | Social media links | 5 | 5 | YES | ✅ |
| Admin | Chatbot for customer queries | 1 | 1 |  |  |
| User | Enquiry form | 5 | 5 | YES | ✅ |
| User | Wishlist | 3 | 3 |  |  |
| User | Product reviews | 4 | 3 |  |  |
| User* | Make blog posts | 4 | 4 |  | ✅ |
| User | Like and comments on posts | 5 | 5 | YES | ✅ |
| User | View liked posts on profile | 4 | 4 |  |  |
| Both | About page | 5 | 5 | YES | ✅ |
| Both | Secure login and logout | 5 | 5 | YES | ✅ |
| Both | Enquiry history | 5 | 5 |  | ✅ |
| Both | Order history | 5 | 3 |  | |
| Both | Automated confirmation of orders | 4 | 4 |  |  |
| Both | Payment via Stripe | 4 | 4 |  |  |
| Both | Account profile | 5 | 5 | YES | ✅ |
| Both | Filter items in store by category | 4 | 4 |  | ✅ |

*In this case Admin/User also refers to authorised users with Moderator=True


### Structure Plane

#### User Stories

#### Database Schema

### Skeleton Plane

#### Wireframes

#### Surface Plane

#### Color Scheme

<details>
<summary>Basic Palette</summary>

Hexadecimal codes that correspond to the company's logo were provided by the client. It was decided 'off-white' would replace the standard white color for text as it creates less of a glare while still maintaining sufficient contrast for accessibility.

![logo-colors](documentation/readme/logo-colors.png)

The colors were then imported into the base.css page and assigned as root colors for ease of use (and all elements using the tags can be instantly amended site-wide in future if the logo changes).

![root-colors](documentation/readme/color-palette.png)
</details>

#### Fonts

<details>
<summary>Horta</summary>

The headline font 'Horta' is used in the company logo and has an open font license.

> "Inspired by the title cards of the original Star Trek television series—even supports Klingon!"
>> Source: [FontLibrary.org](https://fontlibrary.org/en/font/horta)

Sample of Horta font:
![Horta sample](documentation/readme/horta-sample.png)

</details>

<details>
<summary>Nova Square</summary>

The body font 'Nova Square' was chosen for its striking simplicity. It was created by the famous stonemason [Wojciech Kalinowski](http://www.identifont.com/show?3DQU)

> "In 1995 he began to design his own typefaces for carving in stone, like Medieval Sharp, Gothica, and Modern Antiqua. In second half of the 2000's he became interested in digital typefaces, and began to digitise his old typefaces and design new ones. He is a contributor to the Open Font Library."

Sample of Nova Square font:
![Nova Square sample](documentation/readme/nova-font.png)

</details>

#### Photography

---

## Agile Methodology 🗃️

### Sprints

---

## Features ✨

### Current Features

### Future Features

---

## Technologies 🌐

### Languages

### Database

### Frameworks

### Libraries & Packages

### Programs

---

## Testing 📝

---

## Bugs and Fixes 🛠️

<details>
<summary> Bug: Preview on Port 8000 loading as 'Dangerous Website'</summary>

| Preview Bug | Details |
| -------- | -------- |
| Description: | When loading a preview of my website on Port 8000 after deploying my site to Heroku, a warning page appeared in the browser blocking entry to the site |
| Steps to reproduce: | 1. Deploy Django website to Heroku.<br>2. Use 'python3 manage.py runserver' command in the IDE terminal.<br>3. View Port 8000  |
| Expected behaviour: | I expected to see the 'Django launched successfully' page which I had seen before deployment to Heroku |
| Actual behaviour: | ![Screenshot of preview bug](documentation/readme/bug-dangerous-site.png) |
| Environment: | Operating system: Windows 11<br>IDE: Code Anywhere<br>Browser: Chrome Version 120.0.6099.71 |
| Possible causes: | The issue arose once Heroku successfully deployed the site. |
| Additional information: | n/a |
| Steps to fix: | 1. Changing permissions to allow access in the chrome settings ❌<br>2. The issue was because I did not have any views in place yet. This was confirmed when we tried to view the admin app, which loaded without issue in Port 8000.|
| References: | n/a |
| Status: | Resolved ✅ |

</details>

<details>
<summary> Bug: CSS path error</summary>

| Path Bug | Details |
| -------- | -------- |
| Description: | CSS file did not load custom styling to Bootstrap template |
| Steps to reproduce: | 1. Create style.css in folder CSS in static files<br>2. Preview site on Port 8000 |
| Expected behaviour: | I expected to see the curved container edges removed and custom color styling applied to my Bootstrap template. |
| Actual behaviour: | Chrome Developer Tools revealed the CSS was not loading succesfully ![Screenshot of path bug](documentation/readme/bug-css-path.png) |
| Environment: | Operating system: Windows 11<br>IDE: Code Anywhere<br>Browser: Chrome Version 120.0.6099.71 |
| Possible causes: | Incorrect path or unknown error |
| Additional information: | n/a |
| Steps to fix: | 1. Checked the path to my CSS file and this looked in order.<br>2. After troubleshooting, I contacted Tutor Support who supplied me with the following screenshot:<br>![Screenshot of path error](documentation/readme/bug-css-path2.png)<br>The path appeared to me to be within the folder but as I had never encountered this error before, I mistook the indentation for the file being within the folder.
| References: | n/a |
| Status: | Resolved ✅ |

</details>

<details>
<summary> Bug: Django App Name </summary>

| Preview Bug | Details |
| -------- | -------- |
| Description: | When I tried to make an app called 'home', this was not permitted. |
| Steps to reproduce: | 1. In the terminal use the command: 'python3 manage.py startapp home' |
| Expected behaviour: | Creation of new app called 'home' |
| Actual behaviour: | As python has a module named 'home' this is not permitted<br>![screenshot of terminal error](documentation/readme/bug-django-home.png) |
| Environment: | Operating system: Windows 11<br>IDE: Code Anywhere<br>Browser: Chrome Version 120.0.6099.71 |
| Possible causes: | Python permissions |
| Additional information: | n/a |
| Steps to fix: | I chose the name 'landing_page' which is inline with naming conventions. 'home_' was also considered. |
| References: | [GitHub discussion on this topic](https://github.com/nephila/djangocms-installer/issues/359) |
| Status: | Resolved ✅ |

</details>

<details>
<summary> Bug: Migration conflict</summary>

| Preview Bug | Details |
| -------- | -------- |
| Description: | When attempting to migrate my first app, an InconsistentMigrationError was raised `Migration admin.0001_initial is applied before its dependency accounts.0001_initial on database 'default'` |
| Steps to reproduce: | 1. In the terminal use the command: 'python3 manage.py migrate accounts' |
| Expected behaviour: | A successful migration of the accounts models to the ElephantSQL database. |
| Actual behaviour: | ![Migration error](documentation/readme/bug-initial-migration.png) |
| Environment: | Operating system: Windows 11<br>IDE: Code Anywhere<br>Browser: Chrome Version 120.0.6099.71 |
| Possible causes: | 1. I created an instance of a superuser which is part of the Admin site.<br>2. Default Django apps need to be migrated before any custom apps are created as they depend on these. |
| Additional information: | n/a |
| Steps to fix: | 1. Reset the database on ElephantSQL to remove the migration of accounts app.<br>2. Ran the command 'python3 manage.py migrate accounts' and the migration was successful |
| References: | n/a |
| Status: | Resolved ✅ |

</details>

<details>
<summary> Bug: Code Anywhere reserved URL</summary>

| Preview Bug | Details |
| -------- | -------- |
| Description: | When trying to preview my 'login.html', there was a 403 Error |
| Steps to reproduce: | 1. Use 'python3 manage.py runserver' command in the IDE terminal.<br>2. View Port 8000 with app url + 'login/' |
| Expected behaviour: | Get a preview of my login.html page |
| Actual behaviour: | The URL of my website changed to a Code Anywhere one instead of a heroku URL and displayed a 403 error.<br>![URL bug Code Anywhere](documentation/readme/bug-code-anywhere-login.png) |
| Environment: | Operating system: Windows 11<br>IDE: Code Anywhere<br>Browser: Chrome Version 120.0.6099.71 |
| Possible causes: | 'login' is a reserved URL for Code Anywhere |
| Additional information: | n/a |
| Steps to fix: | Rename 'login.html' to 'signin.html' |
| References: | n/a |
| Status: | Resolved ✅ |

</details>

<!-- 
![f](documentation/readme)

<!-- | Preview Bug | Details |
| -------- | -------- |
| Description: |  |
| Steps to reproduce: |  |
| Expected behaviour: |  |
| Actual behaviour: |  |
| Environment: | Operating system: Windows 11<br>IDE: Code Anywhere<br>Browser: Chrome Version 120.0.6099.71 |
| Possible causes: |  |
| Additional information: |  |
| Steps to fix: |  |
| References: |  |  -->

---

## Deployment 🖥️

---

## Credits 💐

### Code

### Content

### Media

### Acknowledgments
