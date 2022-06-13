<div align='center'>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<h3 align="center">Game Resume</h3>

<img src="https://i.imgur.com/QHniYl3.png" alt="Application Screenshot">
  
<h1><a href="https://django-game-archive.herokuapp.com/">View Demo</a></h1>
</div>

## Project Description
Game Resume is an application that allows users to search for every game ever made (database of 746,000+ games and counting). Users can then add that game to their library (stopped playing, currently playing, finished playing, or want to play) and have the ability to edit all of the game's info and picture, move the game to a different list, or delete the game from their list entirely.

### Built With

* [Django](https://www.djangoproject.com/)

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

PostgreSQL must be configured, and an API key must be obtained for Rawg.io (this is the free video game database) if the currently provided API key is not working.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/sean3434/GameArchive-Django.git
   ```
2. Run a Virtual Environment
```sh
   pipenv shell
   ```
3. Start the server
```sh
   python3 manage.py runserver
   ```

   
   ## Usage
   The website does not require any additional resources. Simply make an account, navigate the site through the navbar and search bar, find the game(s) you are looking for, and add them to your library.
   
   ## Wireframes
   ![image](https://i.imgur.com/08Xpr8W.png)
   ![image](https://i.imgur.com/HzgGple.png)
   ![image](https://i.imgur.com/xVOqfhO.png)
   ![image](https://i.imgur.com/w76ezHo.png)
   ![image](https://i.imgur.com/1iXPecN.png)
   ![image](https://i.imgur.com/HOOsic9.png)
   
   ### MVP Goals
* As a user, I want to be able to sign up and create an account.
* As a user, I want to be able to log in and out of my account.
* As a user, I want to be able to search for any game and add it to one of my games lists.
* As a user, I want to be able to change what list a game is in, edit the info for the game, or delete the game from my list entirely.
* As a user, I want to be able to click on a game's icon/cover art to be taken to that game's show page.

### Stretch Goals
* As a user, I want to be able to look at my profile and edit my info
* As a user, I want to be able to see my total game info on my profile page.
* As a user, I want to be redirected to the aproppriate list in my library when a game is updated or added to the database.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

[contributors-shield]: https://img.shields.io/github/contributors/sean3434/GameArchive-Django.svg?style=for-the-badge
[contributors-url]: https://github.com/sean3434/GameArchive-Django/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/sean3434/GameArchive-Django.svg?style=for-the-badge
[forks-url]: https://github.com/sean3434/GameArchive-Django/network/members
[stars-shield]: https://img.shields.io/github/stars/sean3434/GameArchive-Django.svg?style=for-the-badge
[stars-url]: https://github.com/sean3434/GameArchive-Django/stargazers
[issues-shield]: https://img.shields.io/github/issues/sean3434/GameArchive-Django.svg?style=for-the-badge
[issues-url]: https://github.com/sean3434/GameArchive-Django/issues
