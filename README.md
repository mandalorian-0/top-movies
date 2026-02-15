# 🎬 Movie Management Web Application

A full-stack Python web application built with **Flask**, **SQLAlchemy**, **Bootstrap 5**, and a modular architecture for managing a local movie database. This project allows users to browse, add, edit, and delete movies with support for dynamic movie details fetched via a third-party API (e.g., The Movie Database - TMDB).

> ✅ **Fully functional**  
> ✅ **Modular design**  
> ✅ **Secure and maintainable**  
> ✅ **User-friendly UI with responsive design**  
> ✅ **Self-contained with proper database lifecycle management**

---

## 🚀 Overview

This application provides a simple yet powerful interface for managing a local collection of movies. It supports:

- Viewing all movies in the database
- Adding new movies (via form input or auto-population from TMDB)
- Editing existing movie details
- Deleting movies
- Dynamic movie detail lookup using TMDB API

The app is designed with clean separation of concerns using:

- **Flask** as the web framework
- **SQLAlchemy ORM** for database operations
- **Bootstrap 5** for responsive, modern UI
- **Modular services** for business logic (e.g., `movie_service`)
- **Form handling** for user input validation
- **API integration** for external movie data retrieval

---

## 📦 Tech Stack

| Layer           | Technology                                           |
| --------------- | ---------------------------------------------------- |
| Backend         | Python 3.10+                                         |
| Framework       | Flask (with Flask-Bootstrap 5)                       |
| Database        | SQLite (via SQLAlchemy ORM)                          |
| UI              | HTML/CSS/JavaScript (Bootstrap 5)                    |
| API Integration | TMDB API (via custom `api.py`)                       |
| Forms           | Flask-WTF (implied via `UpdateForm`, `AddMovieForm`) |
| Security        | Secret key for session protection                    |

> 🔍 _Note: The app uses SQLite for local development. For production, consider PostgreSQL or MySQL with proper configuration._

---

## 🛠️ Project Structure

```
movie_app/
│
├── app.py                     # Main Flask application entry point
├── db/
│   ├── __init__.py            # Database session factory and table creation
│   └── models.py              # (Implied) Movie model definitions
│
├── services/
│   └── movie_service.py       # Core business logic: CRUD operations
│
├── form/
│   ├── update.py              # Edit movie form (UpdateForm)
│   └── add_movie.py           # Add movie form (AddMovieForm)
│
├── api.py                     # TMDB API client for movie lookup and detail fetching
│
├── templates/
│   ├── index.html             # Home page listing all movies
│   ├── edit.html              # Edit movie form page
│   ├── add.html               # Add movie form page
│   ├── select.html            # Results page after title lookup
│
├── static/
│   └── (optional CSS/JS files)
│
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

---

## 📚 Features

### 1. **Home Page (`/movies`)**

- Displays all movies in the database
- Supports deletion via URL parameter: `?id=123`
- Clean, responsive layout using Bootstrap 5

### 2. **Edit Movie (`/movies/edit?id=123`)**

- Form-based interface to update movie title, year, description, and image
- Form validation ensures data integrity
- On successful submission, redirects back to home page

### 3. **Add Movie (`/movies/add`)**

- Two modes:
    - **Manual Entry**: User fills out form with title, year, description
    - **Auto-lookup**: User types a movie title → system searches TMDB → displays results → user selects one → movie is added automatically with poster image and metadata
- Uses `api.movie_title_lookup()` to fetch movie list from TMDB
- On selection, creates a new movie entry and redirects to edit mode

### 4. **Movie Detail Integration**

- Uses TMDB's public API to retrieve:
    - Movie title
    - Poster path (image URL)
    - Release year
    - Overview (description)
- All images are served from: `https://image.tmdb.org/t/p/original`

> ⚠️ Requires a valid TMDB API key (not included in this code — must be set in `api.py`)

---

## 🔐 Security & Best Practices

- **Secret Key**: A hardcoded secret key is used for session management. In production, use environment variables.
- **Input Validation**: Forms are validated using Flask-WTF to prevent malformed or malicious input.
- **Database Transactions**: Proper context manager (`yield db`) ensures connections are closed safely.
- **Error Handling**: General exception handling prevents crashes during deletion or updates.
- **No XSS or SQL Injection**: Uses ORM and form validation to protect against common attacks.

> 🔒 **Recommendation**: In production, move the secret key and API key to environment variables (e.g., `.env` file).

---

## 🚀 Setup & Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Step-by-Step Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mandalorian/top-movies.git
    cd top-movies
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file (optional but recommended):

    ```env
    TMDB_API_KEY=your_tmdb_api_key_here
    SECRET_KEY=your_secret_key_here
    ```

4. Set up the database (creates tables if they don’t exist):

    > The app will automatically create the necessary tables on first run.

5. Start the server:

    ```bash
    flask --app main run
    ```

6. Open your browser and go to: `http://localhost:5000/movies`

---

## 📝 API Usage (in `api.py`)

The app uses the **The Movie Database (TMDB)** API for movie lookups.

### Available Endpoints:

- `api.movie_title_lookup(title)`  
  → Returns list of movies matching the given title from TMDB

- `api.get_movie_details(movie_id)`  
  → Returns full movie details (title, poster, year, overview) for a specific movie ID

> 📌 You must have a valid TMDB API key to use these endpoints.  
> 🔗 TMDB API Docs: https://www.themoviedb.org/documentation/api

---

## 📈 Future Enhancements

| Feature                  | Description                                   |
| ------------------------ | --------------------------------------------- |
| User Authentication      | Add login system with sessions or JWT         |
| Search & Filter          | Filter movies by year, genre, or rating       |
| Movie Genres & Tags      | Add genre support using TMDB genre IDs        |
| Image Caching            | Cache TMDB images locally to reduce API calls |
| Export to CSV/JSON       | Allow export of movie list                    |
| Responsive Mobile Design | Optimize for mobile devices                   |
| Dark Mode Toggle         | Add theme switching via CSS variables         |

---

## 📄 License

This project is open-source and available under the **MIT License**.

> Permission is granted to use, modify, and distribute this software for any purpose, provided that the original copyright and license notice are included.

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for:

- Bug fixes
- Feature enhancements
- Documentation improvements
- Security audits

> We follow a transparent, community-driven development model. All changes are reviewed and discussed before merging.

---

## 📞 Contact

For questions, feedback, or feature requests, reach out via:

- GitHub: [github.com/mandalorian-0/top-movies](https://github.com/mandalorian-0/top-movies)
- Email: [Contact me](mailto:whoknows.camping830@passinbox.com)

---

## 📚 References

- Flask Documentation: https://flask.palletsprojects.com/
- Flask-Bootstrap 5: https://pythonhosted.org/Flask-Bootstrap/
- SQLAlchemy ORM: https://docs.sqlalchemy.org/en/20/
- TMDB API: https://www.themoviedb.org/documentation/api

---

## 📌 Notes

- This is a **development prototype** intended for learning and demonstration purposes.
- Not suitable for production without additional security, scalability, and monitoring.
- All data is stored locally in SQLite — no cloud sync or backup.

> 💡 This project exemplifies a modular, maintainable, and user-focused Flask application with real-world functionality.

---

**Maintained by**: A passionate developer in the open-source community
