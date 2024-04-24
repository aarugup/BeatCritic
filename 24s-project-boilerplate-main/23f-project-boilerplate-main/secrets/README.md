# MySQL + Flask Boilerplate Project

This repo contains a boilerplate setup for spinning up 3 Docker containers:
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL.
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp.
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`.

#Overview
BeatCritic is a social media platform where people can post their critiques of music. The goal
of this platform is to connect people through music in a way that currently doesnt exist on the
market. A person can be either a user, follower, moderator or artist. They create a profile,
which requires a phone number an email and their name. Users can post reviews on songs
and rate them out of 5. Followers don’t post reviews, rather, they comment on existing
reviews and can like them. Moderators monitor reviews and comments to ensure no
harrassment is occurring, and generate reports when it is, deleting those posts. Artists can
upload, update, and delete their own music to be revoewd, in order to learn about how people
feel about it. All reviews and comments can be viewed by anyone on the platform. This
creates a community where people can learn about new music and share their own
experiences with songs.


#Video Link
https://drive.google.com/file/d/1XTf34x8wHqesASVZpKhmdOcB5lpl_KIF/view
