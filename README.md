<span style="font-size: 24px;"><strong>🎬 Movie Inventory 🎬</strong></span>

A Flask-based web application for managing your personal movie collection and wishlist.

Track what movies you own, what movies you want, and easily add or remove titles through a clean, simple interface.

Version: 0.1

Author: Christian Kurdi



<span style="font-size: 24px;"><strong>📌 Overview 📌</strong></span>

Movie Inventory is a lightweight CRUD-style Flask application backed by SQLite. It provides a simple dashboard for:

·	Viewing movies you currently own

·	Viewing movies you want to own

·	Adding new movies with metadata (genre, actors, possession status)

·	Removing movies from your collection or wishlist

The project is structured using Flask blueprints, service layers, and a database module.



<span style="font-size: 24px;"><strong>🧱 Features 🧱</strong></span>

·	Current Collection

View all owned movies.

·	Wishlist

View movies you want to own in the future.

·	Add Movies

Add new movies with the title, genre, up to three actors, and movie status: is it owned or wanted?

·	Remove Movies

Search for a movie by name and remove it from the database.

·	Modular Architecture

The project uses a clean, scalable structure:

&#x09;"/routes" for endpoints

&#x09;"/services" for business logic

&#x09;"/database" for SQLite operations

&#x09;"/templates" for HTML pages

&#x09;"/static" for CSS/JS assets



<span style="font-size: 24px;"><strong>⚙️ Tech Stack ⚙️</strong></span>

·	Python 3.x

·	Flask

·	SQLite

·	HTML / CSS / JavaScript

·	Blueprint-based routing

·	Service-layer architecture



<span style="font-size: 24px;"><strong>🧪 Future Improvements 🧪</strong></span>

·	Add user authentication

·	Add movie search and filtering

·	Add movie posters via external API

·	Add edit/update functionality

·	Add pages for large collections

·	Add unit tests for services and database layer



<span style="font-size: 24px;"><strong>📄 License 📄</strong></span>

This project is for educational and portfolio purposes.



<span style="font-size: 24px;"><strong>🙌 Acknowledgements 🙌</strong></span>

Built with Flask and SQLite.

Designed as part of a personal software engineering portfolio.



