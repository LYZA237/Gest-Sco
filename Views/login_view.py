from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from controllers.auth_controller import AuthController

class LoginView(QWidget):
    def __init__(self):
        super().__init__()
        self.auth = AuthController()
        self.setWindowTitle("Connexion - Gestion Scolarité")
        self.setFixedSize(350, 200)
        
        layout = QVBoxLayout()
        
        self.username = QLineEdit()
        self.username.setPlaceholderText("Nom d'utilisateur")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Mot de passe")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        
        btn_login = QPushButton("Se connecter")
        btn_login.clicked.connect(self.handle_login)
        
        layout.addWidget(QLabel("Gestion Scolarité"))
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(btn_login)
        
        self.setLayout(layout)
    
    def handle_login(self):
        user = self.auth.login(self.username.text(), self.password.text())
        if user:
            QMessageBox.information(self, "Succès", f"Bienvenue {user['username']} - {user['role']}")
            self.close()
            # Ouvre le dashboard selon le rôle
            if user['role'] == 'admin':
                from views.admin_dashboard import AdminDashboard
                self.dashboard = AdminDashboard()
                self.dashboard.show()
            else:
                from views.etudiant_dashboard import EtudiantDashboard
                self.dashboard = EtudiantDashboard(user['id'])
                self.dashboard.show()
        else:
            QMessageBox.warning(self, "Erreur", "Identifiants incorrects")