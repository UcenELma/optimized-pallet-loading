import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def calculer_chargement(dim_palette, dim_boite, charge_max, poids_boite, nb_couches_max, orientation_choisie=None):
    longueur_p, largeur_p, hauteur_p = dim_palette
    l_b, L_b, H_b = dim_boite

    orientations = []
    # toutes les orientations possibles (l, L, H)
    possibles = [
        (l_b, L_b, H_b),
        (l_b, H_b, L_b),
        (L_b, l_b, H_b),
        (L_b, H_b, l_b),
        (H_b, l_b, L_b),
        (H_b, L_b, l_b)
    ]

    # On filtre selon si une orientation est choisie
    if orientation_choisie is not None:
        if orientation_choisie in possibles:
            orientations = [orientation_choisie]
        else:
            print("Orientation choisie invalide, on teste toutes.")
            orientations = possibles
    else:
        orientations = possibles

    meilleur_resultat = {
        "nb_total": 0,
        "orientation": None,
        "nb_par_couche": 0,
        "nb_couches": 0
    }

    for (lo, la, ha) in orientations:
        # combien on peut mettre sur une couche (sans dépasser surface palette)
        nb_x = int(longueur_p // lo)
        nb_y = int(largeur_p // la)
        nb_par_couche = nb_x * nb_y

        if nb_par_couche == 0:
            continue

        # combien de couches max possible sans dépasser hauteur palette ni charge max
        nb_couches_hauteur = int(hauteur_p // ha)
        nb_couches_charge = int(charge_max // (poids_boite * nb_par_couche))
        nb_couches_possibles = min(nb_couches_hauteur, nb_couches_max, nb_couches_charge)

        nb_total = nb_par_couche * nb_couches_possibles

        if nb_total > meilleur_resultat["nb_total"]:
            meilleur_resultat.update({
                "nb_total": nb_total,
                "orientation": (lo, la, ha),
                "nb_par_couche": nb_par_couche,
                "nb_couches": nb_couches_possibles
            })

    return meilleur_resultat

def draw_box(ax, x, y, z, dx, dy, dz, color='skyblue'):
    vertices = [
        [x, y, z],
        [x + dx, y, z],
        [x + dx, y + dy, z],
        [x, y + dy, z],
        [x, y, z + dz],
        [x + dx, y, z + dz],
        [x + dx, y + dy, z + dz],
        [x, y + dy, z + dz],
    ]

    faces = [
        [vertices[j] for j in [0, 1, 2, 3]],
        [vertices[j] for j in [4, 5, 6, 7]],
        [vertices[j] for j in [0, 1, 5, 4]],
        [vertices[j] for j in [2, 3, 7, 6]],
        [vertices[j] for j in [1, 2, 6, 5]],
        [vertices[j] for j in [0, 3, 7, 4]],
    ]

    box = Poly3DCollection(faces, facecolors=color, edgecolors='k', linewidths=0.5, alpha=0.9)
    ax.add_collection3d(box)

def afficher_chargement_3d(dim_palette, orientation_boite, nb_par_couche, nb_couches):
    longueur_p, largeur_p = dim_palette
    l_b, L_b, H_b = orientation_boite

    boites_x = int(longueur_p // l_b)
    boites_y = int(largeur_p // L_b)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("Visualisation 3D du chargement des boîtes sur la palette")

    # Palette (5 cm d'épaisseur)
    draw_box(ax, 0, 0, 0, longueur_p, largeur_p, 5, color='peru')

    # Placement des boîtes
    for h in range(nb_couches):
        for i in range(boites_x):
            for j in range(boites_y):
                x = i * l_b
                y = j * L_b
                z = 5 + h * H_b
                draw_box(ax, x, y, z, l_b, L_b, H_b)

    ax.set_xlim([0, longueur_p])
    ax.set_ylim([0, largeur_p])
    ax.set_zlim([0, 5 + nb_couches * H_b + 10])

    ax.set_xlabel('Longueur (cm)')
    ax.set_ylabel('Largeur (cm)')
    ax.set_zlabel('Hauteur (cm)')

    plt.tight_layout()
    plt.show()

def main():
    try:
        print("=== Chargement de boîtes sur palette ===")

        longueur_p = float(input("Longueur palette (cm) : "))
        largeur_p = float(input("Largeur palette (cm) : "))
        hauteur_p = float(input("Hauteur max palette (cm) : "))
        charge_max = float(input("Charge max palette (kg) : "))

        l_b = float(input("Longueur boîte (cm) : "))
        L_b = float(input("Largeur boîte (cm) : "))
        H_b = float(input("Hauteur boîte (cm) : "))
        poids_boite = float(input("Poids boîte (kg) : "))

        nb_couches_max = int(input("Nombre max de couches souhaité : "))

        choix_orient = input("Souhaitez-vous choisir une orientation ? (o/n) : ").lower()
        orientation_choisie = None
        if choix_orient == 'o':
            print("Entrez l'orientation choisie :")
            lo = float(input("Longueur boîte dans palette (cm) : "))
            la = float(input("Largeur boîte dans palette (cm) : "))
            ha = float(input("Hauteur boîte dans palette (cm) : "))
            orientation_choisie = (lo, la, ha)

        resultats = calculer_chargement(
            (longueur_p, largeur_p, hauteur_p),
            (l_b, L_b, H_b),
            charge_max,
            poids_boite,
            nb_couches_max,
            orientation_choisie
        )

        if resultats["nb_total"] == 0:
            print("Impossible de charger des boîtes selon les paramètres fournis.")
            return

        print("\nRésultat optimal :")
        print(f"Nombre total de boîtes : {resultats['nb_total']}")
        print(f"Orientation choisie (L, l, H) : {resultats['orientation']}")
        print(f"Boîtes par couche : {resultats['nb_par_couche']}")
        print(f"Nombre de couches : {resultats['nb_couches']}")

        # Affichage 3D
        afficher_chargement_3d(
            (longueur_p, largeur_p),
            resultats["orientation"],
            resultats["nb_par_couche"],
            resultats["nb_couches"]
        )

    except ValueError:
        print("Erreur : veuillez entrer des valeurs numériques valides.")

if __name__ == "__main__":
    main()
