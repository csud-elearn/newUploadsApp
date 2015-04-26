def estProfesseur(user):
    return user.groups.filter(name='professeurs').exists()
    
def estEtudiant(user):
    return user.groups.filter(name='étudiants').exists()