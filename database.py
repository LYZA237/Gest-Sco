import sqlite3
import os

DB_PATH = os.path.join("db", "scolarite.db")

def get_connection():
    os.makedirs("db", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL CHECK(role IN ('admin', 'etudiant'))
    );

    CREATE TABLE IF NOT EXISTS departements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS filieres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        id_departement INTEGER,
        FOREIGN KEY(id_departement) REFERENCES departements(id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS niveaux (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        id_filiere INTEGER,
        FOREIGN KEY(id_filiere) REFERENCES filieres(id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS etudiants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        matricule TEXT UNIQUE NOT NULL,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL,
        id_niveau INTEGER,
        id_user INTEGER,
        FOREIGN KEY(id_niveau) REFERENCES niveaux(id),
        FOREIGN KEY(id_user) REFERENCES users(id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS matieres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        coefficient INTEGER NOT NULL,
        id_niveau INTEGER,
        FOREIGN KEY(id_niveau) REFERENCES niveaux(id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS bulletins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_etudiant INTEGER,
        id_matiere INTEGER,
        cc REAL DEFAULT 0,
        tpe REAL DEFAULT 0,
        tp REAL DEFAULT 0,
        examen REAL DEFAULT 0,
        note_finale REAL DEFAULT 0,
        statut TEXT,
        FOREIGN KEY(id_etudiant) REFERENCES etudiants(id) ON DELETE CASCADE,
        FOREIGN KEY(id_matiere) REFERENCES matieres(id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS inscriptions (
        id_etudiant INTEGER,
        id_matiere INTEGER,
        PRIMARY KEY(id_etudiant, id_matiere),
        FOREIGN KEY(id_etudiant) REFERENCES etudiants(id) ON DELETE CASCADE,
        FOREIGN KEY(id_matiere) REFERENCES matieres(id) ON DELETE CASCADE
    );
    """)
    
    # Créer admin par défaut
    cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('admin', 'admin123', 'admin')")
    conn.commit()
    conn.close()