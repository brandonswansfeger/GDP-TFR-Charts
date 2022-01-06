<img src="https://github.com/brandonswansfeger/GDP-Bar-Charts/blob/main/banner%20tfr.PNG?raw=true" align="center" height="250" width="75%" >

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<img >


<h3 align="center">Economic Development and Access to Family Planning:
Using Bar Charts to Visualize the Data</h3>

  
  <div align="center"> 
   <a href="https://github.com/brandonswansfeger/GDP-Bar-Charts"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://tfr-gdp-bar-chart.herokuapp.com/">View Demo</a>
    ·
    <a href="https://github.com/brandonswansfeger/GDP-Bar-Charts/issues">Report Bug</a>
    ·
    <a href="https://github.com/brandonswansfeger/GDP-Bar-Charts/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

While most demographers and economists have viewed socioeconomic factors as the driving forces behind fertility decline in developing countries, there is growing evidence that the “ease” of access to, or realistic availability of, fertility regulation methods may be at least as important in this demographic change. Much of the world's fertility decline has occurred where fertility regulation methods are relatively easy to obtain regardless of a "program", and those countries have not all exhibited economic development or significant improvements in education before the decline. In addition, there is evidence that removing barriers to family planning options actually builds a desire for small families – which would be consistent with our consumer behavior regarding other products and services. If governments and international donor agencies recognize and move to reduce certain barriers, this will benefit parents by enabling them to achieve their family size goals, and improve maternal health and child survival.

Using date from The World Bank, World Development Indicators, this webapp provides a visualization of data showing that some countries have reduced family size before economic development has increased while also showing that most countries with fertility above replacement level have economies that are less developed.

Economic Development
GDP per capita, PPP* is the indicator selected to measure the econonomic development for each country. The countries are sorted in descending order from highest GDP per capita, PPP on the left towards the lowest GDP per capita, PPP on the right.

Access to Family Planning
Total Fertility Rate (TFR)** is the indicator selected to measure access to family planning. The vertical bars represent the TFR for each country and values are shown on the y axis.


<p align="right">(<a href="#top">back to top</a>)</p>

<div align="center">
  <img src="https://github.com/brandonswansfeger/GDP-Bar-Charts/blob/main/iphonelanding.PNG?raw=true" align="center">
    <img src="https://github.com/brandonswansfeger/GDP-Bar-Charts/blob/main/landing%20page.PNG?raw=true" width="70%" align="center"> 
 </div>
 <div>
  <img src="https://github.com/brandonswansfeger/GDP-Bar-Charts/blob/main/chartview.PNG?raw=true" align="center">
</div>

### Built With

- Django
- Python
- HTML
- CSS
- JavaScript
- Matplotlib
- Pandas
- WBGAPI

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* npm
  ```sh
  npm install npm@latest -g
  ```


To use this template to start your own project:

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
      
After that just install the local dependencies, run migrations, and start the server.

{% endif %}

# {{ project_name|title }}

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
    
    div id="top"></div>
<p align="right">(<a href="#top">back to top</a>)</p>



See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

Data from Covid Act Now API is licensed under <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International</a>.

All commercial entities wishing to access the API should contact api@covidactnow.org to acquire a commercial license.

commercial users are defined as any individual or entity engaged in commercial activities, such as selling goods or services. Non-commercial users can freely download, use, share, modify, or build upon the source code.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

brandonswansfeger@me.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>




<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/brandonswansfeger/GDP-Bar-Charts.svg?style=for-the-badge
[contributors-url]: https://github.com/brandonswansfeger/GDP-Bar-Charts/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/brandonswansfeger/GDP-Bar-Charts.svg?style=for-the-badge
[forks-url]: https://github.com/brandonswansfeger/GDP-Bar-Charts/network/members
[stars-shield]: https://img.shields.io/github/stars/brandonswansfeger/GDP-Bar-Charts.svg?style=for-the-badge
[stars-url]: https://github.com/brandonswansfeger/GDP-Bar-Charts/stargazers
[issues-shield]: https://img.shields.io/github/issues/brandonswansfeger/GDP-Bar-Charts.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/brandonswansfeger/GDP-Bar-Charts.svg?style=for-the-badge
[license-url]: https://github.com/brandonswansfeger/GDP-Bar-Charts/blob/version-2/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/brandonswansfeger
