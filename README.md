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

### Scope Plane

#### Feature Identification

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

* **Bug:** Preview on Port 8000 loading as 'Dangerous Website'

| Preview Bug | Details |
| -------- | -------- |
| Description: | When loading a preview of my website on Port8000 after deploying my site to Heroku, a warning page appeared in the browser blocking entry to the site |
| Steps to reproduce: | 1. Deploy Django website to Heroku.<br>2. Use 'python3 manage.py runserver' command.<br>3. View port  |
| Expected behaviour: | I expected to see the 'Django launched successfully' page which I had seen before deployment to Heroku |
| Actual behaviour: | ![Screenshot of preview bug](documentation/readme/bug-dangerous-site.png) |
| Environment: | Operating system: Windows 11<br>Browser: Chrome Version 120.0.6099.71 |
| Possible causes: | The issue arose once Heroku successfully deployed the site. |
| Additional information: | n/a |
| Steps to fix: | 1. Changing permissions to allow access in the chrome settings ❌<br>2. Contacted Tutor Support who deduced the issue was because I did not have any views in place yet. This was confirmed when we tried to view the admin app while loaded without issue in Port8000 |
| References: | n/a |


<!-- 
![f](documentation/readme)
![f](documentation/readme)
![f](documentation/readme)
![f](documentation/readme)
![f](documentation/readme)

| Preview Bug | Details |
| -------- | -------- |
| Description: |  |
| Steps to reproduce: |  |
| Expected behaviour: |  |
| Actual behaviour: |  |
| Possible causes: |  |
| Additional information: |  |
| Steps to fix: |  |
| References: |  | -->


---

## Deployment 🖥️

---

## Credits 💐

### Code

### Content

### Media

### Acknowledgments
