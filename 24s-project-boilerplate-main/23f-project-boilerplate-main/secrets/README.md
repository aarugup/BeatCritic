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
market. A person can create a profile, which requires a phone number and their online name,
and then begin to post about the music they like or dislike. If the song does not already exist
in the database, they can create a new one and start posting reviews under it. Otherwise they
simply find the song they wish to review, write a critique with a rating out of 5, and then post
publicly. All ratings can be viewed by any user of the platform. This creates a community
where people can learn about new music and share their own experiences with songs.


#Video Link
https://drive.google.com/file/d/1XTf34x8wHqesASVZpKhmdOcB5lpl_KIF/view
