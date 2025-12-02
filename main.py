from astropy.coordinates import SkyCoord
import astropy.units as u

def rechercher_par_nom(nom, catalogue):
    """Cherche un objet céleste par son nom officiel (ex : "Sirius", "Betelgeuse").
    But : Trouver rapidement une étoile à partir de son nom.
    nom : nom de l'étoile a chercher. """
    
    nom = nom.strip().lower()# On enlève les espaces au début et à la fin et on met tout en minuscules
    for etoile in catalogue:
        if etoile["name"].lower() == nom:# On compare le nom de l'étoile actuelle avec le nom recherché,conversion en minuscules pour être sûr que la comparaison est correcte
            return etoile
        
    return None  # si aucune étoile trouvée

def rechercher_par_coordonnees(ra, dec, catalogue, rayon):
    """Cherche des objets proches d’une position en ascension droite (RA) et déclinaison (Dec). 
    But : Trouver ce qui se trouve autour d’un point du ciel.
    ra, dec : coordonnées du point à chercher (ex: '05h55m10s', '+07d24m25s')
    rayon : rayon de recherche en degrés (ex: 2)
    """
    centre = SkyCoord(ra, dec, frame='icrs')# Création de la coordonnée centrale à partir du point donné

    resultats = []

    for etoile in catalogue:
        coord = SkyCoord(etoile["ra"], etoile["dec"], frame='icrs')# On transforme les coordonnées de l’étoile en objet SkyCoord
        separation = centre.separation(coord)# On calcule la distance angulaire entre le centre et l’étoile

        if separation.degree <= rayon:
            etoile_avec_distance = etoile.copy()# On copie le dictionnaire de l’étoile pour ne pas modifier l’original
            etoile_avec_distance["distance_deg"] = round(separation.degree, 4)# On ajoute la distance (en degrés) au résultat
            resultats.append(etoile_avec_distance)

    resultats.sort(key=lambda x: x["distance_deg"])# On trie par distance (plus proches en premier)

    return resultats

